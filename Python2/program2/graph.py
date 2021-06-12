# Submitter: loganw1(Wang, Logan)
# Defined below is a special exception for use with the Graph class methods
# Use it like any exception: e.g., raise GraphError('Graph.method" ...error indication...')

class GraphError(Exception):
    pass  # Inherit all methods, including __init__


class Graph:
    # HELPER METHODS: used for checking legal arguments to methods below
    def legal_tuple2(self, t):
        return type(t) is tuple and len(t) == 2 and \
               type(t[0]) is str and type(t[1]) is str

    def legal_tuple3(self, t):
        return type(t) is tuple and len(t) == 3 and \
               type(t[0]) is str and type(t[1]) is str and self.is_legal_edge_value(t[2])

    # __str__ and many bsc tests use the name self.edges for the outer/inner-dict.
    # So __init__ should use self.edges for the name for this dictionary
    # self should store NO other attributes: compute all results from self.edges ONLY
    # Each value in an edges tuple represents either a 
    #   (a) str    : origin node, or
    #   (b) 3-tuple: (origin node, destination node, edge value) 
    def __init__(self, legal_edge_value_predicate, *edges):
        self.__setattr__.__dict__['initialization_done'] = False
        self.is_legal_edge_value = legal_edge_value_predicate
        d = dict()
        # constructs pieces for all keys in outer dictionary, does not include outlier edges
        for edge in edges:
            if self.legal_tuple3(edge) or type(edge) == str:
                if type(edge) == str:
                    if edge not in d:
                        d[edge] = dict()
                    else:
                        raise GraphError('outlier edge already has existing dictionary')
                else:  # assumes if not outlider edge, must be a valid 3 tuple
                    if edge[0] not in d:
                        try:
                            if self.is_legal_edge_value(edge[2]):
                                d[edge[0]] = dict()
                                d[edge[0]][edge[1]] = edge[2]
                                if edge[1] not in d.keys():
                                    d[edge[1]] = dict()
                            else:
                                raise GraphError('Graph.__init__: value is not a valid value: ' + str(edge[2]))
                        except:
                            raise GraphError('Graph.__init__: value is not a valid value: ' + str(edge[2]))
                    else:
                        if edge[1] in d[edge[0]]:
                            raise GraphError('Start/Destination pair already exists')
                        else:
                            try:

                                if self.is_legal_edge_value(edge[2]):
                                    d[edge[0]][edge[1]] = edge[2]
                                    if edge[1] not in d.keys():
                                        d[edge[1]] = dict()
                                else:
                                    raise GraphError('Graph.__init__: value is not a valid value: ' + str(edge[2]))
                            except:
                                raise GraphError('Graph.__init__: value is not a valid value: ' + str(edge[2]))
            else:
                raise GraphError('graph.py __init__: invalid edge type or invalid tuple: ' + str(type(edge)))
        # lots of complexity but catches any edges involved in tuples that did not act as a starting point
        edges_missed = []
        for outer_val in d.values():
            for inner_val in outer_val.keys():
                if inner_val not in d.keys():
                    edges_missed.append(inner_val)
        for i in edges_missed:
            d[i] = dict()
        self.edges = d

        self.__setattr__.__dict__['initialization_done'] = True

    # Put all other methods here

    def __str__(self):
        s = '\nGraph:\n'
        for edge, endpoints in sorted([(x, y) for x, y in self.edges.items()]):
            s += '  ' + str(edge) + ': '
            for key, val in sorted([(u, z) for u, z in endpoints.items()]):
                s += str(key) + '(' + str(val) + '), '
            if len(endpoints) > 0:
                s = s[:-2]
            else:
                s = s[:-1]
            s += '\n'
        s = s[:-1]
        return s

    def __getitem__(self, item):
        if type(item) == None:
            raise GraphError('Graph.__getitem__: item is not valid type to look up:' + str(type(item)))
        if type(item) == str or self.legal_tuple2(item):
            if type(item) == str:
                if item in self.edges:
                    return self.edges[item]
                else:
                    raise GraphError('Graph.__getitem__: ' + item + 'cannot be found in self.edges:' + str(self.edges))
            else:
                if item[0] in self.edges:
                    if item[1] in self.edges[item[0]]:
                        return self.edges[item[0]][item[1]]
                    else:
                        raise GraphError(
                            'Graph.__getitem__: ' + str(item[1]) + 'cannot be found in self.edges[' + str(
                                item[0]) + ']: ' + str(self.edges[item[0]]))
                else:
                    raise GraphError(
                        'Graph.__getitem__: ' + str(item[0]) + 'cannot be found in self.edges:' + str(self.edges))
        else:
            raise GraphError('Graph.__getitem__: item is not valid type to look up:' + str(type(item)))

    def __setitem__(self, key, value):
        if self.legal_tuple2(key):
            if key[0] in self.edges.keys():
                if key[1] in self.edges.keys():
                    if self.is_legal_edge_value(value):
                        self.edges[key[0]][key[1]] = value
                    else:
                        raise GraphError('Graph.__setitem__: value is not a valid value: ' + str(value))
                else:
                    if self.is_legal_edge_value(value):
                        self.edges[key[0]][key[1]] = value
                        self.edges[key[1]] = dict()  # updating edges to include new point
                    else:
                        raise GraphError('Graph.__setitem__: value is not a valid value: ' + str(value))
            else:
                if self.is_legal_edge_value(value):
                    self.edges[key[0]] = dict()
                    self.edges[key[0]][key[1]] = value
                    if key[1] not in self.edges.keys():
                        self.edges[key[1]] = dict()
                else:
                    raise GraphError('Graph.__setitem__: value is not a valid value: ' + str(value))



        else:
            raise GraphError('Graph.__setitem__: key is not a valid 2 tuple: ' + str(key))

    def node_count(self):
        return len(self.edges)

    def __len__(self):
        sum = 0
        for edge in self.edges.values():
            sum += len(edge)
        return sum

    def out_degree(self, node):
        if type(node) == None:
            raise GraphError('Graph.out_degree(): argument is of type None')
        if type(node) == str and node in self.edges.keys():
            return len(self.edges[node])
        else:
            raise GraphError('Graph.out_degree(): argument(' + str(
                node) + ') is either not of type String or cannot be found in self.edges: ' + str(self.edges))

    def in_degree(self, node):
        if type(node) == None:
            raise GraphError('Graph.in_degree(): argument is of type None')
        if type(node) == str and node in self.edges.keys():
            sum = 0
            for edge in self.edges.values():
                if node in edge:
                    sum += 1
            return sum
        else:
            raise GraphError('Graph.in_degree(): argument(' + str(
                node) + ') is either not of type String or cannot be found in self.edges: ' + str(self.edges))

    def __contains__(self, item):
        if type(item) not in (str, tuple):
            raise GraphError(
                'Graph.__contains__(): item(' + str(item) + ') is of invalid type, must be String or Tuple')
        if type(item) == str:
            if item in self.edges.keys():
                return True
            else:
                return False
        elif self.legal_tuple2(item):
            if item[0] in self.edges.keys():
                if item[1] in self.edges[item[0]].keys():
                    return True
                else:
                    return False
            else:
                return False
        elif self.legal_tuple3(item):
            if item[0] in self.edges.keys():
                if item[1] in self.edges[item[0]].keys():
                    if item[2] == self.edges[item[0]][item[1]]:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            raise GraphError(
                'Graph.__contains__(): item(' + str(item) + ') is of invalid type, must be String or Tuple')

    def __delitem__(self, item):
        if type(item) not in (str, tuple):
            raise GraphError(
                'Graph.__contains__(): item(' + str(item) + ') is of invalid type, must be String or Tuple')
        if type(item) == str:
            if item in self.edges:
                del (self.edges[item])  # delets outer node
                for node, edges in self.edges.items():
                    d = dict()
                    for dest, val in edges.items():
                        if item != dest:
                            d[dest] = val
                    self.edges[node] = d
        elif self.legal_tuple2(item):
            if item[0] in self.edges.keys():
                if item[1] in self.edges[item[0]].keys():
                    del (self.edges[item[0]][item[1]])
        else:
            raise GraphError(
                'Graph.__contains__(): item(' + str(item) + ') is of invalid type, must be String or Tuple')

    def __call__(self, d):
        if type(d) != str:
            raise GraphError(
                'Graph.__call__(): d(' + str(d) + ') is of invalid type, must be String')
        if d in self.edges.keys():
            temp_d = dict()
            for node, value in self.edges.items():
                if d in value.keys():
                    temp_d[node] = value[d]
            return temp_d
        else:
            raise GraphError(
                'Graph.__call__(): d(' + str(d) + ') is not a node in self.edges: ' + str(self.edges))

    def clear(self):
        l = [str(x) for x in self.edges.keys()]
        for i in l:
            del (self.edges[i])
        # self.edges = dict()

    def dump(self, open_file, sep=':', fnctn=str):
        l = []

        for edge, endpoints in sorted([(x, y) for x, y in self.edges.items()]):
            s = fnctn(edge) + str(sep)
            for key, val in sorted([(u, z) for u, z in endpoints.items()]):
                s += fnctn(key) + str(sep) + fnctn(val) + str(sep)
            s = s[:-1] + '\n'
            l.append(s)
        open_file.writelines(l)
        open_file.close()

    def load(self, open_file, sep=':', fnctn=int):
        l = []
        d = dict()
        for text in open_file:
            point_edge_split_text = text.strip().split(sep, 1)
            if len(point_edge_split_text) > 1:
                point, edges = point_edge_split_text
                l.append((point, edges))
                d[point] = dict()
            else:
                d[text.strip()] = dict()
        for point, edges in l:
            i = 0
            s = edges.split(sep)
            for p in range(0, len(s), 2):
                d[point][s[i]] = fnctn(s[i + 1])
                i += 2
        self.clear()
        for point, edges in d.items():
            self.edges[point] = edges
        open_file.close()

    def reverse(self):
        reverse_g = Graph(self.is_legal_edge_value)

        for point, values in self.edges.items():
            if len(values.items()) == 0:
                if point not in reverse_g.edges.keys():
                    reverse_g.edges[point] = dict()
            for dest, value in values.items():
                reverse_g.__setitem__((dest, point), value)
        return reverse_g

    def natural_subgraph(self, *nodes):
        g = Graph(self.is_legal_edge_value)
        l=[]
        for node in nodes:
            if type(node) != str:
                raise GraphError('Graph.natural_subgraph(): argument: ' + str(node) + ' is not of type String')
        for key in nodes:
            if key in self.edges.keys():
                g.edges[key] = dict()
        for point,edges in self.edges.items():
            if point in nodes:
                for edge,value in edges.items():
                    if edge in nodes:
                        g[point][edge] = value
        return g
    def __iter__(self):
        def gen(l):
            for item in l:
                yield item

        l = []
        for edge, endpoints in sorted([(x, y) for x, y in self.edges.items()]):
            if len(endpoints.items()) == 0:
                r = False
                for p, v in self.edges.items():
                    if edge in v.keys():
                        r = True
                if r == False:
                    l.append(edge)
            for key, val in sorted([(u, z) for u, z in endpoints.items()]):
                l.append((edge, key, val))
        return gen(l)

    def __eq__(self, compareObj: 'Graph') -> bool:
        if type(compareObj) == Graph:
            if len(self.edges.keys()) == len(compareObj.edges.keys()):
                for point, edges in self.edges.items():
                    if edges != compareObj.edges[point]:
                        return False
                return True
            else:
                return False
        else:
            return False

    def __le__(self, compareObj: 'Graph') -> bool:
        if type(compareObj) == Graph:
            for point, edges in self.edges.items():
                for dest, val in edges.items():
                    if val != compareObj.edges[point][dest]:
                        return False
                if len(edges.items()) == 0:
                    if point not in compareObj.edges.keys():
                        return False
            return True
        else:
            return False  # maybe raise Graph exception instead

    def __setattr__(self, name, value):
        if self.__setattr__.initialization_done:
            raise AssertionError('Graph.__setattr__: Cannot assign or rebind attributes after __init__')
        else:
            self.__dict__[name] = value
            if name == 'edges':
                self.__setattr__.__dict__['initialization_done'] = True

    def make_graph_copy(self):
        d = dict()
        for point,edges in self.edges.items():
            d[point] = dict()
            for edge,value in edges.items():
                d[point][edge]=value
        g = Graph(self.is_legal_edge_value)
        for point, edges in d.items():
            g.edges[point] = edges
        return g #returns new instance of exact replica of current Graph

    def __add__(self, other):
        if type(other) not in (Graph,str,tuple):
            raise GraphError('Graph.__add__: item being added not of type Graph,str, or tuple')
        if type(other) == Graph:
            g1 = self.make_graph_copy()
            g2 = other.make_graph_copy()
            for point,edges in g1.edges.items():
                if point not in g2.edges.keys():
                    g2.edges[point] = dict()
                for edge,value in edges.items():
                    g2.edges[point][edge] = value
            return g2
        elif type(other) == str:
            g = self.make_graph_copy()
            if other not in self.edges.keys():
                g.edges[other] = dict()
            return g
        elif self.legal_tuple3(other):
            g = self.make_graph_copy()
            if other[0] in self.edges.keys():
                if self.is_legal_edge_value(other[2]):
                    g.edges[other[0]][other[1]] = other[2]
                    if other[1] not in g.edges.keys():
                        g.edges[other[1]] = dict()
                    return g
                else:
                    raise GraphError('Graph.__add__: value being added/updated: ' + str(other[2]) +' is not valid')

            else:
                g.edges[other[0]] = dict()
                if self.is_legal_edge_value(other[2]):
                    g.edges[other[0]][other[1]] = other[2]
                    if other[1] not in g.edges.keys():
                        g.edges[other[1]] = dict()
                    return g
                else:
                    raise GraphError('Graph.__add__: value being added/updated: ' + str(other[2]) + ' is not valid')
        else:
            raise GraphError('Graph.__add__: item being added not of type Graph,str, or legal 3 tuple')

    def __radd__(self, other):
        if type(other) not in (str,tuple):
            raise GraphError('Graph.__add__: item being added not of type Graph,str, or tuple')
        if type(other) == str:
            g = self.make_graph_copy()
            if other not in self.edges.keys():
                g.edges[other] = dict()
            return g
        elif self.legal_tuple3(other):
            g = self.make_graph_copy()
            if other[0] in self.edges.keys():
                if self.is_legal_edge_value(other[2]):
                    g.edges[other[0]][other[1]] = other[2]
                    if other[1] not in g.edges.keys():
                        g.edges[other[1]] = dict()
                    return g
                else:
                    raise GraphError('Graph.__add__: value being added/updated: ' + str(other[2]) +' is not valid')

            else:
                g.edges[other[0]] = dict()
                if self.is_legal_edge_value(other[2]):
                    g.edges[other[0]][other[1]] = other[2]
                    if other[1] not in g.edges.keys():
                        g.edges[other[1]] = dict()
                    return g
                else:
                    raise GraphError('Graph.__add__: value being added/updated: ' + str(other[2]) + ' is not valid')
        else:
            raise GraphError('Graph.__add__: item being added not of type Graph,str, or legal 3 tuple')

    def __iadd__(self, other):
        if type(other) not in (Graph,str,tuple):
            raise GraphError('Graph.__add__: item being added not of type Graph,str, or tuple')
        if type(other) == Graph:
            g1 = self.make_graph_copy()
            g2 = other.make_graph_copy()
            for point,edges in g1.edges.items():
                if point not in g2.edges.keys():
                    g2.edges[point] = dict()
                for edge,value in edges.items():
                    g2.edges[point][edge] = value
            self.clear()
            for point, edges in g2.edges.items():
                self.edges[point] = edges
            return self
        elif type(other) == str:
            if other not in self.edges.keys():
                self.edges[other] = dict()
            return self
        elif self.legal_tuple3(other):
            if other[0] in self.edges.keys():
                if self.is_legal_edge_value(other[2]):
                    self.edges[other[0]][other[1]] = other[2]
                    if other[1] not in self.edges.keys():
                        self.edges[other[1]] = dict()
                    return self
                else:
                    raise GraphError('Graph.__add__: value being added/updated: ' + str(other[2]) +' is not valid')

            else:
                self.edges[other[0]] = dict()
                if self.is_legal_edge_value(other[2]):
                    self.edges[other[0]][other[1]] = other[2]
                    if other[1] not in self.edges.keys():
                        self.edges[other[1]] = dict()
                    return self
                else:
                    raise GraphError('Graph.__add__: value being added/updated: ' + str(other[2]) + ' is not valid')
        else:
            raise GraphError('Graph.__add__: item being added not of type Graph,str, or legal 3 tuple')


if __name__ == '__main__':
    # Simple tests before running driver
    # Put your own test code here to test DictList before doing bsc tests

    print('Start simple testing')
    g = Graph((lambda x: type(x) is int), ('a', 'b', 1), ('a', 'c', 3), ('b', 'a', 2), ('d', 'b', 2), ('d', 'c', 1),
              'e')
    print(g)
    print(g['a'])
    print(g['a', 'b'])
    print(g.node_count())
    print(len(g))
    print(g.out_degree('c'))
    print(g.in_degree('a'))
    print('c' in g)
    print(('a', 'b') in g)
    print(('a', 'b', 1) in g)
    print(g('c'))
    print(g.reverse())
    print(g.natural_subgraph('a','b','c'))
    print()

    import driver

    driver.default_file_name = 'bscp22W21.txt'
    #     driver.default_show_exception = True
    #     driver.default_show_exception_message = True
    #     driver.default_show_traceback = True
    driver.driver()
