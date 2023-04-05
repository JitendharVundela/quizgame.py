print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")

if playing.lower()!="yes":
    quit()

print("Okay! Let's play :)")   
score=0 

answer=input("Who is the person that started amazon? ")
if answer.lower()=="jeff bezos":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

answer=input("Who is the CEO os SpaceX? ")
if answer.lower()=="elon musk":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")    

answer=input("Who is the president of USA? ")
if answer.lower()=="joe biden":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")   

answer=input("What dose CPU stands for? ")
if answer.lower()=="central processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")    

answer=input("What dose ALU stands for? ")
if answer.lower()=="arithmetic logic unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")    


print("You got " +str(score) +" questions correct!")    
print("You got " +str((score/5)*100) +" %.") 