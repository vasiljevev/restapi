import pyodbc

SERVER = 'dev-db-v-08'
DATABASE = 'OmniUS_API'
DRIVER = 'SQL Server'


connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)

def select(uu):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor()
    cursor.execute(uu)
    #cursor.execute("SELECT top 1 C_Name  FROM dbo.SD_divisions")
    #while 1:
    row = cursor.fetchone()
    #    if not row:
    #        break
    return row
    conn.close()