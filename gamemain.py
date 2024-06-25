from room import Room
from character import Character
from character import Enemy
from item import Item

def main():
    tony= Enemy("Tony", "An asian guy", "AAAA", "maths")

    hallway1 = Room('Hallway','empty room with an errie silence', tony, None)
    hallway2 = Room('Hallway','empty room with an errie silence', None, None)
    cheeseroom = Room('Cheese Room', 'aroma of cheese wafts through the room', None, None)
    saferoom = Room('Safe Room','small room only a mouse can fit in and you can freely rest', None, None)

    hallway1.linked_room({"Exit 1": saferoom,"Exit 2": hallway2, "Exit 3": cheeseroom})
    hallway2.linked_room({"Exit 1": hallway1})
    saferoom.linked_room({"Exit 1": hallway1})
    cheeseroom.linked_room({"Exit 1", hallway1})

    current_room = hallway1
    bag=[]

    dead = False

    while dead==False:
        print("\n")
        current_room.get_details()
        inhabitant = current_room.get_char()

        if inhabitant is not None:
            inhabitant.describe()
            if inhabitant is Enemy:
                print(inhabitant.name + "wants to kill you \n What will you fight with?")
                fight_with = input('> ')
                if inhabitant.fight(fight_with) == True:
                    print("Bravo,hero you won the fight!")
                    current_room.get_char(None)
                else:
                    print("You were unable to defeat " + inhabitant.name +". \nYou lay there painfully rotting to death.")
                    dead=True
        item = current_room.get_item()
        command = input("> ")
        if command in ["Exit 1", "Exit 2", "Exit 3"]:
            current_room = current_room.move(command)
            if current_room == saferoom:
                #add code to if in safe room what happens
        elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()
    #     elif command == "fight":
    #         if inhabitant is not None and isinstance(inhabitant, Enemy):
    #             print("What will you fight with?")
    #             fight_with = input('> ')
    #             if inhabitant.fight(fight_with) == True:
    # # What happens if you win?
    #                 print("Bravo,hero you won the fight!")
    #                 current_room.get_char(None)
    #                 if Enemy.enemies_to_defeat == 0:
    #                     print("Congratulations, you have survived another adventure!")
    #                     dead = True
            else:  
                print("Scurry home, you lost the fight.\n That's the end of the game.")
                dead = True
        elif command == "pat":
            if inhabitant is not None:
                if isinstance(inhabitant, Enemy):
                    print("I wouldn’t do that if I were you...")
                else:
                    inhabitant.pat()
            else:
                print("There is no one here to pat :(")
        elif command == "take":
            if item is not None:
                print("You put the " + item.get_name() + " in your bag")
                bag.append(item.get_name())
                current_room.set_item(None)
        else:
            print("You can't go that way")

main()

replay = input('Would you like to play again? \n> ').upper()
if input== 'YES':
    main()
else:
    exit("Bye that was a nice game.")