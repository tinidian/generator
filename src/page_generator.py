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

    
    with open(dest_path, 'w') as f:
        f.write(template)
 