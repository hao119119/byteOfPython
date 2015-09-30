import sys


class Edge:
    def __init__(self, _from=0, _to=0, _cost=0):
        self._from = _from
        self._to = _to
        self._cost = _cost

    def get_from(self):
        return self._from

    def get_to(self):
        return self._to

    def get_cost(self):
        return self._cost

    def set_from(self, _from):
        self._from = _from

    def set_to(self, _to):
        self._to = _to

    def set_cost(self, _cost):
        self._cost = _cost

    _from = property(get_from, set_from)
    _to = property(get_to, set_to)
    _cost = property(get_cost, set_cost)


# num of point
V = 10
# num of edge
E = 12
es = [Edge() for x in range(E)]
d = [0 for x in range(V)]
print es


def shortest_path(s):
    for i in range(V):
        d[i] = sys.maxint
    d[s] = 0
    while True:
        update = False
        for i in range(E):
            e = es[i]
            if d[e._from] != sys.maxint and d[e._to] > d[e._from] + e._cost:
                d[e._to] = d[e._from] + e._cost
                update = True
        if not update:
            break
