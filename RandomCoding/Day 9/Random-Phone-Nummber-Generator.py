# Random Phone Nummber Generator in Python

import random

def generate(count):
    for i in range(count):
        print(f"{random.randrange(6,9)}{random.randrange(100000000,999999999)}")

generate(int(input("How many number you wants to generate ? [Default 10] : " )))
