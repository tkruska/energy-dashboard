import requests
import json
from pathlib import Path


class EnergyDataFetcher:
    def __init__(self, base_url="https://api.energy-charts.info/"):
        self.base_url = base_url
        self.dir = Path("./data")
        self.dir.mkdir(exist_ok=True)

    def fetch_daily_data(self, country: str, date: str) -> dict:
        url = f"{self.base_url}public_power"
        params = {"country": country, "start": date, "end": date}
        try:
            response = requests.get(url, params=params)
        except Exception as e:
            print(f"Network error: {e}")
            return None

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"API request failed with status code: {response.status_code}"
            )

    def save_raw_data(self, country: str, date: str, json_data: dict) -> Path:
        filepath = Path(self.dir / f"{country}_{date}.json")

        with open(filepath, "w") as f:
            json.dump(json_data, f)
        return filepath

    def fetch_and_save(self, country: str, date: str):
        response = self.fetch_daily_data(country=country, date=date)
        filepath = self.save_raw_data(country=country, date=date, json_data=response)
        print(f"Data saved successfully in {filepath}")


if __name__ == "__main__":
    fetcher = EnergyDataFetcher()
    fetcher.fetch_and_save("de", "2025-08-01")
