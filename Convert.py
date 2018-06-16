#!/usr/bin/python
"""
Convert file structure
 :arg -m : to create md file to print (pandoc Out.md -o output.pdf)
 :arg -p : to create gitpitch file
"""

import os
from pathlib import Path
import sys

class Content(object):
    """Content Container"""
    def __init__(self):
        self._content = []

    def add(self, text):
        self._content.append("{}\n".format(text))

    def get(self):
        return "".join(self._content)

excludeFolders = [".git", ".vscode", "_Assets", "_Temp", "__pycache__", "_Tools", "B_Extra"]
excludeFiles = ["__init__.py" ]
codeExtensions = [".py"]

def set_header(filePath, content, level, n):
    """ Extract header from code files """
    with open(filePath) as filetemp:
        line = filetemp.readline()
        if line.strip() == "#!/usr/bin/python":
            filetemp.readline()
        head = filetemp.readline()
        if head:
            content.add("{} {}".format("#" * (level + n), head))

def create_file(filename, content, toprint = False):
    folder = os.path.dirname(os.path.realpath(__file__))
    backupFile = os.path.join(folder, "_Temp", "_" + filename)
    newFile = os.path.join(folder, filename)
    if os.path.isfile(backupFile): os.remove(backupFile)
    if os.path.isfile(newFile): os.rename(newFile, backupFile)
    md = content.get()
    with open(newFile, "w") as file:
        file.write(md)
    if toprint:
        print(md)

def get_topic_name(path):
    t = path.split('\\')[-1].split('_')
    return " ".join(t[1:])

def md(toPrint):
    content = Content()
    #content.Add("---")
    #content.Add("geometry: margin=2cm")
    #content.Add("---")
    #content.Add("\n")
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in excludeFolders]
        level = root.count("\\")
        if level != 0:
            topicName = get_topic_name(root)
            if topicName != "Cover":
                content.add("{} {}".format("#" * (level + 1), topicName))
            files[:] = [f for f in files if f not in excludeFiles]
            for name in files:
                filePath = os.path.join(root, name)
                if name.endswith(".md"):
                    with open(filePath) as file:
                        content.add(file.read())
                if Path(name).suffix in codeExtensions:
                    set_header(filePath, content, level, 2)
                    content.add("```")
                    with open(filePath) as file:
                        content.add(file.read())
                    content.add("```")

    create_file("Output.md", content, toPrint)

def pitch(toPrint):
    content = Content()
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in excludeFolders]
        level = root.count("\\")
        if level != 0:
            topicName = get_topic_name(root)
            if topicName != "Cover":
                content.add("---\n{}  {}".format("#" * (level + 1), topicName))
            files[:] = [f for f in files if f not in excludeFiles]
            for name in files:
                filePath = os.path.join(root, name)
                if name.endswith(".md"):
                    content.add("+++?include={}".format( \
                        filePath.replace(" ", "%20").replace("\\", "/")))
                if Path(name).suffix in codeExtensions:
                    content.add("+++?code={}&lang=python".format( \
                        filePath.replace(" ", "%20").replace("\\", "/")))
                    with open(filePath, "r") as file:
                        start = currentLine = 0
                        for line in file:
                            currentLine += 1
                            if start == 0 and line not in ['\n', '\r\n']:
                                start = currentLine
                            if line in ['\n', '\r\n'] and currentLine != 1:
                                content.add("@[{}-{}]".format(start, currentLine - 1))
                                start = currentLine + 1
                        if start != 0 and currentLine != 0:
                            content.add("@[{}-{}]".format(start, currentLine))

    create_file("PITCHME.md", content, toPrint)

if __name__ == "__main__":
    commands = sys.argv[1:]
    if not commands: commands.append("-p") # create default
    if "-m" in commands: md(True)
    if "-p" in commands: pitch(True)
    print("Done")
