from typing import Dict, List, Optional, Tuple, Type, Any

from .dict import DictWrapper

_Iterables = (Dict, List)

_History = List[Tuple[Any, Any]]


class HistoryMixin:
    _prefix: Any
    _history: _History
    _wrapped_types = _Iterables

    def __init__(self, history: Optional[_History] = None, wrapped_types: Optional[Tuple[Type]] = None, prefix: Any = None):
        self._history = [] if history is None else history
        self._wrapped_types = _Iterables if wrapped_types is None else wrapped_types
        self._prefix = '' if prefix is None else f'.{prefix}'

    def clear_history(self):
        self._history.clear()

    def get_wrapped(self, key: Any, value: Any):
        if isinstance(value, Dict) and Dict in self._wrapped_types:
            return DictWrapper(value, self._history, self._wrapped_types, key)
        elif isinstance(value, List) and List in self._wrapped_types:
            return None  # TODO: ListWrapper(...)
        else:
            return value

    def set_wrapped(self, key: Any, value: Any):
        self._history += [(f'{self._prefix}.{key}', value)]
