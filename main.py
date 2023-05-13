from functions import myFunctions
import os

while True:

    command = myFunctions.menu()


    if command == 0:
        break
    
    elif command == 1:
        myFunctions.insert()

    elif command == 2:
        myFunctions.withdraw()

    elif command == 3:
        myFunctions.search()
    