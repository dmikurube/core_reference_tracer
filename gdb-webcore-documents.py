#!/usr/bin/env python
# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


import gdb

# gdb.printing
# gdb.types
# gdb.prompt


type_code = {
  gdb.TYPE_CODE_PTR: 'TYPE_CODE_PTR',
  gdb.TYPE_CODE_ARRAY: 'TYPE_CODE_ARRAY',
  gdb.TYPE_CODE_STRUCT: 'TYPE_CODE_STRUCT',
  gdb.TYPE_CODE_UNION: 'TYPE_CODE_UNION',
  gdb.TYPE_CODE_ENUM: 'TYPE_CODE_ENUM',
  gdb.TYPE_CODE_FLAGS: 'TYPE_CODE_FLAGS',
  gdb.TYPE_CODE_FUNC: 'TYPE_CODE_FUNC',
  gdb.TYPE_CODE_INT: 'TYPE_CODE_INT',
  gdb.TYPE_CODE_FLT: 'TYPE_CODE_FLT',
  gdb.TYPE_CODE_VOID: 'TYPE_CODE_VOID',
  gdb.TYPE_CODE_SET: 'TYPE_CODE_SET',
  gdb.TYPE_CODE_RANGE: 'TYPE_CODE_RANGE',
  gdb.TYPE_CODE_STRING: 'TYPE_CODE_STRING',
  gdb.TYPE_CODE_BITSTRING: 'TYPE_CODE_BITSTRING',
  gdb.TYPE_CODE_ERROR: 'TYPE_CODE_ERROR',
  gdb.TYPE_CODE_METHOD: 'TYPE_CODE_METHOD',
  gdb.TYPE_CODE_METHODPTR: 'TYPE_CODE_METHODPTR',
  gdb.TYPE_CODE_MEMBERPTR: 'TYPE_CODE_MEMBERPTR',
  gdb.TYPE_CODE_REF: 'TYPE_CODE_REF',
  gdb.TYPE_CODE_CHAR: 'TYPE_CODE_CHAR',
  gdb.TYPE_CODE_BOOL: 'TYPE_CODE_BOOL',
  gdb.TYPE_CODE_COMPLEX: 'TYPE_CODE_COMPLEX',
  gdb.TYPE_CODE_TYPEDEF: 'TYPE_CODE_TYPEDEF',
  gdb.TYPE_CODE_NAMESPACE: 'TYPE_CODE_NAMESPACE',
  gdb.TYPE_CODE_DECFLOAT: 'TYPE_CODE_DECFLOAT',
}


def root_documents():
  gdb.newest_frame().older().select()

  # Have gdb.Value
  live_instances = gdb.parse_and_eval('g_liveInstances')
  print live_instances

  document = gdb.lookup_type('WebCore::Document')
  print document
  for field in document.fields():
    if field.name.find('dump') >= 0:
      print '  ' + field.name

  #symbol = gdb.lookup_global_symbol('listLiveInstances')
  #print symbol

  dumper = gdb.parse_and_eval('listLiveInstances')
  print type_code[dumper.type.code]

  print live_instances
  begin = live_instances['begin']
  print begin
  print type_code[begin.type.code]
  print begin.type
  print begin.dynamic_type
  # result = begin ()
  print '---'
  print live_instances['m_impl']
  print live_instances['m_impl']['m_table']
  print live_instances.type
  for field in live_instances.type.fields():
    print field.name
    for field2 in live_instances[field.name].type.fields():
      print '  ' + field2.name
  print live_instances.address

  # gdb.execute('p WebCore::Document::s_liveInstances')
  # result = gdb.execute('info proc mapping', to_string=True)
  # print result
