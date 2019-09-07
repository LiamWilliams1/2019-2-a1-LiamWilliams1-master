"""
Replace the contents of this module docstring with your own details
Name: Liam Williams
Date started: 27/08/19
GitHub URL: https://github.com/cp1404-students/2019-2-a1-LiamWilliams1
"""
FILE_NAME = "movies.csv"
MENU_OPTIONS = ["Q", "L", "A", "W" "C"]
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

        print("{:3} {:2} {:} {:} ({})".format(index, tag, movie[0], movie[1], movie[2]))
        index = index + 1
    print(count, "movies watch", len(movie_lists) - count, "movies left to watch")

#my intial attempt at an add movie function. For some reason I wouldn't append to the movie list. I couldn't figure out why.
#def add_movie_check(lists_of_movies):
 #   movie_name = input("Title:")
  #  while len(movie_name) < 1:
   #     print("input cannot be blank")
    #    movie_name = input("Title:")
    #year = input("year")
    #while len(year) < 1:
     #   print("input cannot be blank")
     #   year = input("year")
    #Category = input("input genre")
    #while len(Category) < 1:
     #   print("input cannot be blank")
     #   genre = input("input genre")
    #watched = ("u")
    #lists_of_movies.append([movie_name, Category, year, watched])
    #print("{}({} from {}) added to movie list".format(movie_name, Category, year,))

def add_movie(lists_of_movies):
    #new_movie = [lists_of_movies]
    movie_name = input("Title:")
    while len(movie_name) < 1:
        print("input cannot be blank")
        movie_name = input("Title:")
    year = input("year")
    while len(year) < 1:
        print("input cannot be blank")
        year = input("year")
    Category = input("input genre")
    while len(Category) < 1:
        print("input cannot be blank")
        genre = input("input genre")
    watched = ("u")
    lists_of_movies.append([movie_name, Category, year, watched])
    #new_movie.append([movie_name, Category, year, watched])
    #print(new_movie)
    #print(lists_of_movies)
    print("{}({}from {}) added to movie list".format(movie_name, Category, year,))


#def quit():

def main():
    print("Songs To Learn 1.0 - by <Liam Williams>")
    lists_of_movies, counter = load_movie()
    print(counter, "movies loaded")
    Menu_Choice = input(MENU).upper().strip()
    while Menu_Choice != "Q":
        if Menu_Choice == "L":
            display_list(lists_of_movies)
        elif Menu_Choice == "A":
            add_movie(lists_of_movies)
        elif Menu_Choice == "W":
            #watchmovie(lists_of_movies)

        else:
            print("invalid Input please try again")
        Menu_Choice = input(MENU).upper()
    print(len(lists_of_movies), "movies saved to movies.CVS\nhave a nice day :)")


if __name__ == '__main__':
    main()
