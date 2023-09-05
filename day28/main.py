from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Break.", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 1:
        timer_label.config(text="Work!", fg=GREEN)
        count_down(WORK_MIN * 60)
    else:
        timer_label.config(text="Break.", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    count_text = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark_text = ""
        for _ in range(math.floor(reps/2)):
            checkmark_text += CHECKMARK
            checkmark_label.config(text=checkmark_text)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# Labels
timer_label = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 80), bg=YELLOW)
timer_label.grid(column=1, row=0)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

# Buttons
start_button = Button(font=(FONT_NAME, 10), text="Start", bg=PINK, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(font=(FONT_NAME, 10), text="Reset", bg=PINK, command=reset_timer)
reset_button.grid(column=2, row=2)


window.mainloop()