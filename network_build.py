import os
from pathlib import Path

script_path = Path(__file__).resolve()

project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(resources_text.readline())

following_extract_dir = resources_dir / "Following Extract"

unique_person_list = []

for file in following_extract_dir.iterdir():
    username = file.stem

    if username not in unique_person_list:
        unique_person_list.append(username)

    print(username)

    following_list = []

    with open(file, "r") as following:
        following_list = following.readlines()

    for entry in following_list:
        formatted_entry = entry[:-1]
        if formatted_entry not in unique_person_list:
            unique_person_list.append(formatted_entry)

print(unique_person_list)