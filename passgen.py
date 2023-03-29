import string
from random import randint
from typing import Dict


class PasswordGenerator:
    def __init__(self) -> None:
        self._wordLen = 8
        self._config = {"hasNumber": True,
                        "hasSymbol": True, "hasCapital": True}

    def setWordLen(self, val: int) -> None:
        if val < 8:
            raise ValueError("Error: wordLen must be more than or equal to 8")
        if not isinstance(val, int):
            raise ValueError("Error: wordLen must be integer")
        self._wordLen = val

    @property
    def config(self) -> Dict:
        return self._config

    def setConfig(self, hasNumber: bool = True, hasSymbol: bool = True, hasCapital: bool = True) -> Dict:
        if not isinstance(hasNumber, bool) or not isinstance(hasSymbol, bool) or not isinstance(hasCapital, bool):
            raise TypeError("Error: nn, ns, nc must be boolean")
        if not hasNumber:
            self._config["hasNumber"] = hasNumber
        if not hasSymbol:
            self._config["hasSymbol"] = hasSymbol
        if not hasCapital:
            self._config["hasCapital"] = hasCapital

    def _validate(self, passphrase: str = "") -> bool:
        if passphrase == "":  # check empty passphrase
            return False

        def _check(p, l):  # support function to check intersection between 2 strings
            return False if len({p}.intersection({l})) == 0 else True

        # check passphrase has lowercase (at least 1)
        if _check(passphrase, string.ascii_lowercase):
            return False

        # check passphrase has number (at least 1)
        if self._config.get("hasNumber") and _check(passphrase, string.digits):
            return False

        # check passphrase has symbol (at least 1)
        if self._config.get("hasSymbol") and _check(passphrase, string.punctuation):
            return False

        # check passphrase has uppercase (at least 1)
        if self._config.get("hasCapital") and _check(passphrase, string.ascii_uppercase):
            return False

        return True

    def gen(self) -> str:
        """
            Generate a passphrase as a string with default configuration
            - Length 8
            - At least 1 capital letter
            - At least 1 symbol
            - At least 1 number
        """

        # configuration
        chars = string.ascii_lowercase
        if self._config.get("hasNumber"):
            chars += string.digits
        if self._config.get("hasSymbol"):
            chars += string.punctuation
        if self._config.get("hasCapital"):
            chars += string.ascii_uppercase

        # validation
        while True:
            passGen = ""
            for i in range(0, self._wordLen):
                passGen += chars[randint(0, len(chars)-1)]
            # validate the pass
            if self._validate(passphrase=passGen):
                break

        return passGen
