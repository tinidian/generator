import os
from markdown_blocks import (
    extract_title,
    markdown_to_html_node
)
from htmlnode import ParentNode

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    source = ""
    template = ""
    with open(from_path, 'r') as f:
        source = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    title = extract_title(source)

    htmlnodes = markdown_to_html_node(source)
    html = htmlnodes.to_html()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    
    with open(dest_path, 'x') as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, item)):
            print(f"File: {os.path.join(dir_path_content, item)}")
            generate_page(os.path.join(dir_path_content,item), template_path, os.path.join(dest_dir_path, item.replace(".md", ".html")))
        else:
            print(f"Directory: {os.path.join(dest_dir_path, item)}")
            if not os.path.exists(os.path.join(dest_dir_path, item)):
                os.makedirs(os.path.join(dest_dir_path, item))
            generate_pages_recursive(os.path.join(dir_path_content, item,), template_path, os.path.join(dest_dir_path, item))
 