from PySimpleGUI import PySimpleGUI as sg


class Calculadora:
    def __init__(self):
        layout = [
            [sg.Text(size=(20, 2), justification='right', relief=sg.RELIEF_RIDGE, background_color='#F7F3EC', text_color='#000000', key='display',border_width=10)],
            [sg.HorizontalSeparator()],
            [sg.Button('C', size=(16, 2)), sg.Button('Del', size=(4, 2), key='BackSpace:8')],
            [sg.Button('7', size=(4, 2)), sg.Button('8', size=(4, 2)), sg.Button('9', size=(4, 2)), sg.Button('+', size=(4, 2))],
            [sg.Button('4', size=(4, 2)), sg.Button('5', size=(4, 2)), sg.Button('6', size=(4, 2)), sg.Button('-', size=(4, 2))],
            [sg.Button('1', size=(4, 2)), sg.Button('2', size=(4, 2)), sg.Button('3', size=(4, 2)), sg.Button('*', size=(4, 2))],
            [sg.Button('0', size=(10, 2)), sg.Button('.', size=(4, 2)), sg.Button('/', size=(4, 2))],
            [sg.Button('=', size=(22, 2),bind_return_key=True)]
        ]
        sg.theme('BlueMono')
        sg.set_options(element_padding=[4,4])
        self.janela = sg.Window('Calculadora', layout, return_keyboard_events=True)
        self.calculo = '\n'

    def iniciar(self):
        while True:
            eventos, valores = self.janela.read()
            self.ler_comandos(eventos)
            if eventos == sg.WINDOW_CLOSED:
                break

    def ler_comandos(self, eventos):
        if eventos in ['C', '=', '\r','BackSpace:8']:
            if eventos == "C":
                self.clean_calculo()
                self.update_display(self.calculo)
            if eventos == '=':
                resultado = self.calcular()
                self.update_display(resultado)
                self.clean_calculo()
            if eventos == 'BackSpace:8':
                self.remove_calculo()
                self.update_display(self.calculo)
        elif eventos is not None:
            if eventos in str(list(range(0,10))) or eventos in ['+','/','.','-','*']:
                if eventos == ',':
                    print(eventos)
                    eventos = eventos.replace(',','.')
                self.add_calculo(eventos)
                self.update_display(self.calculo)
        else:
            pass

    def calcular(self):
        try:
            resultado = eval(self.calculo)
        except:
            if self.calculo == '\n':
                return '0'
            return self.calculo[-2]

        return resultado

    def add_calculo(self,item):
        self.calculo += item

    def remove_calculo(self):
        try:
            self.calculo = self.calculo.strip(self.calculo[-1])
        except:
            pass

    def clean_calculo(self):
        self.calculo = '\n'

    def update_display(self, item):
        self.janela.Element('display').Update(item)


calculadora = Calculadora()
calculadora.iniciar()
