import numpy as np
import pandas as pd
from surprise import SVD
from Dataset import RecommendationsDataset, MoviesDataset
from collections import defaultdict
from operator import itemgetter
import math
import heapq


def get_example_moviescore():
    return pd.DataFrame([
        ('m1', 3.0), ('m4', 4.0), ('m3', 2.0)
    ], columns=['movieId', 'rating']).set_index('movieId')


def get_recommendation(filename):
    import pickle
    return pickle.load(open(filename, "rb"))


class Rekomendacje:
    def __init__(self):
        self.algorithm = SVD()
        self.movies = MoviesDataset()

    def test(self, test_set):
        return self.algorithm.test(test_set)

    def fit(self, dataset):
        return self.algorithm.fit(dataset)

    def evaluate(self, test_size=.25):
        from surprise.model_selection import cross_validate, train_test_split
        from surprise import accuracy

        recommendation_dataset = RecommendationsDataset()
        cross_validate(self.algorithm, recommendation_dataset.dataset, measures=['RMSE', 'MSE'], cv=5, verbose=True);

        train, test = train_test_split(recommendation_dataset.dataset)
        # train.ur
        # train.ir
        # test
        self.fit(train)
        test_predictions = self.test(test)
        # result
        print("MAE: ", accuracy.mae(test_predictions, verbose=0))
        print("RMSE: ", accuracy.rmse(test_predictions, verbose=0))

    def get_similar_user_ids(self, watched, k=20):
        full_dataset = self.algorithm.trainset
        u_sqrt = math.sqrt(sum([i*i for i in watched.values()]))

        # https://en.wikipedia.org/wiki/Cosine_similarity
        cosine_similarity = defaultdict(lambda: (0, 0))
        for index,rating in watched.items():
            for user_id, user_rating in full_dataset.ir[index]:
                cosine_similarity[user_id] = (cosine_similarity[user_id][0] + rating*user_rating,
                                              cosine_similarity[user_id][1] + user_rating*user_rating)

        similarity = {index: val[0]/(u_sqrt*math.sqrt(val[1])) for index, val in cosine_similarity.items()}

        # from scipy.spatial.distance import cosine
        # import math
        # full_dataset.ur
        # u = [3.0,4.0,2.0], watched [4,2,3]
        # v = [0.0,5.0,2.5]; cosine(u,v)
        # v = [3.0,0.0,0.0];  cosine(u,v)
        # u = [1.0, 0.1]; v = [2.0, 0.1]; cosine(u,v)
        # cosine([5,6333,7],[1,2,3]) = 0.46
        # cosine([1,2,3],[1,2,3]) = 0.0

        return dict(heapq.nsmallest(k, similarity.items(), key=itemgetter(0)))


    def get_recommendation(self, watched: dict, k=10):
        full_dataset = self.algorithm.trainset

        # watched
        watched = {full_dataset.to_inner_iid(index): value
                   for index, value in watched.items()}

        similar_users = self.get_similar_user_ids(watched, k=10)
        # get similar users
        # Calculate for all similar user, predictions
        candidates = defaultdict(float)
        for inner_move_id in range(0, full_dataset.n_items):
            if inner_move_id not in watched:
                movie_id = full_dataset.to_raw_iid(inner_move_id)

                for inner_user_id, similarity in similar_users.items():
                    prediction = self.algorithm.predict(
                        full_dataset.to_raw_uid(inner_user_id),
                        movie_id)
                    candidates[movie_id] += similarity * prediction.est

        movie_ids = heapq.nlargest(k, candidates, key=candidates.get)
        movies = self.movies.get_movies_by_ids(movie_ids)
        return movies

    def save(self):
        import pickle
        with open(type(self).__name__ + ".pkl", "wb") as fw:
            pickle.dump(self, fw)


if __name__ == "__main__":
    """
    %load_ext autoreload
    %autoreload 2
    """
    from Rekomendacje import Rekomendacje, get_example_moviescore, get_recommendation
    from Dataset import RecommendationsDataset

    rekomendacje = Rekomendacje()
    rekomendacje.evaluate()

    recommendation_dataset = RecommendationsDataset()
    rekomendacje.fit(recommendation_dataset.full_dataset)
    # rekomendacje.algorithm.trainset.ir
    # rekomendacje.algorithm.predict('u1','m1',5.0)
    # rekomendacje.algorithm.test([('u0','m3', 4.0)])

    watched = get_example_moviescore()['rating'].to_dict()
    # watched
    # self = rekomendacje
    rekomendacje.get_recommendation(watched, k=10)

    rekomendacje.save()
    rekomendacje_load = get_recommendation('Rekomendacje.pkl')

    #
    # rekomendacje_load.algorithm.predict('u1','m1',5.0)
    # rekomendacje_load.algorithm.test([('u0','m3', 4.0)])

    # rekomendacje.algorithm.predict('u1','m1',5.0)
    # rekomendacje.algorithm.test([('u0','m3', 4.0)])