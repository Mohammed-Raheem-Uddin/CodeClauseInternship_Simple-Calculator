import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x350")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # Display frame
        input_frame = tk.Frame(self.root, width=400, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # Create a display
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, bg="white", fg="black", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=23, fill=tk.BOTH)

        # Buttons frame
        btns_frame = tk.Frame(self.root, width=400, height=450, bg="white")
        btns_frame.pack(fill=tk.BOTH)

        # Colors
        btn_color = "black"
        op_color = "#ff9500"
        text_color = "white"

        # First row
        clear = tk.Button(btns_frame, text="C", fg=text_color, width=32, height=3, bd=0, bg=op_color, cursor="hand2", command=self.clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky="nsew")
        divide = tk.Button(btns_frame, text="/", fg=text_color, width=10, height=3, bd=0, bg=op_color, cursor="hand2", command=lambda: self.click("/")).grid(row=0, column=3, padx=1, pady=1, sticky="nsew")

        # Second row
        seven = tk.Button(btns_frame, text="7", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(7)).grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
        eight = tk.Button(btns_frame, text="8", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(8)).grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
        nine = tk.Button(btns_frame, text="9", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(9)).grid(row=1, column=2, padx=1, pady=1, sticky="nsew")
        multiply = tk.Button(btns_frame, text="*", fg=text_color, width=10, height=3, bd=0, bg=op_color, cursor="hand2", command=lambda: self.click("*")).grid(row=1, column=3, padx=1, pady=1, sticky="nsew")

        # Third row
        four = tk.Button(btns_frame, text="4", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(4)).grid(row=2, column=0, padx=1, pady=1, sticky="nsew")
        five = tk.Button(btns_frame, text="5", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(5)).grid(row=2, column=1, padx=1, pady=1, sticky="nsew")
        six = tk.Button(btns_frame, text="6", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(6)).grid(row=2, column=2, padx=1, pady=1, sticky="nsew")
        subtract = tk.Button(btns_frame, text="-", fg=text_color, width=10, height=3, bd=0, bg=op_color, cursor="hand2", command=lambda: self.click("-")).grid(row=2, column=3, padx=1, pady=1, sticky="nsew")

        # Fourth row
        one = tk.Button(btns_frame, text="1", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(1)).grid(row=3, column=0, padx=1, pady=1, sticky="nsew")
        two = tk.Button(btns_frame, text="2", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(2)).grid(row=3, column=1, padx=1, pady=1, sticky="nsew")
        three = tk.Button(btns_frame, text="3", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(3)).grid(row=3, column=2, padx=1, pady=1, sticky="nsew")
        add = tk.Button(btns_frame, text="+", fg=text_color, width=10, height=3, bd=0, bg=op_color, cursor="hand2", command=lambda: self.click("+")).grid(row=3, column=3, padx=1, pady=1, sticky="nsew")

        # Fifth row
        zero = tk.Button(btns_frame, text="0", fg=text_color, width=21, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1, sticky="nsew")
        point = tk.Button(btns_frame, text=".", fg=text_color, width=10, height=3, bd=0, bg=btn_color, cursor="hand2", command=lambda: self.click(".")).grid(row=4, column=2, padx=1, pady=1, sticky="nsew")
        equals = tk.Button(btns_frame, text="=", fg=text_color, width=10, height=3, bd=0, bg=op_color, cursor="hand2", command=self.equal).grid(row=4, column=3, padx=1, pady=1, sticky="nsew")

        # Configure rows and columns to expand with window
        for i in range(5):
            btns_frame.grid_rowconfigure(i, weight=1)
            for j in range(4):
                btns_frame.grid_columnconfigure(j, weight=1)

    def click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = ""
        except:
            messagebox.showerror("Error", "Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
