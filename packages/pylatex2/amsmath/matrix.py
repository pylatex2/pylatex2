import typing

import numpy

from .. import base


# TODO move those
# TODO walk the import tree to collect `Preamble`s
class Package(base.BasePackage):
    @property
    def name(self):
        return 'amsmath'

class Preamble(base.BasePreamble):
    @property
    def __children__(self):
        return [
            Package()
        ]


# TODO NOTE this is a special ContainerElement
# TODO NOTE amsmath matrix
# TODO support for tables !!!!
class BaseMatrix(base.BaseEnvironment, base.BaseContainer):
    def __init__(
        self,
        data: typing.Collection,
        name: str = 'matrix'
    ):
        self._data = data
        self._name = name

    @property
    def _name_(self):
        return self._name

    @property
    def __children__(self):
        matrix = numpy.array(
            self._data,
            ndmin=2,
            copy=False
        )
        # NOTE ensure array is 2d
        if not matrix.ndim == 2:
            raise ValueError()
        return matrix

    def __inner_text__(self):
        matrix_s = numpy.vectorize(base.text)(self.__children__)
        return str.join(
            r'\\',
            (str.join(r'&', row)
                for row in matrix_s)
        )

# TODO
class Matrix(BaseMatrix):
    pass

# TODO
__all__ = [
    BaseMatrix,
    Matrix
]