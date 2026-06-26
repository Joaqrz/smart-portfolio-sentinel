import yfinance as yf

def fetch_lates_news(ticker_symbol):
    print(f"Buscando noticias para: {ticker_symbol}...\n")
    ticker = yf.Ticker(ticker_symbol)

    # yfinance devuelve una lista de diccionarios con las noticias
    news_data = ticker.news

    if not news_data:
        print("No se encontraron noticias recientes.")
        return


    #Imprimir las 3 noticias más recientes
    for i, article in enumerate(news_data[:3],1):
        print(f"Noticia {i}:")
        print(f"📰 Título: {article.get('title')}")
        print(f"🏢 Medio: {article.get('publisher')}")
        #A veces yfinance no trae un resumen largo, pero trae el link
        print(f"🔗 Link: {article.get('link')}")
        print("-"*60)


fetch_lates_news("AAPL")  # Ejemplo de uso con el ticker de Apple