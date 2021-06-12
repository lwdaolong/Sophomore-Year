# Submitter: loganw1(Wang, Logan)
import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    d = dict()
    for text in file:
        relationships = text.strip().split(sep=';')
        d1 = {}
        d[relationships[0]] = d1
        for i in range(1, len(relationships), 2):
            d1[relationships[i]] = set()
        for i in range(1, len(relationships), 2):
            d1[relationships[i]].add(relationships[i + 1])
    return d


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    s = ''
    fa1 = sorted(ndfa.keys())
    for option in fa1:
        s += "  " + option + ' transitions: ' + str(
            sorted([(inpt, sorted(state)) for inpt, state in ndfa[option].items()])) + '\n'
    return s

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    l = [state]
    curr_state = [state]
    for input in inputs:
        potential_states=set()
        temp_states = []
        for potential_state in curr_state:
            if input in ndfa[potential_state].keys():
                for i in ndfa[potential_state][input]:
                    potential_states.add(i)
                    temp_states.append(i)
        if len(curr_state) >0:
            l.append((input, potential_states))
            curr_state=temp_states
    return l


def interpret(result : [None]) -> str:
    s = 'Start state = ' + result[0] + '\n'
    for i in range(1, len(result)):
        if result[i][1] != None:
            s += '  Input = ' + result[i][0] + '; new possible states = ' + str(sorted(result[i][1])) + '\n'
        else:
            s += '  Input = ' + result[i][0] + '; illegal input: simulation terminated\n'

    s += 'Stop state(s) = ' + str(sorted(result[len(result) - 1][1])) + '\n'
    return s





if __name__ == '__main__':
    # Write script here
    fa_file = goody.safe_open('Furnish any file name containing a Non-Deterministic Finite Automaton: ', 'r', 'Illegal file name',
                              default='ndfaendin01.txt')
    fa_dict = read_ndfa(fa_file)
    print()
    print('The Non-Deterministic Finite Automaton code as: states and lists of transitions')
    print(ndfa_as_str(fa_dict))
    fa_input_file = goody.safe_open('Furnish any file name containing lines with a start-state and its inputs: ', 'r',
                                    'Illegal file name',
                                    default='ndfainputendin01.txt')
    print()
    for text in fa_input_file:
        fa_input_text = text.strip().split(';')
        start_state = fa_input_text[0]
        inputs = []
        for i in range(1, len(fa_input_text)):
            inputs.append(fa_input_text[i])
        print('Start tracing NDFA (from its start-state)')
        print(interpret(process(fa_dict, start_state, inputs)))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
