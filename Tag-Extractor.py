import os, re


def extract_tags(directory):
    tags = set()
    for root, dirs, files in os.walk(directory):
        for file in files:
            match = re.search(r"\[(.*?)\]", file)
            if match:
                file_tags = match.group(1).split()
                tags.update(file_tags)
    return list(tags)


tags = extract_tags(input("Please enter the folder to extract tags from: "))
for i in tags:
    print(i, end=" ")
