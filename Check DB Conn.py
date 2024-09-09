import pyodbc
import configparser


def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return {
        'server': config.get('database', 'server'),
        'database': config.get('database', 'database'),
        'username': config.get('database', 'username'),
        'password': config.get('database', 'password')
    }
 
def test_connection(config):
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"UID={config['username']};"
        f"PWD={config['password']};"
    )
    try:
        conn = pyodbc.connect(conn_str)
        print("Connection successful!")
        conn.close()
    except Exception as e:
        print("Connection failed:", e)
config_file = 'D:\\Exe\\Python\\master.ini'
config = read_config(config_file)
test_connection(config)
