__version__ = '1.0.0'
__author__ = 'RocketBot <alfredo.villegas@rocketbot.com>'

import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'HashEncodingUtils' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from hashEncodingUtils import base64_transform, generate_hash, generate_uuid, url_transform

module = GetParams('module')

if module == 'GenerateHash':
    text = GetParams('text_')
    algorithm = GetParams('algorithm_')
    var_ = GetParams('var_')

    if not text:
        raise Exception('Missing text')
    if not algorithm:
        raise Exception('Missing algorithm')

    digest = generate_hash(text, algorithm)
    if var_:
        SetVar(var_, digest)

if module == 'Base64':
    text = GetParams('text_')
    operation_ = GetParams('operation_')
    var_ = GetParams('var_')

    if not text:
        raise Exception('Missing text')
    if not operation_:
        raise Exception('Missing operation')

    output = base64_transform(text, operation_)
    if var_:
        SetVar(var_, output)

if module == 'UrlEncodeDecode':
    text = GetParams('text_')
    operation = GetParams('operation_')
    var_ = GetParams('var_')

    if not text:
        raise Exception('Missing text')
    if not operation:
        raise Exception('Missing operation')

    output = url_transform(text, operation)
    if var_:
        SetVar(var_, output)

if module == 'GenerateUUID':
    var_ = GetParams('var_')
    if var_:
        SetVar(var_, generate_uuid())
