'''Lab #4.6'''
class Room:
    '''
    Class of room for game.
    '''
    def __init__(self, name, descrp, item=None, enemy=None, friend=None):
        self.name = name
        self.descrp = descrp
        self.item = item
        self.enemy = enemy
        self.friend = friend
        self.next_room = None

    def get_details(self):
        '''
        Print details about the room.
        '''
        print(self.name)
        print('--------------------')
        print(self.descrp)

    def link_room(self, room_to_link):
        '''
        Links the room to another room.
        '''
        self.next_room = room_to_link

    def move(self):
        '''
        Return room to move to.
        True
        '''
        return self.next_room

    def set_item(self, item_to_set):
        '''
        Set item to the room.
        '''
        self.item = item_to_set

class Sykhiv():
    def __init__(self, enemy):
        self.name = 'Sykhiv'
        self.descrp = 'Your last stop...'
        self.enemy = enemy

    def start_battle(self):
        '''
        Prints info about battle.
        '''
        print('Final boss - Syniutka - is standing before you.\n You have to fight him now.')


class Character:
    '''
    Class of character for game.
    '''
    def __init__(self, name, descrp, conv):
        self.name = name
        self.descrp = descrp
        self.conv = conv

    def talk(self):
        '''
        Print character's phrase.
        '''
        print(f"[{self.name} says]: {self.conv}")

    def describe(self):
        '''
        Describes an enemy.
        '''
        print(f'{self.name} is here!\n{self.descrp}')

class Friend(Character):
    '''
    Class of Friend for game.
    '''
    def describe(self):
        '''
        Describes an enemy.
        '''
        print(f'{self.name} is here!\n{self.descrp}')

class Laydak(Friend):
    '''
    Class of Laydak for game.
    '''
    def take_item(self, item):
        '''
        Takes item and return you nothing.
        '''
        print(f"Sorry, but {self.name} doesn't have anything to offer. But he thanks you for {item.name}!)")

class Kavaler(Friend):
    '''
    Class of Kavaler for game.
    '''
    def __init__(self, name, descrp, conv, item, desired_item):
        self.item = item
        self.desired_item = desired_item
        super().__init__(name, descrp, conv)

    def exchange_item(self, item):
        '''
        Takes item and gives away new item.
        '''
        if item == self.desired_item.name:
            print(f'This is exactly what {self.name} wanted! Take {self.item.name} instead!')
        else:
            print(f'Not what {self.name} wanted... But you can have it back.')
        return item == self.desired_item.name

class Enemy(Character):
    '''
    Class of enemy for game.
    '''
    def __init__(self, name, descrp, conv, weakness):
        self.weakness = weakness
        super().__init__(name, descrp, conv)

    def talk(self):
        '''
        Print character's phrase.
        '''
        print(f"[{self.name} says]: {self.conv}")

    def describe(self):
        '''
        Describes an enemy.
        '''
        print(f'{self.name} is here!\n{self.descrp}')

    def fight(self, weapon):
        '''
        Checks if an enemy wins a fight.
        '''
        if weapon == self.weakness.name:
            print(f'You fend {self.name} off with the {weapon}!')
        else:
            print(f'{self.name} crushes you, puny adventurer!')
        return weapon == self.weakness.name

class Batyar(Enemy):
    '''
    Class of Batyar for game.
    '''
    def __init__(self, name, descrp, conv, weakness,shoes):
        self.shoes = shoes
        super().__init__(name, descrp, conv, weakness)

    def chase(self, shoes):
        '''
        Checks if an enemy wins a fight.
        '''
        if shoes.speed >= self.shoes.speed:
            print(f'You ran away from {self.name}!')
        else:
            print(f'{self.name} caught you. You are dead!')
        return shoes.speed >= self.shoes.speed

class Lotr(Enemy):
    '''
    Class of Lotr for game.
    '''
    def __init__(self, name, descrp, conv, weakness, item, desired_item):
        self.item = item
        self.desired_item = desired_item
        super().__init__(name, descrp, conv, weakness)

    def exchange(self, item):
        '''
        Checks if an enemy wins a fight.
        '''
        if item.name == self.desired_item:
            print(f'{self.name} love your gift. He is leaving the city now!')
        else:
            print(f"{self.name} didn't like your gift. You are dead!")
        return item.name == self.desired_item

    def get_desired_item(self):
        '''
        Return desired item.
        '''
        return self.desired_item

class Item:
    '''
    Class of item for game.
    '''
    def __init__(self, name, descrp):
        self.name = name
        self.descrp = descrp

    def describe(self):
        '''
        Describes an enemy.
        '''
        print(f'The {self.name} is here - {self.descrp}')

class Shoes(Item):
    '''
    Class of shoes for game.
    '''
    def __init__(self, name, descrp, speed):
        self.speed = speed
        super().__init__(name, descrp)