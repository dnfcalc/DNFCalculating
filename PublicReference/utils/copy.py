import types
import weakref
from copyreg import dispatch_table


def copy(x):
    cls = type(x)
    copier = _copy_dispatch.get(cls)
    if copier:
        return copier(x)
    if issubclass(cls, type):
        return _copy_immutable(x)
    copier = getattr(cls, "__copy__", None)
    if copier is not None:
        return copier(x)
    reductor = dispatch_table.get(cls)
    if reductor is not None:
        rv = reductor(x)
    else:
        reductor = getattr(x, "__reduce_ex__", None)
        if reductor is not None:
            rv = reductor(4)
        else:
            reductor = getattr(x, "__reduce__", None)
            if reductor:
                rv = reductor()
    if isinstance(rv, str):
        return x
    return _reconstruct(x, None, *rv)


_copy_dispatch = d = {}


def _copy_immutable(x):
    return x


for t in (type(None), int, float, bool, complex, str, tuple, bytes, frozenset,
          type, range, slice, property, types.BuiltinFunctionType,
          type(Ellipsis), type(NotImplemented), types.FunctionType,
          weakref.ref):
    d[t] = _copy_immutable
t = getattr(types, "CodeType", None)
if t is not None:
    d[t] = _copy_immutable

d[list] = list.copy
d[dict] = dict.copy
d[set] = set.copy
d[bytearray] = bytearray.copy


def deepcopy(x):
    cls = type(x)
    copier = _deepcopy_dispatch.get(cls)
    if copier is not None:
        y = copier(x)
    else:
        if issubclass(cls, type):
            y = _deepcopy_atomic(x)
        else:
            copier = getattr(x, "__deepcopy__", None)
            reductor = dispatch_table.get(cls)
            if reductor:
                rv = reductor(x)
            else:
                reductor = getattr(x, "__reduce_ex__", None)
                if reductor is not None:
                    rv = reductor(4)
                else:
                    reductor = getattr(x, "__reduce__", None)
                    if reductor:
                        rv = reductor()
            if isinstance(rv, str):
                y = x
            else:
                y = _reconstruct(x, *rv)
    return y


_deepcopy_dispatch = d = {}


def _deepcopy_atomic(x):
    return x


d[type(None)] = _deepcopy_atomic
d[type(Ellipsis)] = _deepcopy_atomic
d[type(NotImplemented)] = _deepcopy_atomic
d[int] = _deepcopy_atomic
d[float] = _deepcopy_atomic
d[bool] = _deepcopy_atomic
d[complex] = _deepcopy_atomic
d[bytes] = _deepcopy_atomic
d[str] = _deepcopy_atomic
d[types.CodeType] = _deepcopy_atomic
d[type] = _deepcopy_atomic
d[range] = _deepcopy_atomic
d[types.BuiltinFunctionType] = _deepcopy_atomic
d[types.FunctionType] = _deepcopy_atomic
d[weakref.ref] = _deepcopy_atomic
d[property] = _deepcopy_atomic


def _deepcopy_list(x, deepcopy=deepcopy):
    y = []
    append = y.append
    for a in x:
        append(deepcopy(a))
    return y


d[list] = _deepcopy_list


def _deepcopy_dict(x, deepcopy=deepcopy):
    y = {}
    for key, value in x.items():
        y[deepcopy(key)] = deepcopy(value)
    return y


d[dict] = _deepcopy_dict


def _reconstruct(x,
                 func,
                 args,
                 state=None,
                 listiter=None,
                 dictiter=None,
                 deepcopy=deepcopy):
    y = func(*args)
    if state is not None:
        state = deepcopy(state)
        if hasattr(y, '__setstate__'):
            y.__setstate__(state)
        else:
            if isinstance(state, tuple) and len(state) == 2:
                state, slotstate = state
            else:
                slotstate = None
            if state is not None:
                y.__dict__.update(state)
            if slotstate is not None:
                for key, value in slotstate.items():
                    setattr(y, key, value)

    if listiter is not None:
        for item in listiter:
            item = deepcopy(item)
            y.append(item)

    if dictiter is not None:
        for key, value in dictiter:
            key = deepcopy(key)
            value = deepcopy(value)
            y[key] = value
    return y
