import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Initialize tasks list
        self.tasks = []

        # Create GUI elements
        self.task_input = tk.Entry(self.root, width=50)
        self.task_input.grid(row=0, column=0, padx=10, pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, height=15, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_tasks_button = tk.Button(self.root, text="Clear All Tasks", command=self.clear_tasks)
        self.clear_tasks_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def clear_tasks(self):
        self.tasks = []
        self.task_listbox.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
