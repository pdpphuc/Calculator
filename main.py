from Calculator import *

# Cấu hình chung
window = Tk()
window.title('Calculator')
window.geometry('+450+150')
window.iconphoto(False, PhotoImage(file = 'Calculator.png'))

Calculator(window)

window.mainloop()