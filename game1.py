import random
def game(comp, you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'
you=input("Snake(s), Water(w) or Gun(g) for Player 2: ")
print(f"Computer Choose {comp}")
print(f"You Choose {you}")
# print("\n")
a=game(comp, you)
if a==None:
    print("The game is tied!")
elif a:
    print("YOU WON")
else:
    print("You Lose")    
