import os
from pathlib import Path

import pandas as pd

script_path = Path(__file__).resolve()
project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(resources_text.readline())

piplup_input_dir = resources_dir / "Piplup Input"
following_extract_dir = resources_dir / "Following Extract"

for file in piplup_input_dir.iterdir():
    import_dataframe = pd.read_excel(file)

    following_list = []

    for index, row in import_dataframe.iterrows():
        entry = row.iloc[0]
        formatted_entry = entry.split(" ")[1]
        following_list.append(formatted_entry)

    sorted_following_list = sorted(following_list)

    output_text_path = following_extract_dir / f"{str(file.stem)[:-10]}.txt"
    if output_text_path.exists():
        os.remove(output_text_path)

    with open(output_text_path, "w") as output_file:
        for following in sorted_following_list:
            output_file.write(f"{following}\n")
