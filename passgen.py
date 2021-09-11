from random import randint
from typing import Dict, Tuple

from utils import Utils

class PasswordGenerator:
  def __init__(self) -> None:
    self._wordLen = 8
    self._config = {"hasNumber": True, "hasSymbol": True, "hasCapital": True}
  
  @property
  def LETTERS(self) -> Tuple:
    return (
      "a", "b", "c", "d", "e", "f", "g", "h", "i" ,"j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    )
  
  @property
  def CAPITALS(self) -> Tuple:
    return (
      "A", "B", "C", "D", "E", "F", "G", "H", "I" ,"J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    )

  @property
  def NUMBERS(self) -> Tuple:
    return ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

  @property
  def SYMBOLS(self) -> Tuple:
    return ("!", "@", "#", "$", "%", "^", "&", "*", ":", "?", "-", "_", "+", "=", "|", "/")

  @property
  def wordLen(self) -> int:
    return self._wordLen

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

  def _validate(self, passphrase: str = ""):
    if passphrase == "": 
      return False

    passphrase = tuple([l for l in passphrase]) # convert string to tuple

    if self._config.get("hasNumber") and not Utils._checkItemInIter1InIter2(passphrase, self.NUMBERS): 
      return False
    if self._config.get("hasSymbol") and not Utils._checkItemInIter1InIter2(passphrase, self.SYMBOLS): 
      return False
    if self._config.get("hasCapital") and not Utils._checkItemInIter1InIter2(passphrase, self.CAPITALS): 
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
    chars = self.LETTERS
    if self._config.get("hasNumber"): 
      chars += self.NUMBERS
    if self._config.get("hasSymbol"): 
      chars += self.SYMBOLS
    if self._config.get("hasCapital"): 
      chars += self.CAPITALS

    # validation
    while True:
      passGen = ""
      for i in range(0, self._wordLen): 
        passGen += chars[randint(0, len(chars)-1)]
      # validate the pass
      if self._validate(passphrase=passGen): 
        break

    return passGen

if __name__ == "__main__":
  pass