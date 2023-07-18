from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#22A699"
YELLOW = "#F3E99F"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPEAT = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(keep_time_text, text="00:00")
    number_of_rounds.config(text="")
    global REPEAT
    REPEAT = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_time():
    global REPEAT
    REPEAT += 1
    if REPEAT % 8 == 0:
        count_time(LONG_BREAK_MIN*60)
        timer_label.config(text="Break", fg=RED)
        REPEAT = 0
        number_of_rounds.config(text="✔")
    elif REPEAT % 2 == 1:
        count_time(WORK_MIN*60)
        timer_label.config(text="Work", fg=GREEN)
    else:
        count_time(SHORT_BREAK_MIN*60)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_time(time):
    time_minutes = math.floor(time/60)
    if time_minutes < 10:
        time_minutes = f"0{time_minutes}"
    time_seconds = time % 60
    if time_seconds < 10:
        time_seconds = str("0" + str(time_seconds))
    else:
        time_seconds = time_seconds
    canvas.itemconfig(keep_time_text, text=f"{time_minutes}:{time_seconds}")
    if time > 0:
        global timer
        timer = window.after(1000, count_time, time-1)
    else:
        start_time()
        mark = ""
        work_round = math.floor(REPEAT/2)
        for _ in range(work_round):
            mark += "✔"
        number_of_rounds.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodor")
window.config(padx=50, pady=50, bg=YELLOW)
window.iconbitmap("tomato_icon.ico")
canvas = Canvas(width=224, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(112, 112, image=photo)
keep_time_text = canvas.create_text(120, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
timer_label.grid(column=2, row=1)
start_button = Button(text="start", command=start_time)
start_button.grid(column=1, row=3)
number_of_rounds = Label(fg=GREEN, bg=YELLOW)
number_of_rounds.grid(column=2, row=4)
reset_button = Button(text="reset", command=reset)
reset_button.grid(column=3, row=3)
window.mainloop()