import pyodbc
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Function to connect to SQL Server and execute query
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
    select modelno,count(*) from dbo.OP40_FINAL_VIEWING_STATION
    where cast(dts_scan as date)=cast(getdate()-2 as date)
    GROUP BY modelno
    '''

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    conn.close()

    return rows

# Function to create pie chart
def create_pie_chart(data, window_position=None, save_to_file=None):
    labels = [row[0] for row in data]
    counts = [row[1] for row in data]
    total = sum(counts)
    
    fig = plt.figure(figsize=(8, 6), dpi=100)
    
    # Configure subplot layout
    gs = gridspec.GridSpec(2, 2, figure=fig)
    gs.update(top=1.300, bottom=0.035, left=0, right=0.836, hspace=0.000, wspace=0.000)
    
    # Title above pie chart
    ax_title = fig.add_subplot(gs[0, 0])
    ax_title.axis('off')
    ax_title.text(0.0, 0.3, f'Model\nTotal: {total}', ha='left', va='top', fontsize=10)
    
    # Pie chart subplot
    ax_pie = fig.add_subplot(gs[1, 0])
    wedges, texts, autotexts = ax_pie.pie(counts, autopct='%1.1f%%', startangle=90, pctdistance=0.75)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    #ax_pie.axis('equal')
    
    # Legend subplot
    ax_pie.legend(
    labels, 
    loc='best',  # 'best' automatically places the legend in the best location
    bbox_to_anchor=(1.05, 1.39),  # Position the legend outside the plot area
    fontsize=6, 
    title="Categories", 
    title_fontsize='6', 
    shadow=True
    )
    
    plt.setp(autotexts, size=7, weight="bold")

    if window_position:
        mng = plt.get_current_fig_manager()
        mng.window.setGeometry(*window_position)

    if save_to_file:
        plt.savefig(save_to_file, bbox_inches='tight')
       # plt.close()
    else:
        plt.show(block=True)
        #plt.pause(3)
        #plt.close()

# Replace with your SQL Server connection details
server = '192.168.18.146'
database = 'DB_LINE8'
username = 'sa'
password = '1234'

# Fetch data from SQL Server
data = fetch_data(server, database, username, password)

# Create pie chart
create_pie_chart(data,window_position=(1000, 100, 300, 200)) 
create_pie_chart(data, save_to_file='piechart.png')
