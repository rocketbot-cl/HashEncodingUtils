import base64
import hashlib
import urllib.parse
import uuid


def base64_transform(text, operation):
    op_normalized = operation.strip().lower()
    if op_normalized == 'encode':
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')
    if op_normalized == 'decode':
        try:
            return base64.b64decode(text.encode('utf-8'), validate=True).decode('utf-8')
        except Exception:
            raise Exception('Invalid Base64 input')
    raise Exception('Unsupported operation: ' + op_normalized)


def url_transform(text, operation):
    op_normalized = operation.strip().lower()
    if op_normalized == 'encode':
        return urllib.parse.quote(text, safe='')
    if op_normalized == 'decode':
        return urllib.parse.unquote(text)
    raise Exception('Unsupported operation: ' + op_normalized)


def generate_hash(text, algorithm):
    text_normalized = algorithm.strip().lower()
    try:
        hasher = hashlib.new(text_normalized)
    except Exception:
        raise Exception('Unsupported hash algorithm: ' + text_normalized)

    hasher.update(text.encode('utf-8'))
    return hasher.hexdigest()


def generate_uuid():
    return str(uuid.uuid4())
