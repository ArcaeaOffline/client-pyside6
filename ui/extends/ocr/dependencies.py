import cv2
from arcaea_offline_ocr.phash_db import ImagePhashDatabase


def getCv2StatModelStatusText(model: cv2.ml.StatModel):
    if not isinstance(model, cv2.ml.StatModel):
        return '<font color="red">ERROR</font>'

    varCount = model.getVarCount()
    if varCount != 81:
        return f'<font color="darkorange">WARN</font>, varCount {varCount}'
    else:
        return f'<font color="green">OK</font>, varCount {varCount}'


def getPhashDatabaseStatusText(db: ImagePhashDatabase):
    if not isinstance(db, ImagePhashDatabase):
        return '<font color="red">ERROR</font>'

    jacketCount = len(db.jacket_hashes)
    partnerIconCount = len(db.partner_icon_hashes)

    statusText = f"J{jacketCount} PI{partnerIconCount}"

    if partnerIconCount <= 0:
        return f'<font color="darkorange">WARN</font>, {statusText}'
    else:
        return f'<font color="green">OK</font>, {statusText}'
