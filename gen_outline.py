import os
import sys
import glob

def read_script_info(script_file):
    """讀取腳本文件中的標題和URL"""
    try:
        with open(script_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            title = lines[0].replace('標題: ', '').strip()
            url = lines[1].replace('URL: ', '').strip()
            return title, url
    except Exception as e:
        print(f"Error reading script file {script_file}: {str(e)}")
        return None, None

def read_summary_content(summary_file):
    """讀取摘要文件的內容"""
    try:
        with open(summary_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"Error reading summary file {summary_file}: {str(e)}")
        return ""

def generate_outline(input_dir, output_file):
    """生成大綱文件"""
    # 確保目錄存在
    script_dir = os.path.join(input_dir, "script")
    summary_dir = os.path.join(input_dir, "summary")
    
    if not os.path.exists(script_dir) or not os.path.exists(summary_dir):
        print(f"Error: Required directories not found in {input_dir}")
        return False
    
    # 讀取模板
    try:
        with open('output_template.md', 'r', encoding='utf-8') as f:
            template = f.read()
    except Exception as e:
        print(f"Error reading template: {str(e)}")
        return False
    
    # 獲取所有腳本文件
    script_files = sorted(glob.glob(os.path.join(script_dir, "*.txt")))
    
    # 準備輸出內容
    output_content = template.replace("{dir_name}", os.path.basename(input_dir))
    
    # 創建詳細內容部分
    details_template = """<details>
<summary>{#}. {標題}</summary>

[[Youtube]]({URL})

{summary_file}
</details>

"""
    
    details_sections = []
    for script_file in script_files:
        basename = os.path.basename(script_file)
        number = basename[:3]  # 獲取前三個字符 (001, 002, etc.)
        
        # 找到對應的摘要文件
        summary_file = os.path.join(
            summary_dir, 
            os.path.splitext(basename)[0] + '.md'
        )
        
        if not os.path.exists(summary_file):
            print(f"Warning: Summary file not found for {basename}")
            continue
        
        # 讀取必要信息
        title, url = read_script_info(script_file)
        if not title or not url:
            continue
            
        summary_content = read_summary_content(summary_file)
        
        # 創建詳細部分
        detail_section = details_template.format(
            **{
                "#": number,
                "標題": title,
                "summary_file": summary_content,
                "URL": url
            }
        )
        details_sections.append(detail_section)
    
    # 組合最終內容
    final_content = output_content.split("<details>")[0] + "".join(details_sections)
    
    # 寫入輸出文件
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Successfully generated {output_file}")
        return True
    except Exception as e:
        print(f"Error writing output file: {str(e)}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python gen_outline.py <input_dir>")
        return
    
    input_dir = sys.argv[1]
    output_file = os.path.basename(input_dir) + ".md"
    
    if not os.path.isdir(input_dir):
        print(f"Error: {input_dir} is not a directory")
        return
        
    generate_outline(input_dir, output_file)

if __name__ == "__main__":
    main()