# Submitter: loganw1(Wang, Logan)
import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict


def read_graph(open_file : open) -> {str:{str}}:
    file = open_file
    graph = defaultdict(set)
    for text in file:
        relationships = text.strip().split(sep=';')
        if len(relationships) >1:
            graph[relationships[0]].add(relationships[1])
            graph[relationships[1]].add(relationships[0])
        else:
            graph[relationships[0]] = set()

    file.close()#TODO remove?
    return graph

def graph_as_str(graph : {str:{str}}) -> str:
    l=[]
    s=''
    for key,relationship in graph.items():
        l.append((key,list(relationship)))
    l.sort()
    for item in l:
        s+= '  ' + item[0] +' -> ' + str(sorted(item[1])) +'\n'
    return s


def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    infl_dict = {key:[len(relationship)-ceil(len(relationship)/2) if len(relationship) !=0 else -1,len(relationship),key] for key,relationship in graph.items()}
    rmv_can=[]
    for item in infl_dict.values():
        if item[0] >=0:
            rmv_can.append((item[0],item[1],item[2]))
    while len(rmv_can) > 0:
        min_can = min(rmv_can)
        if trace:
            print('influencer dictionary = ' + str(infl_dict))
            print('removal candidates    = ' + str(rmv_can))
            print(min_can, ' is the smallest candidate')
        key_removed = min_can[2]
        infl_dict.pop(min_can[2])
        for key,relationship in graph.items():
            if key_removed in relationship and key in infl_dict:
                infl_dict[key][0] -=1
                infl_dict[key][1] -=1

        rmv_can = []
        for item in infl_dict.values():
            if item[0] >= 0:
                rmv_can.append((item[0], item[1], item[2]))

    return {s[2] for s in infl_dict.values()}

def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    past_influence = {key:True if key in influencers else False for key in graph.keys()}
    i=0
    curr_influence = dict(past_influence)
    while curr_influence != past_influence or i==0:
        past_influence = dict(curr_influence)
        for key,relationships in graph.items():
            if len(relationships) !=0:
                net_influencers =0
                for p in relationships:
                    if past_influence[p]:
                        net_influencers +=1
                if net_influencers >= ceil(len(relationships)/2):
                    curr_influence[key] = True
        i+=1

    n =set()
    for key in curr_influence.keys():
        if curr_influence[key]:
            n.add(key)
    return n
       
            

if __name__ == '__main__':
    # Write script here
    file = safe_open('Furnish any file name containing a friendship graph', 'r', 'Illegal file name', default='graph1.txt')
    g = read_graph(file)
    print('Graph: person -> [friend of person]')
    print(graph_as_str(g))
    s =find_influencers(g,prompt.for_bool("Furnish Trace of Execution", default= True, error_message="Please enter valid bool"))
    print(s)
    user = prompt.for_string("Furnish any subset(or enter done to stop)",default=s)
    while user != 'done':
        test_set = set(user)
        set_exists = True
        for x in test_set:
            if x not in g.keys():
                set_exists = False
        if set_exists:
            print('People influenced by furnished subset('+ str((len(all_influenced(g,test_set))/len(g))*100)+'% of graph) = ' + str(all_influenced(g,test_set)))
        user = prompt.for_string("Furnish any subset(or enter done to stop)", default=s)





    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

