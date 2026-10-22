# ⚽ Football Data ETL Pipeline

Una pipeline **ETL (Extract, Transform, Load)** end-to-end sviluppata in Python per estrarre i dati delle partite di Serie A tramite API REST, pulirli e strutturarli con Pandas, e infine caricarli all'interno di un database relazionale PostgreSQL.

---

## 🚀 Panoramica del Progetto
Questo progetto automatizza il flusso di gestione dei dati calcistici. L'obiettivo è raccogliere le informazioni aggiornate sulle partite della Serie A, effettuare una fase di data cleaning per gestire i risultati e lo stato dei match, e persistere i dati puliti in un database strutturato per successive analisi o query SQL.

---

## 🛠️ Tecnologie e Strumenti Utilizzati
* **Linguaggio:** Python
* **Estrazione Dati:** `requests` (per le chiamate HTTP all'API REST di Football-Data.org)
* **Manipolazione & Pulizia Dati:** `pandas`
* **Connessione & ORM Database:** `SQLAlchemy`, `psycopg2-binary`
* **Database:** PostgreSQL
* **Controllo Versione:** Git / GitHub

---

## ⚙️ Architettura della Pipeline (ETL)

La pipeline è suddivisa in moduli indipendenti richiamati dal file di orchestrazione principale (`main.py`):

1. **Extract (`scripts/extract.py`):**
   * Effettua una richiesta HTTP GET autenticata (tramite API Key nei headers) all'endpoint ufficiale di *football-data.org* per la competizione della Serie A (`SA`).
   * Estrae il payload JSON grezzo contenente l'elenco completo dei match.

2. **Transform (`scripts/transform.py`):**
   * Riceve i dati grezzi e li converte in un DataFrame Pandas.
   * Filtra e pulisce i campi relativi ai punteggi (`home_score` e `away_score`).
   * Calcola dinamicamente il vincitore della partita (`homeTeam`, `awayTeam` o `DRAW` in caso di pareggio, `PENDING` per le partite non ancora giocate).
   * Seleziona e formatta le colonne chiave (`match_id`, `home_team`, `away_team`, `home_score`, `away_score`, `winner`, `match_date`, `status`).

3. **Load (`scripts/load.py`):**
   * Utilizza SQLAlchemy per stabilire una connessione sicura con l'istanza locale di PostgreSQL.
   * Scrive automaticamente il DataFrame pulito all'interno della tabella `matches` del database, gestendo l'append dei record.

---

## 📂 Struttura del Progetto
```text
football-data-etl/
├── scripts/
│   ├── extract.py      # Modulo per le chiamate API REST
│   ├── transform.py    # Modulo di pulizia e trasformazione dati con Pandas
│   └── load.py         # Modulo di caricamento su PostgreSQL via SQLAlchemy
├── main.py             # Script principale (Orchestratore della pipeline)
├── requirements.txt    # Dipendenze del progetto
└── README.md           # Documentazione del progetto
