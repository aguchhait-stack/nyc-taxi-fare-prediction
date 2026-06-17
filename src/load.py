import pandas as pd
from sqlalchemy import create_engine,text

engine = create_engine('postgresql://postgres@localhost:5432/nyc_taxi_fare_prediction')

def ingest_bronze():
    try:

        with engine.connect() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS bronze"))
            conn.execute(text("DROP TABLE IF EXISTS bronze.taxi_trips"))
            conn.commit()
        years_months = [("2026","04"),("2026","03")]
        for year,month in years_months:

            print(f"Fetching {year}-{month} data")
            base_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month}.parquet"

            df = pd.read_parquet(base_url)
            df = df.sample(100000,random_state=42)
                
            df.to_sql(name="taxi_trips",if_exists= "append",schema="bronze",
                      index=False,chunksize=10000,method="multi",con=engine)

            print(f"Loaded {year}-{month} data to database")

    except Exception as e:
        print(f"Ingesting error: {e}")

if __name__ == "__main__":
    ingest_bronze()
