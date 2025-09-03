# Energy-Dashboard

Personal ETL and visualization project. Work in progress.

## Getting started
You will need docker and ideally a database viewer like DBeaver or pgAdmin (to look at the created records for yourself)
1. clone the repo
2. `cp .env.example .env` (try skipping that step at first)
3. `docker compose up --build`
    * wait until you see the container `etl_pipeline` has finished operation (you can also go through the comprehensive logs it provides)
4. in your database viewer, connect to the database using the credentials found in `.env`
5. after all has been done, stop the running containers using (using `ctrl+c` followed by `ctrl+d` on windows)

![Here should be a gif of tumbleweed](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXA0NGo0ODAxODM3Z2toMXlsem1rYzAxOWFuYzJuYTV5ZmQ2b2ticSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d8lUKXD00IXSw/giphy.gif)

## Planned features
- Adding Airflow integration
- Adding interactive data visualizations

## Data Attribution

Data provided by [Energy-Charts.info](https://energy-charts.info), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

---

From Toni Kruska with :green_heart:
