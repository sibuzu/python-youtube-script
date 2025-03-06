import os
import sys
import markdown
import html2text
from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cloud-translation-key.json"

def ensure_chinese_dir(input_file_path):
    """確保 chinese 目錄存在"""
    input_dir = os.path.dirname(input_file_path)
    chinese_dir = os.path.join(input_dir, "../chinese")
    if not os.path.exists(chinese_dir):
        os.makedirs(chinese_dir)
    return chinese_dir

def get_chinese_filename(original_path):
    """生成翻譯後文件的路徑"""
    input_dir = os.path.dirname(original_path)
    base_name = os.path.basename(original_path)
    return os.path.join(input_dir, "../chinese", base_name)

def should_translate_file(file_path):
    """檢查是否需要翻譯該文件"""
    chinese_path = get_chinese_filename(file_path)
    return not os.path.exists(chinese_path)

def read_markdown(file_path):
    """讀取 markdown 文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

def translate_markdown(text, target_language="zh-TW"):
    # 1. Markdown 转 HTML
    html_text = markdown.markdown(text)

    # 2. 调用 Google 翻译 API
    client = translate.Client()
    result = client.translate(html_text, target_language=target_language, format_="html");
    translated_html = result["translatedText"]

    # 3. HTML 转回 Markdown
    md_text = html2text.html2text(translated_html)

    return md_text.strip()

def save_translation(original_path, translation):
    """保存翻譯結果"""
    chinese_path = get_chinese_filename(original_path)
    try:
        with open(chinese_path, 'w', encoding='utf-8') as f:
            f.write(translation)
        return True
    except Exception as e:
        print(f"Error saving translation: {str(e)}")
        return False

def process_file(file_path):
    """處理單個文件"""
    print(f"\nProcessing: {file_path}")
    
    # 讀取 markdown 內容
    content = read_markdown(file_path)
    if not content:
        return False
    
    # 翻譯內容
    translation = translate_markdown(content)
    if not translation:
        return False
    
    # 保存翻譯
    if save_translation(file_path, translation):
        print(f"Translation saved to: {get_chinese_filename(file_path)}")
        return True
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python translate.py <markdown_file>")
        file_path = "Traders and Investors/summary/001-Quantified Strategies - Introduction.md"
    else:    
        file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found")
        return
        
    if not file_path.endswith('.md'):
        print("Error: Input file must be a markdown file (.md)")
        return
    
    # 確保 chinese 目錄存在
    ensure_chinese_dir(file_path)
    
    # 檢查是否需要翻譯
    if should_translate_file(file_path):
        if process_file(file_path):
            print("Translation completed successfully")
        else:
            print("Translation failed")
    else:
        print(f"Skipping (already translated): {file_path}")

if __name__ == "__main__":
    main()