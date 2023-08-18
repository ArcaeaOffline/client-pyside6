import cv2
import numpy as np
from PySide6.QtGui import QImage


def cv2BgrMatToQImage(mat) -> QImage:
    arr = np.ascontiguousarray(mat)
    return QImage(
        arr.data,
        arr.shape[1],
        arr.shape[0],
        arr.strides[0],
        QImage.Format.Format_RGB888,
    ).rgbSwapped()


def qImageToCvMatBgr(qImg: QImage):
    # from Bing AI, references
    # 1: https://stackoverflow.com/q/384759/16484891 | CC BY-SA 4.0
    # 2: https://stackoverflow.com/q/37552924/16484891 | CC BY-SA 3.0
    qImg = qImg.convertToFormat(QImage.Format.Format_RGB888)
    qImg = qImg.copy().rgbSwapped()
    return np.ndarray(
        (qImg.height(), qImg.width(), 3),
        buffer=qImg.constBits(),
        strides=[qImg.bytesPerLine(), 3, 1],
        dtype=np.uint8,
    )
