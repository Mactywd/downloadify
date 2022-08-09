from playlist_tracks import get_playlist_tracks
from downloader import download
from search import search
from classes import SpotifyResult



def run(uri):
    tracks = get_playlist_tracks(uri)
    youtube_urls = [[search(SpotifyResult(track), idx, len(tracks)), idx] for idx, track in enumerate(tracks) if idx > offset]
    for url, idx in youtube_urls:
        download(url, idx, youtube_urls[-1][1]+1, tracks[idx]["track"]["name"])

if __name__ == '__main__':
    uri = '37i9dQZF1E396jDEMSseVb'
    #uri = input('Insert playlist uri: ')
    offset = -1
    run(uri)