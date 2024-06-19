# TODO matplotlib backend
import matplotlib
import matplotlib.figure

from .. import BaseInlinePGraphics

# TODO BaseDocumentElement
class InlinePGraphics(BaseInlinePGraphics):
    def __init__(
        self,
        data: matplotlib.figure.Figure,
        mpl_options: dict = dict()
    ):
        super().__init__()

        self._data = data
        self._mpl_options = mpl_options

    def __text__(self):
        # TODO context mgmt?
        self._data.savefig(
            self._f_data.name,
            format='pgf',
            **self._mpl_options
        )
        return super().__text__()
