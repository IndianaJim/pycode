from time import sleep
import random
spaces = "     "
for i in range(40):
    rand = random.randrange(5)
    sleep(0.3)
    print(spaces[0:rand] + "Hello World!")