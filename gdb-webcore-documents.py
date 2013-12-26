#!/usr/bin/env python
# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.


import gdb


def root_documents():
  gdb.newest_frame().older().select()

  # Have gdb.Value
  live_instances = gdb.parse_and_eval('WebCore::Document::s_liveInstances')

  print live_instances.type
  print live_instances.address

  # gdb.execute('p WebCore::Document::s_liveInstances')
  # result = gdb.execute('info proc mapping', to_string=True)
  # print result
