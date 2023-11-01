import tkinter as tk
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def create_slot_machine_gui():
    def spin():
        nonlocal balance
        nonlocal lines
        nonlocal bet

        # Get the slot machine results
        slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
        canvas.delete("all")  # Clear the canvas

        # Display the slot machine results on the canvas
        for col in range(COLS):
            for row in range(ROWS):
                symbol = slots[col][row]
                canvas.create_text(
                    col * 60 + 30, row * 50 + 25, text=symbol, font=("Helvetica", 24)
                )

        winnings, _ = check_winnings(slots, lines, bet, symbol_value)
        balance += winnings - bet
        update_labels()

    def quit_game():
        window.quit()

    def update_labels():
        balance_label.config(text=f"Balance: ${balance}")
        lines_label.config(text=f"Lines: {lines}")
        bet_label.config(text=f"Bet: ${bet}")

    def change_lines(value):
        nonlocal lines
        lines += value
        if lines < 1:
            lines = 1
        if lines > MAX_LINES:
            lines = MAX_LINES
        update_labels()

    def change_bet(value):
        nonlocal bet
        bet += value
        if bet < MIN_BET:
            bet = MIN_BET
        if bet > MAX_BET:
            bet = MAX_BET
        update_labels()

    window = tk.Tk()
    window.title("Slot Machine")

    balance = 100  # Starting balance
    lines = 1
    bet = 1

    balance_label = tk.Label(window, text=f"Balance: ${balance}")
    lines_label = tk.Label(window, text=f"Lines: {lines}")
    bet_label = tk.Label(window, text=f"Bet: ${bet}")

    spin_button = tk.Button(window, text="Spin", command=spin)
    quit_button = tk.Button(window, text="Quit", command=quit_game)

    canvas = tk.Canvas(window, width=200, height=150)

    lines_increase_button = tk.Button(
        window, text="Increase Lines", command=lambda: change_lines(1)
    )
    lines_decrease_button = tk.Button(
        window, text="Decrease Lines", command=lambda: change_lines(-1)
    )
    bet_increase_button = tk.Button(
        window, text="Increase Bet", command=lambda: change_bet(1)
    )
    bet_decrease_button = tk.Button(
        window, text="Decrease Bet", command=lambda: change_bet(-1)
    )

    balance_label.pack()
    lines_label.pack()
    bet_label.pack()
    spin_button.pack()
    quit_button.pack()
    canvas.pack()
    lines_increase_button.pack()
    lines_decrease_button.pack()
    bet_increase_button.pack()
    bet_decrease_button.pack()

    window.mainloop()

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

create_slot_machine_gui()
