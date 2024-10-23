from models.show import Show
from utils.show_type import ShowType


class ShowFactory:
    @staticmethod
    def create_show(showName, genre, showId):
        # Dynamically create a show based on the genre
        if genre == ShowType.COMEDY.value:
            return Show(showId, showName, ShowType.COMEDY)
        elif genre == ShowType.SINGING.value:
            return Show(showId, showName, ShowType.SINGING)
        elif genre == ShowType.THEATRE.value:
            return Show(showId, showName, ShowType.THEATRE)
        elif genre == ShowType.TECH.value:
            return Show(showId, showName, ShowType.TECH)
        else:
            raise ValueError("Unknown genre")

