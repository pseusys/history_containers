from typing import Optional, Dict, Tuple, Type, Any

from history_containers import _DictWrapper, _ListWrapper, _HistoryManager


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


class HistoryObjectMixin(_HistoryManager):
    _solid_attributes = set()
    _type_prefix = 'self'

    watch_self: bool = False

    @staticmethod
    def _wrap_history_key(key: str) -> str:
        return f'.{key}'

    def __init__(self, watch_self: bool = False, wrapped_types: Optional[Tuple[Type]] = None):
        self._solid_attributes |= set(dir(HistoryObjectMixin))
        _HistoryManager.__init__(self, wrapped_types=wrapped_types)
        self.watch_self = watch_self

    def print(self) -> str:
        raw_history = _HistoryManager.print(self).split('\n')
        print_history = '\n'.join([f'\t{event}' for event in _HistoryManager.print(self).split('\n')]) if raw_history != [''] else '    [empty]'
        return f'value: {self}\nhistory:\n{print_history}'

    def __setattr__(self, name: str, value: Any):
        if self.watch_self and name not in self._solid_attributes:
            attr = object.__getattribute__(self, name)
            self._set_hist(name, attr, value)
        object.__setattr__(self, name, value)

    def __getattribute__(self, name: str) -> Any:
        attr = object.__getattribute__(self, name)
        if name != '_solid_attributes' and name not in self._solid_attributes:
            return self._get_hist(name, attr)
        else:
            return attr

    def __delattr__(self, name: str):
        if self.watch_self:
            attr = object.__getattribute__(self, name)
            self._delete_hist(name, attr)
        object.__delattr__(self, name)
