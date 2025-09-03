from data_fetcher import EnergyDataFetcher
from data_processor import EnergyDataProcessor
from database import DatabaseConnector
from config import DEFAULT_COUNTRIES
from logging_config import setup_logger

logger = setup_logger(__name__)


def test_full_pipeline(countries: list, date: str):
    fetcher = EnergyDataFetcher()
    processor = EnergyDataProcessor()
    db = DatabaseConnector()

    # Setup database
    db.create_schema()

    for country in countries:
        try:
            # Extract data from API and save to JSON
            json_path = fetcher.fetch_and_save(country=country, date=date)
            # Transform data from JSON
            df = processor.extract_renewable_data(json_path=json_path)
            # Load data to database
            db.insert_dataframe(df)
            logger.info(f"Successfully processed --{country.upper()}--")
        except Exception as e:
            logger.error(f"Failed to process {country}: {e}")
            continue

    logger.info(
        "Pipeline has finished. Connect to the database to see the stored records."
    )


if __name__ == "__main__":
    countries = DEFAULT_COUNTRIES
    test_full_pipeline(countries=countries, date="2025-08-17")
