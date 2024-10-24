class Waitlist:
    def __init__(self, showId):
        self.showId = showId
        self.waitlistQueue = []

    def addToWaitlist(self, userId):
        self.waitlistQueue.append(userId)

    def promoteWaitlistedUser(self):
        if self.waitlistQueue:
            return self.waitlistQueue.pop(0)
        return None

    def notify(self):
        # Notify the first person in the waitlist
        if self.waitlistQueue:
            next_user = self.waitlistQueue.pop(0)
            print(f"User {next_user} is being notified for an available slot.")
            return next_user
        return None
