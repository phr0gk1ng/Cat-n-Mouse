from room import Room
from character import Character
from character import Enemy

tony= Enemy("Tony", "An asian guy", "AAAA", "maths")

hallway1 = Room('Hallway','empty room with an errie silence', tony)
hallway2 = Room('Hallway','empty room with an errie silence', None)
cheeseroom = Room('Cheese Room', 'aroma of cheese wafts through the room', None)
saferoom = Room('Safe Room','small room only a mouse can fit in and you can freely rest', None)

hallway1.linked_room({
    "Exit 1": saferoom,
    "Exit 2": hallway2,
    "Exit 3": cheeseroom
})
# hallway1.linked_room(saferoom, "Exit 1")
# hallway1.linked_room(hallway2, "Exit 2")
# hallway1.linked_room(cheeseroom, "Exit 3")

hallway2.linked_room({"Exit 1": hallway1})
saferoom.linked_room({"Exit 1": hallway1})
cheeseroom.linked_room({"Exit 1", hallway1})

current_room = hallway1

dead = False

while dead==False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_char()
    if inhabitant is not None:
        inhabitant.describe()
    command = input("> ")
    current_room = current_room.move(command)
    if command in ["Exit 1", "Exit 2", "Exit 3"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
# Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input('> ')
            if inhabitant.fight(fight_with) == True:
# What happens if you win?
                print("Bravo,hero you won the fight!")
                current_room.get_char(None)
        else:  
            print("Scurry home, you lost the fight.\n That's the end of the game.")
            dead = True
    else:
        print("There is no one here to fight with")

