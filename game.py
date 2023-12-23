import random
# water , snake and gun game computer vs player:
# 1=water
# 2= snake
# 3= gun
def game():    
    if comp==you:
        #print("Result Tied")
        return None
    elif comp=="w":
        if you=="s":
            #print(" you win")
            return  True
        elif you=='g':
            #print("you loss")
            return False
    elif comp=='s':
        if you=='w':
            #print("you loss")
            return False
        elif you=='g':
            #print("you win")
            return True
    elif comp=='g':
        if you=='w':
            #print("you win")
            return True
        elif you=='s':
            #print("you loss")
            return False

randNo= random.randint(1,3)
if randNo==1:
    comp='w'
elif randNo==2:
    comp='s'
elif randNo==3:
    comp='g'
you= input("enter you turn: water(w),snake(s),or  gun(g): ")
gm=game()
if gm==None:
    print("GAME TIED")
elif gm== True:
    print("YOU WIN")
elif gm==False:
    print("YOU LOSS")
print("coputer choice:",comp)
print("your choice :",you)