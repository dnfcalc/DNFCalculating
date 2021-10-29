import uuid
import hashlib
import sys


def get_mac_address():
    if "main.py" not in sys.argv[0]:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        data = ":".join([mac[e:e + 2] for e in range(0, 11, 2)])
        return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    else:
        return ''
