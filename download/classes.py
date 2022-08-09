import re

class VideoResult:
    def __init__(self, result):
        self.title = result["title"].lower()
        self.author = result["channel"]
        self.length = self._extract_length(result["duration"])
        self.views = self._extract_views(result["views"])
        self.suffix = result["url_suffix"]
        self.score = 0

    def _extract_length(self, length):
        if length is None or length == 0:
            return 0

        parts = length.split(':')
        in_seconds = int(parts[-1])
        if len(parts) > 1:
            if parts[-2]:
                in_seconds += int(parts[-2]) * 60

            if len(parts) > 2:
                in_seconds += int(parts[-3]) * 3600
        return in_seconds

    def _extract_views(self, views):
        if views == 0:
            return 0

        _views = views.split(' ')[0]
        views = ''.join(_views.split('.'))

        return int(views)


class SpotifyResult:
    def __init__(self, track):
        self.title = track["track"]["name"].lower()
        self.author = track["track"]["artists"][0]["name"]
        self.alt_title = f'{self.author} {self.title}'
        self.length = track["track"]["duration_ms"] // 1000

    def _get_list_from_title(self, title):
        to_return = re.sub(r'\W+', ' ', title)
        return to_return.split()

    def _get_similarity(self, original, other, simplified=False):
        original = self._get_list_from_title(original)
        other = self._get_list_from_title(other)

        common_words = len(list(set(original).intersection(other)))
        max_score = len(original) * 10
        if simplified:
            score = (common_words * 10) / max_score
        else:
            unique_words = len(other) - common_words
            score = ((common_words * 10) - (unique_words * 4)) / max_score

        return score

    def compare(self, yt_result: VideoResult):

        scores = {
            "title": {
                "score": max(self._get_similarity(self.title, yt_result.title),
                            self._get_similarity(self.alt_title, yt_result.title)),
                "weight": 5
            },
            "author": {
                "score": max(self._get_similarity(self.author, yt_result.author),
                            self._get_similarity(self.author, yt_result.title, True)),
                "weight": 2
            },
            "duration": {
                "score": 1 - abs(self.length - yt_result.length) / 60,
                "weight": 5
            }
        }

        title_score = scores["title"]["score"] * scores["title"]["weight"]
        author_score = scores["author"]["score"] * scores["author"]["weight"]
        duration_score = scores["duration"]["score"] * scores["duration"]["weight"]

        final_score = (title_score + author_score + duration_score) / 3

        return final_score

if __name__ == '__main__':
    pass