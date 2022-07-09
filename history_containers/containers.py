from typing import Optional, Dict, Tuple, Type

from history_containers import _DictWrapper, _ListWrapper, _ObjectWrapper


class HistoryDict(_DictWrapper):
    def __init__(self, dictionary: Optional[Dict] = None, wrapped_types: Optional[Tuple[Type]] = None):
        super().__init__(dictionary, wrapped_types=wrapped_types)

    def __repr__(self) -> str:
        return f'{type(self).__name__}({super(_DictWrapper, self).__repr__()})'

    def __str__(self) -> str:
        return self._dict.__str__()


class HistoryList(_ListWrapper):
    def __init__(self, dictionary: Optional[Dict] = None, wrapped_types: Optional[Tuple[Type]] = None):
        super().__init__(dictionary, wrapped_types=wrapped_types)

    def __repr__(self) -> str:
        return f'{type(self).__name__}({super(_ListWrapper, self).__repr__()})'

    def __str__(self) -> str:
        return self._dict.__str__()


class HistoryObjectMixin(_ObjectWrapper):
    pass
