import pandas as pd
import ast
from nltk.stem.porter import PorterStemmer

class DataTransformation:

    def convert(self, text):

        L = []

        for i in ast.literal_eval(text):
            L.append(i['name'])

        return L

    def convert_cast(self, text):

        L = []
        counter = 0

        for i in ast.literal_eval(text):

            if counter != 3:
                L.append(i['name'])
                counter += 1

            else:
                break

        return L

    def fetch_director(self, text):

        L = []

        for i in ast.literal_eval(text):

            if i['job'] == 'Director':
                L.append(i['name'])
                break

        return L

    def stem(self, text):

        ps = PorterStemmer()

        y = []

        for i in text.split():
            y.append(ps.stem(i))

        return " ".join(y)

    def initiate_data_transformation(self, raw_data_path):

        movies = pd.read_csv(raw_data_path)

        movies = movies[[
            'movie_id',
            'title',
            'overview',
            'genres',
            'keywords',
            'cast',
            'crew'
        ]]

        movies.dropna(inplace=True)

        movies['genres'] = movies['genres'].apply(self.convert)

        movies['keywords'] = movies['keywords'].apply(self.convert)

        movies['cast'] = movies['cast'].apply(
            self.convert_cast
        )

        movies['crew'] = movies['crew'].apply(
            self.fetch_director
        )

        movies['overview'] = movies['overview'].apply(
            lambda x: x.split()
        )

        movies['genres'] = movies['genres'].apply(
            lambda x: [i.replace(" ", "") for i in x]
        )

        movies['keywords'] = movies['keywords'].apply(
            lambda x: [i.replace(" ", "") for i in x]
        )

        movies['cast'] = movies['cast'].apply(
            lambda x: [i.replace(" ", "") for i in x]
        )

        movies['crew'] = movies['crew'].apply(
            lambda x: [i.replace(" ", "") for i in x]
        )

        movies['tags'] = (
            movies['overview']
            + movies['genres']
            + movies['keywords']
            + movies['cast']
            + movies['crew']
        )

        new_df = movies[['movie_id', 'title', 'tags']]

        new_df['tags'] = new_df['tags'].apply(
            lambda x: " ".join(x)
        )

        new_df['tags'] = new_df['tags'].apply(
            lambda x: x.lower()
        )

        new_df['tags'] = new_df['tags'].apply(
            self.stem
        )

        return new_df