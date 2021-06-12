# Submitter: loganw1(Wang, Logan)
import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    d = dict()
    for text in open_file:
        relationships = text.strip().split(sep=';')
        l=[]
        for i in range(1,len(relationships)):
            l.append(relationships[i])
        d[relationships[0]] = [None,l]
    return d


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    l = dict(d)
    s = ''
    l = sorted(l,key =key,reverse=reverse)
    for person in l:
        s += "  " + person + ' -> ' + str(d[person]) + '\n'
    return s


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    for person in order:
        if p1 == person or p2 == person:
            return person
    return None #TODO handle Null Reference


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(man,woman[0])for man,woman in men.items()}


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    temp_men = {}
    for key,relationship in men.items():
        temp_men[key] = [str(relationship[0]),[str(potential_match) for potential_match in relationship[1]]]

    temp_women = {}
    for key, relationship in women.items():
        temp_women[key] = [str(relationship[0]), [str(potential_match) for potential_match in relationship[1]]]

    unmatched = {man for man in men.keys()}

    if(trace):
        print('Women Preferences (unchanging)')
        print(dict_as_str(temp_women))
        print()
        print('Men Preferences (current)')
        print(dict_as_str(temp_men))
        print()
        print('unmatched men = ' + str(unmatched))

    while len(unmatched) > 0:
        prospect = unmatched.pop()

        woman_asked = temp_men[prospect][1].pop(0)

        if(trace):
            print(prospect + ' proposes to ' + woman_asked +', ', end='')

        if temp_women[woman_asked][0] == 'None':
            temp_men[prospect][0] = woman_asked
            temp_women[woman_asked][0] = prospect
            if(trace):
                print('who is currently unmatched and accepts the proposal')
        else:
            if prospect == who_prefer(temp_women[woman_asked][1],prospect,temp_women[woman_asked][0]):
                unmatched.add(temp_women[woman_asked][0])
                temp_men[prospect][0] = woman_asked
                temp_women[woman_asked][0] = prospect
                if(trace):
                    print('who is currently matched and accepts the proposal (likes new match better)')
            else:
                unmatched.add(prospect)
                if (trace):
                    print('who is currently matched and rejects the proposal (likes current match better)')
        if(trace):
            print('Men Preferences (current)')
            print(dict_as_str(temp_men))
            print()
            print('unmatched men = ' + str(unmatched))

    return extract_matches(temp_men)


  
    
if __name__ == '__main__':
    # Write script here
    men_file = goody.safe_open('Furnish any file name containing the preferences of the men:', 'r', 'Illegal file name',
                     default='men0.txt')
    women_file = goody.safe_open('Furnish any file name containing the preferences of the women:', 'r', 'Illegal file name',
                               default='women0.txt')
    men_dict = read_match_preferences(men_file)
    women_dict = read_match_preferences(women_file)
    print()
    print('Men Preferences')
    print(dict_as_str(men_dict))
    print('Women Preferences')
    print(dict_as_str(women_dict))
    user = prompt.for_bool("Furnish Trace of Execution", default=True)
    print()
    print('matches = ' + str(make_match(men_dict,women_dict,user)))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
