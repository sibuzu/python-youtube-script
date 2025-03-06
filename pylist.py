import requests
import re
import sys
from urllib.parse import parse_qs, urlparse
import json

def extract_playlist_id(url):
    # 從 URL 中提取播放清單 ID
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    return query_params.get('list', [None])[0]

def list_videos_in_playlist(playlist_url):
    try:
        # 獲取播放清單 ID
        playlist_id = extract_playlist_id(playlist_url)
        if not playlist_id:
            raise ValueError("無效的播放清單 URL")

        # 構建播放清單 URL
        playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
        
        # 發送請求獲取播放清單頁面
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        response = requests.get(playlist_url, headers=headers)
        html_content = response.text
        
        # 提取播放清單標題
        title_match = re.search(r'<title>(.*?)</title>', html_content)
        title = title_match.group(1) if title_match else "未知播放清單"
        
        # 嘗試從 JSON 數據中提取視頻 ID
        json_data = re.findall(r'var ytInitialData = ({.*?});', html_content)
        video_ids = set()
        
        if json_data:
            try:
                data = json.loads(json_data[0])
                # 遍歷所有可能包含視頻ID的位置
                contents = data.get('contents', {}).get('twoColumnBrowseResultsRenderer', {}).get('tabs', [{}])[0].get('tabRenderer', {}).get('content', {}).get('sectionListRenderer', {}).get('contents', [{}])[0].get('itemSectionRenderer', {}).get('contents', [{}])[0].get('playlistVideoListRenderer', {}).get('contents', [])
                
                for content in contents:
                    video_id = content.get('playlistVideoRenderer', {}).get('videoId')
                    if video_id:
                        video_ids.add(video_id)
            except:
                pass
        
        # 如果 JSON 解析失敗，使用正則表達式作為備用方案
        if not video_ids:
            # 使用多個正則表達式模式
            patterns = [
                r'watch\?v=([0-9A-Za-z_-]{11}).*?list=' + playlist_id,
                r'videoId":"([0-9A-Za-z_-]{11})"',
                r'video-id="([0-9A-Za-z_-]{11})"'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, html_content)
                video_ids.update(matches)
        
        video_urls = [f'https://www.youtube.com/watch?v={video_id}&list={playlist_id}' for video_id in video_ids]
        video_urls = sorted(list(set(video_urls)))  # 移除重複並排序
        
        print(f"播放清單: {title}\n")
        print("影片列表:")
        for index, video_url in enumerate(video_urls, 1):
            print(f"{index}. {video_url}")
            
        print(f"\n總共有 {len(video_urls)} 個影片")
            
    except Exception as e:
        print(f"發生錯誤: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方式: python pylist.py <播放清單URL>")
        playlist_url = "https://www.youtube.com/watch?v=auPTusg4zTo&list=PLHFlSdhbIZ6SuK0pQdrJzhoFuUb-efjGq"
        # sys.exit(1)
    else:        
        playlist_url = sys.argv[1]
    list_videos_in_playlist(playlist_url)
