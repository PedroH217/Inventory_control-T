from functions import myFunctions
import os

for x in range(0,2):

    command = myFunctions.menu()

    os.system('cls' if os.name == 'nt' else 'clear')

    if command == 0:
        break
    
    elif command == 1:
        myFunctions.insert()

    elif command == 2:
        pass

    elif command == 3:
        pass
    