import pandas as pd
import psycopg2

# Function to establish a connection to the PostgreSQL database
def connect_to_database():
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='blen123',
            port='5432'
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

# Function to load feature data from CSV files
def load_feature_data():
    # Load feature data from CSV files or other sources
    feature_data = pd.read_csv('feature_data.csv')  # Example: Replace 'feature_data.csv' with your file path
    return feature_data

# Function to insert feature data into the database
def insert_feature_data(conn, feature_data):
    try:
        cursor = conn.cursor()

        # Iterate through the DataFrame rows and insert data into the database
        for index, row in feature_data.iterrows():
            # Example: Insert data into 'feature_data' table in the public schema
            cursor.execute("""
                INSERT INTO public.feature_data (feature_id, timestamp, value)
                VALUES (%s, %s, %s)
            """, (row['feature_id'], row['timestamp'], row['value']))
        
        conn.commit()
        print("Feature data inserted successfully.")
    except psycopg2.Error as e:
        print("Error inserting feature data:", e)
    finally:
        cursor.close()

def main():
    # Connect to the PostgreSQL database
    conn = connect_to_database()
    if conn is None:
        return

    # Load feature data
    feature_data = load_feature_data()

    # Insert feature data into the database
    insert_feature_data(conn, feature_data)

    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
