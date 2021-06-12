# Submitter: loganw1(Wang, Logan)
import prompt 
from goody       import safe_open,irange
from collections import defaultdict # Use defaultdict for prefix and query


def all_prefixes(fq : (str,)) -> {(str,)}:
    return {fq[:i] for i in irange(len(fq))}


def add_query(prefix : {(str,):{(str,)}}, query : {(str,):int}, new_query : (str,)) -> None:
    for queries in all_prefixes(new_query):
        prefix[queries].add(new_query)
    query[new_query] +=1


def read_queries(open_file : open) -> ({(str,):{(str,)}}, {(str,):int}):
    prefix = defaultdict(set)
    query = defaultdict(int)
    for text in open_file:
        new_query = tuple(text.strip().split())
        add_query(prefix,query,new_query)

    return (prefix,query)


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    s = ''
    l=[(q,num) for q,num in d.items()]
    #if type(l[0][1]) == int:
    #    l= sorted([(-num,q) for q,num in d.items()],key = key,reverse=  reverse)
    #    l=[(q,-num) for num,q in l]
    #else:
    l = [(x, d[x]) for x in sorted(d, key=key, reverse=reverse)]

    for i in range(len(l)):
        s += '  '+str(l[i][0]) + ' -> ' + str(l[i][1]) + '\n'
    return s


def top_n(a_prefix : (str,), n : int, prefix : {(str,):{(str,)}}, query : {(str,):int}) -> [(str,)]:
    if a_prefix in prefix:
        return [x[1] for x in sorted([(-query[query_option],query_option) for query_option in prefix[a_prefix]])[:n]]
    else:
        return []






# Script

if __name__ == '__main__':
    # Write script here
    top_n_results = 3



    file = safe_open('Furnish any file name containing full queries: ', 'r', 'Illegal file name',
                     default='googleq0.txt')
    print()
    prefix,query = read_queries(file)
    print('Prefix dictionary:')
    print(dict_as_str(prefix,lambda x : (len(x),x)))
    print()
    print('Query dictionary: ')
    print(dict_as_str(query,lambda x : (-query[x],x)))
    print()
    user = prompt.for_string("Furnish any prefix sequence (or done to stop): ")
    while user != 'done':
        print('  Most Frequent (up to '+str(top_n_results)+') matching full queries (in order) = ' + str(top_n(tuple(user.strip().split()),top_n_results,prefix,query)))
        print()

        full_query = prompt.for_string('Furnish any full query sequence (or done to stop): ')
        if(full_query.strip().lower() == 'done'):
            break
        else:
            add_query(prefix,query,tuple(full_query.strip().split()))
            print()
            print('Prefix dictionary:')
            print(dict_as_str(prefix,lambda x : (len(x),x)))
            print()
            print('Query dictionary: ')
            print(dict_as_str(query,lambda x : (-query[x],x)))
            print()

        user = prompt.for_string("Furnish any prefix sequence (or done to stop): ")

    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
