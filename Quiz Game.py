print ("WELCOME TO MY QUIZ GAME !")

Intrested  = input("Do you want to play? ")

if Intrested!= ("yes"):
    exit()

print("okay, let's play")
score = 0

#if we use .lower() to the variable then it will convert the answer into lower cases, and .upper() into upper case, doesn't matter in what case you have typed
# example =)

#question = input("what does CPU stands for ? ")
#if question.lower() == ("central processing unit"):
# print ("correct! ")
#else:
# print("incorrect! ")

#question = input("what does CPU stands for ? ")
#if question.upper() == ("central processing unit"):
#  print ("correct! ")
#else:
#   print("incorrect! ")


question = input("what does CPU stands for ? ")
if question == ("central processing unit"):
    print ("correct! ")
    score += 2
else:
    print("incorrect! ")

question = input("what does DVD stands for ? ")
if question == ("digital versatile disk"):
    print ("correct! ")
    score += 2
else:
    print("incorrect! ")

question = input("what does SSD stands for ? ")
if question == ("solid state drive"):
    print ("correct! ")
    score += 2
else:
    print("incorrect! ")

question = input("what does HDD stands for ? ")
if question == ("hard disk drive"):
    print ("correct! ")
    score += 2
else:
    print("incorrect! ")

question = input("what does GPU stands for ? ")
if question == ("graphics processing unit"):
    print ("correct! ")
    score += 2
else:
    print("incorrect! ")

print ("you got " +  str(score/2)  + " questions correct !")
print ("you gained score of " +  str(score) )
print ("you gained " + str((score/10)*100) + "%" + " score")

if score > 6:
    print ("you did great")
elif score == 0:
    print ("you failed")
else:
    print ("well done, try hard")
