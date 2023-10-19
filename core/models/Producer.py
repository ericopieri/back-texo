from django.db import models


class Producer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def get_orderned_win_intervals(self):
        producer_winner_movies = self.movies.filter(winner=True).order_by("year")

        if producer_winner_movies.count() < 2:
            return list()

        win_intervals = []
        for i in range(producer_winner_movies.count() - 1):
            win_intervals.append(
                {
                    "followingWin": producer_winner_movies[i].year,
                    "previousWin": producer_winner_movies[i + 1].year,
                    "interval": producer_winner_movies[i + 1].year
                    - producer_winner_movies[i].year,
                }
            )

        return sorted(win_intervals, key=lambda x: x["interval"])

    def calc_max_win_interval(self):
        ordened_win_intervals = self.get_orderned_win_intervals()

        if len(ordened_win_intervals) == 0:
            return {
                "followingWin": None,
                "previousWin": None,
                "interval": None,
            }

        return ordened_win_intervals[-1]

    def calc_min_win_interval(self):
        ordened_win_intervals = self.get_orderned_win_intervals()

        if len(ordened_win_intervals) == 0:
            return {
                "followingWin": None,
                "previousWin": None,
                "interval": None,
            }

        return ordened_win_intervals[0]

    def __str__(self):
        return self.name
