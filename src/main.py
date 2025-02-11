import os
import shutil
from textnode import TextNode, TextType

if os.path.exists("public"):
    shutil.rmtree("public")
# os.mkdir("public")
shutil.copytree("static", "public")


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()