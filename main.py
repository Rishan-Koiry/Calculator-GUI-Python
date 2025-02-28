import tkinter as tk
import pyperclip
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator RK")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.attributes("-fullscreen", False)
        self.expression = ""

        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(self.root, bg="black")
        self.input_frame.pack(expand=True, fill="both")

        self.input_field = tk.Entry(
            self.input_frame,
            textvariable=self.input_text,
            font=("arial", 35, "bold"),
            bd=10,
            insertwidth=4,
            justify="center",
            bg="gray",
            fg="white",
        )
        self.input_field.pack(expand=True, fill="both", ipady=20, padx=10)

        self.buttons_frame = tk.Frame(self.root, bg="black")
        self.buttons_frame.pack(expand=True, fill="both")

        self.create_buttons()

    def create_buttons(self):
        buttons = [
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

        row = 0
        col = 0
        for button in buttons:
            action = lambda x=button: self.click_event(x)
            tk.Button(
                self.buttons_frame,
                text=button,
                width=5,
                height=2,
                font=("arial", 18, "bold"),
                command=action,
                bg="white",
                fg="black",
                relief="raised",
                bd=5,
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
            try:
                result = str(eval(self.expression))
                self.input_text.set(f"={result}")
                self.expression = result
            except:
                self.input_text.set("Calculation Error")
                self.expression = ""
        elif key == "C":
            self.expression = ""
            self.input_text.set("")
        elif key == "AC":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif key == "COPY":
            pyperclip.copy(self.input_text.get())
            self.show_copy_animation()

        else:
            self.expression += str(key)
            self.input_text.set(self.expression)

    def show_copy_animation(self):
        messagebox.showinfo("Copied", "Number copied to clipboard!")
        # self.root.after(50, lambda: self.input_field.config(bg="gray"))


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
