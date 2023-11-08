import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
#conn = sqlite3.connect('tutorial.db')

#SERVER = 'dev-db-v-08'
#DATABASE = 'OmniUS_API'
#DRIVER = 'SQL Server'


#connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes'
#conn = sqlite3.connect(connectionString)

query_movie = "SELECT name FROM sqlite_master"
#(query_movie)
#print(type(query_movie))

def select(query):
    with sqlite3.connect("C:/Users/e-vasilyev/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db") as conn:
        #print(query)
        #print(type(query))
        cursor = conn.cursor()
        res = cursor.execute(query)
        return res.fetchone()

#print(select(query_movie))

#select(request)