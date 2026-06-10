import pickle

movies = pickle.load(
    open('artifacts/movies.pkl', 'rb')
)

similarity = pickle.load(
    open('artifacts/similarity.pkl', 'rb')
)


class PredictPipeline:

    def recommend(self, movie):

        movie_index = movies[
            movies['title'] == movie
        ].index[0]

        distances = similarity[movie_index]

        movies_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        recommended_movies = []

        for i in movies_list:

            recommended_movies.append(
                movies.iloc[i[0]].title
            )

        return recommended_movies