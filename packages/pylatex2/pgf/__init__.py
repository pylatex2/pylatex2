# TODO refactor!!!!!!
# TODO sep base w backends!!!!

import os

from .. import base


class Package(base.BasePackage):
    @property
    def name(self):
        return 'pgf'

class Preamble(base.BasePreamble):
    @property
    def __children__(self):
        return [
            Package(),
            base.Package('import')
        ]

class BasePGraphics(base.BaseElement):
    @property
    def path(self) -> str:
        ...

    def __text__(self):
        return (
            rf'\import{{{os.path.dirname(self.path)}}}'
            rf'{{{os.path.basename(self.path)}}}'
        )


import tempfile
# TODO BaseDocumentElement
class BaseInlinePGraphics(BasePGraphics):
    def __init__(self):
        # TODO delete only when garb collected
        self._d_workspace = tempfile.TemporaryDirectory()
        self._f_data = tempfile.NamedTemporaryFile(
            dir=self._d_workspace.name,
            # TODO delete separately
            delete=False
        )

    @property
    def path(self):
        return self._f_data.name



class PGraphics(BasePGraphics):
    pass

class InlinePGraphics(BaseInlinePGraphics):
    pass
