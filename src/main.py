import os
import shutil
from page_generator import generate_page



def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    shutil.copytree("static", "public")

    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"

    generate_page(from_path, template_path, dest_path)

main()