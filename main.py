import tkinter as tk
import pyperclip
from tkinter import messagebox


class Calculator:
    BUTTONS = [
        "7",
        "8",
        "9",
        "/",
        "4",
        "5",
        "6",
        "*",
        "1",
        "2",
        "3",
        "-",
        ".",
        "0",
        "=",
        "+",
        "C",
        "AC",
        "COPY",
        "%",
    ]
    BUTTON_PROPERTIES = {
        "width": 5,
        "height": 2,
        "font": ("arial", 18, "bold"),
        "bg": "white",
        "fg": "black",
        "relief": "raised",
        "bd": 5,
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Calculator RK")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.expression = ""

        self.input_text = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.create_input_frame()
        self.create_buttons_frame()
        self.create_buttons()

    def create_input_frame(self):
        input_frame = tk.Frame(self.root, bg="black")
        input_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=("arial", 35, "bold"),
            bd=10,
            insertwidth=4,
            justify="center",
            bg="gray",
            fg="white",
        )
        input_field.pack(expand=True, fill="both", ipady=20, padx=10)

    def create_buttons_frame(self):
        self.buttons_frame = tk.Frame(self.root, bg="black")
        self.buttons_frame.pack(expand=True, fill="both")

    def create_buttons(self):
        row, col = 0, 0
        for button in self.BUTTONS:
            action = lambda x=button: self.click_event(x)
            tk.Button(
                self.buttons_frame,
                text=button,
                command=action,
                **self.BUTTON_PROPERTIES,
            ).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(4):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

    def click_event(self, key):
        if key == "=":
            self.calculate_result()
        elif key == "C":
            self.clear_expression()
        elif key == "AC":
            self.delete_last_character()
        elif key == "COPY":
            self.copy_to_clipboard()
        else:
            self.update_expression(key)

    def calculate_result(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(f"={result}")
            self.expression = result
        except:
            self.input_text.set("Calculation Error")
            self.expression = ""

    def clear_expression(self):
        self.expression = ""
        self.input_text.set("")

    def delete_last_character(self):
        self.expression = self.expression[:-1]
        self.input_text.set(self.expression)

    def copy_to_clipboard(self):
        pyperclip.copy(self.input_text.get())
        messagebox.showinfo("Copied", "Number copied to clipboard!")

    def update_expression(self, key):
        self.expression += str(key)
        self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
