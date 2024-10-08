# Write your solution here:

class Series:

    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.average = 0

    def __str__(self) -> str:
        if len(self.ratings) == 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\nno ratings"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{len(self.ratings)} ratings, average {self.average} points"
    
    def rate(self, rating: int):
        if rating >= 0 and rating <= 5:
            self.ratings.append(rating)
            self.average = round(sum(self.ratings) / len(self.ratings), 1)


def minimum_grade(rating: float, series_list: list):
    min_grade_series = [i for i in series_list if i.average >= rating]
    return min_grade_series

def includes_genre(genre: str, series_list: list):
    genre_series = [i for i in series_list if genre in i.genres]
    return genre_series
    

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)