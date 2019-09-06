"""
Replace the contents of this module docstring with your own details
Name: Liam Williams
Date started: 27/08/19
GitHub URL: https://github.com/cp1404-students/2019-2-a1-LiamWilliams1
"""
FILE_NAME = "movies.csv"
MENU_OPTIONS = ["Q", "L", "A", "W"]
MENU = """L - List Movies
A - Add new movie
W - watch a movie
Q - Quit \n >>> """



def load_movie():
    lists_of_movies = []
    count_movies = 0
    in_file = 0
    try:
        in_file = open(FILE_NAME, 'r')
    except FileNotFoundError:
        print("File not found")
    for movie in in_file:
        movie = movie.strip("\n")
        new_list = movie.split(",")
        lists_of_movies.append(new_list)
        count_movies += 1
    in_file.close()
    return lists_of_movies, count_movies


def display_list(movie_lists):
    tag = ()
    count = 0
    index = 0
    for movie in movie_lists:

        if movie[3] == "w":
            tag = "*"
            count += 1
        else:
            tag = " "

        print("{:3} {:2} {:35} {:25} ({})".format(index, tag, movie[0], movie[1], movie[2]))
        index = index + 1
    print(count, "movies watch", len(movie_lists) - count, "movies left to watch")



def main():
    print("Songs To Learn 1.0 - by <Liam Williams>")
    lists_of_movies, counter = load_movie()
    print(counter, "movies loaded")
    Menu_Choice = input(MENU).upper().strip()
    while Menu_Choice != "Q":
        if Menu_Choice == "L":
            display_list(lists_of_movies)
        else:
            print("invalid Input please try again")
        Menu_Choice = input(MENU).upper()
    print(len(lists_of_movies), "movies saved to movies.CVS\nhave a nice day :)")


if __name__ == '__main__':
    main()
