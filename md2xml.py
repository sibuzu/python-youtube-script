import sys
import os
from markdown_it import MarkdownIt
from lxml import etree

def read_markdown_file(input_path):
    """讀取 Markdown 文件"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"讀取文件錯誤: {str(e)}")
        return None

def convert_token_to_xml(token, parent_element):
    """將 markdown-it token 轉換為 XML 元素"""
    # 創建元素
    element = etree.SubElement(parent_element, "node")
    element.set("type", token.type)
    
    # 保存重要屬性
    if token.tag:
        element.set("tag", token.tag)
    if token.level is not None:
        element.set("level", str(token.level))
    if token.markup:
        element.set("markup", token.markup)
    if token.info:
        element.set("info", token.info)
    if token.content:
        element.set("content", token.content)
    
    # 保存其他可能有用的屬性
    attrs = getattr(token, 'attrs', None)
    if attrs:
        attrs_element = etree.SubElement(element, "attrs")
        for key, value in attrs:
            attr_element = etree.SubElement(attrs_element, "attr")
            attr_element.set("key", key)
            attr_element.set("value", value)
    
    # 處理子節點
    if token.children:
        children_element = etree.SubElement(element, "children")
        for child in token.children:
            convert_token_to_xml(child, children_element)
    
    return element

def markdown_to_xml(markdown_text):
    """將 Markdown 轉換為 XML"""
    # 初始化 markdown-it
    md = MarkdownIt('commonmark')
    
    # 解析 markdown
    tokens = md.parse(markdown_text)
    
    # 創建 XML 根元素
    root = etree.Element("markdown")
    
    # 轉換所有 token
    for token in tokens:
        convert_token_to_xml(token, root)
    
    # 返回格式化的 XML
    return etree.tostring(root, pretty_print=True, encoding='unicode')

def save_xml_file(xml_content, output_path):
    """保存 XML 文件"""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        return True
    except Exception as e:
        print(f"保存文件錯誤: {str(e)}")
        return False

def main():
    # 檢查命令行參數
    if len(sys.argv) != 3:
        print("使用方法: python md2xml.py input.md output.xml")
        return
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # 檢查輸入文件是否存在
    if not os.path.exists(input_path):
        print(f"錯誤: 找不到輸入文件 '{input_path}'")
        return
    
    # 檢查文件副檔名
    if not input_path.endswith('.md'):
        print("錯誤: 輸入文件必須是 Markdown 文件 (.md)")
        return
    if not output_path.endswith('.xml'):
        print("錯誤: 輸出文件必須是 XML 文件 (.xml)")
        return
    
    # 讀取 Markdown 文件
    markdown_text = read_markdown_file(input_path)
    if markdown_text is None:
        return
    
    # 轉換為 XML
    xml_content = markdown_to_xml(markdown_text)
    
    # 保存 XML 文件
    if save_xml_file(xml_content, output_path):
        print(f"轉換完成: {output_path}")
    else:
        print("轉換失敗")

if __name__ == "__main__":
    main()