import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x150")
        
        self.equation = tk.StringVar()
        self.create_widgets()
        self.display.bind("<Return>", self.on_enter)

    def create_widgets(self):
        # Display field for the equation
        self.display = tk.Entry(self, textvariable=self.equation, font=('Arial', 24), borderwidth=3, relief="ridge")
        self.display.grid(row=0, column=0, columnspan=6, pady=2, padx=2)
        
        # Operator buttons
        buttons = [
            {'text': '+', 'row': 2, 'column': 0},
            {'text': '-', 'row': 2, 'column': 1},
            {'text': '*', 'row': 2, 'column': 2},
            {'text': '/', 'row': 2, 'column': 3},
            {'text': 'C', 'row': 2, 'column': 4},
            {'text': '=', 'row': 2, 'column': 5}
        ]
        
        for button in buttons:
            self.create_button(button)
        
        # Result textbox
        self.result_textbox = tk.Text(self, height=1, width=24, font=('Arial', 24), borderwidth=3, relief="ridge")
        self.result_textbox.grid(row=1, column=0, columnspan=6, pady=5, padx=5)
    
    def create_button(self, button):
        action = lambda text=button['text']: self.on_button_click(text)
        b = tk.Button(self, text=button['text'], font=('Arial', 18), command=action)
        b.grid(row=button['row'], column=button['column'], sticky="nsew", padx=2, pady=2, columnspan=button.get('columnspan', 1))
        
        # Make the buttons expand when the window is resized
        self.grid_rowconfigure(button['row'], weight=1)
        self.grid_columnconfigure(button['column'], weight=1)
    
    def on_enter(self, event):
        try:
            result = eval(self.equation.get())
            self.result_textbox.delete(1.0, tk.END)
            self.result_textbox.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
    
    def on_button_click(self, char):
        if char == 'C':
            self.equation.set("")
            self.result_textbox.delete(1.0, tk.END)
        elif char == '=':
            try:
                result = eval(self.equation.get())
                self.result_textbox.delete(1.0, tk.END)
                self.result_textbox.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        else:
            self.equation.set(self.equation.get() + char)
            
if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
