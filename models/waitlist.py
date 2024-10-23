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
