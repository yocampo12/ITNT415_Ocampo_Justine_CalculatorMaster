import time

# ===== ANSI COLOR CODES (no extra installs needed) =====
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def get_number(prompt):
    """Validates numeric input; keeps asking until valid."""
    while True:
        value = input(f"{CYAN}{prompt}{RESET}")
        try:
            return float(value)
        except ValueError:
            print(f"{RED}Uy bes, numero lang po. Wag titik. Try ulit!{RESET}")


def show_banner():
    print(f"""{MAGENTA}{BOLD}
   ██████╗ █████╗ ██╗      ██████╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
  ██╔════╝██╔══██╗██║     ██╔════╝    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
  ██║     ███████║██║     ██║         ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
  ██║     ██╔══██║██║     ██║         ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
  ╚██████╗██║  ██║███████╗╚██████╗    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
{RESET}""")
    print(f"{YELLOW}{BOLD}          welcome to the most sosyal calculator sa buong labvm ✨{RESET}\n")


def show_menu():
    print(f"{BLUE}{'═' * 50}{RESET}")
    print(f"{BOLD}            ⚡ CHOOSE YOUR VIBE ⚡{RESET}")
    print(f"{BLUE}{'═' * 50}{RESET}")
    print(f"  {GREEN}[NEVER GROW OLD]{RESET}   ->   Addition")
    print(f"  {GREEN}[KURAKOT]{RESET}          ->   Subtraction")
    print(f"  {GREEN}[MAMAAA]{RESET}           ->    Multiplication")
    print(f"  {GREEN}[KKB]{RESET}              ->   Division")
    print(f"  {RED}[EXIT]{RESET}             ->   Exit")
    print(f"{BLUE}{'═' * 50}{RESET}")


def show_result(label, value):
    print(f"\n{MAGENTA}{'─' * 30}{RESET}")
    print(f"{BOLD}{GREEN}✅ {label}: {value}{RESET}")
    print(f"{MAGENTA}{'─' * 30}{RESET}\n")


def show_error(message):
    print(f"\n{RED}{BOLD}💥 ERROR: {message}{RESET}\n")


def loading_flair(text="Computing"):
    print(f"{YELLOW}{text}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    print(RESET)


def main():
    valid_choices = {
        "NEVER GROW OLD": "add",
        "KURAKOT": "subtract",
        "MAMAAA": "multiply",
        "KKB": "divide",
    }

    show_banner()

    while True:
        show_menu()
        raw_choice = input(f"{BOLD}Ano vibe mo ngayon? (type exactly, case doesn't matter): {RESET}").strip().upper()

        if raw_choice == "EXIT":
            print(f"\n{MAGENTA}{BOLD}GG! Salamat sa pag-compute, Paalam! {RESET}\n")
            break

        if raw_choice not in valid_choices:
            print(f"{RED}Ay mali bes! Sundan mo lang 'yung nasa loob ng [brackets]. Try ulit.{RESET}")
            continue

        operation = valid_choices[raw_choice]
        num1 = get_number("Unang number: ")
        num2 = get_number("Pangalawang number: ")

        loading_flair()

        if operation == "add":
            show_result("Result", add(num1, num2))
        elif operation == "subtract":
            show_result("Result", subtract(num1, num2))
        elif operation == "multiply":
            show_result("Result", multiply(num1, num2))
        elif operation == "divide":
            try:
                show_result("Result", divide(num1, num2))
            except ZeroDivisionError as e:
                show_error(str(e))


if __name__ == "__main__":
    main()

