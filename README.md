# Arcaea Offline PySide UI

GUI for both [283375/arcaea-offline](https://github.com/283375/arcaea-offline) and [ArcaeaOffline/core-ocr](https://github.com/ArcaeaOffline/core-ocr).

## Prerequisites

* Install requirements
* Release translation files from `ui/resources/lang/*.ts`
* Run `prebuild.py`
* Compile `ui/resources/resources.qrc` to `ui/resources/resources_rc.py`

You can refer to the [GitHub Actions file](./.github/workflows/build.yml) for a rough reference.

```
pip install -r ./requirements.txt
pyside6-lrelease ./ui/resources/lang/en_US.ts ./ui/resources/lang/zh_CN.ts
python prebuild.py
pyside6-rcc ./ui/resources/resources.qrc -o ./ui/resources/resources_rc.py
```

Sometimes you have to install the latest, unpublished version of `arcaea-offline` and `arcaea-offline-ocr`.

```
pip uninstall -y arcaea-offline arcaea-offline-ocr
pip install git+https://github.com/283375/arcaea-offline
pip install git+https://github.com/ArcaeaOffline/core-ocr
```
