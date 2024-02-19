# Setup file for Insta-Verbindung

import os
from pathlib import Path

# Create the resource path text file

resources_dir_text = "Resources_Path.txt"

with open(resources_dir_text, 'a') as writer:
    pass

# Read the directory

entry_list = []

with open(resources_dir_text, 'r') as reader:
    entry_list.append(reader.read())

# Create the necessary folders

if entry_list[0]:
    resources_dir = Path(str(entry_list[0]).replace('"', ''))
    print(f"Resources Directory: {resources_dir}")

    if not resources_dir.exists():
        os.mkdir(resources_dir)

    text_input_dir = resources_dir / "Text Input"
    if not text_input_dir.exists():
        os.mkdir(text_input_dir)

    following_extract_dir = resources_dir / "Following Extract"
    if not following_extract_dir.exists():
        os.mkdir(following_extract_dir)

    network_source_dir = resources_dir / "Network Source"
    if not network_source_dir.exists():
        os.mkdir(network_source_dir)

    output_network_dir = resources_dir / "Output Network"
    if not output_network_dir.exists():
        os.mkdir(output_network_dir)

    piplup_input_dir = resources_dir / "Piplup Input"
    if not piplup_input_dir.exists():
        os.mkdir(piplup_input_dir)