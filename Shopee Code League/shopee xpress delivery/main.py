from cost_node import cost_node as node
from dijkstra import dijkstra

m= 8
n= 8

grid= '''0 0 1 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0'''.split('\n')

grid= '''0 0 0 0 0 1 0 0
0 1 0 0 0 0 2 0
0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0
0 0 0 0 0 2 0 2
0 0 0 0 0 0 0 0
0 0 3 0 0 0 0 3
0 0 0 2 0 0 0 0'''.split('\n')

grid= [[int(j) for j in i.split(' ')] for i in grid]
node_list= [[node(f'{i},{j}') for j in range(n)]for i in range(m)]

shortcut_list= {}
for i in range(m):
    for j in range(n):
        if(j<n-1):
            node_list[i][j].add_adjacent(node_list[i][j+1], 1)

        if(i<m-1):
            node_list[i][j].add_adjacent(node_list[i+1][j], 1)

        if(j>0):
            node_list[i][j].add_adjacent(node_list[i][j - 1], 1)

        if(i>0):
            node_list[i][j].add_adjacent(node_list[i - 1][j], 1)

        if(grid[i][j]!=0):
            if(grid[i][j] in list(shortcut_list.keys())):
                for k in shortcut_list[grid[i][j]]:
                    node_list[i][j].add_adjacent(k, 0)

                shortcut_list[grid[i][j]].append(node_list[i][j])
            else:
                shortcut_list[grid[i][j]]= [node_list[i][j]]

dij= dijkstra(node_list[0][0])
dij.search_shortest_path(node_list[m-1][n-1])
# dij.show_dijkstra_table()
