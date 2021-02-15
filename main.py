# Convert Temperature

from PySimpleGUI import PySimpleGUI as sg


class Temperature:
    def __init__(self):
        sg.theme('Reddit')

        #layout
        self.layout = [
            [sg.Text('Temperature:'), sg.Input(key='text')],  # line1
            [sg.Button('Celsius->Kelvin'), sg.Button('Celsius->Fahrenheit'), sg.Button('Kelvin->Celsius'), sg.Button('Kelvin->Fahrenheit'), sg.Button('Fahrenheit->Celsius'), sg.Button('Fahrenheit->Kelvin')],
            [sg.Output(key='result')],  # line 3
        ]
    
    def start(self):

        # create a window in GUI
        self.w1 = sg.Window('Temperature Case').layout(self.layout)

        while True:

            # obtain data
            self.event, self.value = self.w1.read()
            self.value=float(self.value.get('text'))

            # window closed
            if self.event == sg.WINDOW_CLOSED:            
                break
            
            # cases
            if self.event == 'Celsius->Kelvin' or 'Celsius->Fahrenheit':
                self.celsius()

            if self.event == 'Kelvin->Celsius' or 'Kelvin->Fahrenheit':
                self.kelvin()

            if self.event == 'Fahrenheit->Celsius' or 'Fahrenheit->Kelvin':
                self.fahrenheit()



    def celsius(self):
        if self.event == 'Celsius->Kelvin':
           print(self.value+273.15)
        
        if self.event == 'Celsius->Fahrenheit':
           print(self.value*9/5+32)


    def kelvin(self):
        if self.event == 'Kelvin->Celsius':
           print(self.value-273.15)
        
        if self.event == 'Kelvin->Fahrenheit':
           print(self.value*9/5-459.67)

    def fahrenheit(self):
        if self.event == 'Fahrenheit->Kelvin':
           print((self.value+459.67)*5/9)
        
        if self.event == 'Fahrenheit->Celsius':
           print((self.value-32)*5/9)


t=Temperature()
t.start()
