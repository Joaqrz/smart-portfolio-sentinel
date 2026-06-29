import streamlit as st
import pandas as pd
from database import get_historical_prices

# Placeholder imports from your custom modules
# from database import get_historical_prices, get_latest_news
# from ai module import get_sentiment_analysis

def main():
    # Page config
    st.set_page_config(
        page_title="Smart Portfolio Sentinel",
        layout="wide"
    )

    # Main Header
    st.title("Smart Portfolio Sentinel")
    st.subheader("AI Driven Financial Market Analysis Dashboard")

    #Sidebar for user interaction
    st.sidebar.header("Dashboard Controls")
    asset_ticker = st.sidebar.text_input("Enter Asset Ticker (e.g, AAPL, BTC-USD)", value="AAPL")
    analyze_button = st.sidebar.button("Run Analysis")

    if analyze_button:
        st.markdown("---")
        st.write(f"Executing data pipeline for: **{asset_ticker}**")

        #Create a two column layout
        col1, col2 = st.columns(2)

        with col1:
            st.header("Market Data")

            #Feth data from local database
            with st.spinner("Fetching data from local storage..."):
                df_prices = get_historical_prices(asset_ticker)
            if not df_prices.empty:
                st.write(f"Displaying historical records for {asset_ticker}")
                # Render a native streamlit interactive line chart 
                st.line_chart(df_prices['closing_price'])
                # Show raw data block expandable section
                with st.expander("View Raw Data"):
                    st.dataframe(df_prices)
            else:
                st.warning(f"No price records found for ticker '{asset_ticker}' in the local database. Ensure the data pipeline ingestion has run successfully.")


        with col2:
            # Inside the 'with col2:' block in your app.py

            st.header("AI Sentiment Intelligence")

            # Assuming df_data is your fetched dataframe and it is sorted by newest first
            if not df_prices.empty:
                latest_record = df_prices.iloc[0]
                
                # Display high-level sentiment metrics
                st.metric(
                    label="Latest Sentiment Score", 
                    value=str(latest_record['sentiment_score']), 
                    delta=latest_record['sentiment_label']
                )
                
                # Display the underlying news catalyst
                st.subheader("Market Catalyst")
                st.write(f"**Headline:** {latest_record['news_title']}")
                
                # Use an expander to keep the UI clean while offering deep dives
                with st.expander("Read Full AI Analysis"):
                    st.write(latest_record['analysis_date'])
                    st.write(f"**Processed Headline:** {latest_record['news_title']}")
                # Show historical sentiment trend
                st.subheader("Sentiment Trend")
                
                # Streamlit requires the date as the index for time-series charts
                df_trend = df_prices.copy()
                df_trend.set_index('created_at', inplace=True)
                st.bar_chart(df_trend['sentiment_score'])
            else:
                st.info("Awaiting sentiment data for this asset.")
if __name__ == "__main__":
    main()