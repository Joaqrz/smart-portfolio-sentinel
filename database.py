import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

def get_db_engine():
    """
    Retrieves the database connection URL from Streamlit secrets
    and creates a SQLAlchemy engine.   
    """

    try:
        db_url = st.secrets["connections"]["postgresql"]["url"]
        engine = create_engine(db_url)
        return engine
    except KeyError:
        st.error("Database credentials not found in secrets.toml")
        return None
    
def get_historical_prices(ticker: str) -> pd.DataFrame:
    """
    Fetches stored price data for a specific asset ticker.
    Returns a Pandas dataframe with date as index.
    """

    engine = get_db_engine()
    if engine is None:
        return pd.DataFrame()
    
    # Sql query to fetch historic data (assumes a standard historical table structure)
    query = """
        SELECT 
        created_at,
        closing_price,
        news_title,
        sentiment_label,
        sentiment_score,
        analysis_date
        FROM daily_market_insights
        WHERE ticker = %(ticker)s
        ORDER BY created_at DESC
        LIMIT 30;
    """

    try:
        # Utilizing pandas to execute query and convert directly to dataframe
        df = pd.read_sql(query, con=engine, params={"ticker":ticker.upper()})
        if not df.empty:
            df['analysis_date'] = pd.to_datetime(df['analysis_date'])
            df.set_index('analysis_date', inplace=True, drop=False)
        return df
    except Exception as e:
        st.error(f"Error querying historical data: {e}")
        return pd.DataFrame()

