from transformers import pipeline

def test_financial_brain():
    print("Iniciando y descargnado FinBERT (esto puede tardar unos minutos la primera vez)...")

    # Iniciamos el pipeline de analisis de sentimiento apuntando al modelo FinBERT
    sentiment_analyzer = pipeline("sentiment-analysis", model="prosusAI/finbert")

    print("Modelo cargado existosamente. \n")

    # Vamos con 3 titulares hipoteticos para ver como se comporta (uno positivo, uno negativo y uno neutral)
    test_headlines = [
        "Apple reports ground-breaking revenues for Q3, beating all Wall Street estimates.",
        "Supply chain disruptions cause Apple production delays, dropping shares by 4%.",
        "Tim Cook announces schedule for the next annual developer conference."
    ]

    for headline in test_headlines:
        print(f"Noticia:{headline}")
        #El modelo procesa el texto
        result = sentiment_analyzer(headline)[0]

        #Extraemos la etiqueta y la confianza (0 a 1)
        label = result['label']
        score = result['score']

        print(f"Veredicto IA: {label} (Confianza de {score:.2f})")
        print("-"*50)

if __name__ == "__main__":
    test_financial_brain()


