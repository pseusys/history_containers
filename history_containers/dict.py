from itertools import chain
from sys import version_info
from typing import Optional, Dict, Type, Tuple, Any, Iterator, Iterable, Mapping, ItemsView, KeysView, ValuesView

if version_info.minor >= 11:
    from typing import Self
else:
    Self = 'DictWrapper'

from history_containers import _HistoryManager


RaiseKeyError = object()


class DictWrapper(dict, _HistoryManager):
    __slots__ = ()

    _dict: Dict
    _type_prefix = 'dict'

    @staticmethod
    def _wrap_history_key(key: str) -> str:
        return f'[{key}]'

    def __init__(self, dictionary: Optional[Dict] = None, parent: Optional[_HistoryManager] = None, wrapped_types: Optional[Tuple[Type]] = None, prefix: Optional[Any] = None):
        _HistoryManager.__init__(self, parent, wrapped_types, prefix)
        self._dict = {} if dictionary is None else dictionary

    def print(self) -> str:
        raw_history = self.print_history().split('\n')
        print_history = '\n'.join([f'\t{event}' for event in self.print_history().split('\n')]) if raw_history != [''] else '    [empty]'
        return f'value: {self}\nhistory:\n{print_history}'

    def clear(self):
        self._dict.clear()
        self._clear_hist()

    def copy(self) -> Self:
        copy = DictWrapper(self._dict, self._parent, self._wrapped_types, self._prefix)
        copy.history = self.history
        return copy

    @classmethod
    def fromkeys(cls, keys: Iterable[Any], value: Optional[Any] = None) -> Self:
        return cls(super(DictWrapper).fromkeys(keys, value))

    def get(self, key: Any, default: Optional[Any] = None) -> Any:
        return self.__getitem__(key) if self.__contains__(key) else default

    def items(self) -> ItemsView[Any, Any]:
        return ItemsView(self)

    def keys(self) -> KeysView[Any]:
        return KeysView(self)

    def values(self) -> ValuesView[Any]:
        return ValuesView(self)

    def pop(self, key: Any, default: Any = RaiseKeyError) -> Any:
        if self.__contains__(key):
            result = self._dict.pop(key)
            self._delete_hist(key, result)  # maybe double writing
            return result
        elif default is RaiseKeyError:
            raise KeyError(key)
        else:
            return default

    def popitem(self) -> Tuple[Any, Any]:
        key, value = self._dict.popitem()
        self._delete_hist(key, value)  # maybe double writing
        return key, value

    def setdefault(self, key: Any, default: Any = None) -> Any:
        if self.__contains__(key):
            return self.__getitem__(key)
        else:
            return self.__setitem__(key, default)

    def update(self, mapping: Mapping[Any, Any] = (), **kwargs):
        if hasattr(mapping, 'items'):
            mapping = getattr(mapping, 'items')()
        pairs = ((key, value) for key, value in chain(mapping, getattr(kwargs, 'items')()))
        for key, value in pairs:
            self._set_hist(key, self.get(key, None), value)
        self._dict.update(pairs)

    def __contains__(self, key: Any) -> bool:
        return self._dict.__contains__(key)

    def __delitem__(self, key: Any):
        if self.__contains__(key):
            self._delete_hist(key, self.__getitem__(key))
        return super(DictWrapper).__delitem__(key)

    def __eq__(self, obj: object) -> bool:
        return self._dict.__eq__(obj)

    def __getitem__(self, key: Any) -> Any:
        return self._get_hist(key, self._dict.__getitem__(key))

    def __ge__(self, obj: object) -> bool:
        return self._dict.__ge__(obj)

    def __gt__(self, obj: object) -> bool:
        return self._dict.__gt__(obj)

    def __ior__(self, obj: Dict) -> Self:
        self.update(obj)
        return self

    def __iter__(self) -> Iterator[Tuple[Any, Any]]:
        for key, item in self.items():
            yield key, item

    def __len__(self) -> int:
        return self._dict.__len__()

    def __le__(self, obj: object) -> bool:
        return self._dict.__le__(obj)

    def __lt__(self, obj: object) -> bool:
        return self._dict.__lt__(obj)

    def __ne__(self, obj: object) -> bool:
        return self._dict.__ne__(obj)

    def __or__(self, obj: Dict) -> Self:
        return self.copy().__ior__(obj)

    def __repr__(self) -> str:
        return self._dict.__repr__()

    def __reversed__(self, *args, **kwargs) -> Iterator[Tuple[Any, Any]]:
        for key, item in self.items().__reversed__():
            yield key, item

    def __ror__(self, obj: Dict) -> Dict:
        return obj.__ior__(self._dict)

    def __setitem__(self, key: Any, value: Any):
        item = self._dict.__setitem__(key, value)
        self._set_hist(key, item, value)

    def __str__(self) -> str:
        return self._dict.__str__()
