# Submitter: loganw1(Wang, Logan)
import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    def show_listing(s):
        for line_number, text_of_line in enumerate(s.split('\n'),1):     
            print(f' {line_number: >3} {text_of_line.rstrip()}')

    # put your code here
    # bind class_definition (used below) to the string constructed for the class

    def is_legal_name(s):
        if type(s) == str or type(s) == int or type(s) == float:
            s= str(s)
            if ',' in s:
                l= s.split(',') #splits if field_names
            else:
                l = s.split()
            for i in l:
                i=i.strip()
                if i in keyword.kwlist:
                    raise SyntaxError(f'pcollections.pnamedtuple.is_legal_name: String s: ' + s + ' is not a legal name, is Python keyword')
                else:
                    z = re.match('^[a-zA-Z][\w]*$', i)
                    if z:
                        pass
                    else:
                        raise SyntaxError(f'pcollections.pnamedtuple.is_legal_name: String s: ' + s + ' is not a legal name, must start with alphabetical character and be followed by alphanumeric or underscore characters')

            return True
        elif type(s) == list:
            for i in s:
                if i in keyword.kwlist:
                    raise SyntaxError(
                        f'pcollections.pnamedtuple.is_legal_name: String s: ' + s + ' is not a legal name, is Python keyword')
                else:
                    z = re.match('^[a-zA-Z][\w]*$', i)
                    if z:
                        pass
                    else:
                        raise SyntaxError(
                            f'pcollections.pnamedtuple.is_legal_name: String s: ' + s + ' is not a legal name, must start with alphabetical character and be followed by alphanumeric or underscore characters')

                return True
        raise SyntaxError()

    if is_legal_name(type_name): #Doesn't do anything if legal name, raises SyntaxError otherwise
        pass
    fields=[]
    if is_legal_name(field_names): #If all legal names, constructs list of fields
        if type(field_names) == str:
            if ',' in field_names:
                l= field_names.split(',') #splits if field_names
            else:
                l = field_names.split()
            for i in l:
                if i not in fields: #prevent dups
                    fields.append(i.strip())
        elif type(field_names) == list:
            fields = list(field_names)

    #Checking default params
    for key in defaults.keys():
        if key not in fields:
            raise SyntaxError(f'pcollections.pnamedtuple: key: ' + key + ' from defaults does not exist in this class"s fields: ' + str(fields))


    def gen_init(fields,defaults) ->str:
        s= "    def __init__(self, "
        for field in fields:
            if field in defaults.keys():
                s += str(field) +'=' + str(defaults[field])+', '
            else:
                s += str(field) +', '
        s = s[:-1] + '):\n'
        for field in fields:
            s+= f'        self.{field} = {field}\n'
        return s.rstrip()

    def gen_repr():
        s = "    def __repr__(self):\n"
        s+=f"        s = '{type_name}('\n"
        s+=f"        for key,value in self.__dict__.items():\n"
        s+=f"            s += str(key) + '=' + str(value) + ','\n"
        s+=f"        return s[:-1] + ')'"
        return s

    def gen_accessors(fields):
        s=''
        for field in fields:
            field_getter = f'''\
    def get_{field}(self):
        return self.{field}

'''
            s+= field_getter
        return s

    def gen_get_item():
        s=f'''\
    def __getitem__(self, x):
        if type(x) == int and x < len(self._fields):
            o = 'self.get_' + str(self._fields[x])+'()'
            return eval(o)
        elif type(x) == str and x in self._fields:
            o = 'self.get_' + str(x)+'()'
            return eval(o)
        else:
            raise IndexError('x: ' + str(x) + ' is either out of bounds or not an existing field')
'''
        return s
    def gen_eq():
        s=f'''\
    def __eq__(self, x):
        if type(x) != type(self):
            return False
        if len(self._fields) != len(x._fields):
            return False
        for item in self._fields:
            if self.__getitem__(item) != x.__getitem__(item):
                return False
        return True
'''
        return s
    def gen_asdict():
        s = '''\
    def _asdict(self):
        return {field:self.__getitem__(field) for field in self._fields} 
'''
        return s
    def gen_make():
        s=f'''\
    def _make(iterable):
        return {type_name}(*iterable)
        '''
        return s

    def gen_replace():
        s = f'''\
    def _replace(self, **kargs):
        for item in kargs:
            if item not in self._fields:
                raise TypeError()
        if self._mutable:
            for item in kargs:
                self.__dict__[item] = kargs[item]
            return None
        else:
            d = dict()
            for k,v in self.__dict__.items():
                d[k] = v
            for item in kargs:
                d[item] = kargs[item]
            l = [value for value in d.values()]
            return {type_name}._make(l)
'''
        return s
#    def gen_setattr():
#        s = f'''\
#    def __setattr__(self, name, value):
#        if _mutable:
#            self.__dict__[name] = value
#        else:
#            raise AttributeError('not mutable')
#'''
#        return s
    class_definition = f'''\
class {type_name}:
    _fields = {fields}
    _mutable = {mutable}
{gen_init(fields,defaults)}
{gen_repr()}
{gen_accessors(fields)}
{gen_get_item()}
{gen_eq()}
{gen_asdict()}
{gen_make()}
{gen_replace()}
'''


    # Debugging aid: uncomment show_listing, displays source code for the class
    # show_listing(class_definition)
    
    # Execute class_definition's str within name_space; followed by binding the
    #   attribute source_code to the class_definition; after the try+except
    #   return the created class object; if there were any syntax errors, show
    #   the class and also show the error in the except clause
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )            
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')
    #TODO REMOVE BELOW

    #driver tests
    import driver  
    driver.default_file_name = 'bscp3W21.txt'
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
