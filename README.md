# Arcaea Offline PySide UI (Archived)

## What happened?

To be honest, I no longer have the energy to maintain both clients (the other one being [ArcaeaOffline/client-android](https://github.com/ArcaeaOffline/client-android) as of this writing) **on my own**. So I'm archiving this one, since ***I don't really have any fond memories of writing Qt for Python***.

## Is this project abandoned?

Yes and no. This client, based on PySide6, is abandoned...

...but the Android one is not. And this doesn't mean there won't be any PC clients in the future: I've seen the potential of [Compose Multiplatform](https://kotlinlang.org/compose-multiplatform/), and an [experimental project](https://github.com/SeviveOSS/pdf-im-ex-mp) proved to be quite successful. So if everything goes smoothly, the *client-android* will eventually become *client-multiplatform*, which will bring a very beautiful Kotlin + Compose development experience and a single codebase for Windows, Linux and Android - we'll see if it becomes a reality.

Stay tuned.

*Below is the original README of this project:*

---

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
