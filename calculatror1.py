import tkinter as tk
import math
LARGE_FONT_STYLE=("Arial",40,"bold")
SMALL_FONT_STYLE=("Arial",60)
DIGITS_FONT_STYLE=("Arial",24,"bold")
DEFAULT_FONT_STYLE=("Arial",20)



OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression=""
        self.current_expression=""

        self.display_frame=self.create_display_frame()
        self.total_label, self.label=self.create_display_labels()

        self.digits={
            7:(1,1),
            8:(1,2),
            9:(1,3),
            4:(2,1),
            5:(2,2),
            6:(2,3),
            1:(3,1),
            2:(3,2),
            3:(3,3),
            0:(4,2),
            '.':(4,1)
            }
        self.operations={"/":"\u00F7",
                         "*":"\u00D7",
                         "-":"-",
                         "+":"+"
                         }

        self.buttons_frame=self.create_buttons_frame()
        self.configure_buttons()
        self.bind_keys()

    def configure_buttons(self):
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_button("C", self.clear, 0, 1)
        self.create_button("x\u00b2", self.square, 0, 2)
        self.create_button("\u221ax", self.sqrt, 0, 3)
        self.create_button("=",self.evaluate,4,3,2)

    def create_button(self,text,command,row,column,columnspan=1):
        button=tk.Button(self.buttons_frame,text=text,bg=OFF_WHITE,fg=LABEL_COLOR,font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=command)
        button.grid(row=row, column=column, columnspan=columnspan, sticky=tk.NSEW)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            self.create_button(str(digit), lambda x=digit: self.add_to_expression(x), grid_value[0], grid_value[1])

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            self.create_button(symbol, lambda x=operator: self.append_operator(x), i, 4)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def square(self):
        try:
            result = float(self.current_expression) ** 2
            self.current_expression = str(result)
            self.update_label()
        except ValueError:
            self.current_expression = "Error"
            self.update_label()

    def sqrt(self):
        try:
            result = math.sqrt(float(self.current_expression))
            self.current_expression = str(result)
            self.update_label()
        except ValueError:
            self.current_expression = "Error"
            self.update_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            result = eval(self.total_expression)
            self.current_expression = str(result)
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_display_labels(self):
        total_label=tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label=tk.Label(self.display_frame,
                       text=self.current_expression,anchor=tk.E,
                       bg=LIGHT_GRAY,fg=LABEL_COLOR,
                       padx=24,font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame=tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()

if __name__=="__main__":
    calc = Calculator()
    calc.run()
