from PySimpleGUI import PySimpleGUI as sg


class Calculadora:
    def __init__(self):
        self.calculo = ''
        self.numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        layout = [
            [sg.Text('', size=(23, 2), justification='right', relief=sg.RELIEF_RIDGE, background_color='#F7F3EC', text_color='#000000', key='display')],
            [sg.HorizontalSeparator()],
            [sg.Button('C', size=(23, 2))],
            [sg.Button('7', size=(4, 2)), sg.Button('8', size=(4, 2)), sg.Button('9', size=(4, 2)), sg.Button('+', size=(4, 2))],
            [sg.Button('4', size=(4, 2)), sg.Button('5', size=(4, 2)), sg.Button('6', size=(4, 2)), sg.Button('-', size=(4, 2))],
            [sg.Button('1', size=(4, 2)), sg.Button('2', size=(4, 2)), sg.Button('3', size=(4, 2)), sg.Button('*', size=(4, 2))],
            [sg.Button('0', size=(10, 2)), sg.Button('.', size=(4, 2)), sg.Button('/', size=(4, 2))],
            [sg.Button('=', size=(23, 2))]
        ]
        # sg.theme('LightBrown1')
        sg.theme('BlueMono')
        self.janela = sg.Window('Calculadora', layout)

    def iniciar(self):
        while True:
            eventos, valores = self.janela.read()
            self.ler_comandos(eventos)
            if eventos == sg.WINDOW_CLOSED:
                break

    def ler_comandos(self, eventos):
        if eventos in ['C', '=']:
            if eventos == "C":
                self.calculo = ''
                self.update_display(self.calculo)

            if eventos == '=':
                resultado = self.calcular()
                self.janela.Element('display').Update(resultado)
                self.calculo = ''
        elif eventos is not None:
            self.calculo += eventos
            self.update_display(self.calculo)
        else:
            pass

    def calcular(self):
        try:
            resultado = eval(self.calculo)
        except:
            return '0'
        return resultado

    def update_display(self, item):
        self.janela.Element('display').Update(item)


calculadora = Calculadora()
calculadora.iniciar()
