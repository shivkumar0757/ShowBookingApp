class Show:
    def __init__(self, showId, showName, genre):
        self.showId = showId
        self.showName = showName
        self.genre = genre
        self.capacity = -1
        self.timeSlots = {}

    def addSlot(self, startTime, capacity):
        # # TODO: Check if valid (between 9am to 9pm and is of one hour max)
        #
        # show.addSlot(timeSlot.split('-'), capacity)
        if startTime not in self.timeSlots:
            self.timeSlots[startTime] = capacity
            print(f"Time slot {startTime} added with capacity {capacity}")
        else:
            print(f"Slot {startTime} already exists.")

    def bookTicket(self, userId, timeSlot, noOfPersons):
        # Logic to book tickets for a show
        pass

    def cancelTicket(self, bookingId):
        # Logic to cancel a booking and free the slot
        pass
