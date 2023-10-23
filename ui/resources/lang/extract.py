import argparse
import subprocess
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument(
    "-no-obsolete",
    action="store_true",
    default=False,
    required=False,
    dest="no_obsolete",
)
args = ap.parse_args(sys.argv[1:])


script_file_path = Path(__file__)

root_dir_path = Path(script_file_path.parent.parent.parent)
output_dir_path = Path(script_file_path.parent)

designer = root_dir_path / "designer"
extends = root_dir_path / "extends"
implements = root_dir_path / "implements"
startup = root_dir_path / "startup"

assert designer.exists()
assert extends.exists()
assert implements.exists()
assert startup.exists()

no_obsolete = args.no_obsolete

commands = [
    [
        "pyside6-lupdate",
        "-extensions",
        "py,ui",
        str(designer.absolute()),
        str(extends.absolute()),
        str(implements.absolute()),
        str(startup.absolute()),
        "-ts",
        str((output_dir_path / "zh_CN.ts").absolute()),
    ],  # zh_CN
    [
        "pyside6-lupdate",
        "-extensions",
        "py,ui",
        str(designer.absolute()),
        str(extends.absolute()),
        str(implements.absolute()),
        str(startup.absolute()),
        "-ts",
        str((output_dir_path / "en_US.ts").absolute()),
    ],  # en_US
]
if no_obsolete:
    commands = [command + ["-no-obsolete"] for command in commands]

for command in commands:
    subprocess.run(command)
