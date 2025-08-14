import json
import pandas as pd
from datetime import datetime
from pathlib import Path


class EnergyDataProcessor:
    def __init__(self):
        self.list_of_metric_types = [
            "Renewable share of load",
            "Renewable share of generation",
            "Load",
        ]
        pass

    def extract_renewable_data(self, json_path: dict) -> pd.DataFrame:
        with open(json_path, "r") as f:
            json_data = json.load(f)

        list_of_dicts = []

        for prod_type in json_data["production_types"]:
            if prod_type["name"] in self.list_of_metric_types:
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

        return result_df


if __name__ == "__main__":
    json_path = Path("data/de_2025-08-01.json")
    processor = EnergyDataProcessor()
    res = processor.extract_renewable_data(json_path=json_path)
    print(res)
