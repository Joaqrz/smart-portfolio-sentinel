# Smart Portfolio Sentinel

## GitHub Repository Info

**Repository Name:** `smart-portfolio-sentinel`

**Description:**
> AI-driven portfolio monitor using NLP for real-time sentiment analysis, correlating market data for early alerts. Built security-first with Python, Docker, and Streamlit. Note: Personal project developed in my free time; updates are a continuous work in progress.

---

## Architecture and Workflow

The project is designed under a Security-First philosophy, integrating hardening practices and secrets management from the initial data collection.

### Global Technology Stack
* **Primary Language:** Python 3.10+
* **Containers:** Docker & Docker Compose
* **Version Control:** Git & GitHub

---

## Stage 1: Infrastructure, Data, and Core Security (Data & Security)

This stage establishes the foundations of the project. It collects financial data and ensures the entire environment is hardened from day one.

### Objectives and Functions:
1. **Secrets Management:** Configuration of `.env` and `.gitignore` files to protect API keys (Market, AI, Bots).
2. **Container Security:** Configuration of Dockerfiles to run processes under a non-root user.
3. **Network Isolation:** Creation of an internal virtual network in Docker (Private Network) so that the database does not expose any ports to the internet.
4. **Data Orchestration:** Python script that downloads daily asset prices.
5. **News Ingestion:** Web scraping or consuming RSS feeds/APIs from key financial sources.

### Technology Stack:
* **Orchestration and Security:** Docker, Docker Compose, `python-dotenv`.
* **Financial Market:** Yahoo Finance API (`yfinance`) or Alpha Vantage.
* **News Ingestion:** `BeautifulSoup` / `Scrapy` (for scraping) or Bloomberg/Reuters/Reddit APIs.
* **Database:** PostgreSQL (Relational) or ChromaDB (Vectorial to optimize AI embeddings).

---

## Stage 2: The Analytical Brain (AI Engine)

Processing raw information to extract market sentiment and generate explanatory summaries of asset movements.

### Objectives and Functions:
1. **Sentiment Analysis:** Classification of the impact of each collected financial news item into three categories: Bullish (Positive), Bearish (Negative), or Neutral.
2. **Executive Summaries:** Generation of 3 bullet points explaining why an asset is receiving negative coverage.

### Technology Stack:
* **Large Language Models (LLMs):** Gemini API or Hugging Face.
* **Local Financial Models:** FinBERT (Specialized in NLP for financial texts, ideal for cost control).
* **Processing:** `transformers` library (Hugging Face) in Python.

---

## Stage 3: Interface and Early Warning System (Frontend & Comms)

Visualizing metrics for the user and configuring communication channels for critical alerts.

### Objectives and Functions:
1. **Access Protection:** Implementation of an authentication login system in the dashboard to prevent unauthorized access and abusive API consumption.
2. **Metrics Dashboard:** Visual interface simulating the stock portfolio.
3. **Visual Correlation:** Graphs overlaying news sentiment versus stock price.
4. **Alert System:** Automatic notification dispatch if the overall sentiment of an asset falls below a critical threshold.

### Technology Stack:
* **Frontend / Dashboard:** Streamlit or Dash.
* **Authentication:** `streamlit-authenticator` (or equivalent for Dash).
* **Data Visualization:** Plotly or Matplotlib.
* **Notification Bots:** Telegram API (`python-telegram-bot`) or Discord API.

---

## Stage 4: Optimization and Deployment (Deployment & Monetization Prep)

Refining the project to ensure low operating costs and maximum scalability, preparing it to be a commercial product (SaaS or Micro-SaaS) and an excellent portfolio piece.

### Objectives and Functions:
1. **Cost Control:** Fine-tuning the use of FinBERT or other small models on economical servers to keep the cost per user down to cents.
2. **Cloud Deployment:** Uploading Dockerized containers to a Cloud provider while maintaining private network rules.
3. **Professional Exposure:** Final documentation on GitHub and preparing a video demonstration for LinkedIn.

### Technology Stack:
* **Cloud Hosting:** AWS (EC2), Google Cloud, DigitalOcean, or Render.
* **CI/CD (Opcional):** GitHub Actions for automated deployment.
