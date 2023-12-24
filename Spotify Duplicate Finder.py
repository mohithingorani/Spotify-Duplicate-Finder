import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET


def get_spotify_client():
    client_id = SPOTIPY_CLIENT_ID
    client_secret = SPOTIPY_CLIENT_SECRET
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp

def get_playlist_tracks(sp, playlist_url):
    result = sp.playlist_tracks(playlist_url)
    song_list = []
    for track in result['items']:
        song_name = track['track']['name']
        song_list.append(song_name)
    return song_list

def find_duplicate_songs(lst):
    repetition_info = {}

    for i, element in enumerate(lst):
        if element in repetition_info:
            repetition_info[element]["count"] += 1
            repetition_info[element]["indexes"].append(i + 1)
        else:
            repetition_info[element] = {"count": 1, "indexes": [i + 1]}

    # Print repetitions, counts, and indexes
    flag = 0
    for element, info in repetition_info.items():
        if info["count"] > 1:
            flag = 1
            indexes_str = ', '.join(map(str, info['indexes']))
            print(f"{element} repeats {info['count']} times at places: {indexes_str}")
    if flag == 0:
        print("There are no duplicates in your playlist")

def main():
    sp = get_spotify_client()
    
    # Assuming the playlist URL is obtained from user input or elsewhere
    playlist_url = "https://open.spotify.com/playlist/4z8YaTUR2qVwuBlPoWm23z?si=562ada71bb544609"
    
    # Get playlist tracks
    song_list = get_playlist_tracks(sp, playlist_url)
    
    # Find and print duplicates
    find_duplicate_songs(song_list)

if __name__ == "__main__":
    main()
