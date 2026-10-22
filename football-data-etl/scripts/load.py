from sqlalchemy import create_engine
import pandas as pd

def load_to_postgres(df: pd.DataFrame, db_connection_str: str):
    engine = create_engine(db_connection_str)
    df.to_sql('matches', con=engine, if_exists='append', index=False)
    print(f"Caricate con successo {len(df)} partite su PostgreSQL!")