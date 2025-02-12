import os
import shutil
from page_generator import generate_pages_recursive



def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    shutil.copytree("static", "public")

    from_path = "content"
    template_path = "template.html"
    dest_path = "public"

    generate_pages_recursive(from_path, template_path, dest_path)

    # generate_page(from_path, template_path, dest_path)

main()