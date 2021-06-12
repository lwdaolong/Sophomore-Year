# Submitter: loganw1(Wang, Logan)
from goody import type_as_str
import inspect


class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """

    def __init__(self, *args):
        self._annotations = args

    def __repr__(self):
        return 'Check_All_OK(' + ','.join([str(i) for i in self._annotations]) + ')'

    def __check_annotation__(self, check, param, value, check_history):
        for annot in self._annotations:
            check(param, annot, value,
                  check_history + 'Check_All_OK check: ' + str(annot) + ' while trying: ' + str(self) + '\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """

    def __init__(self, *args):
        self._annotations = args

    def __repr__(self):
        return 'Check_Any_OK(' + ','.join([str(i) for i in self._annotations]) + ')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations:
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param) + ' failed annotation check(Check_Any_OK): value = ' + repr(value) + \
                          '\n  tried ' + str(self) + '\n' + check_history


class Check_Annotation:
    # Start with binding the class attribute to True allowing checking to occur
    #   (but only it the object's attribute self._checking_on is bound to True)
    checking_on = True

    # To check the decorated function f, first bind self._checking_on as True
    def __init__(self, f):
        self._f = f
        self._checking_on = True

    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self, param, annot, value, check_history=''):

        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        def check_default(a, val):
            if isinstance(val, a) == False:
                raise AssertionError(
                    f"'{param}' failed annotation check(wrong type): value = '{val}'\n  was type {type_as_str(val)} ...should be type {str(a)[7:-1]}{check_history}")

        def check_list(a, val):
            if isinstance(val, list) == False:
                raise AssertionError(
                    f"'{param}' failed annotation check(wrong type): value = '{val}'\n  was type {type_as_str(val)} ...should be type list")
            elif len(a) == 1:
                for index in range(len(val)):
                    self.check(param, a[0], val[index], check_history=check_history + f"\nlist[{index}] check: {a[0]}")
            else:
                if len(a) != len(val):
                    raise AssertionError(
                        f"'{param} failed annotation check(wrong number of elements): value = {val}\n  annotation had {len(a)} elements{a}")
                else:
                    for index in range(len(a)): self.check(param, a[index], val[index],
                                                           check_history=check_history + f"\nlist[{index}] check: {a[index]}")

        def check_tuple(a, val):
            if isinstance(val, tuple) == False:
                raise AssertionError(
                    f"'{param}' failed annotation check(wrong type): value = '{val}'\n  was type {type_as_str(val)} ...should be type tuple")
            elif len(a) == 1:
                for index in range(len(val)): self.check(param, a[0], val[index],
                                                         check_history=check_history + f"\ntuple[{index}] check: {a[0]}")
            else:
                if len(a) != len(val):
                    raise AssertionError(
                        f"'{param} failed annotation check(wrong number of elements): value = {val}\n  annotation had {len(a)} elements{a}")
                else:
                    for index in range(len(a)): self.check(param, a[index], val[index],
                                                           check_history=check_history + f"\ntuple[{index}] check: {a[index]}")

        def check_dict(a, val):
            if isinstance(val, dict) == False:
                raise AssertionError(
                    f"'{param}' failed annotation check(wrong type): value = '{val}'\n  was type {type_as_str(val)} ...should be type dict")
            elif len(a) != 1:
                raise AssertionError(
                    f"'{param}' annotation inconsistency: {type_as_str(a)} should have 1 item but had {len(a)}\n  annotation = {a}")
            else:
                for key in val:
                    self.check(param, list(a.keys())[0], key,
                               check_history=check_history + f"\ndict key check: {list(a.keys())[0]}")
                    self.check(param, list(a.values())[0], val[key],
                               check_history=check_history + f"\ndict value check: {list(a.values())[0]}")


        def check_set(a, val):
            if isinstance(val, set) == False:
                raise AssertionError(
                    f"'{param}' failed annotation check(wrong type): value = '{val}'\n  was type {type_as_str(val)} ...should be type set")
            elif len(a) != 1:
                raise AssertionError(
                    f"'{param}' annotation inconsistency: {type_as_str(a)} should have 1 value but had {len(a)}\n  annotation = {a}")
            else:
                for item in val: self.check(param, list(a)[0], item,
                                            check_history=check_history + f"\nset value check: {list(a)[0]}")

        def check_frozenset(a, val):
            if isinstance(val, frozenset) == False:
                raise AssertionError(
                    f"'{param}' failed annotation check(wrong type): value = '{val}'\n  was type {type_as_str(val)} ...should be type frozenset")
            elif len(a) != 1:
                raise AssertionError(
                    f"'{param}' annotation inconsistency: {type_as_str(a)} should have 1 item but had {len(a)}\n  annotation = {a}")
            else:
                for item in val: self.check(param, list(a)[0], item,
                                            check_history=check_history + f"\nfrozenset value check: {list(a)[0]}")

        def check_lambda(a, val):
            if len(a.__code__.co_varnames) != 1:
                raise AssertionError(
                f"'{param}' annotation inconsistency: predicate should have 1 parameter but had {len(a.__code__.co_varnames)}\n  predicate = {a}")
            try:
                a(val)
            except Exception as e:
                raise AssertionError(f"'{param}' annotation predicate({a}) raised exception\n  exception = {e}")
            if not a(val): raise AssertionError(
                f"'{param}' failed annotation check: value = {val}\n  predicate = {a}{check_history}")

        # Start with matching check's function annotation with its arguments
        if annot is None:
            return
        elif annot in (int, str, float, complex, bool, iter,list):
            check_default(annot, value)
        elif isinstance(annot, list):
            check_list(annot, value)
        elif isinstance(annot, tuple):
            check_tuple(annot, value)
        elif isinstance(annot, dict):
            check_dict(annot, value)
        elif isinstance(annot, set):
            check_set(annot, value)
        elif isinstance(annot, frozenset):
            check_frozenset(annot, value)
        elif inspect.isfunction(annot):
            check_lambda(annot, value)
        else:
            try:
                annot.__check_annotation__(self.check, param, value, check_history)
            except:
                raise AssertionError(f"'{param}' annotation undecipherable: {annot}")
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):

        # Return the parameter/argument bindings via an OrderedDict (derived
        #   from dict): it binds the function header's parameters in their order
        def param_arg_bindings():
            f_signature = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args, **kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        if (self._checking_on == False or self.checking_on == False):
            return self._f(*args, **kargs)
        # Otherwise do all the annotation checking
        try:
            # For each detected annotation, check if the parameter satisfies it
            check_history = ''
            params_assigned = param_arg_bindings()
            for annot_to_check, specified_annot_type in self._f.__annotations__.items():
                if annot_to_check != 'return':
                    self.check(annot_to_check, specified_annot_type, params_assigned[annot_to_check],
                               check_history + ' check: ' + str(annot_to_check) + ' while trying: ' + str(
                                   self) + '\n')
            # Compute/remember the value of the decorated function
            answer = self._f(*args, **kargs)
            # If 'return' is in the annotation, check it
            if 'return' in self._f.__annotations__.keys():
                self.check('return', self._f.__annotations__['return'], answer,
                           check_history + ' check: ' + str('return') + ' while trying: ' + str(
                               self) + '\n')
                params_assigned['_return'] = answer
            # Return the decorated answer
            return answer


        # TODO REMOVE COMMENTS
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            '''
            print(80*'-')
            for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
                print(l.rstrip())
            print(80*'-')
        '''
            raise


if __name__ == '__main__':
    # an example of testing a simple annotation  
    def f(x:int): pass
    f = Check_Annotation(f)
    f(3)
    #f('a')

    # driver tests
    import driver

    driver.default_file_name = 'bscp4W21.txt'
    #     driver.default_show_exception= True
    #     driver.default_show_exception_message= True
    #     driver.default_show_traceback= True
    driver.driver()
