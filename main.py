import click
from colorama import Fore, Style

from passgen import PasswordGenerator

@click.command()
@click.option("--length", "-l", default=8, help="length of passphrase (default: 8)")
@click.option("--no-number","-nn", "no_number", is_flag=True, help="has no numbers")
@click.option("--no-symbol","-ns", "no_symbol", is_flag=True, help="has no symbols")
@click.option("--no-capital","-nc", "no_capital", is_flag=True, help="has no capital letters")
def main(length, no_number, no_symbol, no_capital):
  pg = PasswordGenerator()
  if no_number:
    pg.setConfig(hasNumber=False)
  if no_symbol:
    pg.setConfig(hasSymbol=False)
  if no_capital:
    pg.setConfig(hasCapital=False)
  pg.setWordLen(length)
  passphrase = pg.gen()
  print("Password generate: "+ Fore.GREEN + f"{passphrase}")
  print(Style.RESET_ALL)

if __name__ == "__main__":
  try:
    main()
  except Exception as err:
    print(err)