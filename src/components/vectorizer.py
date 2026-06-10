from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

class ModelTrainer:

    def initiate_model_trainer(self, new_df):

        cv = CountVectorizer(
            max_features=5000,
            stop_words='english'
        )

        vectors = cv.fit_transform(
            new_df['tags']
        ).toarray()

        similarity = cosine_similarity(vectors)

        pickle.dump(
            new_df,
            open('artifacts/movies.pkl', 'wb')
        )

        pickle.dump(
            similarity,
            open('artifacts/similarity.pkl', 'wb')
        )

        print('Artifacts Saved Successfully')