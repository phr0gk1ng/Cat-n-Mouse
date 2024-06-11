from room import Room

hallway1 = Room('Hallway','An empty room with an errie silence')
hallway2 = Room('Hallway','Another empty room with an errie silence')
cheeseroom = Room('Cheese Room', 'The aroma of cheese wafts through the room')
saferoom = Room('Safe Room','A small room only a mouse can fit in and you can freely rest')

hallway1.linked_rooms(saferoom, "Exit 1")
hallway1.linked_rooms(hallway2, "Exit 2")
hallway1.linked_rooms(cheeseroom, "Exit 3")


hallway1.describe()