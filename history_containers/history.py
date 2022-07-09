from enum import Enum, unique
from sys import version_info
from typing import Dict, List, Optional, Tuple, Type, Any

if version_info.minor >= 11:
    from typing import Self
else:
    Self = 'HistoryManager'

import history_containers


Iterables = (Dict, List)
History = List[Tuple[Any, Any, Any]]


@unique
class SpecialHistoryEvents(Enum):
    DELETE = object()

    def __str__(self):
        return self.name


class HistoryManager:
    _parent: Optional[Self] = None
    _prefix: Any = ''
    _type_prefix = ''
    history: History = []
    _wrapped_types = Iterables

    @staticmethod
    def _wrap_history_key(key: str) -> str:
        return f'.{key}'

    def __init__(self, parent: Optional[Self] = None, wrapped_types: Optional[Tuple[Type]] = None, prefix: Any = None):
        self._wrapped_types = Iterables if wrapped_types is None else wrapped_types
        self._prefix = '' if prefix is None else prefix
        self._parent = parent
        self.history = []

    def clear_history(self):
        self.history.clear()

    def _get_hist(self, key: Any, value: Any) -> Any:
        if isinstance(value, Dict) and Dict in self._wrapped_types:
            # noinspection PyProtectedMember
            return history_containers._DictWrapper(value, self, self._wrapped_types, key)
        elif isinstance(value, List) and List in self._wrapped_types:
            # noinspection PyProtectedMember
            return value  # TODO: ListWrapper(...)
        else:
            return value

    def _set_hist(self, key: Any, old_value: Any, new_value: Any):
        key = self._wrap_history_key(key)
        self.history += [(f'{self._type_prefix}{key}', old_value, new_value)]
        if self._parent is not None:
            self._parent._set_hist(f'{self._prefix}{key}', old_value, new_value)

    def _delete_hist(self, key: Any, value: Any):
        self._set_hist(key, value, SpecialHistoryEvents.DELETE)

    def _clear_hist(self):
        self.history += [(self._type_prefix, self._type_prefix, SpecialHistoryEvents.DELETE)]
        if self._parent is not None:
            self._parent._set_hist(f'{self._prefix}', self._type_prefix, SpecialHistoryEvents.DELETE)

    def print(self) -> str:
        return '\n'.join([f'{path}: {old} -> {new}' for path, old, new in self.history])
