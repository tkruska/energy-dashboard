from data_fetcher import EnergyDataFetcher
from data_processor import EnergyDataProcessor
from database import DatabaseConnector


def test_full_pipeline(country: str, date: str):
    # Setup database
    db = DatabaseConnector()
    db.create_schema()

    # Extract data from API and save to JSON
    fetcher = EnergyDataFetcher()
    json_path = fetcher.fetch_and_save(country=country, date=date)

    # Transform data from JSON
    processor = EnergyDataProcessor()
    df = processor.extract_renewable_data(json_path=json_path)

    # Load data to database
    db.insert_dataframe(df)

    # Check if number of rows match
    expected_rows = 24 * 4 * 3  # 24h * 4 readings per hour * 3 metrics
    rows_in_df = len(df)
    rows_in_db = db.count_rows()
    print(
        f"Expected: {expected_rows} | Dataframe: {rows_in_df} | Database: {rows_in_db}"
    )


if __name__ == "__main__":
    test_full_pipeline(country="de", date="2025-08-17")
