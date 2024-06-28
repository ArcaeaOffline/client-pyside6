from PySide6.QtGui import QColor


def mixColor(source: QColor, mix: QColor, ratio: float = 0.5):
    r = round((mix.red() - source.red()) * ratio + source.red())
    g = round((mix.green() - source.green()) * ratio + source.green())
    b = round((mix.blue() - source.blue()) * ratio + source.blue())
    a = round((mix.alpha() - source.alpha()) * ratio + source.alpha())

    return QColor(r, g, b, a)
