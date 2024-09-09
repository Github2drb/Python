import pyodbc
server = '192.168.4.218'
database = '2324237'
username = 'sa'
password = '1234'
def fetch_data(server, database, username, password):
    # Establish connection
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )

    # Create a cursor object using the connection
    cursor = conn.cursor()

    # Query to count occurrences of each modelno
    query = '''
    select smodel,count(*) from [2324237].[dbo].[Laser_Data_Log]
    
    GROUP BY smodel
    '''

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    conn.close()

    return rows
    



# Fetch data from SQL Server
data = fetch_data(server, database, username, password)
print(data)
