# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.
def display_message():
    """prints a message about what youre learning in this chapter."""
    print("in this chapter, I am learning about functions in python.")

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.
def favorite_book():
    """prints a message about favorite book()."""
    print("one of my favourite books if {title}. ")

# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
def make_shirt(size, message):
    """print a message summarizing the size of a shirt and the message printed on it."""
    print("the shirt is size {size} and will have a message '(message)' printed on it.")

# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
def make_shirt(message="I love python", size="Large"):
    print("making a {size} shirt with the message: '{message}'")
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", message="python is awesome")

# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
def describe_city(city, country="unknown"):
    print(f"{city} is in {country}.")
describe_city("Toronto")
describe_city("paris", "France")
describe_city("Dubai")

# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
#"Santiago, Chile"
# Call your function with at least three city-country pairs, and print the
# values that are returned.
def city_country(city, country):
    return f"{city.title()}, {country.title()}"
print(city_country("santiago", "chile"))

# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.
def make_album(artist_name, album_title, num_songs=None):
    album = {"artist": artist_name, "title": album_title}
    if num_songs:
        album["songs"] = num_songs
    return album
album1 = make_album("Metallica", "Metallica")
album2 = make_album("Chike", "Boo of the Booless")
album3 = make_album("Bethel music", "come out of that grave", num_songs=8)
print(album1)
print(album2)
print(album3)

# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
#that’s created. Be sure to include a quit value in the while loop.
while True:
    print("\nEnter album information or 'q' to quit.")
    artist = input("Enter artist name: ")
    if artist == "q":
        break
    title = input("Enter album title: ")
    if title == "q":
        break
    num_songs = input("Enter number of songs (optional): ")
    if num_songs == "q":
        break
    if num_songs:
        album = make = make_album(artist, title, num_songs=int(num_songs))
    else:
        album = make_album(artist, title)
    print(album)

# 8-9. Messages: Make a list containing a series of short text messages. Pass the
# list to a function called show_messages(), which prints each text message.
def show_messages(messages):
    for message in messages:
        print(message)
messages = ["Hello, world", "How are you", "Goodbye!"]
show_messages(messages)

# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message and
# moves each message to a new list called sent_messages as it’s printed. After
# calling the function, print both of your lists to make sure the messages were
# moved correctly.
def send_messages(messages):
    sent_message = []
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        send_messages.append(current_message)
    return sent_message
    messages = ["hello, world!", "how are you?", "python is fun!"]
    sent_messages = send_messages(messages)
print("\nOriginal message:")
print(messages)
print("\nsent messages:")

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
# function send_messages() with a copy of the list of messages. After calling the
# function, print both of your lists to show that the original list has retained its
# messages.