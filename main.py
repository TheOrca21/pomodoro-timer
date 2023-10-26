import math
from tkinter import *
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = ""
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global REPS
    REPS = 0
    Timer_Label['text'] = 'Timer'
    Timer_Label['fg'] = GREEN
    canvas.itemconfig(timer_text, text='00:00')
    Tick_label['text'] = ""
    window.after_cancel(TIMER)


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 != 0:
        count_down(WORK_MIN*60)
        Timer_Label['text'] = 'Work'
        Timer_Label['fg'] = RED
    elif REPS % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        Timer_Label['text'] = 'Break'
        Timer_Label['fg'] = PINK
    else:
        count_down(SHORT_BREAK_MIN*60)
        Timer_Label['text'] = 'Break'
        Timer_Label['fg'] = PINK

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = '0' + str(seconds)
    canvas.itemconfig(timer_text, text=f'{minutes}:{seconds}')
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        for _ in range(math.floor(REPS/2)):
            marks += Tick
        winsound.Beep(500, 2000)
        Tick_label['text'] = marks
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=210, height=234, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(112, 117, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

Timer_Label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
Timer_Label.grid(row=0, column=1)

Start_button = Button(text='Start', highlightthickness=0, command=start_timer)
Start_button.grid(row=2, column=0)

Reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
Reset_button.grid(row=2, column=2)

Tick = '✔'
Tick_label = Label(bg=YELLOW, fg=GREEN)
Tick_label.grid(row=3, column=1)


window.mainloop()
