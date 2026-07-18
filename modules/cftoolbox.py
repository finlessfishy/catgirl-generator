import os
import sys



def clear(old=False):
    if old == False:
        try:
            print("\033[2J\033[H", end="")
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

def progress_bar(current, total, bar_length=40):
    percent = current / total
    filled_length = int(bar_length * percent)
    bar = "#" * filled_length + "-" * (bar_length - filled_length)
    return f"\r[{bar}])"

def restart():
    system = platform.system()

    if system == "Windows":
        import subprocess
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit(0)
    elif system in ("Linux", "Darwin"):
        se = sys.executable
        os.execv(se, [se] + sys.argv)
    else:
        raise OSError(f"Unsupported OS: {system}")

def exit(cd=0):
    if str(cd) not in "01":
        print("ERROR")
        return

    if cd == 0:
        sys.exit(0)
    elif cd == 1:
        sys.exit(1)



COLORS = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[0;33m",
    "BLUE": "\033[34m",
    "PINK": "\u001b[38;5;212m",
    "PURPLE": "\033[0;35m",
    "WHITE": "\033[0;37m",
    "CYAN": "\033[0;36m",
    "GRAY": "\033[1;30m",

    "B_YELLOW": "\x1B[1;33m",

    "DARK_GRAY": "\033[38:5:236m",

    "R": "\033[0m"
}