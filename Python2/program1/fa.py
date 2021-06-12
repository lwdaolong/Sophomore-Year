# Submitter: loganw1(Wang, Logan)
import goody


def read_fa(file : open) -> {str:{str:str}}:
    d = dict()
    for text in file:
        relationships = text.strip().split(sep=';')
        d1 = {}
        d[relationships[0]] = d1
        for i in range(1, len(relationships),2):
            d1[relationships[i]] = relationships[i+1]
    return d


def fa_as_str(fa : {str:{str:str}}) -> str:
    s = ''
    fa1 = sorted(fa.keys())
    for option in fa1:
        s += "  " + option + ' transitions: ' + str(sorted([(inpt,state) for inpt,state in fa[option].items()])) + '\n'
    return s

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    l =[state]
    for input in inputs:
        if input in fa[state].keys():
            state = fa[state][input]
            l.append((input,state))
        else:
            l.append((input,None))
    return l



def interpret(fa_result : [None]) -> str:
    s='Start state = ' + fa_result[0] +'\n'
    for i in range(1,len(fa_result)):
        if fa_result[i][1] != None:
            s+= '  Input = ' + fa_result[i][0] +'; new state = ' + fa_result[i][1]+'\n'
        else:
            s+= '  Input = ' + fa_result[i][0] +'; illegal input: simulation terminated\n'

    s+='Stop state = ' +str(fa_result[len(fa_result)-1][1])+'\n'
    return s




if __name__ == '__main__':
    # Write script here
    fa_file = goody.safe_open('Furnish any file name containing a Finite Automaton: ', 'r', 'Illegal file name',
                               default='faparity.txt')
    fa_dict = read_fa(fa_file)
    print()
    print('The Finite Automaton code as: states and lists of transitions')
    print(fa_as_str(fa_dict))
    fa_input_file = goody.safe_open('Furnish any file name containing lines with a start-state and its inputs: ', 'r', 'Illegal file name',
                              default='fainputparity.txt')
    print()
    for text in fa_input_file:
        fa_input_text = text.strip().split(';')
        start_state = fa_input_text[0]
        inputs=[]
        for i in range(1,len(fa_input_text)):
            inputs.append(fa_input_text[i])
        print('Start tracing FA (from its start-state)')
        print(interpret(process(fa_dict, start_state, inputs)))



    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
