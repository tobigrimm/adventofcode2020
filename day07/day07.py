#!/usr/bin/env python3
import sys
import re
from typing import List, Set
import networkx as nx

def count_bags(graph, node):
    number = 1
    for subnode, amount in G[node].items():
        print(subnode, amount)
        subnum = count_bags(G, subnode)
        number += amount['num'] * subnum
        print(subnum, number)
    return number

if __name__ == "__main__":
    G = nx.DiGraph()
    with open(sys.argv[1], "r") as infile:
        for nextline in infile:
            search = "(?P<amount>[0-9])+\ (?P<color>[a-z]*\ [a-z]*)\ bag[s]?"
            left, right = nextline.strip().split("bags contain")
            left = left.strip()
            right = right.strip()
            matches = re.finditer(search, right)
            G.add_node(left)
            for m in matches:
                amount = int(m.group("amount"))
                color = m.group("color")
                #G.add_node(color)
                G.add_edge(left, color, num=int(amount))

    print("Part 1: ", len(nx.ancestors(G, 'shiny gold')))
    print(nx.descendants(G, 'shiny gold'))
    print(G['shiny gold'])
    print(count_bags(G, 'shiny gold'))
    # print(nx.dfs_predecessors(G,"shiny gold"))
    # print(nx.dfs_successors(G,"shiny gold"))
    # print(len(nx.dfs_predecessors(G,"shiny gold")))
    # print(list(nx.edge_dfs(G,'shiny gold', orientation='reverse')))
    # print(list(nx.dfs_edges(G,'shiny gold')))

    # print(
    #     "part 1: ",
    #     sum([check_group(group) for group in groups]),
    #     " answered yes",
    # )
    # print(
    #     "part 2: ",
    #     sum([check_group(group, False) for group in groups]),
    #     " answered yes",
    # )
