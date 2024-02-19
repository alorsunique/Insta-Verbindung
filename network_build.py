import os
from pathlib import Path

import networkx as nx
import numpy as np


def unique_people_extract(file_list):
    unique_person_list = []
    for file in file_list:
        username = file.stem

        if username not in unique_person_list:
            unique_person_list.append(username)

        with open(file, "r") as following:
            following_list = following.readlines()

        for entry in following_list:
            formatted_entry = entry[:-1]
            if formatted_entry not in unique_person_list:
                unique_person_list.append(formatted_entry)

    return sorted(unique_person_list)


def matrix_shell_create(file_list, unique_person_list):
    print(f"People Count: {len(unique_person_list)}")

    matrix_shell = np.zeros((len(unique_person_list), len(unique_person_list)))

    for file in file_list:
        username = file.stem
        row_index = sorted_unique_person_list.index(username)

        with open(file, "r") as following:
            following_list = following.readlines()

        for entry in following_list:
            formatted_entry = entry[:-1]
            column_index = sorted_unique_person_list.index(formatted_entry)

            # print(f"{username} | {row_index} | {formatted_entry} | {column_index}")

            matrix_shell[row_index][column_index] += 1

    return matrix_shell


def network_create(unique_person_list, matrix_shell):
    G = nx.DiGraph()
    for nodes in unique_person_list:
        G.add_node(nodes)

    acount = 0
    while acount < len(matrix_shell):

        if sum(matrix_shell[acount]) > 0:

            bcount = 0

            while bcount < len(matrix_shell):

                if matrix_shell[acount][bcount] != 0:
                    edge_weight = matrix_shell[acount][bcount]
                    G.add_edge(unique_person_list[acount], unique_person_list[bcount], weight=1)

                bcount += 1
        acount += 1
    return G


script_path = Path(__file__).resolve()
project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(resources_text.readline())

network_source_dir = resources_dir / "Network Source"
output_network_dir = resources_dir / "Output Network"

folder_list = []

for entry in network_source_dir.iterdir():
    if entry.is_dir():
        folder_list.append(entry.name)

for folder in folder_list:
    new_source_dir = network_source_dir / folder
    subnetwork_file_list = []
    for entry in new_source_dir.iterdir():
        subnetwork_file_list.append(entry)

    sorted_unique_person_list = unique_people_extract(subnetwork_file_list)
    matrix_shell = matrix_shell_create(subnetwork_file_list, sorted_unique_person_list)
    G = network_create(sorted_unique_person_list, matrix_shell)

    output_path = output_network_dir / f"{folder}_Network.gexf"

    if os.path.exists(output_path):
        os.remove(output_path)

    nx.write_gexf(G, output_path)

# Global network create done here

global_file_list = []
for entry in network_source_dir.rglob('*'):
    if entry.is_file():
        global_file_list.append(entry)

sorted_unique_person_list = unique_people_extract(global_file_list)
matrix_shell = matrix_shell_create(global_file_list, sorted_unique_person_list)
G = network_create(sorted_unique_person_list, matrix_shell)

output_path = output_network_dir / f"Global_Network.gexf"

if os.path.exists(output_path):
    os.remove(output_path)

nx.write_gexf(G, output_path)
