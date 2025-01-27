age = 10
height = 170
ticket = 'Superticket'

if age >=8 and height >= 135 and ticket == 'Superticket':
    print('You can ride the ride!')

if age >= 17 or height >= 160:
    print ("You can ride the scary ride!")

if height < 120:
    print ('You cant ride any of the rides :(')
elif height < 135:
    print ('You can ride level one rides')
elif height < 200:
    print ('You can ride any ride!')
else:
    print ('You are too tall to ride any of the rides :(')

if height > 135 and age % 2 == 0 or age == 1:
    print ('You are weird')


direction = input ('Which direction? ').lower()
match direction:
    case 'north':
        print ('You are going UP')
    case 'west':
        print ('You are going LEFT')
    case 'east':
        print ('You are going RIGHT')
    case 'south':
        print ('You are going DOWN')
    case _:
        print ('That isnt a direction my guy')


floor = 13

match floor:
    case 4:
        print ('Unlucky in Japan')
    case 13:
        print ('Unlucky in USA')
    case _:
        print ('Floor seems fine to me')