import streamlit as st
import mysql.connector
import pandas as pd
import time

# Function to fetch data from MySQL
def fetch_data(query):
    try:
        # Connect to the MySQL database on Hostinger
        connection = mysql.connector.connect(
           host='srv1020.hstgr.io',
            user='u830421930_sensordatabas',
            password='12sensData',
            database='u830421930_sensor_databas'
        )

        # Create a DataFrame from the query results
        df = pd.read_sql(query, connection)
        return df
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return pd.DataFrame()
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()

# Streamlit application
def main():
    st.title('Live Data Visualization')

    # Input for SQL query
    query = "SELECT * FROM sensordata ORDER BY id DESC "
    interval = 5

    #query = st.text_area("Enter your SQL query", "SELECT * FROM sensordata ORDER BY id DESC ")

    # Interval for data updates
    #interval = st.sidebar.slider("Update Interval (seconds)", 5, 60, 10)

    # Create a placeholder for the chart
    chart_placeholder = st.empty()

    while True:
        if query.strip():
            data = fetch_data(query)
            if not data.empty:
                # Update the chart with new data
                with chart_placeholder.container():
                    st.write("Data updated!")
                    st.header("Temprature")
                    if 'reading_time' in data.columns and 'sensor' in data.columns:
                        # Line Chart
                        st.subheader("Line Chart")
                        st.line_chart(data[['reading_time', 'sensor']].set_index('reading_time'))
                        
                        # Bar Chart
                        st.subheader("Bar Chart")
                        st.bar_chart(data[['reading_time', 'sensor']].set_index('reading_time'))
                    else:
                        st.warning("Data does not contain required columns for charting.")
                    st.header("Humdity")
                    if 'reading_time' in data.columns and 'location' in data.columns:
                        # Line Chart
                        st.subheader("Line Chart")
                        st.line_chart(data[['reading_time', 'location']].set_index('reading_time'))
                        
                        # Bar Chart
                        st.subheader("Bar Chart")
                        st.bar_chart(data[['reading_time', 'location']].set_index('reading_time'))
                    else:
                        st.warning("Data does not contain required columns for charting.")
                    st.header("Ethylene Level")
                    if 'reading_time' in data.columns and 'distance' in data.columns:
                        # Line Chart
                        st.subheader("Line Chart")
                        st.line_chart(data[['reading_time', 'distance']].set_index('reading_time'))
                        
                        # Bar Chart
                        st.subheader("Bar Chart")
                        st.bar_chart(data[['reading_time', 'distance']].set_index('reading_time'))
                    else:
                        st.warning("Data does not contain required columns for charting.")
            else:
                st.write("No data found or error in query.")
        
        # Sleep for the specified interval
        time.sleep(interval)
    
if __name__ == "__main__":
    main()
