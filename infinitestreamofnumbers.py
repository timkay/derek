print("inline.py loading... -")
import random
minNumber = int(input("input lowest number> "))
maxnumber = int(input("input highest number> "))
exec(input("Input Test Code\n(Set Target Class to Target)\n"))
try:
    while True:
        Target.add(random.randint(minNumber, maxnumber))
except KeyboardInterrupt:
    pass
