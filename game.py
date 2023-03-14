'''Lab #4.5'''
class Room:
    '''
    Class of room for game.
    '''
    def __init__(self, name):
        self.name = name
        self.descrp = None
        self.item = None
        self.character = None
        self.rooms = {'west': None, 'north': None, 'east': None, 'south': None}

    def set_description(self, description):
        '''
        Set description of the room.
        >>> room0 = Room('Bathroom')
        >>> room0.set_description('a')
        >>> room0.descrp
        'a'
        '''
        self.descrp = description

    def get_details(self):
        '''
        Print details about the room.
        >>> room1 = Room('Bathroom')
        >>> room1.set_description('a')
        >>> room1.get_details()
        Bathroom
        --------------------
        a
        '''
        print(self.name)
        print('--------------------')
        print(self.descrp)
        for val in self.rooms.items():
            if bool(val[1]):
                print(f'The {val[1].name} is {val[0]}')

    def set_character(self, char):
        '''
        Put a character into the room.
        >>> room2 = Room('Bathroom')
        >>> enemy = Enemy('Zombie', 'Stinky')
        >>> room2.set_character(enemy)
        >>> room2.character == enemy
        True
        '''
        self.character = char

    def link_room(self, room_to_link, direction):
        '''
        Links the room to another room.
        >>> room3 = Room('Bathroom')
        >>> room4 = Room('Kitchen')
        >>> room3.link_room(room4, 'south')
        >>> room3.rooms['south'] == room4
        True
        '''
        self.rooms[direction] = room_to_link

    def set_item(self, item_to_set):
        '''
        Set item to the room.
        >>> room5 = Room('Bathroom')
        >>> item = Item('Book')
        >>> room5.set_item(item)
        >>> room5.item == item
        True
        '''
        self.item = item_to_set

    def get_item(self):
        '''
        Return item in the room.
        >>> room6 = Room('Bathroom')
        >>> item69 = Item('Book')
        >>> room6.set_item(item69)
        >>> room6.get_item() == room6.item
        True
        '''
        return self.item

    def get_character(self):
        '''
        Return item in the room.
        >>> room7 = Room('Bathroom')
        >>> enemy69 = Enemy('Book', 'speaks')
        >>> room7.set_character(enemy69)
        >>> room7.get_character() == room7.character
        True
        '''
        return self.character

    def move(self, room_to_move_to):
        '''
        Return room to move to.
        >>> room8 = Room('Bathroom')
        >>> room9 = Room('Kitchen')
        >>> room8.link_room(room9, 'south')
        >>> room8.move('south') == room8.rooms['south']
        True
        '''
        return self.rooms[room_to_move_to]

class Enemy:
    '''
    Class of enemy for game.
    '''
    __defeats = 0
    def __init__(self, name, descrp):
        self.name = name
        self.descrp = descrp
        self.conv = None
        self.weakness = None

    def set_conversation(self, phrase):
        '''
        Set conversation of the enemy.
        >>> enemy0 = Enemy('Zombie', 'Stinky')
        >>> enemy0.set_conversation('b')
        >>> enemy0.conv
        'b'
        '''
        self.conv = phrase

    def set_weakness(self, weakness):
        '''
        Set weakness of the enemy.
        >>> enemy1 = Enemy('Zombie', 'Stinky')
        >>> enemy1.set_weakness('b')
        >>> enemy1.weakness
        'b'
        '''
        self.weakness = weakness

    def talk(self):
        '''
        Print character's phrase.
        >>> enemy2 = Enemy('Zombie', 'Stinky')
        >>> enemy2.set_conversation('b')
        >>> enemy2.talk()
        [Zombie says]: b
        '''
        print(f"[{self.name} says]: {self.conv}")

    def describe(self):
        '''
        Describes an enemy.
        >>> enemy3 = Enemy('Zombie', 'Stinky')
        >>> enemy3.describe()
        Zombie is here!
        Stinky
        '''
        print(f'{self.name} is here!\n{self.descrp}')

    def fight(self, weapon):
        '''
        Checks if an enemy wins a fight.
        >>> enemy4 = Enemy('Zombie', 'Stinky')
        >>> enemy4.set_weakness('b')
        >>> enemy4.fight('b')
        You fend Zombie off with the b
        True
        '''
        if weapon == self.weakness:
            Enemy.__defeats += 1
            print(f'You fend {self.name} off with the {weapon}')
        else:
            print(f'{self.name} crushes you, puny adventurer!')
        return weapon == self.weakness


    def get_defeated(self):
        '''
        Return defeated variable.
        >>> enemy5 = Enemy('Zombie', 'Stinky')
        >>> enemy5.set_weakness('b')
        >>> enemy5.fight('b')
        True
        >>> enemy5.get_defeated()
        2
        '''
        return Enemy.__defeats



class Item:
    '''
    Class of item for game.
    '''
    def __init__(self, name):
        self.name = name
        self.descrp = None

    def set_description(self, description):
        '''
        Set description of the room.
        >>> item0 = Item('Book')
        >>> item0.set_description('c')
        >>> item0.descrp
        'c'
        '''
        self.descrp = description

    def describe(self):
        '''
        Describes an enemy.
        >>> item1 = Item('Book')
        >>> item1.set_description('Stinky')
        >>> item1.describe()
        The [Book] is here - Stinky
        '''
        print(f'The [{self.name}] is here - {self.descrp}')

    def get_name(self):
        '''
        Return name of item.
        >>> item2 = Item('Book')
        >>> item2.get_name()
        'Book'
        '''
        return self.name

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())