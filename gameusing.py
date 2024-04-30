gamelist = ['noun1', 'adjetive1', 'verb1']

#Just a little game that will let the user replace variables inside a list 
#with either a adjetive, noun or verb, which will tell a story, for fun!

a = input("What noun do you want?: ")

gamelist[0]= a

s = input("Pick a adjetive: ")

gamelist[1] = s

d = input("Pick a verb: ")

gamelist[2] = d


print(f"to get to the {gamelist[1]} {gamelist[0]} they had to {gamelist[2]}.")