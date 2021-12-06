from breadth_first_search import breadth_first_search
from node import node



a= node('a')
b= node('b')
c= node('c')
d= node('d')
e= node('e')
f= node('f')
g= node('g')
h= node('h')
i= node('i')

# print(e.info)

a.add_adjacent(b)
a.add_adjacent(c)
a.add_adjacent(d)
a.add_adjacent(g)
b.add_adjacent(e)
c.add_adjacent(f)
d.add_adjacent(h)
e.add_adjacent(f)
f.add_adjacent(i)
g.add_adjacent(h)


bfs= breadth_first_search(echo=True)
bfs.set_start(a)
bfs.search('i')

print()
print('---------------------------------')
print()

bfs.set_start(h)
bfs.search('e')

print(d.info)
