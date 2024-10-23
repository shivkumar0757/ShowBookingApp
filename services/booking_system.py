from models.bookings import Booking
from models.show import Show
from models.user import User, Viewer
from services.ranking_strategy import RankByStartTime
from utils.factory import ShowFactory


class BookingSystem:
    _instance = None

    def __init__(self):
        if not BookingSystem._instance:
            BookingSystem._instance = self
            self.shows = []  # TODO: change to dict
            self.bookings = {}  # Dictionary to map booking IDs to Bookings
            self.waitlists = {}  # Dictionary to map showId to Waitlists
            self.users = {}
            self.rankingStrategy = RankByStartTime()  # Default ranking strategy
            self.bookingIdCounter = 1

    def setRankingStrategy(self, strategy):
        self.rankingStrategy = strategy

    @staticmethod
    def get_instance():
        if not BookingSystem._instance:
            BookingSystem()
        return BookingSystem._instance

    def registerShow(self, showName, genre):
        # Register a new show
        showId = len(self.shows) + 1
        new_show = ShowFactory.create_show(showName, genre, showId)
        self.shows.append(new_show)
        print(f"Show {showName} registered successfully with genre {genre}, Id : {showId}")


    def bookTicket(self, userId, showId, timeSlot, noOfPersons):
        # Simple Logic to book a ticket for now
        for show in self.shows:
            if show.showId == showId:
                if show.bookTicket(userId, timeSlot, noOfPersons):
                    print(f"User {userId} booked {noOfPersons} tickets for {show.showName}")
                    return True
        print(f"Booking failed for Show ID {showId}")
        return False

    def registerUser(self, userId, name, userType=None):
        # new_user = User(userId, name)
        new_user = Viewer(userId, name)
        self.users[userId] = new_user
        print(f"User {name} registered successfully.")

    def searchShowsByGenre(self, genre):
        # Search for shows by genre
        available_shows = [show for show in self.shows if show.genre == genre]
        ranked_shows = self.rankingStrategy.rankShows(available_shows)
        for show in ranked_shows:
            print(f"Show: {show.showName}, Start time: {list(show.timeSlots.keys())[0]}")
        return ranked_shows

    def bookTicket(self, userId, showId, timeSlot, noOfPersons):
        user = self.users.get(userId)
        if not user:
            print("User not found.")
            return

        # Check if the user has another booking in the same time slot
        for booking in user.bookings:
            if booking.timeSlot == timeSlot:
                print(f"User {userId} already has a booking for this time slot.")
                return

        # Find the show and book the ticket if capacity allows
        for show in self.shows:
            if show.showId == showId:
                if show.timeSlots.get(timeSlot, 0) >= noOfPersons:
                    show.timeSlots[timeSlot] -= noOfPersons
                    booking = Booking(self.bookingIdCounter, userId, showId, timeSlot, noOfPersons)
                    self.bookings[self.bookingIdCounter] = booking
                    user.bookings.append(booking)
                    self.bookingIdCounter += 1
                    print(f"User {userId} booked {noOfPersons} tickets for {show.showName} at {timeSlot}")
                else:
                    print(f"Not enough capacity for {noOfPersons} persons in slot {timeSlot}.")
                return
        print(f"Show with ID {showId} not found.")

    def cancelBooking(self, bookingId):
        booking = self.bookings.pop(bookingId, None)
        if booking:
            # Restore capacity to the show
            for show in self.shows:
                if show.showId == booking.showId:
                    show.timeSlots[booking.timeSlot] += booking.noOfPersons
                    break
            # Remove the booking from the user
            user = self.users[booking.userId]
            user.bookings = [b for b in user.bookings if b.bookingId != bookingId]
            print(f"Booking {bookingId} canceled successfully.")
        else:
            print(f"Booking with ID {bookingId} not found.")

