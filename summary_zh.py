import os
import re
from openai import OpenAI
import sys
import glob

def ensure_summary_dir(input_dir):
    """確保 summary 目錄存在"""
    summary_dir = os.path.join(input_dir, "../summary")
    if not os.path.exists(summary_dir):
        os.makedirs(summary_dir)
    return summary_dir

def get_summary_filename(original_path):
    """生成摘要文件的路徑"""
    input_dir = os.path.dirname(original_path)
    base_name = os.path.basename(original_path)
    md_name = os.path.splitext(base_name)[0] + '.md'
    return os.path.join(input_dir, "../summary", md_name)

def should_process_file(file_path):
    """檢查是否需要處理該文件"""
    summary_path = get_summary_filename(file_path)
    return not os.path.exists(summary_path)

def process_file(file_path):
    """處理單個文件"""
    print(f"\nProcessing: {file_path}")
    
    # 讀取字幕內容
    content = read_subtitle_content(file_path)
    if not content:
        print("Error: Could not find subtitle content")
        return False
        
    # 生成摘要
    summary = get_summary(content)
    
    # 保存摘要
    summary_path = save_summary(file_path, content, summary)
    
    print(f"Summary saved to: {summary_path}")
    return True

def read_subtitle_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 找到 === 字幕內容 === 之後的內容
        pattern = r"=== 字幕內容 ===\n\n([\s\S]*)"
        match = re.search(pattern, content)
        
        if match:
            subtitle_content = match.group(1)
        else:
            subtitle_content = content
        
        # 移除時間標記 [00:00]
        cleaned_content = re.sub(r'\[\d{2}:\d{2}\]\s*', '', subtitle_content)
        
        # 移除多餘的空行並整理格式
        cleaned_content = '\n'.join(
            line.strip() for line in cleaned_content.split('\n') 
            if line.strip()
        )
        
        return cleaned_content
    
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

def read_prompt():
    """讀取 prompt.txt 文件內容"""
    try:
        with open('prompt_zh.txt', 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading prompt.txt: {str(e)}")
        return "Please provide a concise summary focusing on the key points."

def get_summary(text):
    client = OpenAI(
        api_key='ollama',
        base_url='http://solarsuna.com:34567/v1'
    )
    
    try:
        content = '''
===== 文章開始 =====

{text}

===== 文章結束 =====

請整理此文章重點，使用正式的學術用語，並以小節作歸納。
歸納重點，包括但不限於主題、策略規則、回測績效、結論等小節，依實際內容可作增減。
各小節以條列格式，作清楚客觀的整理。
'''

        response = client.chat.completions.create(
            model="deepseek-r1:14b",
            messages=[
                {
                    "role": "system",
                    "content": read_prompt()
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            max_tokens=15000,
            temperature=0.7
        )
        
        summary = response.choices[0].message.content.strip()
        
        # 處理 </think> tag
        if '</think>' in summary:
            # 找到最後一個 </think> 的位置
            last_think_pos = summary.rindex('</think>')
            # 只保留 tag 之後的內容，並去除開頭的空白
            summary = summary[last_think_pos + 8:].lstrip()
            
        return summary
        
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def save_summary(original_path, content, summary):
    """保存摘要到 markdown 文件"""
    summary_path = get_summary_filename(original_path)
    
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(f"{summary}\n")
    
    return summary_path

def main():
    if len(sys.argv) != 2:
        print("Usage: python summary2.py <subtitle_dir>")
        input_dir = "Traders and Investors"
    else:    
        input_dir = sys.argv[1]
    
    input_dir = os.path.join(input_dir, "script")
    if not os.path.isdir(input_dir):
        print(f"Error: '{input_dir}' is not a directory")
        return
    
    # 確保 summary 目錄存在
    ensure_summary_dir(input_dir)
    
    # 獲取目錄下所有的 .txt 文件
    txt_files = glob.glob(os.path.join(input_dir, "*.txt"))
    
    if not txt_files:
        print(f"No .txt files found in {input_dir}")
        return
        
    print(f"Found {len(txt_files)} .txt files")
    
    # 統計處理結果
    processed = 0
    skipped = 0
    failed = 0
    
    # 處理每個文件
    for file_path in sorted(txt_files):
        if should_process_file(file_path):
            if process_file(file_path):
                processed += 1
            else:
                failed += 1
        else:
            print(f"\nSkipping (already processed): {file_path}")
            skipped += 1
    
    # 輸出統計結果
    print(f"\nSummary generation completed:")
    print(f"- Processed: {processed}")
    print(f"- Skipped (already exists): {skipped}")
    print(f"- Failed: {failed}")
    print(f"- Total files: {len(txt_files)}")

if __name__ == "__main__":
    main()
