'''import csv, os

with open("100MostStreamedSongs.csv") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        dir = os.listdir()
        artist = row["Artist(s)"].title()
        print(artist)
        if artist not in dir:
            os.mkdir(artist)
        song = row["Song"]
        print(row["Song"])
        path = os.path.join(f"{artist}/", song)
        f = open(path, "w")
        f.close()
        '''

import csv
import os

# Get the list of existing directories once
existing_directories = os.listdir()

with open("100MostStreamedSongs.csv") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        artist = row["Artist(s)"].title()
        print(artist)
        
        if artist not in existing_directories:
            os.mkdir(artist)
        
        song = row["Song"]
        print(song)
        
        path = os.path.join(artist, song)
        
        # Using 'with' statement for file operations
        with open(path, "w") as f:
            pass  # You can do further operations inside this block if needed
