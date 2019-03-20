"""                                'woods.py'        """
from script import s1
from time import sleep
import gameset as gs
import loc as loc
import os

cwd = os.getcwd()
with open (f"{cwd}/cl.json}", 'r') as f:
    cl = f.read()
    cl = int(cl)
def itr(l):
    for i in l:
        x=0
        x+=1
        sleep(3)
        print('\n'+i)
        if x ==2:
            raise StopIteration
def woods(cname, level, reputation, age):

    if print(s1[0]) == 'left':
        if cl == 1:
            itr(s1[1:4])
        else:
            itr(s1[6:7])
    itr(8:9)
    if itr[10] != cname:
        itr(s1[11])
        raise SystemExit
    if itr(s1[12]) == "an african or european swallow?":
        itr(s1[13])
    else:
        raise SystemExit
    itr(14:15)
    if itr(s1[16]) == 'stay':
        if itr(s1[17]) == 'talk':
            itr(s1[18:20])
        else:
            itr(21:22)
            gs.level_up(level,reputation, age, cname)





#            shrub = ['the cave',' the local shruber',' or search the forest.']
#            if ans == 'cave':
#            if ans == 'shrubber':
#                woods2(cname, level, age, reputation)
#            if ans == 'forest':
#                loc.navigate(cname, level, reputation)
