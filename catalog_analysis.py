import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson",
                                                    "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


# TASK 1
def average_rating(movies):
    avg_rating = round(sum(movie["rating"] for movie in movies) / len(movies), 1)
    return avg_rating


def catalog_age_stats(movies, current_year=2026):
    oldest = current_year - min(movie["year"] for movie in movies)
    newest = current_year - max(movie["year"] for movie in movies)
    avg_age = math.ceil(sum(current_year - movie["year"] for movie in movies)
                        / len(movies))
    return (oldest, newest, avg_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# TASK 2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо" if rating >= 0 else "некорректная оценка"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"


# TASK 3
print("NOT comedy movies:")
for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])

i = 0
first_high_rated = ""
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        first_high_rated = movies[i]  # сохраняю в переменную, т.к. по заданию
        # не понятно, надо ли выводить его
        break
    i += 1

else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    counter = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            counter += 1
    return counter


# TASK 4
def normalize_title(title):
    words = title.split()
    for i in range(len(words)):
        words[i] = words[i][0].upper() + words[i][1:]
    return " ".join(words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    return f'"{normalize_title(movie["title"])}" ' \
           f'({movie["year"]}) — {movie["rating"]}/10, ' \
           f'{duration_in_hours(movie["duration_min"])}, ' \
           f'жанры: {", ".join(sorted(movie["genres"]))}'


# TASK 5
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [normalize_title(movie["title"]) for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(normalize_title(movie["title"]), movie["rating"])
            for movie in sorted_movies[:n]]


# TASK 6
def count_by_genre(movies):
    dict_genres = {}
    for movie in movies:
        for genre in movie["genres"]:
            dict_genres[genre] = dict_genres.get(genre, 0) + 1
    return dict_genres


def actor_filmography(movies):
    dict_actors = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in dict_actors:
                dict_actors[actor] = []
            dict_actors[actor].append(normalize_title(movie["title"]))
    return dict_actors


dict_upper_avg = {normalize_title(movie["title"]): movie["rating"]
                  for movie in movies if movie["rating"]
                  > average_rating(movies)}


# TASK 7
def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    set_a = set()
    set_b = set()
    for movie in movies_a:
        set_a.update(movie["genres"])
    for movie in movies_b:
        set_b.update(movie["genres"])
    return set_a - set_b


# TASK 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


for movie in iter_high_rated(movies):
    print(format_report_line(movie))

sum(m["duration_min"] for m in movies if m["rating"] > 7)


# TASK 9
def build_report(movies):
    print("\nОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]}\n")
    print("Топ-3 фильма:")
    top_titles = titles_sorted_by_rating(movies)[:3]
    for title in top_titles:
        for movie in movies:
            if normalize_title(movie["title"]) == title:
                print("  " + format_report_line(movie))
                break

    print("\nФильмов по жанрам:")
    genres = count_by_genre(movies)
    for genre in sorted(genres, key=genres.get, reverse=True):
        print(f'  {genre} — {genres[genre]}')

    print("\nВсе жанры каталога: " + ", ".join(sorted(all_genres(movies))))


build_report(movies)
