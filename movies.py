import random
import matplotlib.pyplot as plt
import difflib


def display_welcome_message():
    print('''\u001b[32m ********** My Movies Database **********

    Menu:
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9. Create Rating Histogram
    \u001b[0m''')


def movies_library():
    movies = {
        "The Shawshank Redemption": 9.5,
        "Pulp Fiction": 8.8,
        "The Room": 3.6,
        "The Godfather": 9.2,
        "The Godfather: Part II": 9.0,
        "The Dark Knight": 9.0,
        "12 Angry Men": 8.9,
        "Everything Everywhere All At Once": 8.9,
        "Forrest Gump": 8.8,
        "Star Wars: Episode V": 8.7
    }
    return movies


def display_movies(movies):
    print()
    print(f"\u001b[37m\u001b[43m{len(movies)} movies in total\u001b[0m")
    for movie, rating in movies.items():
        print(f"\u001b[36m{movie}: {rating}")


def add_movie(movies):
    add_name = input("\u001b[35mPlease enter a name: ")
    add_rating = float(input("\u001b[35mPlease enter a rating: "))
    if 0 > add_rating or add_rating > 10:
        add_rating = float(input("\u001b[31m\u001b[1mPlease provide a number between 0.0 and 10.0: \u001b[0m"))
    print(f"\u001b[36mMovie {add_name} successfully added")
    movies.update({add_name : add_rating})
    display_movies(movies)
    return movies


def delete_movie(movies):
    movie_to_be_deleted = input("\u001b[35mPlease select a movie to be deleted: ")
    movie_found = False
    for movie in list(movies.keys()):
        if movie == movie_to_be_deleted:
            movies.pop(movie_to_be_deleted, None)
            print(f"\u001b[36mThe movie {movie_to_be_deleted} successfully deleted.")
            movie_found = True
            break
    if not movie_found:
        print("\u001b[31m\u001b[1mError! The movie is not part of the database!\u001b[0m")
    return movie


def update_movie(movies):
    movie_to_be_updated= input("\u001b[35mPlease select a movie to be updated: ")
    movie_found = False
    for movie, rating in list(movies.items()):
        if movie == movie_to_be_updated:
            movies[movie_to_be_updated] = float(input("\u001b[35mPlease insert a new rating: "))
            if 0 > movies[movie_to_be_updated] or movies[movie_to_be_updated] > 10:
                movies[movie_to_be_updated] = float(input("\u001b[31m\u001b[1mPlease provide a ration between 0 and 10: \u001b[0m"))
            print(f"\u001b[36mThe movie {movie_to_be_updated} successfully updated.")
            movie_found = True
            break
    if not movie_found:
        print("\u001b[31m\u001b[1mError! The movie you are trying to update is not part of the database!\u001b[0m")
    return movies


def stats(movies):
    ratings_sum = 0
    for movie, rating in list(movies.items()):
        ratings_sum += rating
    average_rating = ratings_sum / len (list(movies.items()))
    print("\u001b[36mAverage rating: ", round(average_rating,2))

    values = list(movies.values())
    values.sort()
    length_of_values_list = len(values)
    if length_of_values_list % 2 == 0:
        median_rating = (values[length_of_values_list // 2 - 1] + values[length_of_values_list // 2]) / 2
    else:
        median_rating = values[length_of_values_list // 2]
    print("\u001b[36mMedian rating: ", median_rating)

    best_movie, best_rating = max(movies.items(), key=lambda x: x[1])
    print(f"\u001b[36mBest movie: {best_movie}, {best_rating}")

    worst_movie, worst_rating = min(movies.items(), key=lambda x: x[1])
    print(f"\u001b[36mWorst movie: {worst_movie}, {worst_rating}")

    return average_rating, median_rating, best_movie, worst_movie


def random_movie(movies):
    random_movie, rating_of_random_movie = random.choice(list(movies.items()))
    print(f"\u001b[36mYour movie for tonight: \u001b[1m{random_movie},\u001b[0m \u001b[36mit's rated \u001b[1m{rating_of_random_movie}\u001b[0m")
    return random_movie, rating_of_random_movie


def search_movie(movies):
    matches = []
    similarity_cutoff = 0.5
    search_key = input("\u001b[35mEnter part of movie name: ")
    for movie in movies.keys():
        ratio = difflib.SequenceMatcher(None, search_key, movie).ratio()
        if ratio >= similarity_cutoff:
            matches.append((movie, movies[movie]))
    if not matches:
        print("\u001b[31m\u001b[1mNo matches found.\u001b[0m")
    for movie, rating in matches:
        print(f"\u001b[36m{movie}, {rating}")
    return matches


def sort_by_rating(movies):
    sorted_movies_dict = dict(sorted(movies.items(), key=lambda item: item[1], reverse=True))
    for movie, rating in sorted_movies_dict.items():
        print(f"\u001b[36m{movie}: {rating}")
    return sorted_movies_dict


def rating_histogram(sorted_movies_dict):
    sorted_movies_dict = dict(sorted(sorted_movies_dict.items(), key=lambda kv: kv[1]))
    fig = plt.figure(figsize=(10, 5))
    movies_list = list(sorted_movies_dict.keys())
    ratings_list = list(sorted_movies_dict.values())
    plt.bar(movies_list, ratings_list, color='skyblue', width=0.4)
    plt.xlabel("Movie name", labelpad=20)
    plt.ylabel("Rating")
    plt.title("Ratings Distribution")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    plt.savefig('Ratings_chart.png')


def show_options(movies):
    user_choice = int(input("\u001b[35mEnter choice (1-9): \u001b[0m"))

    if user_choice == 1:
        display_movies(movies)
    elif user_choice == 2:
        add_movie(movies)
    elif user_choice == 3:
        delete_movie(movies)
    elif user_choice == 4:
        update_movie(movies)
    elif user_choice == 5:
        stats(movies)
    elif user_choice == 6:
        random_movie(movies)
    elif user_choice == 7:
        search_movie(movies)
    elif user_choice == 8:
        sort_by_rating(movies)
    elif user_choice == 9:
        rating_histogram(movies)
    else:
        print("\u001b[31m\u001b[1mPlease select a number between 1 and 9.\u001b[0m")

    print()
    input("\u001b[33mPress Enter to continue...")

    while True:
        print()
        search_again = input('\u001b[35mDo you want to select another option (Y/N)?\u001b[0m')
        if search_again == 'Y' or search_again == 'y':
            display_welcome_message()
            show_options(movies)
        elif search_again == 'N' or search_again == 'n':
            exit()
        else:
            print('\u001b[31m\u001b[1mSelect Y for Yes or, N for No\u001b[0m')


def main():
    display_welcome_message()
    movies = movies_library()
    show_options(movies)


if __name__ == "__main__":
    main()
