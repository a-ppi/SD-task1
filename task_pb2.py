# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='task.proto',
  package='task',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ntask.proto\x12\x04task\"\"\n\x04Task\x12\x0c\n\x04task\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\t\"\x1e\n\x0cTaskResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2A\n\x08SendTask\x12\x35\n\x11GetServerResponse\x12\n.task.Task\x1a\x12.task.TaskResponse\"\x00\x62\x06proto3'
)




_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='task.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='task.Task.task', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file', full_name='task.Task.file', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=54,
)


_TASKRESPONSE = _descriptor.Descriptor(
  name='TaskResponse',
  full_name='task.TaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='task.TaskResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['TaskResponse'] = _TASKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.Task)
  })
_sym_db.RegisterMessage(Task)

TaskResponse = _reflection.GeneratedProtocolMessageType('TaskResponse', (_message.Message,), {
  'DESCRIPTOR' : _TASKRESPONSE,
  '__module__' : 'task_pb2'
  # @@protoc_insertion_point(class_scope:task.TaskResponse)
  })
_sym_db.RegisterMessage(TaskResponse)



_SENDTASK = _descriptor.ServiceDescriptor(
  name='SendTask',
  full_name='task.SendTask',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=88,
  serialized_end=153,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='task.SendTask.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_TASK,
    output_type=_TASKRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENDTASK)

DESCRIPTOR.services_by_name['SendTask'] = _SENDTASK

# @@protoc_insertion_point(module_scope)
