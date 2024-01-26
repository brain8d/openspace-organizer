import pandas as pd
from src.openspace import OpenSpace
from random import sample




# testing here
# names = [
#     "Peter", "Patrick", "Lea", "Dorothy",
#     "Lenny", "Richie", "Chaim", "Maja",
#     "Raffael", "Cormac", "Kirsty", "Norman",
#     "Rosario", "Mar", "Merida", "Luke",
#     "Robert", "Ari", "Ali", "Sander",
#     "Kiki", "Mo", "Jad", "Jabari"]


# put the main code here
if __name__ == "__main__":
    #path = input("Please provide a filepath to the list of colleagues: ")
    path = "/Users/ibex/becode/openspace-organizer/names.xlsx"
    df = pd.read_excel(path, header = None)
    names = df.iloc[:,0].tolist()
    space = OpenSpace(number_of_tables=6)
    space.organize(names)
   
    def help():
        print("Options: ")
        print("0 exit")
        print("1 display different tables and their occupants")
        print("2 get free seats in room")
        print("3 number of people in room")


    while True:
        print()
        help()
        option = int(input("Pick option: "))
        print("")
        if option == 0:
            break
        elif option == 1:
            space.display()
        elif option == 2:
            print(f"Free seats in room: {space.free_seats()}")
        elif option == 3:
            print(f"There are {space.persons_in_room()} persons in the room")
        # elif option == 4:
        #     names = sample(names, len(names))
        #     space.organize(names)
        #     print("Reshuffling...")
