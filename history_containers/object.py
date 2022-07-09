from sys import version_info
from typing import Optional, Dict, Type, Tuple, Any, Iterator, Iterable, Mapping, ItemsView, KeysView, ValuesView

if version_info.minor >= 11:
    from typing import Self
else:
    Self = 'ObjectWrapper'

from history_containers import _HistoryManager


class ObjectWrapper(_HistoryManager):
    def __init__(self) -> None:
        ...

    def __setattr__(self, name: str, value: Any) -> None:
        ...

    def __getattribute__(self, name: str) -> Any:
        ...

    def __delattr__(self, name: str) -> None:
        ...

    def __reduce__(self) -> str | Tuple[Any, ...]:
        ...

    if sys.version_info >= (3, 8):
        def __reduce_ex__(self, protocol: SupportsIndex) -> str | Tuple[Any, ...]:
            ...
    else:
        def __reduce_ex__(self, protocol: int) -> str | Tuple[Any, ...]:
            ...

    def __init_subclass__(cls) -> None:
        ...
