import sys
import os
from lxml import etree

def read_xml_file(input_path):
    """讀取 XML 文件"""
    try:
        tree = etree.parse(input_path)
        return tree.getroot()
    except Exception as e:
        print(f"讀取文件錯誤: {str(e)}")
        return None

def convert_node_to_markdown(node, level=0):
    """將 XML 節點轉換回 Markdown"""
    result = []
    
    # 獲取節點類型
    node_type = node.get("type")
    
    if node_type == "text":
        content = node.get("content", "")
        if content:
            result.append(content)
            
    elif node_type == "strong_open":
        result.append("**")
    elif node_type == "strong_close":
        result.append("**")
        
    elif node_type == "em_open":
        result.append("*")
    elif node_type == "em_close":
        result.append("*")
        
    elif node_type == "code_inline":
        content = node.get("content", "")
        result.append(f"`{content}`")
        
    elif node_type == "link_open":
        href = node.get("href", "")
        result.append(f"[")
    elif node_type == "link_close":
        href = node.get("href", "")
        result.append(f"]({href})")
        
    elif node_type == "heading":
        level = int(node.get("level", "1"))
        content = node.get("content", "")
        result.append("#" * level + " " + content)
    
    elif node_type == "paragraph":
        content = node.get("content", "")
        if content:
            result.append(content)
    
    elif node_type == "fence":
        info = node.get("info", "")
        content = node.get("content", "")
        result.append(f"```{info}\n{content}```")
    
    elif node_type == "code_block":
        content = node.get("content", "")
        result.append(f"```\n{content}```")
    
    elif node_type == "bullet_list":
        # 處理子節點
        for child in node.xpath(".//node[@type='list_item']"):
            content = child.get("content", "").strip()
            result.append(f"- {content}")
    
    elif node_type == "ordered_list":
        # 處理子節點
        for i, child in enumerate(node.xpath(".//node[@type='list_item']"), 1):
            content = child.get("content", "").strip()
            result.append(f"{i}. {content}")
    
    elif node_type == "blockquote":
        content = node.get("content", "")
        if content:
            result.append(f"> {content}")
    
    elif node_type == "hr":
        result.append("---")
    
    elif node_type == "table":
        # 處理表格
        for child in node.xpath(".//node[@type='tr']"):
            cells = child.xpath(".//node[@type='td' or @type='th']")
            row = [cell.get("content", "").strip() for cell in cells]
            result.append("|" + "|".join(row) + "|")
            
            # 如果是表頭，添加分隔行
            if child.get("tag") == "thead":
                result.append("|" + "|".join(["---"] * len(cells)) + "|")
    
    # 處理子節點
    for child in node.findall(".//children/node"):
        child_result = convert_node_to_markdown(child, level)
        if child_result:
            result.extend(child_result)
    
    return result

def save_markdown_file(markdown_content, output_path):
    """保存 Markdown 文件"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        return True
    except Exception as e:
        print(f"保存文件錯誤: {str(e)}")
        return False

def main():
    # 檢查命令行參數
    if len(sys.argv) != 3:
        print("使用方法: python xml2md.py input.xml output.md")
        input_path = "output.xml"
        output_path = "input2.md"
    else:    
        input_path = sys.argv[1]
        output_path = sys.argv[2]
    
    # 檢查輸入文件是否存在
    if not os.path.exists(input_path):
        print(f"錯誤: 找不到輸入文件 '{input_path}'")
        return
    
    # 檢查文件副檔名
    if not input_path.endswith('.xml'):
        print("錯誤: 輸入文件必須是 XML 文件 (.xml)")
        return
    if not output_path.endswith('.md'):
        print("錯誤: 輸出文件必須是 Markdown 文件 (.md)")
        return
    
    # 讀取 XML 文件
    root = read_xml_file(input_path)
    if root is None:
        return
    
    # 轉換為 Markdown
    markdown_lines = convert_node_to_markdown(root)
    markdown_content = "\n\n".join(markdown_lines)
    
    # 保存 Markdown 文件
    if save_markdown_file(markdown_content, output_path):
        print(f"轉換完成: {output_path}")
    else:
        print("轉換失敗")

if __name__ == "__main__":
    main()
