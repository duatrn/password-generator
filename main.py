import click
from colorama import Fore, Style
import pyperclip

from passgen import PasswordGenerator

class App():
  @classmethod
  def yes_or_no(cls, questions: str) -> str:
    """
    Generate yes or no question and return the choice
    """
    while True:
      yn = input("[" + Fore.GREEN + "?" + Style.RESET_ALL + "] " + questions + ": (y/n) ").lower()
      if yn != "y" and yn != "n":
        print(Fore.RED + ">> " + Style.RESET_ALL + "Please enter valid 'y' or 'n'")
      else:
        return yn

  @click.command()
  @click.option("--length", "-l", default=8, help="length of passphrase (default: 8)")
  @click.option("--no-number","-nn", "no_number", is_flag=True, help="has no numbers")
  @click.option("--no-symbol","-ns", "no_symbol", is_flag=True, help="has no symbols")
  @click.option("--no-capital","-nc", "no_capital", is_flag=True, help="has no capital letters")
  def run(length, no_number, no_symbol, no_capital) -> None:
    pg = PasswordGenerator()
    if no_number:
      pg.setConfig(hasNumber=False)
    if no_symbol:
      pg.setConfig(hasSymbol=False)
    if no_capital:
      pg.setConfig(hasCapital=False)
    pg.setWordLen(length)
    passphrase = pg.gen()
    print("Password generate: "+ Fore.GREEN + f"{passphrase}" + Style.RESET_ALL)
    
    # want to copy password just generated to clipboard
    choice = App.yes_or_no("Save to clipboard")
    if choice == "y":
      pyperclip.copy(passphrase)
      print("[" + Fore.GREEN + "!" + Style.RESET_ALL + "] Password has been saved to clipboard")
    else:
      print("[" + Fore.RED + "!" + Style.RESET_ALL + "] Password has not been saved to clipboard")
    
if __name__ == "__main__":
  try:
    app = App()
    app.run()
  except Exception as err:
    print(err)