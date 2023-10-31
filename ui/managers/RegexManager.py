from PyQt6 import (
    QtGui, QtCore,
)

class RegexManager:

    __NICKNAME = "^[a-zA-Z0-9_]*$"

    @staticmethod
    def get_regex_nickname_validator() -> QtGui.QRegularExpressionValidator:
        return QtGui.QRegularExpressionValidator(QtCore.QRegularExpression(RegexManager.__NICKNAME))

