import os
from pathlib import Path

script_path = Path(__file__).resolve()

project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(resources_text.readline())

input_text_dir = resources_dir / "Input Text"
following_extract_dir = resources_dir / "Following Extract"

for text_file in input_text_dir.iterdir():
    with open(text_file, "r", encoding="utf-8") as following:
        import_list = following.readlines()

    below_count = import_list.index("Contact Uploading & Non-Users\n")
    raw_following_list = import_list[below_count:]

    following_list = []

    for entry in raw_following_list:
        if "profile picture" in entry:
            following_list.append(entry[:-19])

    sorted_following_list = sorted(following_list)

    output_text_path = following_extract_dir / f"{text_file.stem}.txt"
    if output_text_path.exists():
        os.remove(output_text_path)

    with open(output_text_path, "w") as output_file:
        for following in sorted_following_list:
            output_file.write(f"{following}\n")
