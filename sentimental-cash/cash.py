from math import *
from cs50 import get_float

while True:
    cash = get_float("Cash owed: ")
    if cash < 0:
        continue
    else:
        break

coins = 0
if cash>0:
    cents = round(cash*100)
    quarters = int(cents/25)
    dime = int((cents%25)/10)
    nick = int(((cents%25)%10)/5)
    pennies = int(((cents%25)%10)%5)

    coins += quarters
    if dime>0:
        coins+=dime
    if nick>0:
        coins+=nick
    if pennies > 0:
        coins+=pennies

    print(coins)
