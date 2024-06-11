class Room():
    def __init__(self, room_name, description):
        self.name = room_name
        self.description = description
        self.linked_rooms = {}
        
    def describe(self):
        print(self.description)
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
    
    def get_details(self):
        print(self.name)
        print("----------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.description + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
    

