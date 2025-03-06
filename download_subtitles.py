import sys
import re
import os
from datetime import datetime
import requests
from urllib.parse import parse_qs, urlparse
import json
import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled

def sanitize_filename(title):
    # 移除不合法的檔案名稱字元
    return re.sub(r'[<>:"/\\|?*]', '', title)

def create_directory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return True
    except Exception as e:
        print(f"建立目錄失敗: {str(e)}")
        return False

def extract_playlist_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('list', [None])[0]

def extract_video_id(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('v', [None])[0]

def list_videos_in_playlist(playlist_url):
    try:
        playlist_id = extract_playlist_id(playlist_url)
        if not playlist_id:
            raise ValueError("無效的播放清單 URL")

        playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        response = requests.get(playlist_url, headers=headers)
        html_content = response.text
        
        title_match = re.search(r'<title>(.*?)</title>', html_content)
        playlist_title = title_match.group(1) if title_match else "未知播放清單"
        # 移除 YouTube 後綴
        playlist_title = re.sub(r' - YouTube$', '', playlist_title)
        
        json_data = re.findall(r'var ytInitialData = ({.*?});', html_content)
        video_ids = set()
        
        if json_data:
            try:
                data = json.loads(json_data[0])
                contents = data.get('contents', {}).get('twoColumnBrowseResultsRenderer', {}).get('tabs', [{}])[0].get('tabRenderer', {}).get('content', {}).get('sectionListRenderer', {}).get('contents', [{}])[0].get('itemSectionRenderer', {}).get('contents', [{}])[0].get('playlistVideoListRenderer', {}).get('contents', [])
                
                for content in contents:
                    video_id = content.get('playlistVideoRenderer', {}).get('videoId')
                    if video_id:
                        video_ids.add(video_id)
            except:
                pass
        
        if not video_ids:
            patterns = [
                r'watch\?v=([0-9A-Za-z_-]{11}).*?list=' + playlist_id,
                r'videoId":"([0-9A-Za-z_-]{11})"',
                r'video-id="([0-9A-Za-z_-]{11})"'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, html_content)
                video_ids.update(matches)
        
        video_urls = [f'https://www.youtube.com/watch?v={video_id}&list={playlist_id}' for video_id in video_ids]
        return sorted(list(set(video_urls))), playlist_title
            
    except Exception as e:
        print(f"發生錯誤: {str(e)}")
        return [], "未知播放清單"

def get_video_title(video_url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }
        response = requests.get(video_url, headers=headers)
        match = re.search(r'<title>(.*?)</title>', response.text)
        if match:
            title = match.group(1)
            # 移除 YouTube 後綴
            title = re.sub(r' - YouTube$', '', title)
            return title
        return None
    except:
        return None

def download_video_info(video_url, index, output_dir, max_retries=3):
    video_id = extract_video_id(video_url)
    if not video_id:
        print(f"錯誤: 無法從URL提取視頻ID: {video_url}")
        return

    # 先獲取視頻標題
    title = get_video_title(video_url)
    if not title:
        title = f"video_{video_id}"
    
    # 生成目標檔案名稱
    index_str = f"{index:03d}"
    safe_title = sanitize_filename(title)
    filename = os.path.join(output_dir, f"{index_str}-{safe_title}.txt")
    
    # 檢查檔案是否已存在
    if os.path.exists(filename):
        print(f"\n跳過視頻 {index}: {title} (檔案已存在)")
        return

    print(f"\n處理視頻 {index}: {title}")

    for attempt in range(max_retries):
        try:
            # 獲取字幕
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
            
            # 優先選擇語言順序
            preferred_langs = ['en', 'ja', 'zh-Hant', 'zh-Hans', 'zh']
            transcript = None
            
            # 嘗試獲取首選語言的字幕
            for lang in preferred_langs:
                try:
                    transcript = transcript_list.find_transcript([lang])
                    break
                except:
                    continue
            
            # 如果沒有找到首選語言，使用第一個可用的字幕
            if not transcript:
                transcript = transcript_list.find_transcript([transcript_list.transcript_data[0]['language_code']])
            
            # 獲取字幕內容
            captions = transcript.fetch()
            
            # 寫入文件
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"標題: {title}\n")
                f.write(f"URL: {video_url}\n")
                f.write(f"語言: {transcript.language_code}\n")
                f.write(f"下載時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("\n=== 字幕內容 ===\n\n")
                
                # 寫入字幕內容
                for caption in captions:
                    start_time = int(caption['start'])
                    text = caption['text'].replace('\n', ' ')
                    minutes = start_time // 60
                    seconds = start_time % 60
                    f.write(f"[{minutes:02d}:{seconds:02d}] {text}\n")
            
            print(f"成功下載字幕到文件: {filename}")
            return  # 成功則退出函數
            
        except NoTranscriptFound:
            print(f"警告: 視頻 {title} 沒有可用字幕，跳過")
            return
        except TranscriptsDisabled:
            print(f"警告: 視頻 {title} 已禁用字幕，跳過")
            return
        except Exception as e:
            if attempt < max_retries - 1:
                print(f"嘗試 {attempt + 1}/{max_retries} 失敗: {str(e)}")
                time.sleep(2)  # 等待2秒後重試
                continue
            print(f"錯誤: 處理視頻 {video_url} 時發生錯誤: {str(e)}")
            return

def process_playlist(playlist_url):
    try:
        video_urls, playlist_title = list_videos_in_playlist(playlist_url)
        if not video_urls:
            print("沒有找到任何視頻")
            return

        # 建立以播放清單標題為名的目錄
        safe_playlist_title = sanitize_filename(playlist_title)
        output_dir = os.path.join(os.getcwd(), safe_playlist_title, "script")
        
        if not create_directory(output_dir):
            print("無法建立目錄，程序終止")
            return
            
        print(f"開始處理播放清單: {playlist_title}")
        print(f"輸出目錄: {output_dir}")
        print(f"共有 {len(video_urls)} 個視頻")
        
        for index, video_url in enumerate(video_urls, 1):
            download_video_info(video_url, index, output_dir)
            time.sleep(1)  # 添加延遲避免過快請求
            
    except Exception as e:
        print(f"錯誤: 處理播放清單時發生錯誤: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方式: python download_subtitles.py <播放清單URL>")
        playlist_url = "https://www.youtube.com/watch?v=auPTusg4zTo&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq"
    else:        
        playlist_url = sys.argv[1]
    
    process_playlist(playlist_url)
