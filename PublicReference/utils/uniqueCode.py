import hashlib
import sys
import wmi


def get_mac_address():
    if "main.py" not in sys.argv[0]:
        try:
            w = wmi.WMI()
            return hashlib.md5(w.Win32_DiskDrive()[0].SerialNumber.encode(encoding='UTF-8')).hexdigest()
        except:
            return ''
    else:
        return ''
