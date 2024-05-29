userName = input("Hey! What is your name? ")
priceOfApples = 6
moneyYouHave = 30
change = priceOfApples * int(input("Hey " + userName + "!" + " Welcome to the program!! " + " How many apples do you want to buy? " ) )
howManyMoreYouCanBuy = ( moneyYouHave / change )
if change > moneyYouHave:
    print(userName + " you do not have enough money!!! ")

elif change < moneyYouHave:
    print(howManyMoreYouCanBuy)
