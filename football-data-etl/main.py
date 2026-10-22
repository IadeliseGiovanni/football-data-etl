import os
from scripts.extract import fetch_serie_a_matches
from scripts.transform import transform_matches
from scripts.load import load_to_postgres

def run_pipeline():
    print("🚀 Avvio della pipeline ETL di Football Data...")
    
    # 1. Inserisci qui la tua API Key gratuita di football-data.org
    API_TOKEN = "f7ac561eedfd47ba9b34b496eb95f334"
    
    if API_TOKEN == " INSERISCI_LA_TUA_API_KEY_QUI":
        print("⚠️ Attenzione: ricordati di inserire la tua API key valida nel file main.py!")
        return

    # 2. Stringa di connessione a PostgreSQL 
    # (Modifica 'postgres', 'tuapassword' e 'football_db' con i tuoi dati reali)
    DB_CONNECTION_STR = "postgresql+psycopg2://postgres:root@localhost:5432/football_db"

    try:
        # STEP 1: EXTRACT
        print("📥 Estrazione dei dati in corso dall'API...")
        raw_data = fetch_serie_a_matches(API_TOKEN)
        print(f"-> Estratte {len(raw_data)} partite grezze.")

        # STEP 2: TRANSFORM
        print("🧹 Trasformazione e pulizia dei dati con Pandas...")
        df_cleaned = transform_matches(raw_data)
        print(f"-> Dati puliti pronti. Totale record validi: {len(df_cleaned)}")

        # STEP 3: LOAD
        print("💾 Caricamento dei dati all'interno del database PostgreSQL...")
        load_to_postgres(df_cleaned, DB_CONNECTION_STR)
        
        print("✅ Pipeline completata con successo!")

    except Exception as e:
        print(f"❌ Errore durante l'esecuzione della pipeline: {e}")

if __name__ == "__main__":
    run_pipeline()