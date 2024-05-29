priceOfApples = 6
moneyYouHave = 30

change = priceOfApples * int(input("how many apples do you want to buy? " ) )

if change > moneyYouHave:
    print("you do not have enough money!!! ")

else:
    print("proceed to transaction!! ")
