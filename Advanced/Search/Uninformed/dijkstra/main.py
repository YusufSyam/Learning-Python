from cost_node import cost_node as node
from dijkstra import dijkstra

a= node('a')
b= node('b')
c= node('c')
d= node('d')
e= node('e')
f= node('f')
g= node('g')
h= node('h')
i= node('i')

a.add_adjacent(b, 6)
a.add_adjacent(d, 1)
b.add_adjacent(c, 5)
b.add_adjacent(d, 2)
b.add_adjacent(e, 2)
c.add_adjacent(e, 5)
d.add_adjacent(e, 1)

dij= dijkstra(a, echo=True)
dij.search_shortest_path(c)
dij.show_dijkstra_table()

print('-----------')
dij.search_shortest_path(b)