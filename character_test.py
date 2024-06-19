from character import Character
from character import Enemy

tony= Enemy("Tony", "An asian guy", "AAAA", "maths")

#tony.describe()
tony.talk()

print("What will you fight with?")
fight_with = input()
tony.fight(fight_with)

