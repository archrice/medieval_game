"""                                'woods.py'        """

import time
import gameset as gs
import loc as loc

a1 = ['town', 'woods','cave','castle','cottage'
        ,'dungeon','cathedral']
        if wq2 == 'right':
            print("\nYou went right, it is dry, foggy,  and life seems sparse.")
            time.sleep(2)
            print("\nAs you venture down the path you hear scurried movement and see"+
                  " shadows in the periphery.")
            time.sleep(2)
            print("\nYou start to get anxious...")
            time.sleep(2)
            print("\nYou look up and suddenly see tall people draped in dark ragged clothing!")
            time.sleep(2)
            print(
            """\nOne of them says, "We are the knights of ni, ping, and nee-wom. In order to pass we require a...""")
            time.sleep(2)
            print("SHRUBBERY!")
            time.sleep(2)
            print("Your task is to now find a shrubbery, where do you look?")
            time.sleep(2)
            shrub = ['the cave',' the local shruber',' or search the forest.']
            for s in shrub:
                print('\n['+s+']')
            ans = input("[cave, shrubber, or forest]\n: ")
            if ans == 'cave':
                time.sleep(2)
                print("\nYou enter the cave...")
                time.sleep(2)
                print("\nThere is nothing but rocks. (Suprise)")
                time.sleep(2)
                print("\nYou see writing etched in the wall, it reads"+
                      """ 'Here may be found the last words of Joseph of
                Arathamia. He who is valiant and pure of spirit may find
              the holy grail in the castle of Aaauuuggghhh...'""")
                time.sleep(2)
                print("The monster appears and kills you. :(")
                raise SystemExit
            if ans == 'shrubber':
                print("\nYou go to the town shrubber.")
                time.sleep(2)
                print(cname + ": 'Hello I would like to purchase a shrubbery.'")
                time.sleep(3)
                print("\nShrubber: 'And why do you think I would have that?'")
                time.sleep(2)
                print(cname + ": 'Becuase you're the shrubber...'")
                time.sleep(2)
                print("\nShrubber: 'And?'")
                time.sleep(3)
                print(cname + ": 'What?'")
                time.sleep(3)
                print("\nShrubber: 'Ok fine I will sell you a shrubbery for...'")
                time.sleep(2)
                print("\nA CHICKEN!'")
                time.sleep(2)
                print("\nYou kill the shrubber and take the shrubbery.")
                time.sleep(2)
                print("\nYou return to the knights of Ni and give them the shrubbery.")
                time.sleep(2)
                print("\nThey say, 'Thank you for the shrubbery...'")
                time.sleep(2)
                print(cname +": Can I pass?")
                time.sleep(2)
                print("Knights of Ni: To pass we need a...")
                time.sleep(2)
                print("You kill the Knights of Ni.")
                woods2(cname, level, age, reputation)
            if ans == 'forest':
                print("You search around the forest.")
                time.sleep(2)
                print("You search the forest.")
                time.sleep(2)
                print("You walk along the path.")
                time.sleep(2)
                print("Ow! You tripped and fell down a large hole.")
                time.sleep(2)
                print("It was a rabbit hole.")
                time.sleep(2)
                print("This isn't very good....")
                loc.navigate(cname, level, reputation)

