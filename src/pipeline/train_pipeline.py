from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.vectorizer import ModelTrainer


if __name__ == "__main__":

    ingestion = DataIngestion()

    raw_data_path = (
        ingestion.initiate_data_ingestion()
    )

    transformation = DataTransformation()

    transformed_df = (
        transformation.initiate_data_transformation(
            raw_data_path
        )
    )

    trainer = ModelTrainer()

    trainer.initiate_model_trainer(
        transformed_df
    )