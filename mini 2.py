# 1) Create a class named Vehicle.
# d) Create a constructor that takes 3 arguments and passes each argument to the appropriate
# property.
class Vehicle:
    def __init__(self, color, num_of_doors, gas_powered):
        """
        This __init__ set the Vehicle object with specified attributes

        a) The class will have the following PRIVATE attributes
            i) color
            ii) number of doors (whole number)
            iii) whether the vehicle is gas powered (Boolean)

        :param color: color of vehicle
        :param num_of_doors: number of door of the vehicle
        :param gas_powered: define the vehicle if is gas_powered
        :type color: str
        :type num_of_doors: int
        :type gas_powered: bool
        """
        self.__color = color
        self.__num_of_doors = num_of_doors
        self.__gas_powered = gas_powered
        """
        b) Each private attribute will have restricted values
            i) For color, only allow string values, AND only allow any 5 colors (you choice)
            ii) For doors, only allow 2, 4 and 5 doors (only accept 1 of 3 whole numbers)
            iii) For gas powered, only allow Boolean values
        """
    """
    d) Create the getters and setters for the private attributes
    """
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        allow_colors = ["Red", "Blue", "Green", "Black", "White"]
        if value in allow_colors:
            self.__color = value
        else:
            print("Invalid color. Please choose from: RED, BLUE, GREEN, BLACK, WHITE")
            raise ValueError("Invalid color. Please choose from: RED, BLUE, GREEN, BLACK, WHITE")

    @property
    def num_of_doors(self):
        return self.__num_of_doors

    @num_of_doors.setter
    def num_of_doors(self, value):
        allow_number = [2, 4, 5]
        if value in allow_number:
            self.__num_of_doors = value
        else:
            raise ValueError("Invalid number of doors. Please choose from: 2, 4, 5")

    @property
    def gas_powered(self):
        return self.__gas_powered

    @gas_powered.setter
    def gas_powered(self, value):
        if isinstance(value, bool):
            self.__gas_powered = value
        else:
            raise ValueError("Gas powered attribute must be True or False")

    # e) Override the toString method to summarize all instance variables of the class
    def __str__(self):
        return f"\tVehicle\nColor: {self.color}\nDoors: {self.num_of_doors}\nGas Powered: {self.gas_powered}"

    def is_eco_friendly(self):
        """
        f) Create a method named is_eco_friendly().
            i) It requires no parameters and returns a Boolean value
                (1) It determines whether the Vehicle is two-doored and is not gas powered

        Determine Vehicle is eco-friendly and two-doored
        :return: True if vehicle is eco-friendly, False not eco-friendly.
        :rtype: bool
        """
        if self.__num_of_doors == 2:
            case = True
        else:
            case = False

        if self.gas_powered:
            eco = True
        else:
            eco = False

        return f"Number of door met: {case}\nEco-friendly: {eco}"


class Truck(Vehicle):
    """
    c) Create a constructor that takes 5 arguments and passes each argument to the appropriate property.
    """
    def __init__(self, color, num_of_doors, gas_powered, seats, trunk_space):
        """
        1) Create a class named Truck that is based on the Vehicle class
            a) Create two additional private attributes
                i) seats (whole number)
                ii) trunk space (whole number)

        :param color: color of truck
        :param num_of_doors: number of doors of the truck
        :param gas_powered: define whether the truck is gas powered
        :param seats: number of seats in the truck
        :param trunk_space: available trunk space in the truck
        :type color: str
        :type num_of_doors: int
        :type gas_powered: bool
        :type seats: int
        :type trunk_space: int
        """
        super().__init__(color, num_of_doors, gas_powered)
        self.__seats = seats
        self.__trunk_space = trunk_space

    """
    d) Override the toString method to summarize all properties variables of the class (2 marks)
        **Please note, there are 5 properties to summarize **
    """
    def __str__(self):
        return f"\tTruck {super().__str__()}\nSeats: {self.seats}\nTrunk Space: {self.trunk_space}"
    """
    2) Override the is_eco_friendly() method. In addition to its original behavior, it also determines if the
        Truck has at most two seats and has no trunk space.
    """
    def is_eco_friendly(self):
        """
        Determined whether the Truck is eco_friendly
        :return: True if the Truck is eco-friendly. False Truck is not eco-friendly
        :rtype: bool
        """
        old_condition = super().is_eco_friendly()

        if self.seats >= 2:
            seat = True
        else:
            seat = False

        if self.trunk_space == 0:
            space = True
        else:
            space = False

        return f"{old_condition}\nNumber of seats met: {seat}\nNumber of trunk space met: {space}"
    """
    b) Create the getters and setters for the private attributes. Ensure that each attribute corresponds
        to the data type outlined about and has a value greater than zero
    """
    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        if isinstance(value, int) and value > 0:
            self.__seats = value
        else:
            raise ValueError("Your Truck must have at lease 1 seat")

    @property
    def trunk_space(self):
        return self.__trunk_space

    @trunk_space.setter
    def trunk_space(self, value):
        if isinstance(value, int):
            self.__trunk_space = value
        else:
            raise ValueError("Please input whole number")


car = Vehicle("pink", 2, True)  # This line won't raise a ValueError
print(car)
car.color = "Red"
car.num_of_doors = 2
car.gas_powered = False
print(car)
print(car.is_eco_friendly())
# car.color = "purple"
# print(car)
truck = Truck("Green", 2, False, 1, 0)
print(truck)
print(truck.is_eco_friendly())
