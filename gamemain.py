from room import Room
from character import Character
from character import Enemy
from character import Friend
from item import Item


def welcome():
    input('Hello! Welcome to Rat and Cheeses')
    #add instructions

def main():
    # character name= Enemy/Friend("name", "description", "dialogue", "weakness")

    meancat1 = Enemy("Whiskerblade", "Long whiskers twitch with every movement, sharp claws glint like blades in the light", "You won't see me coming until it's too late, little mouse", "catnip")
    meancat2 = Enemy("Clawdia", "A black cat with piercing green eyes that glow menacingly in the dark", "Toying with you is almost too easy", None)
    meancat3 = Enemy("Fang", "Muscular tabby cat, a scar across his nose and fur is rough and ragged, a testament to the many battles he has fought", "Enter my territory, and you'll leave with more than just a scratch", None)
    meancat4 = Enemy("Viper", "A cat with a serpentine grace to her movements, dark brown fur is mottled with darker spots", "Careful where you step; one wrong move and you're mine.", None)
    meancat5 = Enemy("Raven", "His sharp claws glistens in the darkness, glowing amber eyes hover above", "From the shadows, I'll strike when you least expect it.", None)

    nicecat1 = Friend("Mittens", "White-tipped paws and a sweet disposition, gray tabby with soft fur stands eagerly", "You're safe with me, you can rest here for a bit before they come to get you", None)
    nicecat2 = Friend("Luna", "A sleek, black cat with mysterious, silver eyes and a calming presence.", "You're close to them, watch out, take out a lily if you run into an enemy int he next room", None)
    nicecat3 = Friend("Whiskers", "Long whiskers droop tiredly", "Don't let my brother get you, here take some catnip to distract him", None)

    # item name= Item("name", "description")
    catnip = Item("Catnip", "A leafy green with saw-toothed edges shredded into also a powder")
    lilyflower = Item("A Lily flower", "A white six pointed flower with petals that curl outwards towards the top")
    cheese = Item("Cheese", "A complex blend of sharp tang and earthy richness. The cheese seemed to hold secrets of distant lands and whispered tales of daring adventurers who dared to taste its bold and mysterious flavors.")
    


    # roomname = Room('name','description', character, item, {"Exit 1": linked room,"Exit 2": linked room, "Exit 3": linked room})
    room1 = Room(None, None, None, {"Exit 1": room2,"Exit 2": room8, "Exit 3": room5})
    room2 = Room(None, None, None, {"Exit 1": room3,"Exit 2": room10, "Exit 3": room1})
    room3 = Room(None, None, None, {"Exit 1": room2,"Exit 2": room12, "Exit 3": room4})
    room4 = Room(None, None, None, {"Exit 1": room3,"Exit 2": room14, "Exit 3": room5})
    room5 = Room(None, None, None, {"Exit 1": room1,"Exit 2": room6, "Exit 3": room4})
    room6 = Room(None, None, None, {"Exit 1": room5,"Exit 2": room7, "Exit 3": cheeseroom})
    room7 = Room(None, None, None, {"Exit 1": room8,"Exit 2": room17, "Exit 3": room6})
    room8 = Room(None, None, None, {"Exit 1": room1,"Exit 2": room9, "Exit 3": room7})
    room9 = Room(None, None, None, {"Exit 1": room10,"Exit 2": room18, "Exit 3": room8})
    room10 = Room(None, None, None, {"Exit 1": room2,"Exit 2": room11, "Exit 3": room9})
    room11 = Room(None, None, None, {"Exit 1": room10,"Exit 2": room12, "Exit 3": saferoom})
    room12 = Room(None, None, None, {"Exit 1": room11,"Exit 2": room3, "Exit 3": room13})
    room13 = Room(None, None, None, {"Exit 1": room12,"Exit 2": room14, "Exit 3": room20})
    room14 = Room(None, None, None, {"Exit 1": room13,"Exit 2": room4, "Exit 3": cheeseroom})
    cheeseroom = Room(None, None, None, cheese, {"Exit 1": room14,"Exit 2": room16, "Exit 3": room6})
    room16 = Room(None, None, None, {"Exit 1": room20,"Exit 2": cheeseroom, "Exit 3": room17})
    room17 = Room(None, None, None, {"Exit 1": room18,"Exit 2": room16, "Exit 3": room7})
    room18 = Room(None, None, None, {"Exit 1": room9,"Exit 2": saferoom, "Exit 3": room17})
    saferoom = Room(None, None, None, {"Exit 1": room11,"Exit 2": room18, "Exit 3": room20})
    room20 = Room(None, None, None, {"Exit 1": saferoom,"Exit 2": room13, "Exit 3": room16})

    current_room = room1
    bag=[]

    dead = False

    while dead==False:
        print("\n")
        current_room.get_details()
        inhabitant = current_room.get_char()

        if inhabitant is not None:
            inhabitant.describe()
            if inhabitant is Enemy:
                inhabitant.talk()
                print(inhabitant.name + "wants to kill you \n What will you fight with?")
                fight_with = input('> ')
                if fight_with in bag:
                    bag.remove(fight_with)
                    if inhabitant.fight(fight_with) == True:
                        print("Bravo,hero you won the fight!")
                        current_room.set_char(None)
                else:
                    print("You were unable to defeat " + inhabitant.name +". \nYou lay there painfully rotting to death.")
                    dead=True
        item = current_room.get_item()
        command = input("> ").upper
        if command in ["EXIT 1", "EXIT 2", "EXIT 3"]:
            current_room = current_room.move(command)
            if current_room == saferoom:
                print("You have seemed to entered a room with a door to the outside world.")
                if cheese in bag:
                    print("You have successfully opened the door with the cheese and are free!!")
                    break
                else:
                    print("The door is locked and seems to have a cheese shaped key hole")

        elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()
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
        elif command == "eat":
            if cheese in bag:
                bag.remove(cheese)
                print("You eat the cheese. But a weird feeling travels down your spine. The cheese starts to crawl out of your belly buttom and encase you. You suffocate to death from the cheese touch")
                break
            else:
                print("You can't eat anything in your bag")

        else:
            print("You can't go that way")

def replay():
    replay = input('Would you like to play again? \n> ').upper()
    if replay == 'YES':
        main()
    else:
        exit("Bye that was a nice game.")

main()
replay()
