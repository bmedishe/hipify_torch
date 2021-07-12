#!/usr/bin/env python

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import os
import sys
import argparse
import json
from hipify import hipify_python

parser = argparse.ArgumentParser(
    description='Top-level script for HIPifying, filling in most common parameters')
parser.add_argument(
    '--project-directory',
    type=str,
    help="The root of the project. (default: %(default)s)",
    required=True)

parser.add_argument(
    '--output-directory',
    type=str,
    help="The Directory to Store the Hipified Project",
    required=True)

parser.add_argument(
    '--list-files-only',
    action='store_true',
    help="Only print the list of hipify files.")

parser.add_argument(
    '--includes',
    default=['*'],
    help="Source files to be included for hipify",
    required=False)

parser.add_argument(
    '--ignores',
    default=[],
    help="Source files to be excluded for hipify",
    required=False)

parser.add_argument(
    '--dump-dict-file',
    type=str,
    help="The file to Store the return dict output after hipification",
    required=False)

args = parser.parse_args()
print(args)

HipifyFinalResult = hipify_python.hipify(
    project_directory=args.project_directory,
    output_directory=args.output_directory,
    includes=args.includes,
    ignores=args.ignores,
    is_pytorch_extension=True)

if args.dump_dict_file:
    with open(args.dump_dict_file, 'w') as dict_file:
        dict_file.write(json.dumps(HipifyFinalResult))
