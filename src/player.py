# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room, items=[]):
        self.room = room
        self.items = items
    def move(self, dir):
        if dir.lower() == 'north':
            if self.room.n_to != None:
                self.room = self.room.n_to
                print(self.room.description)
            else:
                print("There's nothing there. You head back.")
        if dir.lower() == 'south':
            if self.room.s_to != None:
                self.room = self.room.s_to
                print(self.room.description)
            else:
                print("There's nothing there. You head back.")
        if dir.lower() == 'east':
            if self.room.e_to != None:
                self.room = self.room.e_to
                print(self.room.description)
            else:
                print("There's nothing there. You head back.")
        if dir.lower() == 'west':
            if self.room.w_to != None:
                self.room = self.room.w_to
                print(self.room.description)
            else:
                print("There's nothing there. You head back.")

    def room_items(self):
        for item in self.room.items:
            print(item)
    
    def take_item(self, command):
        for item in self.room.items:
            if item in command.lower():
                self.items.append(item)
                self.room.items.remove(item)
                print(f'Took {item}')
        
    def inventory(self):
        for item in self.items:
            print(item)