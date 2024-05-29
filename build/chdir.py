#!/usr/bin/env python3
# Copyright 2024 The Chromium Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""change work dir

This module works much like the cd posix command.
"""

import os
import subprocess
import sys

if len(sys.argv) < 2:
  print("Usage: %s work_dir command..." % sys.argv[0], file=sys.stderr)
  sys.exit(1)

os.chdir(sys.argv[1])
sys.exit(subprocess.check_call(sys.argv[2:]))
