class Item:
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def describe(self):
        print("\nItem: [" + self.name + "] is here - " + self.description)