import hashlib
import sys
from .storex import store


def get_mac_address():
    try:
        import wmi
        uniqueCode = store.get("uniqueCode")
        if uniqueCode == None:
            w = wmi.WMI()
            uniqueCode = hashlib.md5(
                w.Win32_DiskDrive()[0].SerialNumber.encode(
                    encoding='UTF-8')).hexdigest()
            store.set("uniqueCode", uniqueCode)
        return uniqueCode
    except:
        return ''
