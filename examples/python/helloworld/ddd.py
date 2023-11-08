import sqlite3
import grpc

from concurrent import futures
from sqlite_pb2 import *
from sqlite_pb2_grpc import SQLiteServiceServicer, add_SQLiteServiceServicer_to_server


class SQLiteServiceImplementation(SQLiteServiceServicer):
    def Insert(self, request, context):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            columns = ', '.join(request.data.keys())
            values = ', '.join(['"{}"'.format(value) for value in request.data.values()])
            cursor.execute('INSERT INTO {} ({}) VALUES ({});'.format(request.table_name, columns, values))
            conn.commit()
            conn.close()
            return InsertResponse(success=True, message='Data inserted successfully.')
        except Exception as e:
            return InsertResponse(success=False, message=str(e))

    def Update(self, request, context):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            set_clause = ', '.join(['{} = "{}"'.format(key, value) for key, value in request.data.items()])
            cursor.execute('UPDATE {} SET {} WHERE {};'.format(request.table_name, set_clause, request.where_clause))
            conn.commit()
            conn.close()
            return UpdateResponse(success=True, message='Data updated successfully.')
        except Exception as e:
            return UpdateResponse(success=False, message=str(e))

    def Delete(self, request, context):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM {} WHERE {};'.format(request.table_name, request.where_clause))
            conn.commit()
            conn.close()
            return DeleteResponse(success=True, message='Data deleted successfully.')
        except Exception as e:
            return DeleteResponse(success=False, message=str(e))

    def Get(self, request, context):
        try:
            conn = sqlite3.connect('test.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM {} WHERE {};'.format(request.table_name, request.where_clause))
            data = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
            conn.close()
            return GetResponse(data=data)
        except Exception as e:
            return GetResponse(data=[], message=str(e))


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SQLiteServiceServicer_to_server(SQLiteServiceImplementation(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
