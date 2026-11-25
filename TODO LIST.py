
import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.geometry("500x550")
        self.root.configure(bg="#f4f4f4")

        self.tasks = []

        title = tk.Label(
            root, text="MY TO-DO LIST",
            font=("Arial", 22, "bold"),
            bg="#f4f4f4", fg="#333"
        )
        title.pack(pady=20)

        self.task_entry = tk.Entry(
            root, font=("Arial", 13), width=30
        )
        self.task_entry.pack(pady=10)

        tk.Button(
            root, text="Add Task",
            command=self.add_task,
            bg="#28a745", fg="white",
            font=("Arial", 11, "bold")
        ).pack(pady=5)

        self.task_list = tk.Listbox(
            root, width=45, height=15,
            font=("Arial", 12),
            selectbackground="#007bff"
        )
        self.task_list.pack(pady=15)

        tk.Button(
            root, text="Mark as Completed",
            command=self.complete_task,
            bg="#007bff", fg="white"
        ).pack(pady=5)

        tk.Button(
            root, text="Delete Task",
            command=self.delete_task,
            bg="#dc3545", fg="white"
        ).pack(pady=5)

        self.load_tasks()
        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()

        if not task:
            messagebox.showwarning(
                "Warning", "Please enter a task!"
            )
            return

        self.tasks.append({
            "task": task,
            "completed": False
        })

        self.task_entry.delete(0, tk.END)
        self.save_tasks()
        self.refresh_tasks()

    def complete_task(self):
        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning", "Select a task first!"
            )
            return

        index = selected[0]
        self.tasks[index]["completed"] = True

        self.save_tasks()
        self.refresh_tasks()

    def delete_task(self):
        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning", "Select a task first!"
            )
            return

        index = selected[0]
        del self.tasks[index]

        self.save_tasks()
        self.refresh_tasks()

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END)

        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            self.task_list.insert(
                tk.END, f"{status} {task['task']}"
            )

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            try:
                with open(FILE_NAME, "r") as file:
                    self.tasks = json.load(file)
            except (json.JSONDecodeError, OSError):
                messagebox.showerror(
                    "Error", "Could not load saved tasks."
                )


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
