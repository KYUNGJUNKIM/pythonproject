import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 0.1
REPETITION = 0
TIME_CONTROL = ""
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(TIME_CONTROL)
    label1.config(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    label2.config(text="", bg=YELLOW)
    canvas.itemconfig(timer, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global REPETITION
    REPETITION += 1
    working_time = round(WORK_MIN * 60)
    break_time = round(SHORT_BREAK_MIN * 60)
    long_break_time = round(LONG_BREAK_MIN * 60)

    if REPETITION % 8 == 0:
        countdown(long_break_time)
        label1.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
    elif REPETITION % 2 == 0:
        countdown(break_time)
        label1.config(text="Break", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
    else:
        label1.config(text="Work", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
        countdown(working_time)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global TIME_CONTROL
    mark = ""
    minute = count // 60
    second = count % 60

    if minute >= 10:
        canvas.itemconfig(timer, text=f"{minute}:{second}")
        if second < 10:
            canvas.itemconfig(timer, text=f"{minute}:0{second}")
    else:
        canvas.itemconfig(timer, text=f"0{minute}:{second}")
        if second < 10:
            canvas.itemconfig(timer, text=f"0{minute}:0{second}")

    if count > 0:
        TIME_CONTROL = window.after(1000, countdown, count-1)
    elif count == 0:
        start()
        for _ in range(REPETITION//2):
            mark += "✔"
        label2.config(text=mark, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label1 = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label1.grid(row=0, column=1)

label2 = tkinter.Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
label2.grid(row=4, column=1)

button1 = tkinter.Button(text="Start", highlightthickness=0, command=start)
button1.grid(row=3, column=0)

button2 = tkinter.Button(text="Reset",  highlightthickness=0, command=reset)
button2.grid(row=3, column=2)





window.mainloop()
