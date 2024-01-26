class Seat:
    '''
    Creates a class of Seat. A Seat object is by default free can be occupied by a person
    '''
    def __init__(self, occupant : str="", free: bool=True):
        self.free = free
        self.occupant = occupant

    def set_occupant(self, occupant): # working
        #  Allows the program to assign someone a seat if it's free
        if self.free == True:
            self.free = False
            self.occupant = occupant

    def remove_occupant(self, occupant): # working
        # Removes someone from a seat and returns the name of the person occupying the seat before
        if self.free == False:
            self.free = True
            self.occupant = ""
            return self.occupant

    def __str__(self):
        return self.occupant

class Table:
    '''
    The class Table accomodates Seat objects. By default creates a list of 4 empty Seat objects,
    which in turn can be assigned a person to sit on. It also keeps track of the people sitting there and the
    capacity the Table still has
    '''
    def __init__(self, capacity: int=4): # takes a list of Seat objects
        self.capacity = capacity
        self.capacity_counter = capacity
        self.index = 0
        self.seats = [Seat() for i in range(self.capacity)]


    # returns a boolean (True if a spot is available)
    def has_free_spots(self):
        if self.index < self.capacity:
            return True
        else:
            return False

    # places someone at the table
    def assign_seat(self, name): # working
        if self.has_free_spots():
            self.seats[self.index].set_occupant(name)
            self.index += 1
            self.capacity_counter -= 1

    def capacity_left(self): # working
        # returns integer
        return self.capacity_counter

    # def __repr__(self):
    #     return f"This is a table with capacity {self.capacity_counter}"


