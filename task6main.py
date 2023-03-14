'''Lab #4.5'''
import task6gamelviv

palka = task6gamelviv.Item('Palka', 'a wooden stick from nearby forest.')
trakt = task6gamelviv.Room('Trakt', 'This is were you start your journey, adventurer! There is no enemies here yet but be careful.', palka)

kluch_na_9 = task6gamelviv.Item('Kluch na 9', 'great tool ro repair anything!')
shliopky = task6gamelviv.Shoes('Shliopky', 'not the best shoes ever but still OK.', 2)
laydak = task6gamelviv.Laydak('Laydak Ivan', 'Ordinary homeless man, but some people say he is a wizard...',\
                    'I will make you mighty and strong, but the price for it is palka.')
vodiy_29 = task6gamelviv.Lotr('Vodiy 29ої', 'Angry marshrutka driver whose transport broke down.\nWell known bandit in Lviv.',\
                    'Give me your palka and I will mercy you!', palka, kluch_na_9, desired_item=palka)
lychakivska = task6gamelviv.Room('Lychakivska', 'This Lychakivska street - road to the heart of the city.', shliopky, friend=laydak, enemy=vodiy_29)

pivo = task6gamelviv.Item('Lvivske Rizdviane', 'temne - yak zymova nich, vesele - yak koliada!')
podkraduli = task6gamelviv.Shoes('Podkraduli', 'podkraduli-skorohody. Allows you to travel with the speed of light!', 666)
meshtu = task6gamelviv.Shoes('Meshtu', 'Napastovani meshtu in mate black.', 2)
kavaler = task6gamelviv.Kavaler('Kavaler Bogdan', 'Handsome young man whose bycicle broke down.', 'I really need your help to repair this bycicle!',\
                        podkraduli, kluch_na_9)
sadovyi = task6gamelviv.Batyar('Sadovyi', 'Most wanted Lviv crime boss. Almost...', 'Dai brukivky kurva!', pivo, meshtu)
centr = task6gamelviv.Room('Centr', 'Heart of the city and our last stop before finale.', pivo, friend=kavaler, enemy=sadovyi)

sobachi_podkraduli = task6gamelviv.Shoes('Sobachi podkraduli', 'Podkraduli for dogs, last model.', 228)
pes_patron = task6gamelviv.Batyar('Pes Patron', 'National leader and top 1 dog in the world!', 'Gav, gav!', pivo, sobachi_podkraduli)
sykhiv = task6gamelviv.Sykhiv(pes_patron)

trakt.link_room(lychakivska)
lychakivska.link_room(centr)
centr.link_room(sykhiv)

current_room = trakt
backpack = []
shoes = task6gamelviv.Shoes('Bosyi', 'walking barefoot is not the best idea.', 1)

alive = True

while alive:
    print()
    if isinstance(current_room, task6gamelviv.Sykhiv):
        enemy0 = current_room.enemy
        print(current_room.name)
        print('--------------------')
        print(current_room.descrp)
        enemy0.describe()
        enemy0.talk()
        print('Available commands:\nfight (fight with enemy),\nrun (run from enemy)')
        command = input("> ")
        if command == 'fight':
            print('Narrow streets of Sykhiv is a great location for Pes Patron to hunt. You are dead!')
            alive = False
            print('You lost(( Try again!')
        elif command == 'run':
            if enemy0.chase(shoes):
                print('Do you want to run again or to fight?')
                choice = input()
                if choice == 'fight':
                    print("What will you fight with?")
                    print('You have:')
                    for b_item10 in backpack:
                        print(b_item10.name)
                    print()
                    fight_with0 = input()
                    for b_item5 in backpack:
                        if b_item5.name == fight_with0:
                            fight_with0 = b_item5
                            break
                    else:
                        print(f'You do not have {fight_with0}.')
                    if isinstance(fight_with0, task6gamelviv.Item):
                        if enemy0.fight(fight_with0.name):
                            print('Pes Patron is Lvivske Rizdviane enjoyer, so he let you go! You won the game!')
                            break
                        else:
                            alive = False
                            print('You lost(( Try again!')
                elif choice == 'run':
                    print('Pes Patron have put mines all over Sykhiv and you blow up!')
                    alive = False
                    print('You lost(( Try again!')
            else:
                alive = False
                print('You lost(( Try again!')
        else:
            print("I don't know how to " + command)

    else:
        print('Available commands: go (proceed to next location),\ntalk (talk to inhabitants),\ntake (take item),\nhelp (interact with friends),\nfight (fight with enemy),\nrun (run from enemy),\nnegotiate(negotiate with enemy).')
        print()
        current_room.get_details()

        inhabitants = [current_room.friend, current_room.enemy]
        for inhabitant1 in inhabitants:
            if inhabitant1 is not None:
                inhabitant1.describe()
        if current_room.item is not None:
            item = current_room.item
            item.describe()

        command = input("> ")

        if command == 'go':
            current_room = current_room.move()
        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            for inhabitant2 in inhabitants:
                if inhabitant2 is not None:
                    inhabitant2.talk()
        elif command == "take":
            if item is not None:
                print("You put the " + item.name + " in your backpack")
                if isinstance(item, task6gamelviv.Shoes):
                    shoes = item
                else:
                    backpack.append(item)
                current_room.set_item(None)
            else:
                print("There's nothing here to take!")
        elif command == 'help':
            if inhabitants[0]:
                if backpack:
                    if isinstance(inhabitants[0], task6gamelviv.Laydak):
                        print(f'What do you want to give to {inhabitants[0].name}')
                        print('You have:')
                        for b_item1 in backpack:
                            print(b_item1.name)
                        print()
                        item_to_give = input()
                        for b_item2 in backpack:
                            if b_item2.name == item_to_give:
                                item_to_give = b_item2
                                break
                        else:
                            print(f'You do not have {item_to_give}.')
                        if isinstance(item_to_give, task6gamelviv.Item):
                            inhabitants[0].take_item(item_to_give)
                            inds0 = []
                            for ind0, val0 in enumerate(backpack):
                                if val0.name == item_to_give.name:
                                    inds0.append(ind0)
                            for ind00 in inds0:
                                backpack.pop(ind00)
                    else:
                        print(f'What do you want to give to {inhabitants[0].name}')
                        print('You have:')
                        for b_item3 in backpack:
                            print(b_item3.name)
                        print()
                        item_to_give = input()
                        for b_item4 in backpack:
                            if b_item4.name == item_to_give:
                                item_to_give = b_item4
                                break
                        else:
                            print(f'You do not have {item_to_give}.')
                        if isinstance(item_to_give, task6gamelviv.Item):
                            if inhabitants[0].exchange_item(item_to_give.name):
                                if isinstance(inhabitants[0].item, task6gamelviv.Shoes):
                                    shoes = inhabitants[0].item
                                else:
                                    backpack.append(inhabitants[0].item)
                                inds1 = []
                                for ind1, val1 in enumerate(backpack):
                                    if val1.name == item_to_give.name:
                                        inds1.append(ind1)
                                for ind11 in inds1:
                                    backpack.pop(ind11)
                else:
                    print('Your backpack is empty.')
            else:
                print('Nobody is around for you to help him!')
        elif command == "fight":
            if inhabitants[1]:
                print("What will you fight with?")
                print('You have:')
                for b_item10 in backpack:
                    print(b_item10.name)
                print()
                fight_with = input()
                for b_item5 in backpack:
                    if b_item5.name == fight_with:
                        fight_with = b_item5
                        break
                else:
                    print(f'You do not have {fight_with}.')

                if isinstance(fight_with, task6gamelviv.Item):
                    if inhabitants[1].fight(fight_with.name):
                        if isinstance(inhabitants[1], task6gamelviv.Lotr):
                            backpack.append(inhabitants[1].item)
                            inds2 = []
                            for ind2, val2 in enumerate(backpack):
                                if val2.name == fight_with.name:
                                    inds2.append(ind2)
                            for ind22 in inds2:
                                backpack.pop(ind22)
                            current_room.enemy = None
                        else:
                            inds10 = []
                            for ind10, val10 in enumerate(backpack):
                                if val2.name == fight_with.name:
                                    inds10.append(ind10)
                            for ind1010 in inds10:
                                backpack.pop(ind1010)
                            current_room.enemy = None
                    else:
                        alive = False
                        print('You lost(( Try again!')
            else:
                print("There is no one here to fight with")
        elif command == 'run':
            if inhabitants[1]:
                if isinstance(inhabitants[1], task6gamelviv.Batyar):
                    if inhabitants[1].chase(shoes):
                        print(f'{inhabitants[1].name} was too slow and got lost!')
                        current_room.enemy = None
                    else:
                        alive = False
                        print('You lost(( Try again!')
                else:
                    print('Nobody is here you can run from!')
            else:
                print('Nobody is here you can run from!')
        elif command == 'negotiate':
            if inhabitants[1]:
                if isinstance(inhabitants[1], task6gamelviv.Lotr):
                    print("What will you fight with?")
                    print('You have:')
                    for b_item11 in backpack:
                        print(b_item11.name)
                    print()
                    exchange_item = input()
                    for b_item6 in backpack:
                        if b_item6.name == exchange_item:
                            exchange_item = b_item6
                            break
                    else:
                        print(f'You do not have {exchange_item}.')
                else:
                    print('Nobody to negotiate with!')
                if isinstance(exchange_item, task6gamelviv.Item):
                    if inhabitants[1].exchange(exchange_item.name):
                        inds3 = []
                        for ind3, val3 in enumerate(backpack):
                            if val3.name == exchange_item.name:
                                inds3.append(ind3)
                        for ind33 in inds3:
                            backpack.pop(ind33)
                        current_room.enemy = None
                    else:
                        alive = False
                        print('You lost(( Try again!')
            else:
                print('Nobody to negotiate with!')
        else:
            print("I don't know how to " + command)
