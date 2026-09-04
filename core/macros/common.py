from datetime import datetime

import config
from core.macros.base import BaseMacro


class DateMacro(BaseMacro):
    @property
    def name(self) -> str:
        return "date"

    def execute(self, arg: str) -> str:
        fmt = arg.strip().strip("'\"") or "%d.%m.%Y"
        return datetime.now().strftime(fmt)

class LoremMacro(BaseMacro):
    @property
    def name(self) -> str:
        return "lorem"

    def execute(self, arg: str) -> str:
        try:
            with open(config.RESOURCES_DIR / arg, "r", encoding="utf-8") as f:
                lorem = f.read()
        except FileNotFoundError:
            lorem = "Error: `resources/lorem.md` not found :("

        return lorem
