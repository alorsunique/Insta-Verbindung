import os
import time
from pathlib import Path

import networkx as nx
import numpy as np
import time

script_path = Path(__file__).resolve()
project_dir = script_path.parent
os.chdir(project_dir)

with open("Resources_Path.txt", "r") as resources_text:
    resources_dir = Path(resources_text.readline())

following_extract_dir = resources_dir / "Following Extract"
output_network_dir = resources_dir / "Output Network"

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

sorted_unique_person_list = sorted(unique_person_list)

print(f"People Count: {len(sorted_unique_person_list)}")

matrix_shell = np.zeros((len(sorted_unique_person_list), len(sorted_unique_person_list)))

for file in following_extract_dir.iterdir():
    username = file.stem

    print(username)

    row_index = sorted_unique_person_list.index(username)

    with open(file, "r") as following:
        following_list = following.readlines()

    for entry in following_list:
        formatted_entry = entry[:-1]
        column_index = sorted_unique_person_list.index(formatted_entry)

        print(f"{username} | {row_index} | {formatted_entry} | {column_index}")

        matrix_shell[row_index][column_index] += 1

print(f"Creating network")

G = nx.DiGraph()

for nodes in sorted_unique_person_list:
    G.add_node(nodes)

acount = 0

while acount < len(matrix_shell):

    if sum(matrix_shell[acount]) > 0:

        bcount = 0

        while bcount < len(matrix_shell):

            if matrix_shell[acount][bcount] != 0:
                edge_weight = matrix_shell[acount][bcount]
                G.add_edge(sorted_unique_person_list[acount], sorted_unique_person_list[bcount], weight=1)

            bcount += 1

    acount += 1

leaf_nodes_list = []

for node in G.nodes:
    #print(f"{node} | {G.in_degree[node]} | {G.out_degree[node]}")
    if G.in_degree[node] < 2 and not G.out_degree[node] > 0:
        leaf_nodes_list.append(node)

for entry in leaf_nodes_list:
    print(f"Removing: {entry}")
    G.remove_node(entry)

output_path = output_network_dir / "Stripped Network.gexf"

if os.path.exists(output_path):
    os.remove(output_path)

nx.write_gexf(G, output_path)
