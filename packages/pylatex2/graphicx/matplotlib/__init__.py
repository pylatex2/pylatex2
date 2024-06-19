import matplotlib.image
from .. import BaseInlineGraphics

class InlineGraphics(BaseInlineGraphics):
    # TODO backend
    # TODO ext is mandatory!!!!!
    @classmethod
    def from_array(cls, arr, ext=None, **kwargs):
        # TODO image export backend!!!!!

        o = cls(ext=ext, **kwargs)
        if arr is not None:
            matplotlib.image.imsave(o._file.name, arr)
        return o
