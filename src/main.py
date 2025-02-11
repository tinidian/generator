import os
import shutil
from textnode import TextNode, TextType

if os.path.exists("public"):
    os.rmdir("public")
os.mkdir("public")
shutil.copytree("src", "public")


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

main()