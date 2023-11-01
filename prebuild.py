import os
import platform
import subprocess
from importlib import metadata
from pathlib import Path


def getGitDesc():
    gitDescribe = subprocess.run(
        ["git", "describe", "--tags", "--long"],
        capture_output=True,
        encoding="utf-8",
    )
    if gitDescribe.returncode == 0:
        return gitDescribe.stdout.replace("\n", "")

    # describe failed, try rev-parse
    gitRevParse = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        capture_output=True,
        encoding="utf-8",
    )
    if gitRevParse.returncode == 0:
        return f"commit {gitRevParse.stdout}".replace("\n", "")

    return "version/commit unknown"


def getBuildToolsVer():
    texts = []
    possibleBuildTools = ["Nuitka", "pyinstaller"]
    for possibleBuildTool in possibleBuildTools:
        try:
            version = metadata.version(possibleBuildTool)
            texts.append(f"{possibleBuildTool}=={version}")
        except metadata.PackageNotFoundError:
            texts.append(f"{possibleBuildTool} not installed")
    return ", ".join(texts)


def writeVersionFile():
    versionFile = Path("ui/resources/VERSION")

    versionText = (
        "arcaea-offline-pyside-ui\n{gitDesc}\n{buildToolsVer}\n\n"
        "{pythonVer}\n\n"
        "{depsVer}\n"
    )

    gitDesc = getGitDesc()
    buildToolsVer = getBuildToolsVer()

    pythonVer = f"{platform.python_implementation()} {platform.python_version()} ({platform.python_build()[0]})"

    importLibTexts = [
        f"{module}=={metadata.version(module)}"
        for module in sorted(
            [
                "arcaea-offline",
                "arcaea-offline-ocr",
                "exif",
                "numpy",
                "opencv-python",
                "Pillow",
                "PySide6",
                "SQLAlchemy",
                "SQLAlchemy-Utils",
                "Whoosh",
            ],
            key=lambda s: s.lower(),
        )
    ]
    importLibText = "\n".join(importLibTexts)

    with versionFile.open("w", encoding="utf-8") as vf:
        vf.write(
            versionText.format(
                gitDesc=gitDesc,
                buildToolsVer=buildToolsVer,
                pythonVer=pythonVer,
                depsVer=importLibText,
            )
        )


writeVersionFile()
