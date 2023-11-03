import pyodbc

SERVER = 'dev-db-v-08'
DATABASE = 'OmniUS_API'
DRIVER = 'SQL Server'


connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)

#request="SELECT top 10 link FROM dbo.ED_Meter_Readings order by link asc"

def select(request):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor() # создаем курсор
    cursor.fast_executemany = True  # активируем быстрое выполнение
    cursor.execute(request)  # execute
    row = cursor.fetchone()
    for r in row:
        print(r)
    #print(row)
    conn.close()
    return row

#select(request)