import yfinance as yf

def fetch_test_data():
    print("Conectando con el mercado...")
    ticker_name = "AAPL"  # AAPL es el simbolo o "sticker" de Apple Inc. en la bolsa.
    apple = yf.Ticker(ticker_name)

    # Intentamos obtener el historial y capturamos errores.
    try:
        hist = apple.history(period="5d")
    
        if hist.empty:
            print(f"Advertencia: No se encontraron datos para {ticker_name}.")
        else:
            print(f"/n--- ultimos 5 dias de {ticker_name} ---")
            print(hist[['Close', 'Volume']])
    except Exception as e:
        print(f"Error al conectar con la api: {e}")
if __name__ == "__main__":
    fetch_test_data()