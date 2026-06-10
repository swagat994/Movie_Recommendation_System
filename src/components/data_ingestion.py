import pandas as pd
import os

class DataIngestion:

    def initiate_data_ingestion(self):

        movies = pd.read_csv(
            'notebook/data/movies.csv'
        )

        credits = pd.read_csv(
            'notebook/data/credits.csv'
        )

        movies = movies.merge(credits, on='title')

        os.makedirs('artifacts', exist_ok=True)

        movies.to_csv(
            'artifacts/raw_data.csv',
            index=False
        )

        return 'artifacts/raw_data.csv'