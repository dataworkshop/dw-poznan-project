import pandas as pd
from surprise import Reader, Dataset

class MoviesDataset:
    def __init__(self, file='movies.csv'):
        self.movies_df = pd.read_csv(file, index_col='movieId')

    def get_movies_by_ids(self, ids):
        return self.movies_df.loc[ids]


class RecommendationsDataset:
    def __init__(self, file='ratings.csv', columns=['userId', 'movieId', 'rating']):
        self.ratings_df = pd.read_csv(file)[columns]
        self.columns = columns
        reader = Reader(rating_scale=(1, 5))
        self.dataset = Dataset.load_from_df(self.ratings_df, reader)
        self.full_dataset = self.dataset.build_full_trainset()


if __name__ == '__main__':
    movies = MoviesDataset()
    movies.get_movies_by_ids(['m1','m5'])

    recommendations_ds = RecommendationsDataset()
    recommendations_ds.full_dataset.ur
    recommendations_ds.full_dataset.ir

    recommendations_ds.full_dataset.to_inner_uid('u4')
    recommendations_ds.full_dataset.to_inner_uid('u7')  # ValueError
    recommendations_ds.full_dataset.to_inner_iid('m7')
    recommendations_ds.full_dataset.to_inner_iid('m123')  # ValueError
