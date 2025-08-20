import pandas as pd
import psycopg
import os
from contextlib import contextmanager
from logging_config import setup_logger
from dotenv import load_dotenv
from sqlalchemy import create_engine

logger = setup_logger(__name__)
load_dotenv()


class DatabaseConnector:
    def __init__(
        self,
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "energy_db"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    ):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    @contextmanager
    def get_connection(self):
        try:
            conn = psycopg.connect(
                f"host={self.host} dbname={self.database} user={self.user} password={self.password}"
            )
            logger.debug(f"Connected to database {self.database}.")
            yield conn
        except psycopg.Error as e:
            logger.error(f"Database connection failed: {e}")
            raise
        finally:
            conn.close()
            logger.debug(f"Connection to {self.database} has been closed.")

    def insert_dataframe(self, data: pd.DataFrame):
        connection_string = f"postgresql+psycopg://{self.user}:{self.password}@{self.host}/{self.database}"
        engine = create_engine(connection_string)
        try:
            data.to_sql(
                "metrics", con=engine, schema="energy", if_exists="append", index=False
            )
            logger.info("Dataframe has been inserted successfully.")
        except Exception as e:
            logger.error(f"Failed to insert dataframe: {e}")
            raise

    def query(self):
        pass

    def count_rows(self):
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM energy.metrics")
            return cursor.fetchone()[0]

    def create_schema(self):
        try:
            with open("schema.sql", "r") as f:
                schema_sql = f.read()
        except FileNotFoundError:
            logger.error("Schema file 'schema.sql' was not found.")
            return None

        with self.get_connection() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute(schema_sql)
                conn.commit()
                logger.info("Database schema created successfully.")
            except psycopg.Error as e:
                logger.error(f"Failed to create schema: {e}")
                raise


if __name__ == "__main__":
    pass
