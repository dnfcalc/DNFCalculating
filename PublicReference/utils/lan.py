from ctypes import sizeof
from operator import le
import os
import json


class Language():
    def __init__(self):
        self.dicts = {}
        self.dicts[""] = ""
        pass

    def load_json(self, path):
        if os.path.exists(path):
            with open(path, encoding='utf-8') as fp:
                self.dicts.update(json.load(fp))
                fp.close()

    def __getitem__(self, key):
        return self.dicts.get(key, key)

    ## key: 原始文本 使用{word}的格式 可以格式化为对应的值
    ## **kwargs: 键值对可变参数 在{word} 之前 将#key转换为对应的value
    def trans(self, text, **kwargs):
        if isinstance(text, list):
            return list(map(lambda i: self.trans(i, **kwargs), text))
        text = str(text)
        value = text
        if self.dicts.__contains__(text):
            value = self.dicts.get(text)
            if value == '':
                value = text
        else:
            for kw in kwargs.keys():
                _old = "${}".format(kw)
                _new = str(kwargs.get(kw))
                text = text.replace(_old, _new)
            try:
                value = text.format_map(self)
            except Exception:
                # 后续待完善
                return value
        value = value.replace("$", "{}")
        return value
