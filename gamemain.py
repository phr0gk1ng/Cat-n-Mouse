from room import Room

hallway1 = Room('Hallway','empty room with an errie silence')
hallway2 = Room('Hallway','empty room with an errie silence')
cheeseroom = Room('Cheese Room', 'aroma of cheese wafts through the room')
saferoom = Room('Safe Room','small room only a mouse can fit in and you can freely rest')

hallway1.linked_room(saferoom, "Exit 1")
hallway1.linked_room(hallway2, "Exit 2")
hallway1.linked_room(cheeseroom, "Exit 3")
hallway2.linked_room(hallway1, "Exit 1")
saferoom.linked_room(hallway1, "Exit 1")
cheeseroom.linked_room(hallway1, "Exit 1")

current_room = hallway1
while True:
    print("\n")
    current_room.get_details()
    command = input(">")
    current_room = current_room.move(command)