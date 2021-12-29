import datetime
from typing import (
    Any,
    Dict,
    Generic,
    Iterable,
    Iterator,
    List,
    MutableMapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from django.db.models import Combinable
from django.db.models.base import Model
from django.db.models.query import QuerySet, RawQuerySet

from django_stubs_ext import ValuesQuerySet

_T = TypeVar("_T", bound=Model, covariant=True)
_M = TypeVar("_M", bound="BaseManager")

class BaseManager(Generic[_T]):
    creation_counter: int = ...
    auto_created: bool = ...
    use_in_migrations: bool = ...
    name: str = ...
    model: Type[_T] = ...
    db: str
    _db: Optional[str]
    def __init__(self) -> None: ...
    def deconstruct(self) -> Tuple[bool, str, None, Tuple, Dict[str, int]]: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    @classmethod
    def from_queryset(cls, queryset_class: Type[QuerySet], class_name: Optional[str] = ...) -> Any: ...
    @classmethod
    def _get_queryset_methods(cls, queryset_class: type) -> Dict[str, Any]: ...
    def contribute_to_class(self, model: Type[Model], name: str) -> None: ...
    def db_manager(self: _M, using: Optional[str] = ..., hints: Optional[Dict[str, Model]] = ...) -> _M: ...
    def get_queryset(self) -> QuerySet[_T]: ...
    # NOTE: The following methods are in common with QuerySet, but note that the use of QuerySet as a return type
    # rather than a self-type (_QS), since Manager's QuerySet-like methods return QuerySets and not Managers.
    def iterator(self, chunk_size: int = ...) -> Iterator[_T]: ...
    def aggregate(self, *args: Any, **kwargs: Any) -> Dict[str, Any]: ...
    def get(self, *args: Any, **kwargs: Any) -> _T: ...
    def create(self, **kwargs: Any) -> _T: ...
    def bulk_create(
        self, objs: Iterable[_T], batch_size: Optional[int] = ..., ignore_conflicts: bool = ...
    ) -> List[_T]: ...
    def bulk_update(self, objs: Iterable[_T], fields: Sequence[str], batch_size: Optional[int] = ...) -> None: ...
    def get_or_create(self, defaults: Optional[MutableMapping[str, Any]] = ..., **kwargs: Any) -> Tuple[_T, bool]: ...
    def update_or_create(
        self, defaults: Optional[MutableMapping[str, Any]] = ..., **kwargs: Any
    ) -> Tuple[_T, bool]: ...
    def earliest(self, *fields: Any, field_name: Optional[Any] = ...) -> _T: ...
    def latest(self, *fields: Any, field_name: Optional[Any] = ...) -> _T: ...
    def first(self) -> Optional[_T]: ...
    def last(self) -> Optional[_T]: ...
    def in_bulk(self, id_list: Iterable[Any] = ..., *, field_name: str = ...) -> Dict[Any, _T]: ...
    def delete(self) -> Tuple[int, Dict[str, int]]: ...
    def update(self, **kwargs: Any) -> int: ...
    def exists(self) -> bool: ...
    def explain(self, *, format: Optional[Any] = ..., **options: Any) -> str: ...
    def raw(
        self,
        raw_query: str,
        params: Any = ...,
        translations: Optional[Dict[str, str]] = ...,
        using: Optional[str] = ...,
    ) -> RawQuerySet: ...
    # The type of values may be overridden to be more specific in the mypy plugin, depending on the fields param
    def values(self, *fields: Union[str, Combinable], **expressions: Any) -> ValuesQuerySet[_T, Dict[str, Any]]: ...
    # The type of values_list may be overridden to be more specific in the mypy plugin, depending on the fields param
    def values_list(
        self, *fields: Union[str, Combinable], flat: bool = ..., named: bool = ...
    ) -> ValuesQuerySet[_T, Any]: ...
    def dates(self, field_name: str, kind: str, order: str = ...) -> ValuesQuerySet[_T, datetime.date]: ...
    def datetimes(
        self, field_name: str, kind: str, order: str = ..., tzinfo: Optional[datetime.tzinfo] = ...
    ) -> ValuesQuerySet[_T, datetime.datetime]: ...
    def none(self) -> QuerySet[_T]: ...
    def all(self) -> QuerySet[_T]: ...
    def filter(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def exclude(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def complex_filter(self, filter_obj: Any) -> QuerySet[_T]: ...
    def count(self) -> int: ...
    def union(self, *other_qs: Any, all: bool = ...) -> QuerySet[_T]: ...
    def intersection(self, *other_qs: Any) -> QuerySet[_T]: ...
    def difference(self, *other_qs: Any) -> QuerySet[_T]: ...
    def select_for_update(
        self, nowait: bool = ..., skip_locked: bool = ..., of: Sequence[str] = ..., no_key: bool = ...
    ) -> QuerySet[_T]: ...
    def select_related(self, *fields: Any) -> QuerySet[_T]: ...
    def prefetch_related(self, *lookups: Any) -> QuerySet[_T]: ...
    def annotate(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def alias(self, *args: Any, **kwargs: Any) -> QuerySet[_T]: ...
    def order_by(self, *field_names: Any) -> QuerySet[_T]: ...
    def distinct(self, *field_names: Any) -> QuerySet[_T]: ...
    # extra() return type won't be supported any time soon
    def extra(
        self,
        select: Optional[Dict[str, Any]] = ...,
        where: Optional[List[str]] = ...,
        params: Optional[List[Any]] = ...,
        tables: Optional[List[str]] = ...,
        order_by: Optional[Sequence[str]] = ...,
        select_params: Optional[Sequence[Any]] = ...,
    ) -> QuerySet[Any]: ...
    def reverse(self) -> QuerySet[_T]: ...
    def defer(self, *fields: Any) -> QuerySet[_T]: ...
    def only(self, *fields: Any) -> QuerySet[_T]: ...
    def using(self, alias: Optional[str]) -> QuerySet[_T]: ...
    @property
    def ordered(self) -> bool: ...

class Manager(BaseManager[_T]): ...

class RelatedManager(Manager[_T]):
    related_val: Tuple[int, ...]
    def add(self, *objs: Union[_T, int], bulk: bool = ...) -> None: ...
    def remove(self, *objs: Union[_T, int], bulk: bool = ...) -> None: ...
    def set(
        self, objs: Union[QuerySet[_T], Iterable[Union[_T, int]]], *, bulk: bool = ..., clear: bool = ...
    ) -> None: ...
    def clear(self) -> None: ...

class ManagerDescriptor:
    manager: Manager = ...
    def __init__(self, manager: Manager) -> None: ...
    def __get__(self, instance: Optional[Model], cls: Type[Model] = ...) -> Manager: ...

class EmptyManager(Manager):
    def __init__(self, model: Type[Model]) -> None: ...
