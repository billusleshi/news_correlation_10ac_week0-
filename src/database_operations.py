import psycopg2

host = 'localhost'  # Server
database = 'postgres'  # Database
port = '5432'  # Port
user = 'postgres'  # Username
password = 'blen123'  # Password for user postgres

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host=host,
    database=database,
    port=port,
    user=user,
    password=password,  # Corrected variable name
)

# Open and read SQL script
with open('your_script.sql', 'r') as file:
    sql_script = file.read()

# Execute SQL script
with conn.cursor() as cursor:
    cursor.execute(sql_script)

# Commit changes and close connection
conn.commit()
conn.close()
