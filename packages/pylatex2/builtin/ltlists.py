from .. import base

import typing



class BaseItem(base.BaseElement):
    @property
    def _label_(self) -> base.BaseElement:
        raise NotImplementedError

    @property
    def _content_(self) -> base.BaseElement:
        raise NotImplementedError

    def __text__(self):
        # TODO
        label, content = self._label_, self._content_
        return (
            r'\item'
            + (rf'[{base.text(label)}]'
                if not base.isnothing(label) else '')
            + (rf'{{{base.text(content)}}}'
                if not base.isnothing(content) else '')
        )

class BaseItemList(base.BaseEnvironment, base.BaseContainer):
    _item_type_: typing.Type[BaseItem] = BaseItem

    @property
    def __children__(self) -> typing.List[_item_type_]:
        raise NotImplementedError

    def __inner_text__(self):
        return str.join(
            '',
            (base.text(c)
                for c in self.__children__)
        )




import dataclasses


@dataclasses.dataclass
class Item(BaseItem):
    label: base.BaseElement = base.Nothing
    content: base.BaseElement = base.Nothing

    @property
    def _label_(self):
        return self.label

    @property
    def _content_(self):
        return self.content

# TODO Metaclass environment !!!!!!
class ItemList(BaseItemList):
    _item_type_ = Item

    @classmethod
    def from_iterable(cls, data: typing.Iterable):
        return cls(
            data=[
                cls._item_type_(content=value)
                for value in data
            ]
        )

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data=[
                cls._item_type_(label=key, content=value)
                for key, value in data.items()
            ]
        )

    def __init__(self, data):
        self._data = data

    @property
    def __children__(self):
        return self._data


class Description(ItemList):
    @property
    def _name_(self):
        return 'description'

class Itemize(ItemList):
    @property
    def _name_(self):
        return 'itemize'
