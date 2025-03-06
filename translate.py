import os
import sys
from google.cloud import translate_v2 as translate
import html
import time
import re
from markdown import markdown
from bs4 import BeautifulSoup

def ensure_chinese_dir(input_file_path):
    """確保 chinese 目錄存在"""
    input_dir = os.path.dirname(input_file_path)
    chinese_dir = os.path.join(input_dir, "chinese")
    if not os.path.exists(chinese_dir):
        os.makedirs(chinese_dir)
    return chinese_dir

def get_chinese_filename(original_path):
    """生成翻譯後文件的路徑"""
    input_dir = os.path.dirname(original_path)
    base_name = os.path.basename(original_path)
    return os.path.join(input_dir, "chinese", base_name)

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

class MarkdownTranslator:
    def __init__(self):
        self.translate_client = translate.Client()
        self.protected_blocks = {}
        self.block_counter = 0

    def protect_code_blocks(self, text):
        """保護代碼塊"""
        def replace_code_block(match):
            block_id = f"CODE_BLOCK_{self.block_counter}"
            self.protected_blocks[block_id] = match.group(0)
            self.block_counter += 1
            return block_id

        # 保護多行代碼塊
        text = re.sub(r'```[\s\S]*?```', replace_code_block, text)
        # 保護行內代碼
        text = re.sub(r'`[^`]+`', replace_code_block, text)
        return text

    def restore_protected_blocks(self, text):
        """還原被保護的內容"""
        for block_id, content in self.protected_blocks.items():
            text = text.replace(block_id, content)
        return text

    def translate_text(self, text, max_retries=3):
        """翻譯文本"""
        # 首先保護代碼塊
        text = self.protect_code_blocks(text)
        
        # 將 Markdown 轉換為 HTML
        html_content = markdown(text)
        
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 獲取所有文本節點
        text_nodes = []
        for element in soup.find_all(text=True):
            if element.parent.name not in ['code', 'pre']:  # 排除代碼塊
                text_nodes.append(element)
        
        # 翻譯每個文本節點
        for node in text_nodes:
            if not node.strip():  # 跳過空白節點
                continue
                
            original_text = node.string
            if not any(char.isalpha() for char in original_text):  # 跳過純數字或符號
                continue
                
            for attempt in range(max_retries):
                try:
                    result = self.translate_client.translate(
                        original_text,
                        target_language='zh-TW',
                        source_language='en',
                        format='html'  # 使用 HTML 格式
                    )
                    
                    translated_text = html.unescape(result['translatedText'])
                    node.string.replace_with(translated_text)
                    
                    # 添加延遲避免超過 API 限制
                    time.sleep(0.1)
                    break
                    
                except Exception as e:
                    if attempt == max_retries - 1:
                        print(f"Error translating text: {str(e)}")
                    time.sleep(1)
        
        # 將 HTML 轉回 Markdown 格式
        translated_html = str(soup)
        
        # 使用正則表達式恢復 Markdown 語法
        # 恢復標題
        translated_html = re.sub(r'<h1>(.*?)</h1>', r'# \1', translated_html)
        translated_html = re.sub(r'<h2>(.*?)</h2>', r'## \1', translated_html)
        translated_html = re.sub(r'<h3>(.*?)</h3>', r'### \1', translated_html)
        translated_html = re.sub(r'<h4>(.*?)</h4>', r'#### \1', translated_html)
        
        # 恢復列表
        translated_html = re.sub(r'<ul>\s*<li>(.*?)</li>\s*</ul>', r'- \1', translated_html)
        translated_html = re.sub(r'<ol>\s*<li>(.*?)</li>\s*</ol>', r'1. \1', translated_html)
        
        # 恢復強調
        translated_html = re.sub(r'<strong>(.*?)</strong>', r'**\1**', translated_html)
        translated_html = re.sub(r'<em>(.*?)</em>', r'*\1*', translated_html)
        
        # 恢復鏈接
        translated_html = re.sub(r'<a href="(.*?)">(.*?)</a>', r'[\2](\1)', translated_html)
        
        # 清理 HTML 標籤
        translated_html = re.sub(r'<[^>]+>', '', translated_html)
        
        # 還原被保護的代碼塊
        final_text = self.restore_protected_blocks(translated_html)
        
        return final_text

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
    translator = MarkdownTranslator()
    translation = translator.translate_text(content)
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
        return
        
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