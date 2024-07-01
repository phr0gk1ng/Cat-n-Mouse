from room import Room
from character import Character
from character import Enemy
from character import Friend
from item import Item

def welcome():
    startgame = input("------------------------ Hello! Welcome to Rat and Cheeses ------------------------\nYou will be a mouse trying to make your way through a maze of rooms to the outside world. \nAlong the way you will have to grab items, talk to some cats and defeat the ones trying to kill you. \n To interact with the game use the following commands: \n- Exit 1, 2 or 3: To move between rooms \n- talk: To talk to cats \n- take: To take items from rooms and add it to your pouch \n- inventory: To check your inventory \n- quit: To exit the game \n Would you like to continue to the game? (Y/N) ").upper()
    if startgame == 'Y':
        print('Good Luck!')
        main()
    if startgame == 'N':
        exit('Cya')
    else:
        print('invalid command')

def main():
    # character name= Enemy/Friend("name", "description", "dialogue", "weakness")
    meancat1 = Enemy("Whiskerblade", "Long whiskers twitch with every movement, sharp claws glint like blades in the light", "You won't see me coming until it's too late, little mouse", "catnip")
    meancat2 = Enemy("Clawdia", "A black cat with piercing green eyes that glow menacingly in the dark", "Toying with you is almost too easy", "mirror")
    meancat3 = Enemy("Fang", "Muscular tabby cat, a scar across his nose and fur is rough and ragged, a testament to the many battles he has fought", "Enter my territory, and you'll leave with more than just a scratch", "ginger")
    meancat4 = Enemy("Viper", "A cat with a serpentine grace to her movements, dark brown fur is mottled with darker spots", "Careful where you step; one wrong move and you're mine", "chocolate")
    meancat5 = Enemy("Raven", "His sharp claws glistens in the darkness, glowing amber eyes hover above", "From the shadows, I'll strike when you least expect it", "lily flower")

    nicecat1 = Friend("Luna", "A sleek, black cat with mysterious, silver eyes and a calming presence", "You're close to them, watch out, take out some cocoa if you run into an enemy in an adjacent room")
    nicecat2 = Friend("Mittens", "White-tipped paws and a sweet disposition, gray tabby with soft fur stands eagerly", "You're safe with me, you can rest here for a bit before they come to get you. But when you leave pick up some ginger, it'll hurt anyone with scars")
    nicecat3 = Friend("Whiskers", "Long whiskers droop tiredly", "Don't let my brother get you, here take some catnip to distract him")
    nicecat4 = Friend("Dahlia", "Her arms look uncontrollable, scribbling line after line, while she sings", "LA LA LA BLACK CATS HATE MIRRORS")
    nicecat5 = Friend("Ryan", "Fur swoops in every direction and he's sitting calming on a chair, a crane resting near by", "My legs are weak so I can't help guide you but you must remember flowers for amber eyes")

    # item name= Item("name", "description")
    catnip = Item("catnip", "A leafy green with saw-toothed edges shredded into also a powder")
    lilyflower = Item("lily flower", "A white six pointed flower with petals that curl outwards towards the top")
    chocolate = Item("chocolate", "A tapestry of cocoa, caramel and vanilla waft through the air like a warm embrace")
    garlic = Item('garlic', "It's just a garlic clove")
    mirror = Item("mirror", "You see your own reflection")
    cheese = Item("cheese", "A complex blend of sharp tang and earthy richness. The cheese seemed to hold secrets of distant lands and whispered tales of daring adventurers who dared to taste its bold and mysterious flavors.")

    # roomname = Room('name','description', character, item, {"Exit 1": linked room,"Exit 2": linked room, "Exit 3": linked room})
    room1 = Room("Whisker Way", "A dark, narrow path winding with the faint scent of cat fur", nicecat5, None)
    room2 = Room("Mousetrap Maze", "A cluttered storage room filled with old furniture and dusty boxes, the air thick with the smell of must and the constant threat of hidden traps.", nicecat3, catnip)
    room3 = Room("Squeak Street", "A narrow hallway cluttered with discarded items and old crates, the acrid smell of dust and decay in the air", meancat3, None)
    room4 = Room("Claw Room", "A foreboding room, the walls are scarred with claw marks, and the air is heavy", None, mirror)
    room5 = Room("Nibble Nook", "A cozy kitchen corner with crumbs scattered about, the enticing smell of old cheese and bread mixing", None, None)
    room6 = Room("Pawprint Hallway", "A well-worn corridor with overlapping paw prints on the floor", meancat1, None)
    room7 = Room("Tail Trail", "A winding hallway with the faint smell of dust and fur, lined with claw-marked baseboards", None, garlic)
    room8 = Room("Rodent Run", "A damp basement corridor with the smell of mold and wet concrete", None, None)
    room9 = Room("Kitty Kingdom", "A luxurious sitting room with plush cushions and ornate cat statues", nicecat4, None)
    room10 = Room("Furry Forest", "A dense, cluttered room with tall potted plants and overgrown foliage", meancat5, None)
    room11 = Room("Mousehole Manor", "The musty smell of old wood and hidden dangers filling the air", None, chocolate)
    room12 = Room("Hideaway Haven", "A hidden crawl space behind old furniture, the air musty and stale", None, None)
    room13 = Room("Feline Fields", "A large living room with tall furniture and the fresh scent of recently cleaned floors", None, lilyflower)
    room14 = Room("Sniff Spot", "The air thick with the smell of fear and curiosity", nicecat1, None)
    cheeseroom = Room("Cheese Chamber", "A pantry with a singular aging cheese left, the air heavy with it's pungent aroma and the lurking danger of prowling felines", meancat4, cheese)
    room16 = Room("Whisker Wood", "A storage room with tall shelves and overgrown plants, the air thick with the smell of damp earth", None, None)
    room17 = Room("Squeak Sanctuary", "A serene, hidden room filled with old, forgotten items and the faint smell of dust", meancat2, None)

    room18 = Room("Catnip Corner", "A fragrant corner where the intoxicating smell of catnip is overpowering", nicecat2, None)
    saferoom = Room("Rodent Retreat", "A room with sunlight peering through", None, None)
    room20 = Room("Feline Frenzy", "A chaotic playroom with overturned furniture and scattered toys", None, None)

    room1.linked_room({"EXIT 1": room2,"EXIT 2": room8, "EXIT 3": room5})
    room2.linked_room({"EXIT 1": room3,"EXIT 2": room10, "EXIT 3": room1})
    room3.linked_room({"EXIT 1": room2,"EXIT 2": room12, "EXIT 3": room4})
    room4.linked_room({"EXIT 1": room3,"EXIT 2": room14, "EXIT 3": room5})
    room5.linked_room({"EXIT 1": room1,"EXIT 2": room6, "EXIT 3": room4})
    room6.linked_room({"EXIT 1": room5,"EXIT 2": room7, "EXIT 3": cheeseroom})
    room7.linked_room({"EXIT 1": room8,"EXIT 2": room17, "EXIT 3": room6})
    room8.linked_room({"EXIT 1": room1,"EXIT 2": room9, "EXIT 3": room7})
    room9.linked_room({"EXIT 1": room10,"EXIT 2": room18, "EXIT 3": room8})
    room10.linked_room({"EXIT 1": room2,"EXIT 2": room11, "EXIT 3": room9})
    room11.linked_room({"EXIT 1": room10,"EXIT 2": room12, "EXIT 3": saferoom})
    room12.linked_room({"EXIT 1": room11,"EXIT 2": room3, "EXIT 3": room13})
    room13.linked_room({"EXIT 1": room12,"EXIT 2": room14, "EXIT 3": room20})
    room14.linked_room({"EXIT 1": room13,"EXIT 2": room4, "EXIT 3": cheeseroom})
    cheeseroom.linked_room({"EXIT 1": room14,"EXIT 2": room16, "EXIT 3": room6})
    room16.linked_room({"EXIT 1": room20,"EXIT 2": cheeseroom, "EXIT 3": room17})
    room17.linked_room({"EXIT 1": room18,"EXIT 2": room16, "EXIT 3": room7})
    room18.linked_room({"EXIT 1": room9,"EXIT 2": saferoom, "EXIT 3": room17})
    saferoom.linked_room({"EXIT 1": room11,"EXIT 2": room18, "EXIT 3": room20})
    room20.linked_room({"EXIT 1": saferoom,"EXIT 2": room13, "EXIT 3": room16})

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
        command = input("> ").upper()
        
        if command in ["EXIT 1", "EXIT 2", "EXIT 3"]:
            current_room = current_room.move(command)
            # if current_room == saferoom:
            #     print("You have seemed to entered a room with a door to the outside world.")
            #     if cheese in bag:
            #         print("You have successfully opened the door with the cheese and are free!!")
            #         break
            #     else:
            #         print("The door is locked and seems to have a cheese shaped key hole")

        elif command == "TALK":
            if inhabitant is not None:
                inhabitant.talk()
        
        elif command == "TAKE":
            if item is not None:
                print("You put the " + item.get_name() + " in your bag")
                bag.append(item.get_name())
                current_room.set_item(None)
        
        elif command == "EAT":
            if cheese in bag:
                bag.remove(cheese)
                print("You eat the cheese. But a weird feeling travels down your spine. The cheese starts to crawl out of your belly buttom and encase you. You suffocate to death from the cheese touch")
                break
            else:
                print("You can't eat anything in your bag")
        
        elif command == "INVENTORY":
            print(bag)
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
