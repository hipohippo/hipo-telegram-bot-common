from configparser import ConfigParser, SectionProxy
from pathlib import Path
from typing import Union


def parse_from_ini(ini_file: Union[str, Path]) -> SectionProxy:
    ini_parser = ConfigParser()
    ini_parser.read(ini_file, encoding="utf-8")
    return ini_parser["main"]
