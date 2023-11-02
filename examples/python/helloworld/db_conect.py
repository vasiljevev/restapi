import pyodbc

SERVER = 'dev-db-v-08'
DATABASE = 'OmniUS_API'
DRIVER = 'SQL Server'


connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)

def select(self, request):
    conn = pyodbc.connect(connectionString)
    cursor = conn.cursor() # создаем курсор
    cursor.fast_executemany = True  # активируем быстрое выполнение

    # создаём заготовку для создания таблицы (начало)
    #query = "SELECT top 1 C_Name  FROM dbo.SD_divisions"
    cursor.execute(request)  # execute
    #cursor.execute("SELECT top 1 C_Name  FROM dbo.SD_divisions")
    row = cursor.fetchone()
    #print(row)
    return row
    conn.close()