class Room():
    def __init__(self, room_name, description, character, item):
        self.name = room_name
        self.description = description
        self.character = character
        self.item = item
        self.linked_rooms = {}

    def get_char(self):
        return self.character
    
    def get_name(self):
        return self.name

    def set_char(self, character):
        self.character = character
        
    def describe(self):
        print(self.description)
    
    # def linked_room(self, room_to_link, direction):
    #     self.linked_rooms[direction] = room_to_link

    def linked_room(self, linked_rooms):
         self.linked_rooms = linked_rooms

    def get_description(self):
        return self.description
    
    def get_details(self):
        print(self.name)
        print("----------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction].get_description()
            print(room + " is " + direction)

    def get_item(self):
        return self.item
    
    def set_item(self, item_name):
        self.item = item_name

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
