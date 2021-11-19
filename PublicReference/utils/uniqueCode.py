import hashlib
import sys
import wmi
from .storex import store


def get_mac_address():
    if "main.py" in sys.argv[0]:
        try:
            uniqueCode = store.get("uniqueCode")
            print(uniqueCode)
            if uniqueCode == None:
                w = wmi.WMI()
                uniqueCode = hashlib.md5(w.Win32_DiskDrive()[0].SerialNumber.encode(encoding='UTF-8')).hexdigest()
                store.set("uniqueCode",uniqueCode)
            return uniqueCode
        except:
            return ''
    else:
        return ''
