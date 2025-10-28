import dataclasses
from enum import StrEnum
from pathlib import Path

import structlog
from arcaea_offline.models import (
    CalculatedPotential,
    Chart,
    ConfigBase,
    ScoreBest,
    ScoreCalculated,
    ScoresBase,
    ScoresViewBase,
    SongsBase,
    SongsViewBase,
)
from arcaea_offline.models import (
    Property as AoProperty,
)
from PySide6.QtCore import Property, QObject, QUrl, Signal, Slot
from PySide6.QtQml import QmlElement
from sqlalchemy import inspect, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from core.database import create_engine, db_path_to_sqlite_url, sqlite_url_to_db_path
from core.settings import SettingsKeys, settings
from core.settings.values import GeneralDatabaseType

from .common import VM_QML_IMPORT_NAME

logger: structlog.stdlib.BoundLogger = structlog.get_logger()


QML_IMPORT_NAME = VM_QML_IMPORT_NAME
QML_IMPORT_MAJOR_VERSION = 1
QML_IMPORT_MINOR_VERSION = 0


class _FmwiwsDatabase:
    """Fuck Me Why I Wrote Singleton Database"""

    def __init__(self, url: str):
        self.engine = create_engine(url)

    def init(self, *, checkfirst: bool = True):
        # create tables & views
        if checkfirst:
            # > https://github.com/kvesteri/sqlalchemy-utils/issues/396
            # > view.create_view() causes DuplicateTableError on
            # > Base.metadata.create_all(checkfirst=True)
            # so if `checkfirst` is True, drop these views before creating
            SongsViewBase.metadata.drop_all(self.engine)
            ScoresViewBase.metadata.drop_all(self.engine)

        SongsBase.metadata.create_all(self.engine, checkfirst=checkfirst)
        SongsViewBase.metadata.create_all(self.engine)
        ScoresBase.metadata.create_all(self.engine, checkfirst=checkfirst)
        ScoresViewBase.metadata.create_all(self.engine)
        ConfigBase.metadata.create_all(self.engine, checkfirst=checkfirst)

        version_property = AoProperty(key="version", value="4")
        with Session(self.engine) as session:
            session.merge(version_property)
            session.commit()

    def is_initialized(self):
        expect_tables = (
            list(SongsBase.metadata.tables.keys())
            + list(ScoresBase.metadata.tables.keys())
            + list(ConfigBase.metadata.tables.keys())
            + [
                Chart.__tablename__,
                ScoreCalculated.__tablename__,
                ScoreBest.__tablename__,
                CalculatedPotential.__tablename__,
            ]
        )

        return all(inspect(self.engine).has_table(t) for t in expect_tables)

    def version(self):
        with Session(self.engine) as session:
            stmt = select(AoProperty.value).where(AoProperty.key == "version")
            result = session.scalar(stmt)

            return None if result is None else int(result)


class _UiMode(StrEnum):
    SELECT = "select"
    CREATE = "create"


@dataclasses.dataclass
class DatabaseInfo:
    url: str
    error: Exception | None = None
    initialized: bool | None = None
    version: int | None = None

    @property
    def error_dict(self):
        e = self.error

        if e is None:
            return None

        return {
            "title": e.__class__.__name__,
            "message": str(e),
        }

    def to_qml_dict(self):
        return {
            "url": self.url,
            "error": self.error_dict,
            "initialized": self.initialized,
            "version": self.version,
        }


@QmlElement
class DatabaseInitViewModel(QObject):
    _void = Signal()
    uiModeChanged = Signal()
    selectFileUrlChanged = Signal()
    directoryUrlChanged = Signal()
    filenameChanged = Signal()
    databaseUrlChanged = Signal()
    databaseInfoChanged = Signal()
    canContinueChanged = Signal()
    canConfirmSilentlyChanged = Signal()

    def __init__(self):
        super().__init__()

        self._selectFileUrl: QUrl | None = None
        self._directoryUrl: QUrl = QUrl()
        self._filename: str = ""
        self._databaseInfo: DatabaseInfo | None = None

        self._uiMode = _UiMode.SELECT

        self.directoryUrlChanged.connect(lambda: self.databaseUrlChanged.emit())
        self.filenameChanged.connect(lambda: self.databaseUrlChanged.emit())
        self.selectFileUrlChanged.connect(self.databaseUrlChanged)
        self.databaseInfoChanged.connect(self.canContinueChanged)

        self.databaseUrlChanged.connect(self.onDatabaseUrlChanged)

        self._loadSettings()

    def onDatabaseUrlChanged(self):
        self.loadDatabaseInfo()

    @property
    def _settingsDatabaseFile(self) -> Path | None:
        # TODO: process database type when available
        if (
            settings.stringValue(SettingsKeys.General.DatabaseType)
            != GeneralDatabaseType.FILE
        ):
            return None

        file = settings.stringValue(SettingsKeys.General.DatabaseConn)

        if not file:
            logger.debug("No database file specified in settings")
            return

        filepath = Path(file)
        if not filepath.exists():
            logger.warning("Cannot find database file: %s", file)
            return

        return filepath

    def _loadSettings(self) -> None:
        fileUrl = self._settingsDatabaseFile
        if fileUrl is None:
            return
        logger.info("Loading database from settings: %s", fileUrl)

        self.setUiMode(_UiMode.SELECT)
        self.setSelectFileUrl(fileUrl)
        self.loadDatabaseInfo()

    def _makeDatabaseInfo(self, dbUrl: str):
        info = DatabaseInfo(url=dbUrl)

        path = sqlite_url_to_db_path(dbUrl)
        if not path.exists():
            e = FileNotFoundError()
            e.strerror = f"{path} does not exist"
            info.error = e
            return info

        try:
            db = _FmwiwsDatabase(dbUrl)
            info.initialized = db.is_initialized()
            info.version = db.version()
        except SQLAlchemyError as e:
            logger.exception("Error loading database info")
            info.error = e

        logger.debug("Database info for %r: %r", dbUrl, info)
        return info

    @Slot()
    def loadDatabaseInfo(self):
        dbUrl = self.getDatabaseUrl()
        logger.info("Loading database info: %s", dbUrl)
        if dbUrl is None:
            logger.warning("Database URL is None")
            return

        self._databaseInfo = self._makeDatabaseInfo(dbUrl.toString())
        self.databaseInfoChanged.emit()

    @Slot(str)
    def createFile(self, dbUrl: str):
        file = sqlite_url_to_db_path(dbUrl)

        if file.exists():
            logger.warning(
                "Attempted to create an existing file, check UI logic? (%s)", file
            )
            return

        file.touch(mode=0o644)
        logger.info("Created file %s", file)

    @Slot()
    def confirmCurrentConnection(self):
        dbInfo = self._databaseInfo
        if dbInfo is None:
            logger.warning("Current database info is None, ignoring")
            return

        settings.setValue(
            SettingsKeys.General.DatabaseType,
            GeneralDatabaseType.FILE.value,
        )
        settings.setValue(
            SettingsKeys.General.DatabaseConn,
            str(sqlite_url_to_db_path(dbInfo.url).resolve().as_posix()),
        )

    @Slot(str)
    def initialize(self, dbUrl: str):
        try:
            db = _FmwiwsDatabase(dbUrl)
            db.init()
        except SQLAlchemyError:
            logger.exception("Error initializing database %s", dbUrl)

    # region properties
    def getUiMode(self):
        return self._uiMode.value

    def setUiMode(self, mode: str | _UiMode):
        if isinstance(mode, _UiMode):
            self._uiMode = mode
        elif isinstance(mode, str):
            try:
                self._uiMode = _UiMode(mode)
            except ValueError:
                logger.warning("Invalid UI mode: %s", mode)

        self.uiModeChanged.emit()

    def getSelectFileUrl(self):
        return self._selectFileUrl

    def setSelectFileUrl(self, value: Path | QUrl | None):
        if isinstance(value, Path):
            value = QUrl.fromLocalFile(value.as_posix())

        self._selectFileUrl = value
        self.selectFileUrlChanged.emit()

    def getDirectoryUrl(self):
        return self._directoryUrl

    def setDirectoryUrl(self, value: QUrl | None):
        self._directoryUrl = value or QUrl()
        self.directoryUrlChanged.emit()

    def getFilename(self):
        return self._filename

    def setFilename(self, value: str | None):
        self._filename = value or ""
        self.filenameChanged.emit()

    def getDatabaseUrl(self):
        if self._uiMode == _UiMode.SELECT:
            fileUrl = self.getSelectFileUrl()
            if fileUrl is None:
                return None
            return db_path_to_sqlite_url(Path(fileUrl.toLocalFile()))

        directoryUrl = self.getDirectoryUrl()
        filename = self.getFilename()

        databasePath = Path(directoryUrl.toLocalFile()) / filename
        databaseUrl = db_path_to_sqlite_url(databasePath)

        return databaseUrl

    def getDatabaseInfo(self):
        if self._databaseInfo is None:
            return {
                "url": "",
                "initialized": None,
                "version": None,
                "error": None,
            }

        return self._databaseInfo.to_qml_dict()

    def getCanContinue(self):
        return (
            self._databaseInfo is not None
            and self._databaseInfo.error is None
            and self._databaseInfo.version == 4  # noqa: PLR2004
            and self._databaseInfo.initialized
        )

    def getCanConfirmSilently(self):
        """Whether the user can confirm database connection without a dialog popping up"""
        if self.getUiMode() != _UiMode.SELECT:
            return False

        filepath = self._settingsDatabaseFile
        if filepath is None:
            return False

        return (
            self._databaseInfo is not None
            and self._databaseInfo.error is None
            and self.getDatabaseUrl() == db_path_to_sqlite_url(filepath)
        )

    uiMode = Property(str, getUiMode, setUiMode, notify=uiModeChanged)
    selectFileUrl = Property(
        QUrl,
        getSelectFileUrl,
        setSelectFileUrl,
        notify=selectFileUrlChanged,
    )
    directoryUrl = Property(
        QUrl,
        getDirectoryUrl,
        setDirectoryUrl,
        notify=directoryUrlChanged,
    )
    filename = Property(str, getFilename, setFilename, notify=filenameChanged)
    databaseUrl = Property(QUrl, getDatabaseUrl, None, notify=databaseUrlChanged)
    databaseInfo = Property(dict, getDatabaseInfo, None, notify=databaseInfoChanged)
    canContinue = Property(bool, getCanContinue, None, notify=canContinueChanged)
    canConfirmSilently = Property(
        bool,
        getCanConfirmSilently,
        None,
        notify=canConfirmSilentlyChanged,
    )
    # endregion
