# Energy-Dashboard

Personal ETL and visualization project showcasing data pipeline development with Python, PostgreSQL, and Docker. Work in progress.

## What this project does
- Fetches energy data from an external API
- Processes and transforms the data using Python
- Stores results in a PostgreSQL database
- Demonstrates containerized ETL pipeline architecture

## Getting started

### Prerequisites
- Docker and Docker Compose
- Database viewer like [DBeaver](https://dbeaver.io/) or [pgAdmin](https://www.pgadmin.org/) (optional, to explore the data)

### Running the project
1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd energy-dashboard
   ```

2. Start the application
   ```bash
   docker compose up --build
   ```
   - This builds both containers and runs the ETL pipeline
   - Wait until the `etl_pipeline` container finishes execution
   - Check the comprehensive logs to see the pipeline progress

3. Connect to the database to view results
   - **Host:** `localhost`
   - **Port:** `5433`
   - **Database:** `energy_db`
   - **Username:** `postgres`
   - **Password:** `postgres`

4. Stop the containers
    * `ctrl+c` followed by `ctrl+d` on Windows
    * `ctrl+c` on MacOS

## Planned features
- Airflow integration for workflow orchestration
- Interactive data visualizations with Streamlit/Dash

## Data Attribution

Data provided by [Energy-Charts.info](https://energy-charts.info), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

---

From Toni Kruska with :green_heart:
