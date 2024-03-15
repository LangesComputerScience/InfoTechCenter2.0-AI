import random
from time import sleep

GAS_LEVELS = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
GAS_STATIONS = ["Shell", "Speedway", "Marathon", "Circle K", "Moble", "Costco", "Meijer", "7Eleven"]
LOW_MILES_RANGE = (1, 25)
QUARTER_TANK_MILES_RANGE = (25.1, 50)
SLEEP_TIME = 2.5

def getGasLevel():
    return random.choice(GAS_LEVELS)

def getNearestGasStation():
    return random.choice(GAS_STATIONS)

def gasLevelAlert():
    gasLevel = getGasLevel()
    if gasLevel == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(SLEEP_TIME)
        print("    ***Calling Triple AAA***")
    elif gasLevel == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station...")
        sleep(SLEEP_TIME)
        print(f"The closest gas station is {getNearestGasStation()}, which is {random.uniform(*LOW_MILES_RANGE):.1f} miles away.")
    elif gasLevel == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station...")
        sleep(SLEEP_TIME)
        print(f"The closest gas station is {getNearestGasStation()}, which is {random.uniform(*QUARTER_TANK_MILES_RANGE):.1f} miles away.")
    elif gasLevel == "Half Tank":
        print("Your gas tank is half full, which is plenty to get to your destination.")
    elif gasLevel == "Three Quarter Tank":
        print("Your gas tank is three quarters full.")
    else:
        print("Your gas tank is full. Congratulations!")

gasLevelAlert()