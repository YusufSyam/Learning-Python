from node import node
from depth_first_search import depth_first_search

if __name__ == '__main__':
    a= node(1)
    b= node()
    b.set_data(2)
    c= node(3)
    d= node(4)
    e= node(5)
    f= node(6)

    # print(e.info)

    a.add_adjacent(b)
    a.add_adjacent(c)
    a.add_adjacent(d)
    b.add_adjacent(e)
    c.add_adjacent(f)
    e.add_adjacent(f)

    dfs= depth_first_search(echo=True)
    dfs.set_start(a)
    dfs.search(6)

    print('---------------------------------')

    dfs.set_start(d)
    dfs.search(3)

    print(e.info)