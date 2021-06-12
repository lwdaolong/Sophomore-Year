# Submitter: loganw1(Wang, Logan)
from collections import defaultdict
from goody import type_as_str
import prompt

class Bag:
    def __init__(self, *values):
        d = defaultdict(int)
        if values !=None:
            for value in values:
                for value1 in value:
                    d[value1] +=1
        self.data_struct = d


    def __repr__(self,):
        return 'Bag(' +str([a for a,i in self.data_struct.items() for x in range(i)])+ ')'

    def __str__(self):
        s= 'Bag('
        for key,value in self.data_struct.items():
            s+= str(key)+'['+str(value)+'],'
        if len(self.data_struct) >0:
            s = s[:-1]
        return s+')'

    def __len__(self):
        sum=0
        for value in self.data_struct.values():
            sum+= value
        return sum

    def unique(self):
        sum=0
        for key in self.data_struct:
            sum+=1
        return sum

    def __contains__(self, item):
        if item in self.data_struct:
            return True
        else:
            return False

    def count(self,item):
        if item in self.data_struct:
            return self.data_struct[item]
        else:
            return 0

    def add(self,item):
        self.data_struct[item] +=1

    def __add__(self, other):
        new_bag = Bag()
        if type(other) != Bag:
            raise TypeError('object added should be of type Bag(), object added instead type:' + type(other))
        for item in self.data_struct.keys():
            for num in range(self.data_struct[item]):
                new_bag.add(item)
        for item in other.data_struct.keys():
            for num in range(other.data_struct[item]):
                new_bag.add(item)
        return new_bag

    def remove(self, item):
        if item in self.data_struct:
            self.data_struct[item] -=1
            if self.data_struct[item] <=0:
                del(self.data_struct[item])
        else:
            raise ValueError("item not found in Bag")

    def __eq__(self,compareObj:'Bag')->bool:
        if type(compareObj) == Bag:
            if len(self) == len(compareObj) and self.unique() == compareObj.unique():
                for key,val in self.data_struct.items():
                    if val != compareObj.data_struct[key]:
                        return False
                return True
            else:
                return False
        else:
            return False

    def __iter__(self):
        def gen(l):
            for item in l:
                yield item
        return gen([a for a,i in self.data_struct.items() for x in range(i)])



if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    b = Bag(['d','a','d','b','c','b','d'])
    print(repr(b))
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)

    b2 = Bag(['a','a','b','x','d'])
    print(repr(b2+b2))
    print(str(b2+b2))
    print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    b = Bag(['a','b','a'])
    print(repr(b))
    print()
    
    import driver
    driver.default_file_name = 'bscp21W21.txt'
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
