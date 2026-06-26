import os
import requests
import yfinance as yf
import psycopg2
from datetime import date
from dotenv import load_dotenv
from transformers import pipeline

# 1. Cargar config.

load_dotenv()

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname = os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT")
        )
        return conn
    except Exception as e: 
        print(f"Error conectando a la base de datos: {e}")
        return None

def fetch_closing_price(ticker):
    print(f"Obteniendo precio de cierre para {ticker}...")
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    if not todays_data.empty:
        return float(todays_data['Close'].iloc[0])
    return None

def analyze_and_save_insight(ticker, price):
    api_key = os.getenv("NEWS_API_KEY")
    query = f"({ticker}) AND (stock OR market OR shares OR earnings)"
    url  = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&pageSize=1&apiKey={api_key}"

    print("Buscando la noticia financiera más relevante...")
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if not articles:
            print("No hay noticias para guardar.")
            return
        
        article = articles[0]
        title = article.get('title')
        text_to_analyze = article.get('description') or title

        print("Analizando sentimiento con FinBERT...")
        sentiment_analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")
        result = sentiment_analyzer(text_to_analyze)[0]

        label = result['label']
        score = result['score']

        print(f"Resultado: {label} ({score:.2}) | {title}")

        #Guardar en la db
        save_to_database(ticker, price, title, label, score)
    else:
        print("Error al consultar NewsAPI")

def save_to_database(ticker, price, news_title, sentiment_label, sentiment_score):
    print("Guardando datos en PostgreSQL...")
    conn = get_db_connection()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        insert_query = """
            INSERT INTO  daily_market_insights
            (ticker, analysis_date, closing_price, news_title, sentiment_label, sentiment_score)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        today = date.today()
        record_to_insert = (ticker, today, price, news_title, sentiment_label, sentiment_score)

        cursor.execute(insert_query, record_to_insert)
        conn.commit()
        print("¡Registro guardado exitosamente en la base de datos!")

    except Exception as e:
        print(f"Error al guardar en la DB: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
if __name__ == "__main__":
    target_ticker = "AAPL"
    #Ejecutamos el pipeline secuencial
    current_price = fetch_closing_price(target_ticker)

    if current_price:
        analyze_and_save_insight(target_ticker,current_price)
    else:
        print("No se pudo obtener el precio de mercado. Proceso abortado catastroficamente. Bobo.")

