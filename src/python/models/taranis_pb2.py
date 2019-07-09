# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: taranis.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='taranis.proto',
    package='taranis',
    syntax='proto3',
    serialized_options=_b('\n\nio.taranisB\014TaranisProtoP\001\242\002\004TRNS'),
    serialized_pb=_b(
        '\n\rtaranis.proto\x12\x07taranis\"\x07\n\x05\x45mpty\" \n\x10NewDatabaseModel\x12\x0c\n\x04name\x18\x01 \x01(\t\"!\n\x11\x44\x61tabaseNameModel\x12\x0c\n\x04name\x18\x01 \x01(\t\"l\n\rDatabaseModel\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncreated_at\x18\x02 \x01(\x03\x12\x17\n\x0flast_trained_at\x18\x03 \x01(\x03\x12\x12\n\nupdated_at\x18\x04 \x01(\x03\x12\x0c\n\x04size\x18\x05 \x01(\x03\"6\n\x0fIndexQueryModel\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\"D\n\rNewIndexModel\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\"\xcf\x01\n\nIndexModel\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x03 \x01(\t\x12\x12\n\ncreated_at\x18\x04 \x01(\x03\x12\x17\n\x0flast_trained_at\x18\x05 \x01(\x03\x12\x12\n\nupdated_at\x18\x06 \x01(\x03\x12(\n\x05state\x18\x07 \x01(\x0e\x32\x19.taranis.IndexModel.State\"!\n\x05State\x12\x0b\n\x07\x43REATED\x10\x00\x12\x0b\n\x07TRAINED\x10\x01\"9\n\x0bVectorModel\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x10\n\x08metadata\x18\x03 \x01(\t\"]\n\x0fNewVectorsModel\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12%\n\x07vectors\x18\x03 \x03(\x0b\x32\x14.taranis.VectorModel\"1\n\x11VectorsQueryModel\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x0b\n\x03ids\x18\x02 \x03(\x03\":\n\x11VectorsReplyModel\x12%\n\x07vectors\x18\x02 \x03(\x0b\x32\x14.taranis.VectorModel\"f\n\x12SearchRequestModel\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x12\n\nindex_name\x18\x02 \x01(\t\x12\x0f\n\x07vectors\x18\x03 \x03(\x0c\x12\t\n\x01k\x18\x04 \x01(\x05\x12\x0f\n\x07n_probe\x18\x05 \x01(\x05\"/\n\x11SearchResultModel\x12\r\n\x05\x64ists\x18\x01 \x03(\x02\x12\x0b\n\x03knn\x18\x02 \x03(\x03\"D\n\x15SearchResultListModel\x12+\n\x07results\x18\x01 \x03(\x0b\x32\x1a.taranis.SearchResultModel\"N\n\x0eVectorsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\r\n\x05\x63ount\x18\x03 \x01(\x05\x12\x11\n\tdimension\x18\x04 \x01(\x05\"U\n\x12SearchResultsReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x11\n\tdimension\x18\x03 \x01(\x05\x12\r\n\x05\x63ount\x18\x04 \x01(\x05\x32\xce\x05\n\x07Taranis\x12\x43\n\x0bgetDatabase\x12\x1a.taranis.DatabaseNameModel\x1a\x16.taranis.DatabaseModel\"\x00\x12\x45\n\x0e\x63reateDatabase\x12\x19.taranis.NewDatabaseModel\x1a\x16.taranis.DatabaseModel\"\x00\x12>\n\x0e\x64\x65leteDatabase\x12\x1a.taranis.DatabaseNameModel\x1a\x0e.taranis.Empty\"\x00\x12;\n\x08getIndex\x12\x18.taranis.IndexQueryModel\x1a\x13.taranis.IndexModel\"\x00\x12\x39\n\x0b\x64\x65leteIndex\x12\x18.taranis.IndexQueryModel\x1a\x0e.taranis.Empty\"\x00\x12<\n\x0b\x63reateIndex\x12\x16.taranis.NewIndexModel\x1a\x13.taranis.IndexModel\"\x00\x12\x38\n\ntrainIndex\x12\x18.taranis.IndexQueryModel\x1a\x0e.taranis.Empty\"\x00\x12\x35\n\x07reindex\x12\x18.taranis.IndexQueryModel\x1a\x0e.taranis.Empty\"\x00\x12\x38\n\naddVectors\x12\x18.taranis.NewVectorsModel\x1a\x0e.taranis.Empty\"\x00\x12\x46\n\ngetVectors\x12\x1a.taranis.VectorsQueryModel\x1a\x1a.taranis.VectorsReplyModel\"\x00\x12N\n\rsearchVectors\x12\x1b.taranis.SearchRequestModel\x1a\x1e.taranis.SearchResultListModel\"\x00\x42#\n\nio.taranisB\x0cTaranisProtoP\x01\xa2\x02\x04TRNSb\x06proto3')
)

_INDEXMODEL_STATE = _descriptor.EnumDescriptor(
    name='State',
    full_name='taranis.IndexModel.State',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='CREATED', index=0, number=0,
            serialized_options=None,
            type=None),
        _descriptor.EnumValueDescriptor(
            name='TRAINED', index=1, number=1,
            serialized_options=None,
            type=None),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=515,
    serialized_end=548,
)
_sym_db.RegisterEnumDescriptor(_INDEXMODEL_STATE)

_EMPTY = _descriptor.Descriptor(
    name='Empty',
    full_name='taranis.Empty',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
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
    serialized_start=26,
    serialized_end=33,
)

_NEWDATABASEMODEL = _descriptor.Descriptor(
    name='NewDatabaseModel',
    full_name='taranis.NewDatabaseModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='taranis.NewDatabaseModel.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=35,
    serialized_end=67,
)

_DATABASENAMEMODEL = _descriptor.Descriptor(
    name='DatabaseNameModel',
    full_name='taranis.DatabaseNameModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='taranis.DatabaseNameModel.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=69,
    serialized_end=102,
)

_DATABASEMODEL = _descriptor.Descriptor(
    name='DatabaseModel',
    full_name='taranis.DatabaseModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='taranis.DatabaseModel.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='created_at', full_name='taranis.DatabaseModel.created_at', index=1,
            number=2, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='last_trained_at', full_name='taranis.DatabaseModel.last_trained_at', index=2,
            number=3, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='updated_at', full_name='taranis.DatabaseModel.updated_at', index=3,
            number=4, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='size', full_name='taranis.DatabaseModel.size', index=4,
            number=5, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=104,
    serialized_end=212,
)

_INDEXQUERYMODEL = _descriptor.Descriptor(
    name='IndexQueryModel',
    full_name='taranis.IndexQueryModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='db_name', full_name='taranis.IndexQueryModel.db_name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='index_name', full_name='taranis.IndexQueryModel.index_name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=214,
    serialized_end=268,
)

_NEWINDEXMODEL = _descriptor.Descriptor(
    name='NewIndexModel',
    full_name='taranis.NewIndexModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='db_name', full_name='taranis.NewIndexModel.db_name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='index_name', full_name='taranis.NewIndexModel.index_name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='config', full_name='taranis.NewIndexModel.config', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=270,
    serialized_end=338,
)

_INDEXMODEL = _descriptor.Descriptor(
    name='IndexModel',
    full_name='taranis.IndexModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='db_name', full_name='taranis.IndexModel.db_name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='index_name', full_name='taranis.IndexModel.index_name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='config', full_name='taranis.IndexModel.config', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='created_at', full_name='taranis.IndexModel.created_at', index=3,
            number=4, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='last_trained_at', full_name='taranis.IndexModel.last_trained_at', index=4,
            number=5, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='updated_at', full_name='taranis.IndexModel.updated_at', index=5,
            number=6, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='state', full_name='taranis.IndexModel.state', index=6,
            number=7, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
        _INDEXMODEL_STATE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=341,
    serialized_end=548,
)

_VECTORMODEL = _descriptor.Descriptor(
    name='VectorModel',
    full_name='taranis.VectorModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='taranis.VectorModel.id', index=0,
            number=1, type=3, cpp_type=2, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='taranis.VectorModel.data', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='metadata', full_name='taranis.VectorModel.metadata', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=550,
    serialized_end=607,
)

_NEWVECTORSMODEL = _descriptor.Descriptor(
    name='NewVectorsModel',
    full_name='taranis.NewVectorsModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='db_name', full_name='taranis.NewVectorsModel.db_name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='index_name', full_name='taranis.NewVectorsModel.index_name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='vectors', full_name='taranis.NewVectorsModel.vectors', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=609,
    serialized_end=702,
)

_VECTORSQUERYMODEL = _descriptor.Descriptor(
    name='VectorsQueryModel',
    full_name='taranis.VectorsQueryModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='db_name', full_name='taranis.VectorsQueryModel.db_name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='ids', full_name='taranis.VectorsQueryModel.ids', index=1,
            number=2, type=3, cpp_type=2, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=704,
    serialized_end=753,
)

_VECTORSREPLYMODEL = _descriptor.Descriptor(
    name='VectorsReplyModel',
    full_name='taranis.VectorsReplyModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='vectors', full_name='taranis.VectorsReplyModel.vectors', index=0,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=755,
    serialized_end=813,
)

_SEARCHREQUESTMODEL = _descriptor.Descriptor(
    name='SearchRequestModel',
    full_name='taranis.SearchRequestModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='db_name', full_name='taranis.SearchRequestModel.db_name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='index_name', full_name='taranis.SearchRequestModel.index_name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='vectors', full_name='taranis.SearchRequestModel.vectors', index=2,
            number=3, type=12, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='k', full_name='taranis.SearchRequestModel.k', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='n_probe', full_name='taranis.SearchRequestModel.n_probe', index=4,
            number=5, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=815,
    serialized_end=917,
)

_SEARCHRESULTMODEL = _descriptor.Descriptor(
    name='SearchResultModel',
    full_name='taranis.SearchResultModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='dists', full_name='taranis.SearchResultModel.dists', index=0,
            number=1, type=2, cpp_type=6, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='knn', full_name='taranis.SearchResultModel.knn', index=1,
            number=2, type=3, cpp_type=2, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=919,
    serialized_end=966,
)

_SEARCHRESULTLISTMODEL = _descriptor.Descriptor(
    name='SearchResultListModel',
    full_name='taranis.SearchResultListModel',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='results', full_name='taranis.SearchResultListModel.results', index=0,
            number=1, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=968,
    serialized_end=1036,
)

_VECTORSREQUEST = _descriptor.Descriptor(
    name='VectorsRequest',
    full_name='taranis.VectorsRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='name', full_name='taranis.VectorsRequest.name', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='taranis.VectorsRequest.data', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='count', full_name='taranis.VectorsRequest.count', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='dimension', full_name='taranis.VectorsRequest.dimension', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=1038,
    serialized_end=1116,
)

_SEARCHRESULTSREPLY = _descriptor.Descriptor(
    name='SearchResultsReply',
    full_name='taranis.SearchResultsReply',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='message', full_name='taranis.SearchResultsReply.message', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='taranis.SearchResultsReply.data', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='dimension', full_name='taranis.SearchResultsReply.dimension', index=2,
            number=3, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='count', full_name='taranis.SearchResultsReply.count', index=3,
            number=4, type=5, cpp_type=1, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=1118,
    serialized_end=1203,
)

_INDEXMODEL.fields_by_name['state'].enum_type = _INDEXMODEL_STATE
_INDEXMODEL_STATE.containing_type = _INDEXMODEL
_NEWVECTORSMODEL.fields_by_name['vectors'].message_type = _VECTORMODEL
_VECTORSREPLYMODEL.fields_by_name['vectors'].message_type = _VECTORMODEL
_SEARCHRESULTLISTMODEL.fields_by_name['results'].message_type = _SEARCHRESULTMODEL
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['NewDatabaseModel'] = _NEWDATABASEMODEL
DESCRIPTOR.message_types_by_name['DatabaseNameModel'] = _DATABASENAMEMODEL
DESCRIPTOR.message_types_by_name['DatabaseModel'] = _DATABASEMODEL
DESCRIPTOR.message_types_by_name['IndexQueryModel'] = _INDEXQUERYMODEL
DESCRIPTOR.message_types_by_name['NewIndexModel'] = _NEWINDEXMODEL
DESCRIPTOR.message_types_by_name['IndexModel'] = _INDEXMODEL
DESCRIPTOR.message_types_by_name['VectorModel'] = _VECTORMODEL
DESCRIPTOR.message_types_by_name['NewVectorsModel'] = _NEWVECTORSMODEL
DESCRIPTOR.message_types_by_name['VectorsQueryModel'] = _VECTORSQUERYMODEL
DESCRIPTOR.message_types_by_name['VectorsReplyModel'] = _VECTORSREPLYMODEL
DESCRIPTOR.message_types_by_name['SearchRequestModel'] = _SEARCHREQUESTMODEL
DESCRIPTOR.message_types_by_name['SearchResultModel'] = _SEARCHRESULTMODEL
DESCRIPTOR.message_types_by_name['SearchResultListModel'] = _SEARCHRESULTLISTMODEL
DESCRIPTOR.message_types_by_name['VectorsRequest'] = _VECTORSREQUEST
DESCRIPTOR.message_types_by_name['SearchResultsReply'] = _SEARCHRESULTSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
    DESCRIPTOR=_EMPTY,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.Empty)
))
_sym_db.RegisterMessage(Empty)

NewDatabaseModel = _reflection.GeneratedProtocolMessageType('NewDatabaseModel', (_message.Message,), dict(
    DESCRIPTOR=_NEWDATABASEMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.NewDatabaseModel)
))
_sym_db.RegisterMessage(NewDatabaseModel)

DatabaseNameModel = _reflection.GeneratedProtocolMessageType('DatabaseNameModel', (_message.Message,), dict(
    DESCRIPTOR=_DATABASENAMEMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.DatabaseNameModel)
))
_sym_db.RegisterMessage(DatabaseNameModel)

DatabaseModel = _reflection.GeneratedProtocolMessageType('DatabaseModel', (_message.Message,), dict(
    DESCRIPTOR=_DATABASEMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.DatabaseModel)
))
_sym_db.RegisterMessage(DatabaseModel)

IndexQueryModel = _reflection.GeneratedProtocolMessageType('IndexQueryModel', (_message.Message,), dict(
    DESCRIPTOR=_INDEXQUERYMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.IndexQueryModel)
))
_sym_db.RegisterMessage(IndexQueryModel)

NewIndexModel = _reflection.GeneratedProtocolMessageType('NewIndexModel', (_message.Message,), dict(
    DESCRIPTOR=_NEWINDEXMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.NewIndexModel)
))
_sym_db.RegisterMessage(NewIndexModel)

IndexModel = _reflection.GeneratedProtocolMessageType('IndexModel', (_message.Message,), dict(
    DESCRIPTOR=_INDEXMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.IndexModel)
))
_sym_db.RegisterMessage(IndexModel)

VectorModel = _reflection.GeneratedProtocolMessageType('VectorModel', (_message.Message,), dict(
    DESCRIPTOR=_VECTORMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.VectorModel)
))
_sym_db.RegisterMessage(VectorModel)

NewVectorsModel = _reflection.GeneratedProtocolMessageType('NewVectorsModel', (_message.Message,), dict(
    DESCRIPTOR=_NEWVECTORSMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.NewVectorsModel)
))
_sym_db.RegisterMessage(NewVectorsModel)

VectorsQueryModel = _reflection.GeneratedProtocolMessageType('VectorsQueryModel', (_message.Message,), dict(
    DESCRIPTOR=_VECTORSQUERYMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.VectorsQueryModel)
))
_sym_db.RegisterMessage(VectorsQueryModel)

VectorsReplyModel = _reflection.GeneratedProtocolMessageType('VectorsReplyModel', (_message.Message,), dict(
    DESCRIPTOR=_VECTORSREPLYMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.VectorsReplyModel)
))
_sym_db.RegisterMessage(VectorsReplyModel)

SearchRequestModel = _reflection.GeneratedProtocolMessageType('SearchRequestModel', (_message.Message,), dict(
    DESCRIPTOR=_SEARCHREQUESTMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.SearchRequestModel)
))
_sym_db.RegisterMessage(SearchRequestModel)

SearchResultModel = _reflection.GeneratedProtocolMessageType('SearchResultModel', (_message.Message,), dict(
    DESCRIPTOR=_SEARCHRESULTMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.SearchResultModel)
))
_sym_db.RegisterMessage(SearchResultModel)

SearchResultListModel = _reflection.GeneratedProtocolMessageType('SearchResultListModel', (_message.Message,), dict(
    DESCRIPTOR=_SEARCHRESULTLISTMODEL,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.SearchResultListModel)
))
_sym_db.RegisterMessage(SearchResultListModel)

VectorsRequest = _reflection.GeneratedProtocolMessageType('VectorsRequest', (_message.Message,), dict(
    DESCRIPTOR=_VECTORSREQUEST,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.VectorsRequest)
))
_sym_db.RegisterMessage(VectorsRequest)

SearchResultsReply = _reflection.GeneratedProtocolMessageType('SearchResultsReply', (_message.Message,), dict(
    DESCRIPTOR=_SEARCHRESULTSREPLY,
    __module__='taranis_pb2'
    # @@protoc_insertion_point(class_scope:taranis.SearchResultsReply)
))
_sym_db.RegisterMessage(SearchResultsReply)

DESCRIPTOR._options = None

_TARANIS = _descriptor.ServiceDescriptor(
    name='Taranis',
    full_name='taranis.Taranis',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=1206,
    serialized_end=1924,
    methods=[
        _descriptor.MethodDescriptor(
            name='getDatabase',
            full_name='taranis.Taranis.getDatabase',
            index=0,
            containing_service=None,
            input_type=_DATABASENAMEMODEL,
            output_type=_DATABASEMODEL,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='createDatabase',
            full_name='taranis.Taranis.createDatabase',
            index=1,
            containing_service=None,
            input_type=_NEWDATABASEMODEL,
            output_type=_DATABASEMODEL,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='deleteDatabase',
            full_name='taranis.Taranis.deleteDatabase',
            index=2,
            containing_service=None,
            input_type=_DATABASENAMEMODEL,
            output_type=_EMPTY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='getIndex',
            full_name='taranis.Taranis.getIndex',
            index=3,
            containing_service=None,
            input_type=_INDEXQUERYMODEL,
            output_type=_INDEXMODEL,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='deleteIndex',
            full_name='taranis.Taranis.deleteIndex',
            index=4,
            containing_service=None,
            input_type=_INDEXQUERYMODEL,
            output_type=_EMPTY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='createIndex',
            full_name='taranis.Taranis.createIndex',
            index=5,
            containing_service=None,
            input_type=_NEWINDEXMODEL,
            output_type=_INDEXMODEL,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='trainIndex',
            full_name='taranis.Taranis.trainIndex',
            index=6,
            containing_service=None,
            input_type=_INDEXQUERYMODEL,
            output_type=_EMPTY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='reindex',
            full_name='taranis.Taranis.reindex',
            index=7,
            containing_service=None,
            input_type=_INDEXQUERYMODEL,
            output_type=_EMPTY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='addVectors',
            full_name='taranis.Taranis.addVectors',
            index=8,
            containing_service=None,
            input_type=_NEWVECTORSMODEL,
            output_type=_EMPTY,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='getVectors',
            full_name='taranis.Taranis.getVectors',
            index=9,
            containing_service=None,
            input_type=_VECTORSQUERYMODEL,
            output_type=_VECTORSREPLYMODEL,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='searchVectors',
            full_name='taranis.Taranis.searchVectors',
            index=10,
            containing_service=None,
            input_type=_SEARCHREQUESTMODEL,
            output_type=_SEARCHRESULTLISTMODEL,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_TARANIS)

DESCRIPTOR.services_by_name['Taranis'] = _TARANIS

# @@protoc_insertion_point(module_scope)