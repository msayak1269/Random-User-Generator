import random

def randomUser():
    firstNameLength = random.randrange(3,10)
    lastNameLength = random.randrange(4,10)

    firstName = ""
    lastName = ""

    for i in range(firstNameLength):
        firstName += 97+ (random.randrange(0,26))

    for i in range(lastNameLength):
        lastName += 97+ (random.randrange(0,26))

    userEmail = f"{lastname}@{firstName}.com"    

    return firstName,lastName,userEmail        