import os
import requests
from dotenv import load_dotenv
from transformers import pipeline

# 1. Cargar Variables de entorno 
load_dotenv()

# 2. Inicializar FinBERT
print("Cargando el motor de FinBERT...")
sentiment_analyzer = pipeline("sentiment-analysis", model="ProsusAI/finbert")
print("Motor listo. \n")

def analyze_market_sentiment(ticker):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        print(f"Error: Falta la NEWS_API_KEY")
        return
    
    #Búsqueda estructurada
    query = f"({ticker}) AND (stock OR market OR shares OR earnings)"
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&pageSize=5&apiKey={api_key}"

    print(f"Buscando las ultimas 5 noticias financieras para {ticker}...")
    response = requests.get(url)

    if response.status_code == 200:
        articles = response.json().get('articles',[])

        if not articles:
            print("No hay noticias recientes para analizar.")
            return
        
        # 3. Procesar cada noticia con IA
        print("\n--- INICIANDO ANALISIS DE SENTIMIENTO ---")
        for i, article in enumerate(articles, 1):
            title = article.get('title')
            #A veces la desc. puede venir vacia, usemos el título si es así.
            text_to_analyze = article.get('description') or title

            #Pasamos el texto al modelo 
            result  = sentiment_analyzer(text_to_analyze)[0]
            label = result['label']
            score = result['score']

            print(f"\nNoticia {i}: {title}")
            print(f"Veredicto IA: {label.upper()} (Confianza: {score:.2f})")

        print("\n-----------------------------------------")

    else:
        print(f"Error con NewsAPI: {response.status_code}")

#Probamos el pipeline completo con Apple
if __name__ == "__main__":
    analyze_market_sentiment("AAPL")