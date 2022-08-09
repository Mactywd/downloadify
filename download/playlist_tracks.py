import json
from spoti import spotify

def get_playlist_tracks(playlist_id):
    print("Playlist: " + spotify.playlist(playlist_id)["name"])
    print("Getting playlist titles...")
    results = spotify.playlist_items(playlist_id, limit=100, market='IT')
    tracks = results["items"]
    while results['next']:
        results = spotify.next(results)
        tracks.extend(results["items"])
    print("Done")
    return tracks

if __name__ == '__main__':
    playlist_id = 'https://open.spotify.com/playlist/5PDhc5zYCiF6ut8inAChmn?si=d9ece151346142a9'.split('/')[-1].split('?')[0]
    
    results = get_playlist_tracks(playlist_id)

    with open('results.json', 'w') as f:
        f.write(json.dumps(results))