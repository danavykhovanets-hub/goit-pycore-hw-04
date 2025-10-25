#підключаємо необхідні бібліотеки
import sys
from pathlib import Path
from colorama import Fore, init

#назначаємо кольори для виводу
init(autoreset=True)
def show_dir_structure(path, indent=0):
    for item in path.iterdir():
        if item.is_dir():
            print("  " * indent + Fore.BLUE + f"{item.name}/")
            show_dir_structure(item, indent + 1)
        else:
            print("  " * indent + Fore.GREEN + item.name)

#обробка + помилки

def main():
    if len(sys.argv) < 2:
        directory = Path.cwd()
    else:
        directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + "Такої директорії не існує.")
        return
    if not directory.is_dir():
        print(Fore.RED + "Це не директорія.")
        return

    print(Fore.CYAN + f"\n Вміст директорії: {directory}\n")
    show_dir_structure(directory)

if __name__ == "__main__":
    main()