import abc


class BaseNothingType(abc.ABC):
    pass

class NothingType(BaseNothingType):
    pass
Nothing = NothingType()

isnothing = lambda x: isinstance(x, BaseNothingType)


class BaseContainer(abc.ABC):
    @property
    def __children__(self):
        ...



# TODO NOTE BaseElement or str
class BaseElement(abc.ABC):
    def __text__(self) -> str:
        ...

def text(data: str | BaseElement):
    return (
        data.__text__()
        if isinstance(data, BaseElement)
        else
        str(data)
    )


# TODO ipython addon
BaseElement._repr_latex_ = lambda self: self.text

# TODO __str__ addon!!
# BaseElement.__str__ = lambda self: self.text

# TODO name
class BaseContainerElement(BaseContainer, BaseElement):
    def __text__(self):
        return str.join('', map(text, self.__children__))


# TODO Metaclass???
# TODO .children
class BaseEnvironment(BaseElement):
    @property
    def _name_(self) -> str:
        raise NotImplementedError

    def __inner_text__(self) -> str:
        raise NotImplementedError

    def __text__(self) -> str:
        # TODO options !!!!
        return (
            rf'\begin{{{self._name_}}}'
            rf'{self.__inner_text__()}'
            rf'\end{{{self._name_}}}'
        )

class BasePackage(BaseElement):
    @property
    def name(self) -> str:
        raise NotImplementedError

    def __text__(self):
        return rf'\usepackage{{{self.name}}}'

class Package(BasePackage):
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

# TODO
class BaseDocument(BaseEnvironment):
    pass

# TODO
class BasePreamble(BaseContainerElement):
    pass