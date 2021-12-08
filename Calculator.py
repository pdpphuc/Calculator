from tkinter import *
from playsound import playsound
from functools import partial

class Calculator:

    SYNTAX_ERROR = '#Syntax ERROR'
    ANS_ERROR = '#Must have answer first'

    def __init__(self, tk_window):
        self.__exp = ''
        self.__txt_input = StringVar(value=self.__exp)
        self.__txt_display = Entry(tk_window, width=30, font=('Arial', 20, 'bold'), textvariable=self.__txt_input, 
                    bd=30, insertwidth=4, justify='right', state=DISABLED, disabledbackground='aqua', disabledforeground='black').grid(columnspan=4)
        self.__ans = ''
        self.__justcal = False

        # Tạo các phím của máy tính bỏ túi
        self.__numbtns = [Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text=str(i), bg='silver', command=partial(self.onclick, i)).grid(row=(9-i)//3+1, column=(i+2)%3) for i in range(9, 0, -1)]
        
        self.bt_div = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='/', bg='silver', command=lambda:self.onclick('/')).grid(row=1, column=3)
        self.bt_mul = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='*', bg='silver', command=lambda:self.onclick('*')).grid(row=2, column=3)
        self.bt_sub = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='-', bg='silver', command=lambda:self.onclick('-')).grid(row=3, column=3)
        
        self.bt_0 = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'),
            text='0', bg='silver', command=lambda:self.onclick(0)).grid(row=4, column=0)
        self.bt_dot = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='.', bg='silver', command=lambda:self.onclick('.')).grid(row=4, column=1)
        self.bt_ans = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='Ans', bg='silver', command=lambda:self.onclick('Ans')).grid(row=4, column=2)
        self.bt_add = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='+', bg='silver', command=lambda:self.onclick('+')).grid(row=4, column=3)

        self.bt_open = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='(', bg='silver', command=lambda:self.onclick('(')).grid(row=5, column=0)
        self.bt_close = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text=')', bg='silver', command=lambda:self.onclick(')')).grid(row=5, column=1)
        self.bt_del = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='DEL', bg='silver', command=lambda:self.onclick('DEL')).grid(row=5, column=2)
        self.bt_equal = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='=', bg='silver', command=lambda:self.onclick('=')).grid(row=5, column=3)

        self.bt_ac = Button(tk_window, width=5, bd=8, fg='black', font=('Arial', 20, 'bold'), 
            text='AC', bg='silver', command=lambda:self.onclick('AC')).grid(row=6, column=2)
        
    @property
    def exp(self):
        return self.__exp

    @exp.setter
    def exp(self, value):
        self.__exp = value
        self.__txt_input.set(self.__exp)

    def onclick(self, text):
        playsound('tit.wav', block=False)
        if text == 'Ans' and self.__ans == '':
            self.exp = Calculator.ANS_ERROR
        elif text == '=':
            # Tiền xử lý
            if self.exp == '':
                self.__ans = ''
                return
            ex = self.exp.lstrip('0').replace('Ans', self.__ans)
            try:  
                self.exp = str(eval(ex))
            except:
                self.exp = Calculator.SYNTAX_ERROR
                return
            # Hậu xử lý
            if '.' in self.exp:
                self.exp = self.exp.rstrip('0')
                self.exp = self.exp.rstrip('.')
            self.__ans = self.exp
            self.__justcal = True
        elif text == 'DEL':
            self.__justcal = False
            if '#' in self.exp:
                self.exp = ''
            elif self.exp.endswith('Ans'):
                self.exp = self.exp[:-3]
            else:
                self.exp = self.exp[:-1]
        elif text == 'AC':
            self.__justcal = False
            self.exp = ''
        else:
            if self.exp in (Calculator.SYNTAX_ERROR, Calculator.ANS_ERROR):
                self.exp = str(text)
            else:
                if self.__justcal:
                    self.__justcal = False
                    self.exp = 'Ans'
                self.exp += str(text)
