######################### Calculator project ########################
import tkinter as tk 

# Calculator class : 
class Calculator :
    # class's constructor to create the app's window : 
    def __init__(self) :
        self.window = tk.Tk()
        self.window.geometry("375x667") # define window's height and width
        self.window.resizable(0, 0)
        self.window.title("Calculator") # define window's title
        self.total_expression = ""
        self.current_expression = ""
        # display frame : 
        self.display_frame = self.createDisplayFrame()
        # to display labels :
        self.total_label, self.current_label = self.createLabels()
        # numbers table :
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            6: (2, 1), 5: (2, 2), 4: (2, 3),
            3: (3, 1), 2: (3, 2), 1: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        # operators table :
        self.operators = {'/': '\u00F7', '*': '\u00D7', '-': '-', '+': '+'}
        # button frame :
        self.buttons_frame = self.createButtonsFrame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for i in range(1, 5) :
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)
        # to create digit buttons :
        self.createDigitButtons()
        # to create operators buttons :
        self.createOperatorButtons()
        # to create square button :
        self.createSquareButton()
        # to create sqrt button :
        self.createSqrtButton()

    # to create display labels :
    def createLabels(self) :
        # total expression display : 
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg='black', fg='white', padx=24, 
            font=('arial', 40, 'bold'))
        total_label.pack(expand=True, fill='both')   
        # current expression display :  
        current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg='black', fg='white', padx=24, 
            font=('arial', 16))
        current_label.pack(expand=True, fill='both')    
        return total_label, current_label

    # add user's input to exprissions :
    def addToExpression(self, val) :
        self.current_expression += str(val)
        self.updateCurrentLabel()

    # to create digit buttons :
    def createDigitButtons(self) :
        for digit, grid_value in self.digits.items() :
            button = tk.Button(self.buttons_frame, text=str(digit), bg='#28282B', fg='white', font=('arial', 24, 'bold'), borderwidth=0, 
                command=lambda x=digit: self.addToExpression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    # calcul function :
    def evaluate(self) :
        self.total_expression += str(eval(self.current_expression))
        self.updateTotalLabel()
        self.current_expression = ""
        self.updateCurrentLabel()

    # to create operators buttons :
    def createOperatorButtons(self) :
        # to create operators (+, -, *, /) :
        i = 0
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg='#191970', fg='white', font=("Arial", 24, "bold"), borderwidth=0, 
                command=lambda x=operator: self.addToExpression(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1
        # to create equal (=) operator :
        equal_button = tk.Button(self.buttons_frame, text='=', bg='#191970', fg='white', font=("Arial", 24, "bold"), borderwidth=0, 
            command=self.evaluate)
        equal_button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
        # to create clear (C) operator :
        clear_button = tk.Button(self.buttons_frame, text="C", bg='#28282B', fg='white', font=("Arial", 24, "bold"), borderwidth=0,
            command=self.clearButton)
        clear_button.grid(row=0, column=1, sticky=tk.NSEW)
 
    # clear button fucntion :
    def clearButton(self) :
        self.total_expression = ""
        self.current_expression = ""
        self.updateCurrentLabel()
        self.updateTotalLabel()

    # to calcul square (x**2):
    def square(self) :
        self.current_expression = str(eval(f"{ self.current_expression }**2"))
        self.updateCurrentLabel()
    
    # to create square button :
    def createSquareButton(self) :
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg='#28282B', fg='white', font=("Arial", 24, "bold"), borderwidth=0,
            command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    # to calcul sqrt:
    def sqrt(self) :
        self.current_expression = str(eval(f"{ self.current_expression }**0.5"))
        self.updateCurrentLabel()
    
    # to create sqrt button :
    def createSqrtButton(self) :
        button = tk.Button(self.buttons_frame, text="\u221ax", bg='#28282B', fg='white', font=("Arial", 24, "bold"), borderwidth=0,
            command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    # to create result and numbers's display frame :
    def createDisplayFrame(self) :
        frame = tk.Frame(self.window, height=221, bg='#000000')
        frame.pack(expand=True, fill='both')
        return frame

    # to create numbers and operators's buttons frame :
    def createButtonsFrame(self) :
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    # update total label :
    def updateTotalLabel(self) :
        self.total_label.config(text=self.total_expression)

    # update current label :
    def updateCurrentLabel(self) :
        expression = self.current_expression
        for operator, symbol in self.operators.items() :
            expression = expression.replace(operator, f' {symbol} ')
        self.current_label.config(text=expression)

    # to run the app : 
    def run(self) :
        self.window.mainloop()


if __name__ == "__main__" :
    calcul = Calculator()
    calcul.run()