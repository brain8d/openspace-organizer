from src.table import Table, Seat
from random import sample

class OpenSpace:
    '''
    The class OpenSpace accomodates Table objects, which in turn have Seat objects. Initializing the object will by default
    create an openspace with 6 tables, with 4 tables each. The class allows to organize the default spaces (24) seats randomly over the available tables.
    '''
    def __init__(self, number_of_tables: int, tables: list=[]):
        self.tables = tables
        self.number_of_tables = number_of_tables
        self.tables = [Table() for i in range(self.number_of_tables)]
        self.persons = 0

    def organize(self, names: list):
        # Randomly assign people to the Seat objects in the different Table objects
        names = sample(names, len(names))
        for name in names: 
            for table in self.tables:
                # go to the next table if table is full
                if table.has_free_spots() == False:
                    continue
                table.assign_seat(name)
                self.persons += 1
                break
        if len(names) > len(self.tables)*4:
            raise ValueError("There are too many persons in the room to be seated!!! The default amount is 24 seats, please add a table")

    def display(self):
        # Displays the different tables and their occupants in a nice and readable way
        for i, table in enumerate(self.tables):
            print(f"At table {i+1} sits:")
            for person in table.seats:
                print(person)
    
    def free_seats(self):
        # returns the total free seats available
            seats = [table.capacity_left() for table in self.tables]
            seats = sum(seats)
            return seats

    def persons_in_room(self):
        return self.persons
    
    def store(self):
        # Store the repartition in an Excel file
        pass







# table1 = Table()
# print("this is table 1")
# table1.assign_seat("Peter")
# table1.assign_seat("Lea")
# table1.assign_seat("Cormac")
# table1.assign_seat("Mar")
# print("has free spots", table1.has_free_spots())
# table1.assign_seat("Brian")
# print("has free spots", table1.has_free_spots())

# for person in table1.seats:
#     print(person)