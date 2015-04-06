# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bnet/protocol/game_utilities.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import attribute_pb2 as bnet_dot_protocol_dot_attribute__pb2
from .. import protocol_0_pb2 as bnet_dot_protocol__0__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bnet/protocol/game_utilities.proto',
  package='bnet.protocol.game_utilities',
  syntax='proto2',
  serialized_pb=_b('\n\"bnet/protocol/game_utilities.proto\x12\x1c\x62net.protocol.game_utilities\x1a\x1d\x62net/protocol/attribute.proto\x1a\x15\x62net/protocol_0.proto\"G\n\x0e\x43lientResponse\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"G\n\x0eServerResponse\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"\x83\x01\n\x0fPlayerVariables\x12)\n\x08identity\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.Identity\x12\x0e\n\x06rating\x18\x02 \x01(\x01\x12\x35\n\tattribute\x18\x03 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\"e\n\x1aGetPlayerVariablesResponse\x12G\n\x10player_variables\x18\x01 \x03(\x0b\x32-.bnet.protocol.game_utilities.PlayerVariables\"\xd2\x01\n\rClientRequest\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12&\n\x04host\x18\x02 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\x12\x30\n\x0f\x62net_account_id\x18\x03 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x30\n\x0fgame_account_id\x18\x04 \x01(\x0b\x32\x17.bnet.protocol.EntityId\"z\n\x1eGameAccountOfflineNotification\x12\x30\n\x0fgame_account_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12&\n\x04host\x18\x02 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\"y\n\x1dGameAccountOnlineNotification\x12\x30\n\x0fgame_account_id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12&\n\x04host\x18\x02 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\"\x8c\x01\n\x19GetPlayerVariablesRequest\x12G\n\x10player_variables\x18\x01 \x03(\x0b\x32-.bnet.protocol.game_utilities.PlayerVariables\x12&\n\x04host\x18\x02 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\"\xd0\x01\n\x1dPresenceChannelCreatedRequest\x12#\n\x02id\x18\x01 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x30\n\x0fgame_account_id\x18\x03 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12\x30\n\x0f\x62net_account_id\x18\x04 \x01(\x0b\x32\x17.bnet.protocol.EntityId\x12&\n\x04host\x18\x05 \x01(\x0b\x32\x18.bnet.protocol.ProcessId\"\x7f\n\rServerRequest\x12\x35\n\tattribute\x18\x01 \x03(\x0b\x32\".bnet.protocol.attribute.Attribute\x12\x0f\n\x07program\x18\x02 \x01(\x07\x12&\n\x04host\x18\x03 \x01(\x0b\x32\x18.bnet.protocol.ProcessId')
  ,
  dependencies=[bnet_dot_protocol_dot_attribute__pb2.DESCRIPTOR,bnet_dot_protocol__0__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CLIENTRESPONSE = _descriptor.Descriptor(
  name='ClientResponse',
  full_name='bnet.protocol.game_utilities.ClientResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.ClientResponse.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=193,
)


_SERVERRESPONSE = _descriptor.Descriptor(
  name='ServerResponse',
  full_name='bnet.protocol.game_utilities.ServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.ServerResponse.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=195,
  serialized_end=266,
)


_PLAYERVARIABLES = _descriptor.Descriptor(
  name='PlayerVariables',
  full_name='bnet.protocol.game_utilities.PlayerVariables',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='bnet.protocol.game_utilities.PlayerVariables.identity', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rating', full_name='bnet.protocol.game_utilities.PlayerVariables.rating', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.PlayerVariables.attribute', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=400,
)


_GETPLAYERVARIABLESRESPONSE = _descriptor.Descriptor(
  name='GetPlayerVariablesResponse',
  full_name='bnet.protocol.game_utilities.GetPlayerVariablesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_variables', full_name='bnet.protocol.game_utilities.GetPlayerVariablesResponse.player_variables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=402,
  serialized_end=503,
)


_CLIENTREQUEST = _descriptor.Descriptor(
  name='ClientRequest',
  full_name='bnet.protocol.game_utilities.ClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.ClientRequest.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.ClientRequest.host', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bnet_account_id', full_name='bnet.protocol.game_utilities.ClientRequest.bnet_account_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.game_utilities.ClientRequest.game_account_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=716,
)


_GAMEACCOUNTOFFLINENOTIFICATION = _descriptor.Descriptor(
  name='GameAccountOfflineNotification',
  full_name='bnet.protocol.game_utilities.GameAccountOfflineNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.game_utilities.GameAccountOfflineNotification.game_account_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.GameAccountOfflineNotification.host', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=718,
  serialized_end=840,
)


_GAMEACCOUNTONLINENOTIFICATION = _descriptor.Descriptor(
  name='GameAccountOnlineNotification',
  full_name='bnet.protocol.game_utilities.GameAccountOnlineNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.game_utilities.GameAccountOnlineNotification.game_account_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.GameAccountOnlineNotification.host', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=963,
)


_GETPLAYERVARIABLESREQUEST = _descriptor.Descriptor(
  name='GetPlayerVariablesRequest',
  full_name='bnet.protocol.game_utilities.GetPlayerVariablesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_variables', full_name='bnet.protocol.game_utilities.GetPlayerVariablesRequest.player_variables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.GetPlayerVariablesRequest.host', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=966,
  serialized_end=1106,
)


_PRESENCECHANNELCREATEDREQUEST = _descriptor.Descriptor(
  name='PresenceChannelCreatedRequest',
  full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='game_account_id', full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest.game_account_id', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bnet_account_id', full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest.bnet_account_id', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.PresenceChannelCreatedRequest.host', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1109,
  serialized_end=1317,
)


_SERVERREQUEST = _descriptor.Descriptor(
  name='ServerRequest',
  full_name='bnet.protocol.game_utilities.ServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attribute', full_name='bnet.protocol.game_utilities.ServerRequest.attribute', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='program', full_name='bnet.protocol.game_utilities.ServerRequest.program', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='bnet.protocol.game_utilities.ServerRequest.host', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1319,
  serialized_end=1446,
)

_CLIENTRESPONSE.fields_by_name['attribute'].message_type = bnet_dot_protocol_dot_attribute__pb2._ATTRIBUTE
_SERVERRESPONSE.fields_by_name['attribute'].message_type = bnet_dot_protocol_dot_attribute__pb2._ATTRIBUTE
_PLAYERVARIABLES.fields_by_name['identity'].message_type = bnet_dot_protocol__0__pb2._IDENTITY
_PLAYERVARIABLES.fields_by_name['attribute'].message_type = bnet_dot_protocol_dot_attribute__pb2._ATTRIBUTE
_GETPLAYERVARIABLESRESPONSE.fields_by_name['player_variables'].message_type = _PLAYERVARIABLES
_CLIENTREQUEST.fields_by_name['attribute'].message_type = bnet_dot_protocol_dot_attribute__pb2._ATTRIBUTE
_CLIENTREQUEST.fields_by_name['host'].message_type = bnet_dot_protocol__0__pb2._PROCESSID
_CLIENTREQUEST.fields_by_name['bnet_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_CLIENTREQUEST.fields_by_name['game_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_GAMEACCOUNTOFFLINENOTIFICATION.fields_by_name['game_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_GAMEACCOUNTOFFLINENOTIFICATION.fields_by_name['host'].message_type = bnet_dot_protocol__0__pb2._PROCESSID
_GAMEACCOUNTONLINENOTIFICATION.fields_by_name['game_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_GAMEACCOUNTONLINENOTIFICATION.fields_by_name['host'].message_type = bnet_dot_protocol__0__pb2._PROCESSID
_GETPLAYERVARIABLESREQUEST.fields_by_name['player_variables'].message_type = _PLAYERVARIABLES
_GETPLAYERVARIABLESREQUEST.fields_by_name['host'].message_type = bnet_dot_protocol__0__pb2._PROCESSID
_PRESENCECHANNELCREATEDREQUEST.fields_by_name['id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_PRESENCECHANNELCREATEDREQUEST.fields_by_name['game_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_PRESENCECHANNELCREATEDREQUEST.fields_by_name['bnet_account_id'].message_type = bnet_dot_protocol__0__pb2._ENTITYID
_PRESENCECHANNELCREATEDREQUEST.fields_by_name['host'].message_type = bnet_dot_protocol__0__pb2._PROCESSID
_SERVERREQUEST.fields_by_name['attribute'].message_type = bnet_dot_protocol_dot_attribute__pb2._ATTRIBUTE
_SERVERREQUEST.fields_by_name['host'].message_type = bnet_dot_protocol__0__pb2._PROCESSID
DESCRIPTOR.message_types_by_name['ClientResponse'] = _CLIENTRESPONSE
DESCRIPTOR.message_types_by_name['ServerResponse'] = _SERVERRESPONSE
DESCRIPTOR.message_types_by_name['PlayerVariables'] = _PLAYERVARIABLES
DESCRIPTOR.message_types_by_name['GetPlayerVariablesResponse'] = _GETPLAYERVARIABLESRESPONSE
DESCRIPTOR.message_types_by_name['ClientRequest'] = _CLIENTREQUEST
DESCRIPTOR.message_types_by_name['GameAccountOfflineNotification'] = _GAMEACCOUNTOFFLINENOTIFICATION
DESCRIPTOR.message_types_by_name['GameAccountOnlineNotification'] = _GAMEACCOUNTONLINENOTIFICATION
DESCRIPTOR.message_types_by_name['GetPlayerVariablesRequest'] = _GETPLAYERVARIABLESREQUEST
DESCRIPTOR.message_types_by_name['PresenceChannelCreatedRequest'] = _PRESENCECHANNELCREATEDREQUEST
DESCRIPTOR.message_types_by_name['ServerRequest'] = _SERVERREQUEST

ClientResponse = _reflection.GeneratedProtocolMessageType('ClientResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTRESPONSE,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.ClientResponse)
  ))
_sym_db.RegisterMessage(ClientResponse)

ServerResponse = _reflection.GeneratedProtocolMessageType('ServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVERRESPONSE,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.ServerResponse)
  ))
_sym_db.RegisterMessage(ServerResponse)

PlayerVariables = _reflection.GeneratedProtocolMessageType('PlayerVariables', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERVARIABLES,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.PlayerVariables)
  ))
_sym_db.RegisterMessage(PlayerVariables)

GetPlayerVariablesResponse = _reflection.GeneratedProtocolMessageType('GetPlayerVariablesResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERVARIABLESRESPONSE,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.GetPlayerVariablesResponse)
  ))
_sym_db.RegisterMessage(GetPlayerVariablesResponse)

ClientRequest = _reflection.GeneratedProtocolMessageType('ClientRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTREQUEST,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.ClientRequest)
  ))
_sym_db.RegisterMessage(ClientRequest)

GameAccountOfflineNotification = _reflection.GeneratedProtocolMessageType('GameAccountOfflineNotification', (_message.Message,), dict(
  DESCRIPTOR = _GAMEACCOUNTOFFLINENOTIFICATION,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.GameAccountOfflineNotification)
  ))
_sym_db.RegisterMessage(GameAccountOfflineNotification)

GameAccountOnlineNotification = _reflection.GeneratedProtocolMessageType('GameAccountOnlineNotification', (_message.Message,), dict(
  DESCRIPTOR = _GAMEACCOUNTONLINENOTIFICATION,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.GameAccountOnlineNotification)
  ))
_sym_db.RegisterMessage(GameAccountOnlineNotification)

GetPlayerVariablesRequest = _reflection.GeneratedProtocolMessageType('GetPlayerVariablesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPLAYERVARIABLESREQUEST,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.GetPlayerVariablesRequest)
  ))
_sym_db.RegisterMessage(GetPlayerVariablesRequest)

PresenceChannelCreatedRequest = _reflection.GeneratedProtocolMessageType('PresenceChannelCreatedRequest', (_message.Message,), dict(
  DESCRIPTOR = _PRESENCECHANNELCREATEDREQUEST,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.PresenceChannelCreatedRequest)
  ))
_sym_db.RegisterMessage(PresenceChannelCreatedRequest)

ServerRequest = _reflection.GeneratedProtocolMessageType('ServerRequest', (_message.Message,), dict(
  DESCRIPTOR = _SERVERREQUEST,
  __module__ = 'bnet.protocol.game_utilities_pb2'
  # @@protoc_insertion_point(class_scope:bnet.protocol.game_utilities.ServerRequest)
  ))
_sym_db.RegisterMessage(ServerRequest)


# @@protoc_insertion_point(module_scope)