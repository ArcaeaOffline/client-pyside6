from dataclasses import dataclass
from typing import Optional

from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon, QPixmap


@dataclass
class NavItem:
    id: str
    icon: Optional[QIcon | QPixmap | str] = None

    def text(self):
        return QCoreApplication.translate("NavItem", f"{self.id}.title")
