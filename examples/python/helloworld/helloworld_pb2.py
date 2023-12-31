# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\")\n\x07Number2\x12\x0e\n\x06value1\x18\x01 \x01(\x02\x12\x0e\n\x06value2\x18\x02 \x01(\x02\"@\n\nCalcResult\x12\x10\n\x08valueIn1\x18\x01 \x01(\x02\x12\x10\n\x08valueIn2\x18\x02 \x01(\x02\x12\x0e\n\x06Result\x18\x03 \x01(\x02\"\x1a\n\tNumberInt\x12\r\n\x05value\x18\x01 \x01(\x05\"\x19\n\x06SqlReq\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1a\n\x07SqlResp\x12\x0f\n\x07message\x18\x01 \x01(\t2\xdb\x01\n\x07Greeter\x12>\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12K\n\x13SayHelloStreamReply\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x30\x01\x12\x43\n\rSayHelloAgain\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x32\xe2\x02\n\nCalculator\x12\x36\n\nSquareRoot\x12\x12.helloworld.Number\x1a\x12.helloworld.Number\"\x00\x12\x34\n\x03Pow\x12\x13.helloworld.Number2\x1a\x16.helloworld.CalcResult\"\x00\x12\x34\n\x03Sum\x12\x13.helloworld.Number2\x1a\x16.helloworld.CalcResult\"\x00\x12;\n\nDifference\x12\x13.helloworld.Number2\x1a\x16.helloworld.CalcResult\"\x00\x12\x38\n\x07Product\x12\x13.helloworld.Number2\x1a\x16.helloworld.CalcResult\"\x00\x12\x39\n\x08Quotient\x12\x13.helloworld.Number2\x1a\x16.helloworld.CalcResult\"\x00\x32\x86\x02\n\tFibonacci\x12\x37\n\x07\x41tIndex\x12\x15.helloworld.NumberInt\x1a\x15.helloworld.NumberInt\x12=\n\x0bGetSequence\x12\x15.helloworld.NumberInt\x1a\x15.helloworld.NumberInt0\x01\x12=\n\x0bSumIndicies\x12\x15.helloworld.NumberInt\x1a\x15.helloworld.NumberInt(\x01\x12\x42\n\x0eStreamSequence\x12\x15.helloworld.NumberInt\x1a\x15.helloworld.NumberInt(\x01\x30\x01\x32?\n\x08SqlQuare\x12\x33\n\x06Select\x12\x12.helloworld.SqlReq\x1a\x13.helloworld.SqlResp\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _globals['_HELLOREQUEST']._serialized_start=32
  _globals['_HELLOREQUEST']._serialized_end=60
  _globals['_HELLOREPLY']._serialized_start=62
  _globals['_HELLOREPLY']._serialized_end=91
  _globals['_NUMBER']._serialized_start=93
  _globals['_NUMBER']._serialized_end=116
  _globals['_NUMBER2']._serialized_start=118
  _globals['_NUMBER2']._serialized_end=159
  _globals['_CALCRESULT']._serialized_start=161
  _globals['_CALCRESULT']._serialized_end=225
  _globals['_NUMBERINT']._serialized_start=227
  _globals['_NUMBERINT']._serialized_end=253
  _globals['_SQLREQ']._serialized_start=255
  _globals['_SQLREQ']._serialized_end=280
  _globals['_SQLRESP']._serialized_start=282
  _globals['_SQLRESP']._serialized_end=308
  _globals['_GREETER']._serialized_start=311
  _globals['_GREETER']._serialized_end=530
  _globals['_CALCULATOR']._serialized_start=533
  _globals['_CALCULATOR']._serialized_end=887
  _globals['_FIBONACCI']._serialized_start=890
  _globals['_FIBONACCI']._serialized_end=1152
  _globals['_SQLQUARE']._serialized_start=1154
  _globals['_SQLQUARE']._serialized_end=1217
# @@protoc_insertion_point(module_scope)
