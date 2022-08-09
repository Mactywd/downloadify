from youtube_search import YoutubeSearch
from classes import VideoResult, SpotifyResult


def search(spotify_result: SpotifyResult, idx, total):
    print("Searching for song: " + spotify_result.title, f'  {idx+1}/{total}')

    results = YoutubeSearch(
        f'{spotify_result.author} {spotify_result.title}', max_results=10).to_dict()
    video_results = [VideoResult(result) for result in results]
    compared = [spotify_result.compare(result) for result in video_results]

    best = compared.index(max(compared))

    suffix = video_results[best].suffix

    return 'https://www.youtube.com' + suffix


if __name__ == '__main__':
    example = SpotifyResult({
        "track": {
            "name": "The crystal ship",
            "artists": [{"name": "Doors"}],
            "duration_ms": 250000
        }})
    url = search(example, 0, 1)
    print(url)
