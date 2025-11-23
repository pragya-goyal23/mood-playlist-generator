print("Name: Pragya Goyal")
print("Registration no. : 25BCE10111")
# Course: Introduction to Programming & Problem Solving
# Mood-Based Playlist Generator
#Features: view moods, add moods, add songs, shuffle playlists, loading animation, tips
import random
import time
# Core data structure: dictionary storing moods and their songs
playlists = {
    "happy": ["Song A", "Song B"],
    "sad": ["Song C"],
    "relaxed": ["Song D", "Song E"]
}

# Simple loading animation for effect
def loading():
    print("Processing", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()
while True:
    print("─────────────── ⋆⋅☆⋅⋆ ───────────────")
    print("   Mood-Based Playlist Generator ")
    print("─────────────── ⋆⋅☆⋅⋆ ───────────────")
    print("  [happy 😄] [sad 😭] [relaxed 😌] ")
    print("-------------------------------------")
    print("1. View moods")
    print("2. Get playlist")
    print("3. Add mood")
    print("4. Add song to a mood")
    print("5. Exit")

    choice = input("Enter your choice: ")
    # Option 5: Exit the application
    if choice == "5":
        print("Goodbye!")
        break
    # Option 1: Display all existing moods
    if choice == "1":
        print("Available moods:")
        loading()
        for mood in playlists:
            print("-", mood)
    # Option 3: Add a new mood to the playlist dictionary
    elif choice == "3":
        new_mood=input("Enter mood name: ")
        if new_mood in playlists:
            print("New mood already exists")
        else:
            loading()
            playlists[new_mood]=[]
            print(f"Mood '{new_mood}' added")
    # Option 4: Add a song to an existing mood
    elif choice == "4":
        mood=input("Enter mood to add song to: ")
        if mood not in playlists:
            print("Mood does not exist")
        else:
            song=input("Enter song name: ")
            playlists[mood].append(song)
            loading()
            print(f"Added '{song}' to '{mood}'")
    # Option 2: Fetch and shuffle playlist for a given mood
    elif choice == "2":
        mood=input("Enter mood to get playlist: ")
        if mood not in playlists:
            print("Mood does not exist")
        else:
            loading()
            random.shuffle(playlists[mood])
            print(f"Playlist for {mood}: ")
            i=1
            for song in playlists[mood]:
                print(str(i) + ". " + song)
                i += 1
# End of program