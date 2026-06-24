import yfinance as yf
from sqlalchemy import create_engine
import os 
from dotenv import load_dotenv 

# Cargamos las variables del .env
load_dotenv()

# Construimos la url de conexión a la base de datos
# Asegúrate de escribir 'postgresql+psycopg2'
db_url = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/{os.getenv('POSTGRES_DB')}"
def save_data():
    engine = create_engine(db_url)
    ticker = yf.Ticker("AAPL")
    hist = ticker.history(period="5d")

    # Esto guarda el dataframe directamente en una tabla llamada "stock_prices"
    hist.to_sql("stock_prices", engine, if_exists="append")
    print("Datos guardados existosamente en la base de datos.")

if __name__ == "__main__":
    save_data()