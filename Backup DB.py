import configparser
import pyodbc
import pandas as pd
from datetime import datetime
import os

# Read configuration from master.ini
def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return {
        'server': config.get('database', 'server'),
        'database': config.get('database', 'database'),
        'username': config.get('database', 'username'),
        'password': config.get('database', 'password')
    }

# Connect to the MSSQL database
def connect_to_database(config):
    conn_str = (
        f"DRIVER={{ODBC Driver 13 for SQL Server}};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"UID={config['username']};"
        f"PWD={config['password']};"
    )
    conn = pyodbc.connect(conn_str)
    return conn

# Fetch data from the database
def fetch_data(conn):
    query = "SELECT * FROM DBO.Box_Label_Log"  # Replace with your query
    df = pd.read_sql(query, conn)
    #conn.disconnect
    return df

# Convert DataFrame to XML
def convert_to_xml(df):
    xml_data = df.to_xml(root_name='Data', row_name='Record', index=False)
    return xml_data

# Archive the database (simplified example)
def archive_database(conn, database_name):
    cursor = conn.cursor()
    
    # Commit any ongoing transaction
    conn.commit()
    
    # Backup file name
    backup_file = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.bak"
    
    # Backup query
    backup_query = f"""
    BACKUP DATABASE [{database_name}] 
    TO DISK = '{backup_file}' 
    WITH INIT;
    """
    print(backup_query)
    # Execute backup query
    #cursor.execute(backup_query)
    
    # Commit the backup operation
    conn.commit()
    
    cursor.close()
    return backup_file


# Main function to execute the tasks
def main():
    config_file = 'D:\\Python\\master.ini'
    config = read_config(config_file)
    
    conn = connect_to_database(config)
    
    # Archive the database
    backup_file = archive_database(conn, config['database'])
    print(f"Database archived to {backup_file}")
    
    # Fetch and convert data
    df = fetch_data(conn)
    xml_data = convert_to_xml(df)
    
    # Save XML data to a file
    xml_file = 'data.xml'
    with open(xml_file, 'w') as file:
        file.write(xml_data)
    print(f"Data exported to {xml_file}")
    
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
