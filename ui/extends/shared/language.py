from PySide6.QtCore import QEvent, QLibraryInfo, QLocale, QObject, QTranslator
from PySide6.QtWidgets import QApplication

INSTALLED_TRANSLATORS = []


def changeAppLanguage(
    locale: QLocale,
    fallbackLocale: QLocale = QLocale("en_US"),
):
    app = QApplication.instance()

    for translator in INSTALLED_TRANSLATORS:
        app.removeTranslator(translator)

    translator = QTranslator()
    translatorLoadSuccess = translator.load(locale, "", "", ":/lang/")
    if not translatorLoadSuccess:
        translator.load(fallbackLocale, "", "", ":/lang/")
    qtTranslator = QTranslator()
    qtTranslatorLoadSuccess = qtTranslator.load(
        locale,
        "qt",
        "_",
        QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath),
    )
    if not qtTranslatorLoadSuccess:
        qtTranslator.load(
            fallbackLocale,
            "qt",
            "_",
            QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath),
        )

    app.installTranslator(translator)
    INSTALLED_TRANSLATORS.append(translator)
    app.installTranslator(qtTranslator)
    INSTALLED_TRANSLATORS.append(qtTranslator)


def localeToCode(locale: QLocale):
    code = QLocale.languageToCode(locale.language())
    country = locale.country()
    if country and country != QLocale.Country.AnyCountry:
        code += f"_{QLocale.countryToCode(country)}"
    return code


def localeToFullName(locale: QLocale):
    ret = QLocale.languageToString(locale.language())
    country = locale.country()
    if country and country != QLocale.Country.AnyCountry:
        ret += f" ({QLocale.countryToString(country)})"
    return ret


class LanguageChangeEventFilter(QObject):
    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if (
            event.type() == QEvent.Type.LanguageChange
            and hasattr(watched, "retranslateUi")
            and callable(watched.retranslateUi)
        ):
            watched.retranslateUi(watched)

        return super().eventFilter(watched, event)
