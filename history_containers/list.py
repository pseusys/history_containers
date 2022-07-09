from sys import version_info
from typing import Optional, Dict, Type, Tuple, Any, Iterator, Iterable, Mapping, ItemsView, KeysView, ValuesView

if version_info.minor >= 11:
    from typing import Self
else:
    Self = 'ListWrapper'

from history_containers import _HistoryManager


class ListWrapper(list, _HistoryManager):
    __slots__ = ()

    def __init__(self, seq=()):  # TODO
        """
        Built-in mutable sequence.

        If no argument is given, the constructor creates a new empty list.
        The argument must be an iterable if specified.
        # (copied from class doc)
        """
        pass

    def append(self, *args, **kwargs):  # TODO
        """ Append object to the end of the list. """
        pass

    def clear(self, *args, **kwargs):  # TODO
        """ Remove all items from list. """
        pass

    def copy(self, *args, **kwargs):  # TODO
        """ Return a shallow copy of the list. """
        pass

    def count(self, *args, **kwargs):  # TODO
        """ Return number of occurrences of value. """
        pass

    def extend(self, *args, **kwargs):  # TODO
        """ Extend list by appending elements from the iterable. """
        pass

    def index(self, *args, **kwargs):  # TODO
        """
        Return first index of value.

        Raises ValueError if the value is not present.
        """
        pass

    def insert(self, *args, **kwargs):  # TODO
        """ Insert object before index. """
        pass

    def pop(self, *args, **kwargs):  # TODO
        """
        Remove and return item at index (default last).

        Raises IndexError if list is empty or index is out of range.
        """
        pass

    def remove(self, *args, **kwargs):  # TODO
        """
        Remove first occurrence of value.

        Raises ValueError if the value is not present.
        """
        pass

    def reverse(self, *args, **kwargs):  # TODO
        """ Reverse *IN PLACE*. """
        pass

    def sort(self, *args, **kwargs):  # TODO
        """
        Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).

        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.

        The reverse flag can be set to sort in descending order.
        """
        pass

    def __add__(self, *args, **kwargs):  # TODO
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs):  # TODO
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs):  # TODO
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs):  # TODO
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs):  # TODO
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, y):  # TODO
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, *args, **kwargs):  # TODO
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs):  # TODO
        """ Return self>value. """
        pass

    def __iadd__(self, *args, **kwargs):  # TODO
        """ Implement self+=value. """
        pass

    def __imul__(self, *args, **kwargs):  # TODO
        """ Implement self*=value. """
        pass

    def __iter__(self, *args, **kwargs):  # TODO
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs):  # TODO
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs):  # TODO
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs):  # TODO
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs):  # TODO
        """ Return self*value. """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # TODO
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs):  # TODO
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs):  # TODO
        """ Return repr(self). """
        pass

    def __reversed__(self, *args, **kwargs):  # TODO
        """ Return a reverse iterator over the list. """
        pass

    def __rmul__(self, *args, **kwargs):  # TODO
        """ Return value*self. """
        pass

    def __setitem__(self, *args, **kwargs):  # TODO
        """ Set self[key] to value. """
        pass

    def __sizeof__(self, *args, **kwargs):  # TODO
        """ Return the size of the list in memory, in bytes. """
        pass

    def __str__(self) -> str:  # TODO
        pass
