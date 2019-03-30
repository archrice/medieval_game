"""                                     Locations   'loc.py'        """
from woods import woods
from town import town
from cave import runcave
from castle import castle
import gameset as gs
#from unknown import unknown

def navigate(cname, level, reputation, age):
    while True:
        locs = {'town':town, 'woods':woods
                ,'cave':runcave ,'castle':castle}
#       'camelot':camelot, 'Unknown':unknown}
        p = input("\nDo you want to travel? ")
        if p == 'yes' or p == 'y':
            print("Where do you want to travel to?")
            for k in locs.keys():
                print(k.title())
            dest = input('\n: ')
            if dest in locs.keys():
                return locs[dest](cname, level, reputation, age)
                gs.save(level, age, cname, reputation)
                break
        else:
            raise SystemExit

