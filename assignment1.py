# DO NOT ADD LIBRARIES/PACKAGES.
# If you want to cover additional error cases other than the given below,
# feel free to create a error message.

spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile",
        "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather",
        "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things",
        "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild",
        "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Sabrina Carpenter"], "title": "Espresso",
        "length": "2:55"},
    10: {"artists": ["Lady Gaga"], "title": "Abracadabra", "length": "3:43"}
}


user_choice_question = "Enter what you would like to browse:\n \
                        \t1: A list of artists in the top 10 most played songs\n \
                        \t2: Song by ranking\n \
                        \t3: Songs by an artist\n \
                        \t4: Songs ordered by length\n \
                        \t0: Exit\n"

ranking_question = "Enter the ranking you're interested in (between 1 and 10): "
ranking_value_error = "Invalid input. Please enter a number."
ranking_range_error = "Ranking out of range."

artist_question = "Enter the name of the artist you're interested in: "
artist_error = "No songs were found by "

length_question = "Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): "
length_value_error = "Invalid value. Please enter a number."

def menu():
    """
    Continuously prompts user for menu option input
    """
    while True:
        try:
            choice = int(input(user_choice_question))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            list_artists()
        elif choice == 2:
            song_details()
        elif choice == 3:
            artist_songs()
        elif choice == 4:
            songs_by_length()
        elif choice == 0:
            break
        else:
            print("Invalid input. Please enter a number from 0-4.")
            

def list_artists():
    """
    Displays unique artists alphabetically 
    """ 
    artists = []
    for i in spotify.values():
        for j in i["artists"]:
            if j not in artists:
                artists.append(j)
    print(*sorted(artists), sep=", ")

def song_details():
    """
    Displays a song requested by user
    """
    choice = 0
    while not choice:
        try:
            choice = int(input(ranking_question))
            if choice not in spotify:
                raise IndexError
        except ValueError:
            print(ranking_value_error)
            continue
        except IndexError:
            print(ranking_range_error)
            continue
    print(f"{choice}: {spotify[choice].get("title")} by", end=" ")
    print(*spotify[choice].get("artists"), sep=", ")

def artist_songs():
    """
    Displays songs by artist requested by user; case insensitive
    """
    artist = 0
    while not artist:
        artist = input(artist_question)
    out = ""
    for k, v in spotify.items():
        for a in v["artists"]:
            if artist.lower() == a.lower():
                out += f"{k}: {spotify[k]["title"]}\n"
    if out == "":
        print(artist_error, artist, sep="")
    else:
        print(out, end="")


def main():
    menu()

if __name__ == "__main__":
    main() 