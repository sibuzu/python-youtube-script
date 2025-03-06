import os
import re
from openai import OpenAI
import sys

def ensure_summary_dir(input_file_path):
    """確保 summary 目錄存在"""
    # 獲取輸入文件的目錄
    input_dir = os.path.dirname(input_file_path)
    # 在輸入文件目錄下創建 summary 子目錄
    summary_dir = os.path.join(input_dir, "summary")
    if not os.path.exists(summary_dir):
        os.makedirs(summary_dir)
    return summary_dir

def get_summary_filename(original_path):
    """生成摘要文件的路徑"""
    # 獲取輸入文件的目錄
    input_dir = os.path.dirname(original_path)
    # 獲取原始文件名（不含路徑）
    base_name = os.path.basename(original_path)
    # 更改副檔名為 .md
    md_name = os.path.splitext(base_name)[0] + '.md'
    # 組合完整路徑
    return os.path.join(input_dir, "summary", md_name)

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
        
        subtitle_content = match.group(1)
        
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
    
def get_summary(text):
    client = OpenAI(
        api_key='ollama',
        base_url='http://solarsuna.com:34567/v1'
    )
    
    try:
        response = client.chat.completions.create(
            model="deepseek-r1:14b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes trading strategies.\nPlease provide a concise summary focusing on the key trading rules and performance metrics."
                },
                {
                    "role": "user",
                    "content": f"Please summarize this trading strategy:\n\n{text}"
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
        print("Usage: python summary.py <subtitle_file>")
        file_path = "TRADING STRATEGIES Backtested - Shorts/001-Simple Bond Trading Strategy (Backtest & Rules) #shorts #short.txt"
    else:    
        file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found")
        return
    
    # 確保 summary 目錄存在
    ensure_summary_dir(file_path)
    
    # 讀取字幕內容
    content = read_subtitle_content(file_path)
    if not content:
        print("Error: Could not find subtitle content")
        return
        
    # 生成摘要
    summary = get_summary(content)
    
    # 保存摘要
    summary_path = save_summary(file_path, content, summary)
    
    print(f"\nSummary has been saved to: {summary_path}")

if __name__ == "__main__":
    main()
