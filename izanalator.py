import tkinter as tk

exp = ""
done = False

def update_main(val):
    if val == "":
        screen.set("0")
    else:
        screen.set(val)

def update_small(val):
    expr.set(val)

def press_num(n):
    global exp, done
    if done:
        exp = ""
        done = False
    exp = exp + n
    update_main(exp)
    update_small("")

def press_op(o):
    global exp, done
    done = False

    if len(exp) > 0:
        last = exp[-1]
        if last in "+-*/%":
            exp = exp[:-1]

    exp = exp + o
    update_main(exp)
    update_small("")

def press_dot():
    global exp

    parts = exp.split("+")
    parts = parts[-1].split("-")
    parts = parts[-1].split("*")
    parts = parts[-1].split("/")
    parts = parts[-1].split("%")

    last = parts[-1]

    if "." in last:
        return

    if exp == "":
        exp = "0"

    exp = exp + "."
    update_main(exp)

def equals():
    global exp, done

    if exp == "":
        return

    try:
        update_small(exp + " =")
        ans = eval(exp)

        ans = round(ans, 10)

        exp = str(ans)
        done = True

        update_main(exp)

    except:
        update_main("Error")
        update_small("")
        exp = ""

def clear_all():
    global exp, done
    exp = ""
    done = False
    update_main("0")
    update_small("")

def back():
    global exp
    if exp == "":
        return
    exp = exp[:-1]
    update_main(exp)

# -------- UI --------

root = tk.Tk()
root.title("Izzanalator")

expr = tk.StringVar()
screen = tk.StringVar(value="0")

top = tk.Label(root, textvariable=expr, anchor="e", fg="gray")
top.pack(fill="both")

main = tk.Label(root, textvariable=screen, anchor="e",
                font=("Arial", 22), bg="#d4edda")
main.pack(fill="both", pady=5)

frame = tk.Frame(root)
frame.pack()

def make_btn(t, cmd, r, c, span=1):
    b = tk.Button(frame, text=t, width=5, height=2, command=cmd)
    b.grid(row=r, column=c, columnspan=span)

make_btn("AC", clear_all, 0, 0)
make_btn("DEL", back, 0, 1)
make_btn("%", lambda: press_op("%"), 0, 2)
make_btn("/", lambda: press_op("/"), 0, 3)

make_btn("7", lambda: press_num("7"), 1, 0)
make_btn("8", lambda: press_num("8"), 1, 1)
make_btn("9", lambda: press_num("9"), 1, 2)
make_btn("*", lambda: press_op("*"), 1, 3)

make_btn("4", lambda: press_num("4"), 2, 0)
make_btn("5", lambda: press_num("5"), 2, 1)
make_btn("6", lambda: press_num("6"), 2, 2)
make_btn("-", lambda: press_op("-"), 2, 3)

make_btn("1", lambda: press_num("1"), 3, 0)
make_btn("2", lambda: press_num("2"), 3, 1)
make_btn("3", lambda: press_num("3"), 3, 2)
make_btn("+", lambda: press_op("+"), 3, 3)

make_btn("0", lambda: press_num("0"), 4, 0, 2)
make_btn(".", press_dot, 4, 2)
make_btn("=", equals, 4, 3)

root.mainloop()