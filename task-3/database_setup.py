import psycopg2
import csv

def create_tables():
    # Establish connection to PostgreSQL database
    conn = psycopg2.connect(
        dbname="news_correlation_10ac_week0",
        user="Blen",
        password="123blen",
        host="localhost"
    )

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # SQL commands to create tables
    create_data_table = """
    CREATE TABLE IF NOT EXISTS data (
        article_id INT PRIMARY KEY,
        source_id VARCHAR(255),
        source_name VARCHAR(255),
        author VARCHAR(255),
        title TEXT,
        description TEXT,
        url TEXT,
        url_to_image TEXT,
        published_at TIMESTAMP,
        content TEXT,
        category VARCHAR(255),
        full_content TEXT
    )
    """

    create_domains_location_table = """
    CREATE TABLE IF NOT EXISTS domains_location (
        SourceCommonName VARCHAR(255) PRIMARY KEY,
        location VARCHAR(255),
        Country VARCHAR(255)
    )
    """

    create_rating_table = """
    CREATE TABLE IF NOT EXISTS rating (
        article_id INT PRIMARY KEY,
        rating INT
    )
    """

    create_traffic_table = """
    CREATE TABLE IF NOT EXISTS traffic (
        GlobalRank INT,
        TldRank INT,
        Domain VARCHAR(255) PRIMARY KEY,
        TLD VARCHAR(255),
        RefSubNets INT,
        RefIPs INT,
        IDN_Domain VARCHAR(255),
        IDN_TLD VARCHAR(255),
        PrevGlobalRank INT,
        PrevTldRank INT,
        PrevRefSubNets INT,
        PrevRefIPs INT
    )
    """

    # Execute SQL commands to create tables
    cur.execute(create_data_table)
    cur.execute(create_domains_location_table)
    cur.execute(create_rating_table)
    cur.execute(create_traffic_table)

    # Commit the transaction
    conn.commit()

    # Close cursor and connection
    cur.close()
    conn.close()

def load_data():
    # Establish connection to PostgreSQL database
    conn = psycopg2.connect(
        dbname="news_correlation_10ac_week0",
        user="Blen",
        password="123blen",
        host="localhost"
    )

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Load data from CSV files into respective tables
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            cur.execute(
                "INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                row
            )

    with open('domains_location.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            cur.execute(
                "INSERT INTO domains_location VALUES (%s, %s, %s)",
                row
            )

    with open('rating.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            cur.execute(
                "INSERT INTO rating VALUES (%s, %s)",
                row
            )

    with open('traffic.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            cur.execute(
                "INSERT INTO traffic VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                row
            )

    # Commit the transaction
    conn.commit()

    # Close cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()
    load_data()
