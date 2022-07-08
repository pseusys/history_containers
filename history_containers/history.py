from sys import version_info
from typing import Dict, List, Optional, Tuple, Type, Any
if version_info.minor >= 11:
    from typing import Self
else:
    Self = 'HistoryMixin'


_Iterables = (Dict, List)

_History = List[Tuple[Any, Any, Any]]


class HistoryMixin:
    _parent: Optional[Self]
    _prefix: Any
    history: _History
    _wrapped_types = _Iterables

    def __init__(self, parent: Optional[Self] = None, wrapped_types: Optional[Tuple[Type]] = None, prefix: Any = None):
        self._wrapped_types = _Iterables if wrapped_types is None else wrapped_types
        self._prefix = 'self' if prefix is None else prefix
        self._parent = parent
        self.history = []

    def clear_history(self):
        self.history.clear()

    def get_wrapped(self, key: Any, value: Any):
        from .dict import DictWrapper
        if isinstance(value, Dict) and Dict in self._wrapped_types:
            return DictWrapper(value, self, self._wrapped_types, key)
        elif isinstance(value, List) and List in self._wrapped_types:
            return None  # TODO: ListWrapper(...)
        else:
            return value

    def set_wrapped(self, key: Any, old_value: Any, new_value: Any):
        key = f'{self._prefix}.{key}'
        self.history += [(key, old_value, new_value)]
        if self._parent is not None:
            self._parent.set_wrapped(key, old_value, new_value)
