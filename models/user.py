from abc import ABC, abstractmethod

# from services.booking_system import BookingSystem


class User(ABC):
    def __init__(self, userId, name):
        self.userId = userId
        self.name = name


class Organizer(User):
    def registerShow(self, showName, genre):
        # Logic to register a new show
        pass

    def onboardShowSlots(self, showId, timeSlot, capacity):
        # Adds time slots to the show
        pass



class Viewer(User):
    def __init__(self, userId, name):
        super().__init__(userId, name)
        self.bookings = []



    def viewBookings(self):
        # Logic to view the user's bookings
        if not self.bookings:
            print(f"{self.name} has no bookings.")
        else:
            print(f"{self.name}'s bookings:")
            for booking in self.bookings:
                print(booking)
