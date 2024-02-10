# Setup file for Insta-Verbindung

import os
from pathlib import Path

# Create the resource path text file

resources_dir_text = "Resources_Path.txt"

with open(resources_dir_text, 'a') as writer:
    writer.close()

# Read the directory

entry_list = []

with open(resources_dir_text, 'r') as reader:
    entry_list.append(reader.read())
    reader.close()

# Create the necessary folders

if entry_list[0]:
    resources_dir = Path(entry_list[0])
    print(f"Resources Directory: {resources_dir}")

    if not resources_dir.exists():
        os.mkdir(resources_dir)

    input_text_dir = resources_dir / "Input Text"

    if not input_text_dir.exists():
        os.mkdir(input_text_dir)

    following_extract_dir = resources_dir / "Following Extract"

    if not following_extract_dir.exists():
        os.mkdir(following_extract_dir)
