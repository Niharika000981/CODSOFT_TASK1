import tkinter as tk
from tkinter import ttk

tasks = []
selected_index = None

# ---------- FUNCTIONS ---------- #

def add_task():
    task = entry.get().strip()

    if task == "":
        return

    tasks.append({"task": task, "status": "Pending"})
    entry.delete(0, tk.END)

    update_table()


def mark_done(index):
    tasks[index]["status"] = "Done"
    update_table()


def delete_task(index):
    tasks.pop(index)
    update_table()


def select_task(index):
    global selected_index

    selected_index = index
    entry.delete(0, tk.END)
    entry.insert(0, tasks[index]["task"])


def update_task():
    global selected_index

    if selected_index is None:
        return

    new_task = entry.get().strip()

    if new_task == "":
        return

    tasks[selected_index]["task"] = new_task
    entry.delete(0, tk.END)

    selected_index = None
    update_table()


def update_table():

    for widget in table_frame.winfo_children():
        widget.destroy()

    headers = ["#", "Tasks", "Status", "Action"]

    for col, text in enumerate(headers):
        label = tk.Label(
            table_frame,
            text=text,
            font=("Courier", 18, "bold"),
            bg="#e6e6e6"
        )
        label.grid(row=0, column=col, padx=40, pady=10)

    for i, task in enumerate(tasks):

        num = tk.Label(table_frame, text=i+1, font=("Courier", 14), bg="#e6e6e6")
        num.grid(row=i+1, column=0)

        task_label = tk.Label(table_frame, text=task["task"], font=("Courier", 14), bg="#e6e6e6")
        task_label.grid(row=i+1, column=1)
        task_label.bind("<Button-1>", lambda e, x=i: select_task(x))

        status = tk.Label(table_frame, text=task["status"], font=("Courier", 14), bg="#e6e6e6")
        status.grid(row=i+1, column=2)

        action_frame = tk.Frame(table_frame, bg="#e6e6e6")
        action_frame.grid(row=i+1, column=3)

        done_btn = tk.Button(
            action_frame,
            text="✔",
            font=("Arial", 14, "bold"),
            fg="green",
            bd=0,
            command=lambda x=i: mark_done(x)
        )
        done_btn.pack(side="left", padx=8)

        delete_btn = tk.Button(
            action_frame,
            text="✖",
            font=("Arial", 14, "bold"),
            fg="red",
            bd=0,
            command=lambda x=i: delete_task(x)
        )
        delete_btn.pack(side="left")


# ---------- WINDOW ---------- #

root = tk.Tk()
root.title("ToDo App")
root.geometry("900x550")
root.configure(bg="#708c2c")

# ---------- STYLE (Fix Mac faded buttons) ---------- #

style = ttk.Style()
style.theme_use("clam")

style.configure("Green.TButton",
                background="#1e5b0f",
                foreground="white",
                font=("Courier", 13, "bold"),
                padding=8)

style.map("Green.TButton",
          background=[("active", "#2f7d17")])

# ---------- HEADER ---------- #

header = tk.Frame(root, bg="#1e5b0f", height=80)
header.pack(fill="x")

title = tk.Label(
    header,
    text="ToDo  App",
    font=("Courier", 30, "bold"),
    fg="white",
    bg="#1e5b0f"
)
title.pack(pady=15)

# ---------- INPUT AREA ---------- #

input_frame = tk.Frame(root, bg="#708c2c")
input_frame.pack(pady=30)

entry = tk.Entry(input_frame, font=("Courier", 16), width=35)
entry.grid(row=0, column=0, padx=10, ipady=8)

add_btn = ttk.Button(input_frame, text="Add Task", style="Green.TButton", command=add_task)
add_btn.grid(row=0, column=1, padx=10)

update_btn = ttk.Button(input_frame, text="Update Task", style="Green.TButton", command=update_task)
update_btn.grid(row=0, column=2)

# ---------- TABLE ---------- #

table_frame = tk.Frame(root, bg="#e6e6e6")
table_frame.pack(padx=60, pady=20, fill="both")

update_table()

# ---------- RUN ---------- #

root.mainloop()