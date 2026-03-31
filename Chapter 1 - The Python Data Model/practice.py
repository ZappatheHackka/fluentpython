# ------ Implementing dunder methods in a custom PLaylist class ------
songs = [

    {"The Basement": {"length": '3:50',
                         "artist": "Lunar Vacation"}},

    {"Trans Balkan Express": {"length": '5:13',
                                 "artist": "OMFO"}},

    {"Judas": {"length": '4:47',
                  "artist": "Lady Gaga"}},

    {"Ma'a Ibnat": {"length": '6:21',
                       "artist": "Ouiness"}},

    {"Why Does it Hurt When I Pee?": {"length": '5:16',
                                        "artist": "Frank Zappa"}},

    {"Infohazard": {"length": '3:19',
                       "artist": "Ninajirachi"}},

    {"Pulsewidth": {"length": '3:50',
                "artist": "Aphex Twin"}},

    {"Aizo": {"length": '4:50',
                 "artist": "King Gnu"}}
    ]

class Playlist:

    def __init__(self):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, index):
        return self.songs[index]

    def __repr__(self):
        return f"Playlist({self.songs})"

    def __str__(self):
        string = ""
        for song in self.songs:
            for title, info in song.items():
                str = f"{title} - {info["artist"]} : {info["length"]}"
                string += f"\n{str}"
        return string

playlist = Playlist()
print(playlist)
print(f"Our playlist is {len(playlist)} songs long.")
print("Now we will loop through the playlist, only printing every other track: ")

for index, song in enumerate(playlist):
    if index % 2 == 0:
        for key in song.keys():
            print(key)

print(f"The last song in our playlist is....{playlist[-1]}")


# sequence ops like random.choice(), or index-based element selection don't work on dictionaries.
# hence why playlist[-1] doesn't return the last song, nor does random.choice do anything
# until we wrap our dictionary into a list of mini dictionaries.