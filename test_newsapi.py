import requests
import os 
from dotenv import load_dotenv

load_dotenv()

def fetch_financial_news(company_query):
    api_key = os.getenv("NEWS_API_KEY")  # Asegúrate de tener tu API key en el archivo .env

    if not api_key:
        print("No se encontró la API key. Por favor, configura tu NEWS_API_KEY en el archivo .env.")
        return
    
    #Agregamos un contexto financiero a la búsqueda para filtrar noticias relevantes
    financial_context = "AND (stock OR market OR earnings OR shares OR revenue)"
    full_query = f"{company_query} {financial_context}"


    # Buscamos noticias ordenadas por las más recientes
    url = f"https://newsapi.org/v2/everything?q={full_query}&sortBy=publishedAt&language=en&apiKey={api_key}"
    print(f"Buscando noticias para: {company_query}...\n")
    response = requests.get(url)

    # Verificamos si la solicitud fue exitosa (cod 200)
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        if not articles:
            print("No se encontraron noticias.")
            return
        
        # Imprimir las 3 noticias más recientes
        for i, article in enumerate(articles[:3], 1):
            print(f"Noticia {i}:")
            print(f"📰 Título: {article.get('title')}")
            print(f"🏢 Medio: {article.get('source', {}).get('name')}")
            print(f"🔗 Link: {article.get('url')}")
            print("-"*60)
    else:
        print(f"Error al conectar con la API: {response.status_code}")

fetch_financial_news("(AAPL OR\"Apple Inc\")")  # Ejemplo de uso con la palabra clave "Apple"