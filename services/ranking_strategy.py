from abc import ABC, abstractmethod

class RankingStrategy(ABC):
    @abstractmethod
    def rankShows(self, shows):
        pass


class RankByStartTime(RankingStrategy):
    def rankShows(self, shows):
        # Rank shows by start time (assuming each show has time slots sorted by start time)
        return sorted(shows, key=lambda show: list(show.timeSlots.keys())[0])


# class RankByPopularity(RankingStrategy):
#     def rankShows(self, shows):
#         # Rank by the number of bookings (popularity)
#         return sorted(shows, key=lambda show: len(show.bookings), reverse=True)
