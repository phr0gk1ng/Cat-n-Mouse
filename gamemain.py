from room import Room

hallway1 = Room('Hallway','An empty room with an errie silence')
hallway2 = Room('Hallway','Another empty room with an errie silence')
cheeseroom = Room('Cheese Room', 'The aroma of cheese wafts through the room')
saferoom = Room('Safe Room','A small room only a mouse can fit in and you can freely rest')

hallway1.linked_room(saferoom, "Exit 1")
hallway1.linked_room(hallway2, "Exit 2")
hallway1.linked_room(cheeseroom, "Exit 3")
hallway2.linked_room(hallway1, "Exit 1")
saferoom.linked_room(hallway1, "Exit 1")
cheeseroom.linked_room(cheeseroom, "Exit 1")

hallway1.get_details()
hallway2.get_details()
cheeseroom.get_details()
saferoom.get_details()

hallway1.describe()