from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5D9C59"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=YELLOW)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

label1=Label()
label1.config(text="Timer", font=("Times New Roman", 30, "bold"), bg=YELLOW, fg=GREEN)
label1.grid(column=1, row=0)

start_butt=Button(text="Start")
start_butt.grid(column=0, row=2)

reset_butt=Button(text="Reset")
reset_butt.grid(column=2, row=2)

checkmarks=Label(text="✔", bg= YELLOW, fg=GREEN, font=(FONT_NAME, 14))
checkmarks.grid(column=1, row=3)

window.mainloop()
