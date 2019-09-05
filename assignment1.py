"""
Replace the contents of this module docstring with your own details
Name: Liam Williams
Date started: 27/08/19
GitHub URL: https://github.com/cp1404-students/2019-2-a1-LiamWilliams1
"""

MENU_OPTIONS = ["Q", "L", "A", "W"]
MENU = """MENU:
L - List Movies
A - Add new movie
W - watch a movie
Q - Quit \n >>> """

def load_movies():
    lists_of_movies = []
    in_file = 0
    try:
        in_file = open("movies.csv", 'r')
    except FileNotFoundError:
        print("File not found")
    for movie in in_file:
        movie = movie.strip("\n")
        new_list = movie.split(",")
        lists_of_movies.append(new_list)
    in_file.close()
    print(in_file)
    return lists_of_movies


def main():

    """..."""
    print("Movies To Watch 1.0 - by <Liam Williams>")
    #print({} .format(movies_loaded_count))
    lists_of_movies = []
    Menu_Choice = input(MENU).upper().strip()
    while Menu_Choice != "Q":
        if Menu_Choice == "L":
            print("you sele ted l")
        elif Menu_Choice == "A":
            print("you select a")
        elif Menu_Choice == "W":


            print("invalid Input please try again")
        Menu_Choice = input(MENU).upper()
    print("end")


if __name__ == '__main__':
    main()
