##
##
## 用于存储数据,及组件间通信
# Author: Apateat
##
##
from copy import copy
import re


class Store:
    def __init__(self):
        self.__states = {}
        self.last_state = None
        pass

    # 设置值
    def set(self, key: str, value: any):
        field = self.__get_field__(key)
        field.setValue(value)
        return self

    # 获取值
    def get(self, key: str, defaultValue: any = None):
        field = self.__get_field__(key)
        _value = field.getValue()
        if _value is None:
            _value = defaultValue
        return _value

    def __getitem__(self, __key: str):
        return self.get(__key)

    # 获取一个克隆值
    def clone(self, key: str, defaultValue: any = None):
        value = self.get(key, defaultValue)
        return copy(value)

    # 主动通知变化
    def emit(self, key: str, value: any = None):
        field = self.__get_field__(key)
        field.emit(value)
        return self

    # 找到首个不为空的值
    def first(self, *names):
        value = None
        for name in names:
            value = self.get(name)
            if value is not None:
                break
        return value

    # 计算属性
    def compute(self, key: str, getter, setter=None):
        field = self.__get_field__(key)
        field.apply(setter)
        field.getter = getter
        return self

    # 获取值并设置值
    def use(self, key: str, handle):
        if callable(handle):
            value = handle(self.get(key))
            self.set(key, value)
        return self

    # 批量修改整个集合
    def convert(self, key: str, handle):
        return self.use(key, lambda value: list(map(handle, value)))

    # 绑定对象的属性
    def bind(self, obj: object, name: str, key=None, defaultValue: any = None):
        def getter():
            return getattr(obj, name)

        def setter(value):
            setattr(obj, name, value)

        # 如果属性不存在 则初始化
        if hasattr(obj, name) is False or defaultValue is not None:
            setattr(obj, name, defaultValue)

        return self.compute(key, getter, setter)

    # 根据指定的条件删除
    def delete(self, pattern=None):
        match = lambda _: True
        if pattern is not None:
            if callable(pattern):
                match = pattern
            elif isinstance(pattern, str):
                match = lambda s: re.match(pattern, s)
        keys = list(filter(match, self.__states.keys()))
        for key in keys:
            self.__states.pop(key)
        return self

    # 根据指定的条件导出
    def exports(self, match=lambda _: True):
        result = {}
        for key in self.__states.keys():
            if match(key):
                result[key] = self.get(key)
        return result

    # 导入
    def imports(self, pairs: dict = {}, prefix=''):
        for key in pairs.keys():
            self.set(prefix + str(key), pairs[key])
        return self

    # 只读属性
    def const(self, key: str, value: any):
        return self.compute(key, lambda: value)

    # 监听值的变化
    def watch(self, key: str, valueChanged):
        return self.compute(key, None, valueChanged)

    def linstener(self, key: str):
        def change(value):
            self.set(key, value)
            pass

        return change

    def __get_field__(self, key: str):
        field = None
        if re.search("\{\w+\}", key):
            key = key.format_map(self)
        if self.__states.__contains__(key):
            field = self.__states[key]
        else:
            field = Store.Field()
            self.__states[key] = field
        self.last_state = (key, field)
        return field

    class Field:
        def __init__(self, value=None):
            self.__value = None
            self.getter = None
            self.valueChangeds = []
            self.locked = False
            self.setValue(value)
            pass

        def setValue(self, value):
            if self.locked:
                return
            self.locked = True
            self.__value = value
            self.emit(value)
            self.locked = False
            return self

        def getValue(self):
            if callable(self.getter):
                self.__value = self.getter()
            return self.__value

        def emit(self, value=None):
            if value is None:
                value = self.getValue()
            for valueChanged in self.valueChangeds:
                if (callable(valueChanged)):
                    valueChanged(value)
            return

        def apply(self, valueChanged):
            if callable(valueChanged):
                self.valueChangeds.append(valueChanged)


store = Store()
