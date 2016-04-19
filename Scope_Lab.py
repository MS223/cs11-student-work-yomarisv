a = [1, 2, 4]
b = a
#Adapting B to A will not effect A because they are both a seperate variable.
a = [1, 2, 4]
b = a
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
print my_list 
#It printed the list.
var_1 = "kittens"
var_2 = "cookies"
# input: a string
# output: a string
def my_function(my_favorite_things):
    song_lyrics = "rain drops on roses,"
    combined_song = song_lyrics + my_favorite_things
    print combined_song
# input: a string
# output: a string
def my_function_2(item, item2):
    full_lyrics = item + "on " + item2
    full_song = my_function(full_lyrics)
    return full_song
my_song = my_function_2(var_1, var_2)
#Since I know that print is for people I decided to change the first return to print and got "rain drops on roses,kittenson cookies".
