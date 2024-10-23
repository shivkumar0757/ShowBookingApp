from services.booking_system import BookingSystem

# if __name__ == "__main__":
#     booking_system = BookingSystem.get_instance()
#
#     # Organizer registers new shows
#     booking_system.registerShow("TMKOC", "Comedy")
#     booking_system.registerShow("Sonu Nigam Live", "Singing")
#
#     # Add time slots for the shows
#     tmkoc = booking_system.shows[0]
#     tmkoc.addSlot("9:00-10:00", 5)
#     tmkoc.addSlot("10:00-11:00", 3)
#
#     sonu_nigam = booking_system.shows[1]
#     sonu_nigam.addSlot("10:00-11:00", 4)
#     sonu_nigam.addSlot("11:00-12:00", 2)


if __name__ == "__main__":
    booking_system = BookingSystem.get_instance()

    # Registering users
    booking_system.registerUser("UserA", "Alice")
    booking_system.registerUser("UserB", "Bob")

    # Registering shows
    booking_system.registerShow("TMKOC", "Comedy")
    booking_system.registerShow("Sonu Nigam Live", "Singing")

    # Adding time slots for shows
    tmkoc = booking_system.shows[0]
    tmkoc.addSlot("9:00-10:00", 5)
    tmkoc.addSlot("12:00-13:00", 3)

    sonu_nigam = booking_system.shows[1]
    sonu_nigam.addSlot("10:00-11:00", 4)
    sonu_nigam.addSlot("13:00-14:00", 2)

    # Search and rank shows by start time
    print("\nAvailable Comedy Shows:")
    booking_system.searchShowsByGenre("Comedy")

    print("\nAvailable Singing Shows:")
    booking_system.searchShowsByGenre("Singing")

    # Booking tickets
    print("\nBooking tickets:")
    booking_system.bookTicket("UserA", 1, "9:00-10:00", 2)  # Alice books 2 tickets for TMKOC
    booking_system.bookTicket("UserB", 1, "9:00-10:00", 3)  # Bob books remaining 3 tickets for TMKOC

    # Trying to book more than available capacity
    booking_system.bookTicket("UserB", 1, "12:00-13:00", 4)  # Should fail, capacity is only 3

    # Cancel a booking
    booking_system.cancelBooking(1)  # Alice cancels her booking for TMKOC
