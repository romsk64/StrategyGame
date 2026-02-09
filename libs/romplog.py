# Romsk Python Log Library v0.1
# Распространяется по лицензии MIT
# romsk64, 2025-2026
# Русская документация по пути ../docs/ru-doc.md

from datetime import date

class Logger:
    def __init__(self, logdir: str, toconsole: bool = True, tofile: bool = False):
        self.logdir = logdir
        self.toconsole = toconsole
        self.tofile = tofile

        self.levels = {
            10: "DEBUG",
            20: "INFO",
            30: "WARNING",
            40: "ERROR",
            50: "CRITICAL ERROR"
        }
    def baseconfig(self, debug = 10, info = 20, warning = 30, error = 40, criterror = 50):
        self.levels.clear()
        self.levels[debug] = "DEBUG"
        self.levels[info] = "INFO"
        self.levels[warning] = "WARNING"
        self.levels[error] = "ERROR"
        self.levels[criterror] = "CRITICAL ERROR"
    def log(self, level: int, message: str, method: str):
        if self.toconsole:
            print(f"")