# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import calculator
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import db_conect



class Greeter(helloworld_pb2_grpc.GreeterServicer):
  def SayHello(self, request, context):
    return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)

  def SayHelloAgain(self, request, context):
    return helloworld_pb2.HelloReply(message=f"Hello again, {request.name}!")

class CalculatorServicer(helloworld_pb2_grpc.CalculatorServicer):

  # calculator.square_root is exposed here
  # the request and response are of the data type
  # calculator_pb2.Number
  def SquareRoot(self, request, context):
    response = helloworld_pb2.Number()
    response.value = calculator.square_root(request.value)
    return response

  def Pow(self, request, context):
    response = helloworld_pb2.CalcResult()
    response.Result = calculator.power_x_y(request.value1, request.value2)
    response.valueIn1 = request.value1
    response.valueIn2 = request.value2
    return response

  def Difference(self, request, context):
    response = helloworld_pb2.CalcResult()
    response.Result= calculator.diff(request.value1, request.value2)
    response.valueIn1 = request.value1
    response.valueIn2 = request.value2
    return response

  def Sum(self, request, context):
    response = helloworld_pb2.CalcResult()
    response.Result = calculator.sum_of(request.value1, request.value2)
    response.valueIn1 = request.value1
    response.valueIn2 = request.value2
    return response

  def Product(self, request, context):
    response = helloworld_pb2.CalcResult()
    response.Result = calculator.produ(request.value1, request.value2)
    response.valueIn1 = request.value1
    response.valueIn2 = request.value2
    return response

  def Quotient(self, request, context):
    response = helloworld_pb2.CalcResult()
    response.Result = calculator.quoti(request.value1, request.value2)
    response.valueIn1 = request.value1
    response.valueIn2 = request.value2
    return response

class Fibonacci(helloworld_pb2_grpc.FibonacciServicer):

  def calculate(self, index):
    a, b = 0, 1
    for _ in range(index):
      a, b = b, a + b
    return a

  def AtIndex(self, request: helloworld_pb2.NumberInt, context):
    result = self.calculate(request.value)
    return helloworld_pb2.NumberInt(value=result)

class SqlQuare(helloworld_pb2_grpc.SqlQuareServicer):
  def Select(self, request: helloworld_pb2.SqlReq, context):
    response = helloworld_pb2.SqlResp
    response.value = db_conect.select(request.quare)
    return response

def serve():
  port = "50051"
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
  helloworld_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
  helloworld_pb2_grpc.add_FibonacciServicer_to_server(Fibonacci(), server)
  helloworld_pb2_grpc.add_SqlQuareServicer_to_server(SqlQuare(), server)
  server.add_insecure_port("[::]:" + port)
  server.start()
  print("Server started, listening on " + port)
  server.wait_for_termination()


if __name__ == "__main__":
  logging.basicConfig()
  serve()
