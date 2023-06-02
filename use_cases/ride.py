# RideShare class:
#
# Attributes
# drivers (list of Driver objects)
# passengers (list of Passenger objects)
# rides (list of Ride objects)
# Methods
# add_driver(driver): Add a new driver to the ride-sharing service.
# add_passenger(passenger): Add a new passenger to the ride-sharing service.
# request_ride(passenger_id, destination): Allow a passenger to request a ride to a specific destination.
# complete_ride(ride_id): Mark a ride as completed.
# get_total_drivers(): Return the total number of drivers in the ride-sharing service.
# get_total_passengers(): Return the total number of passengers in the ride-sharing service.
# get_active_rides(): Return the number of active rides.
# get_completed_rides(): Return the number of completed rides.
# get_driver_with_highest_rating(): Return the driver object with the highest rating.
# get_passenger_with_most_rides(): Return the passenger object with the most rides.

# Driver class:
#
# Attributes:
#
# driver_id (integer),
# name (string),
# rating (float)
# Methods:
#
# None
# Passenger class:
#
# Attributes:
# passenger_id (integer)
# name (string)
# total_rides (integer)
# Methods:
# None

# Ride class:
#
# Attributes:
# ride_id (integer)
# passenger_id (integer)
# driver_id (integer)
# destination (string)
# completed (boolean)
# Methods - None
# Your task is to implement these classes and write a program to simulate
# the ride-sharing service. The program should allow the user to perform the following
#
# operations
# Add drivers and passengers to the ride-sharing service.
# Allow passengers to request rides to specific destinations.
# Mark rides as completed.
# Retrieve and display the total number of drivers and passengers in the ride-sharing service.
# Retrieve and display the number of active rides and completed rides.
# Retrieve and display the driver with the highest rating.
# Retrieve and display the passenger with the most rides.
# Note: You are free to design the program structure and logic as per your understanding
# and preferences. The problem statement provides a basic outline of the required classes and their
# methods. You may add additional methods or attributes to enhance the functionality of the
# ride-sharing service.


class Driver:
    def __init__(self, driver_id, name, rating):
        self.driver_id = driver_id
        self.name = name
        self.rating = rating


class Passenger:
    def __init__(self, passenger_id, name, total_rides):
        self.passenger_id = passenger_id
        self.name = name
        self.total_rides = total_rides


class Ride:
    def __init__(self, ride_id, passenger_id, driver_id, destination, completed=False):
        self.ride_id = ride_id
        self.passenger_id = passenger_id
        self.driver_id = driver_id
        self.destination = destination
        self.completed = completed


class RideShare:
    def __init__(self):
        self.drivers = {}
        self.passengers = {}
        self.rides = {}

    def add_driver(self, driver: Driver):
        self.drivers[driver.driver_id] = driver
        return f"Driver '{driver.driver_id, driver.name} added"

    def add_passenger(self, passenger: Passenger):
        self.passengers[passenger.passenger_id] = passenger
        return f"Passenger '{passenger.passenger_id, passenger.name} added"

    def add_rides(self, ride):
        self.rides[ride.ride_id] = ride

    def request_ride(self, passenger_id, destination):
        print(f"passenger with id {passenger_id} has requested a ride and destination is {destination}")

    def marking_rides_as_completed(self, ride_id):
        ride: Ride = self.rides.get(ride_id)
        ride.completed = True
        return ride.completed

    def get_total_drivers(self):
        return f"Total drivers: {len(self.drivers)}"

    def get_total_passengers(self):
        return f"Total passengers: {len(self.passengers)}"

    def get_active_rides(self):
        return f"Total no of active rides: {len([ride.ride_id for ride in self.rides.values() if not ride.completed])}"

    def get_completed_rides(self):
        return f"Total no of completed rides: {len([ride.ride_id for ride in self.rides.values() if ride.completed])}"

    def get_driver_with_highest_rating(self):
        ratings = {driver.rating: driver.name for driver in self.drivers.values()}
        return f"Driver with the highest rating: {ratings[max(ratings)]}"

    def get_passenger_with_most_rides(self):
        passengers = {passenger.total_rides: passenger.name for passenger in self.passengers.values()}
        return f"Passenger with most no of rides: {passengers[max(passengers)]}"


if __name__ == "__main__":
    ride1 = Ride(ride_id=1, passenger_id=121, driver_id=20, destination="calicut")
    ride2 = Ride(ride_id=2, passenger_id=11, driver_id=35, destination="mangalore")
    share_ride = RideShare()
    share_ride.add_rides(ride1)
    share_ride.add_rides(ride2)

    driver1 = Driver(driver_id=20, name='Tom', rating=4.1)
    driver2 = Driver(driver_id=35, name='Ravi', rating=3.9)
    share_ride.add_driver(driver1)
    share_ride.add_driver(driver2)

    passenger1 = Passenger(passenger_id=121, name='John', total_rides=2)
    passenger2 = Passenger(passenger_id=11, name='Riya', total_rides=5)
    share_ride.add_passenger(passenger1)
    share_ride.add_passenger(passenger2)
    print(share_ride.marking_rides_as_completed(1))
    print(share_ride.get_total_drivers())
    print(share_ride.get_total_passengers())
    print(share_ride.get_active_rides())
    print(share_ride.get_completed_rides())
    print(share_ride.get_driver_with_highest_rating())
    print(share_ride.get_passenger_with_most_rides())
