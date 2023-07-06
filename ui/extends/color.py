from PySide6.QtGui import QColor


def mix_color(source_color: QColor, mix_color: QColor, mix_ratio: float = 0.5):
    r = round((mix_color.red() - source_color.red()) * mix_ratio + source_color.red())
    g = round(
        (mix_color.green() - source_color.green()) * mix_ratio + source_color.green()
    )
    b = round(
        (mix_color.blue() - source_color.blue()) * mix_ratio + source_color.blue()
    )
    a = round(
        (mix_color.alpha() - source_color.alpha()) * mix_ratio + source_color.alpha()
    )

    return QColor(r, g, b, a)
