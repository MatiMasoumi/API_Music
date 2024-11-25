Using the iTunes Search API,
create an object-oriented Python application to interact with it.
: Allow the user to search for music by entering the name of the song.
Display the search results in a clear and user-friendly format, including
details such as track name, artist name, album name, and a link to listen to the track on iTunes.
The iTunes Search APl is open and does not require authentication or API tokens for basic functionality. 
url = f"https://itunes.apple.com/search?term={track_name}&media=music"
