import os
from importlib import metadata
from pathlib import Path

# fill VERSION file
versionFile = Path("ui/resources/VERSION")
assert versionFile.exists()

versionTexts = []

projectVersionText = "arcaea-offline-pyside-ui\n"
gitDescribe = os.popen("git describe --tags --long")
gitDescribeContent = gitDescribe.read().replace("\n", "")
if gitDescribe.close() is None:
    projectVersionText += f"{gitDescribeContent}"
else:
    gitRevParse = os.popen("git rev-parse --short HEAD")
    gitRevParseContent = gitRevParse.read().replace("\n", "")
    projectVersionText += f"commit {gitRevParseContent}"
    gitRevParse.close()
projectVersionText += "\n"

versionTexts.append(projectVersionText)


# detect pip
pipName = None
possiblePipNames = ["pip3", "pip"]
for possiblePipName in possiblePipNames:
    result = os.popen(possiblePipName).read()
    if (
        "<command> [options]" in result
        and "install" in result
        and "--upgrade" in result
    ):
        pipName = possiblePipName
        break


# if possiblePipName:
#     pipFreezeLines = os.popen(f"{possiblePipName} freeze").read().split("\n")
#     text = [
#         pipFreezeResult
#         for pipFreezeResult in pipFreezeLines
#         if (
#             "arcaea-offline" in pipFreezeResult
#             or "PySide6" in pipFreezeResult
#             or "exif" in pipFreezeResult
#             or "opencv-python" in pipFreezeResult
#             or "SQLAlchemy" in pipFreezeResult
#         )
#     ]
#     versionTexts.append("\n".join(text))

importLibTexts = [
    f"{module}=={metadata.version(module)}"
    for module in [
        "arcaea-offline",
        "arcaea-offline-ocr",
        "exif",
        "opencv-python",
        "PySide6",
        "SQLAlchemy",
        "SQLAlchemy-Utils",
    ]
]
versionTexts.append("\n".join(importLibTexts))

with versionFile.open("w", encoding="utf-8") as vf:
    vf.write("\n".join(versionTexts))
