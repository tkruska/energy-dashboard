import json
import pandas as pd
from datetime import datetime
from pathlib import Path
from logging_config import setup_logger

logger = setup_logger(__name__)


class EnergyDataProcessor:
    def __init__(self):
        self.list_of_metric_types = [
            "Renewable share of load",
            "Renewable share of generation",
            "Load",
        ]
        pass

    def extract_renewable_data(self, json_path: dict) -> pd.DataFrame:
        try:
            with open(json_path, "r") as f:
                json_data = json.load(f)
        except FileNotFoundError:
            error_msg = f"The file {json_path} could not be found."
            logger.error(error_msg)
            return None

        list_of_dicts = []
        list_of_returned_metrics = []

        for prod_type in json_data["production_types"]:
            if prod_type["name"] in self.list_of_metric_types:
                list_of_returned_metrics.append(prod_type["name"])
                for i, val in enumerate(prod_type["data"]):
                    list_of_dicts.append(
                        {
                            "timestamp": datetime.fromtimestamp(
                                json_data["unix_seconds"][i]
                            ),
                            "metric_type": prod_type["name"],
                            "value": val,
                        }
                    )

        result_df = pd.DataFrame(list_of_dicts)
        for metric in self.list_of_metric_types:
            if metric not in list_of_returned_metrics:
                logger.warning(f"Metric {metric} is missing in the API response.")
        logger.info("Dataframe has been successfully created.")
        return result_df


if __name__ == "__main__":
    json_path = Path("data/de_2025-08-07.json")
    processor = EnergyDataProcessor()
    res = processor.extract_renewable_data(json_path=json_path)
