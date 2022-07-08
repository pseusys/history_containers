from itertools import chain
from typing import Optional, Dict, Type, Tuple, Any, Iterator

from .history import HistoryMixin, _History

str_base = str, bytes, bytearray
items = 'items'

_RaiseKeyError = object()


class DictWrapper(dict, HistoryMixin):
    _dict: Dict

    def clear(self):  # TODO
        """ D.clear() -> None.  Remove all items from D. """
        pass

    def copy(self):  # TODO
        return type(self)(self)

    @classmethod
    def fromkeys(cls, keys, value=None):  # TODO
        return super(DictWrapper, cls).fromkeys(keys, value)

    def get(self, k, default=None):  # TODO
        return super(DictWrapper, self).get(k, default)

    def items(self):
        return self._dict.items()

    def keys(self):
        return self._dict.keys()

    def pop(self, k, v=_RaiseKeyError):  # TODO
        if v is _RaiseKeyError:
            return super(DictWrapper, self).pop(k)
        return super(DictWrapper, self).pop(k, v)

    def popitem(self, *args, **kwargs):  # TODO
        """
        Remove and return a (key, value) pair as a 2-tuple.

        Pairs are returned in LIFO (last-in, first-out) order.
        Raises KeyError if the dict is empty.
        """
        pass

    def setdefault(self, k, default=None):  # TODO
        return super(DictWrapper, self).setdefault(k, default)

    def update(self, mapping=(), **kwargs):  # TODO
        if hasattr(mapping, items):
            mapping = getattr(mapping, items)()
        pairs = ((k, v) for k, v in chain(mapping, getattr(kwargs, items)()))
        super(DictWrapper, self).update(pairs)

    def values(self):  # TODO
        """ D.values() -> an object providing a view on D's values """
        pass

    def __class_getitem__(cls, *args, **kwargs):  # TODO
        """ See PEP 585 """
        pass

    def __contains__(self, key: Any) -> bool:
        return self._dict.__contains__(key)

    def __delitem__(self, k):  # TODO
        return super(DictWrapper, self).__delitem__(k)

    def __eq__(self, obj: object) -> bool:
        return self._dict.__eq__(obj)

    def __getattribute__(self, name: str) -> Any:
        return self._dict.__getattribute__(name)

    def __getitem__(self, key: Any) -> Any:
        return super().get_wrapped(key, super().__getitem__(key))

    def __ge__(self, obj: object) -> bool:
        return self._dict.__ge__(obj)

    def __gt__(self, obj: object) -> bool:
        return self._dict.__gt__(obj)

    def __init__(self, dictionary: Optional[Dict] = None, history: Optional[_History] = None, wrapped_types: Optional[Tuple[Type]] = None, prefix: Any = None):
        self._dict = dictionary
        super(HistoryMixin, DictWrapper).__init__(history, wrapped_types, prefix)

    def __ior__(self, obj: Dict) -> Dict:  # TODO
        return self._dict.__ior__(obj)

    def __iter__(self) -> Iterator[Any]:
        return self._dict.__iter__()

    def __len__(self) -> int:
        return self._dict.__len__()

    def __le__(self, obj: object) -> bool:
        return self._dict.__le__(obj)

    def __lt__(self, obj: object) -> bool:
        return self._dict.__lt__(obj)

    def __ne__(self, obj: object) -> bool:
        return self._dict.__ne__(obj)

    def __or__(self, obj: Dict) -> Dict:  # TODO
        return self._dict.__or__(obj)

    def __repr__(self) -> str:
        return f'{type(self).__name__}({super(DictWrapper, self).__repr__()})'

    def __reversed__(self, *args, **kwargs):  # TODO
        """ Return a reverse iterator over the dict keys. """
        pass

    def __ror__(self, *args, **kwargs):  # TODO
        """ Return value|self. """
        pass

    def __setitem__(self, key: Any, value: Any):
        item = super().__setitem__(key, value)
        super().set_wrapped(key, item)
        return item