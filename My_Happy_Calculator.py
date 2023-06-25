
import PySimpleGUI as sg

sg.theme('DarkAmber')
sg.set_options(font = 'verdana 20', text_justification= 'justified')

button_size = (3,1)
typed_keys = []
typed_number = []
full_operations = []

layout = [
    [sg.Text('', font = 'verdana 28', expand_x=True, justification= 'center', pad = (10,0), key='Screen', background_color = '#32334d')],
    [sg.Button('Clear', expand_x=True), sg.Button('Erase', expand_x=True)],
    [sg.Button('7', size=button_size),sg.Button('8', size=button_size),sg.Button('9', size=button_size),sg.Button('÷', size=button_size)],
    [sg.Button('4', size=button_size),sg.Button('5', size=button_size),sg.Button('6', size=button_size),sg.Button('x', size=button_size)],
    [sg.Button('1', size=button_size),sg.Button('2', size=button_size),sg.Button('3', size=button_size),sg.Button('-', size=button_size)],
    [sg.Button('0', size=button_size),sg.Button('.', size = button_size),sg.Button('+', size = button_size), sg.Button('=', expand_x=True, bind_return_key=True)]
    ]

window = sg.Window('Calculator', layout, return_keyboard_events = True)

while True:
    event, values = window.read()

    if typed_keys == []: typed_keys.append('0')

    if event == sg.WIN_CLOSED:
        break
    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        typed_keys.append(event)
        if typed_keys[0] == '0' and typed_keys[1] != '.': typed_keys.pop(0) 
        typed_equation = ''.join(typed_keys)
        window['Screen'].update(typed_equation)

    if event in ['÷','x','-','+','/','*'] and typed_keys[-1] not in ['÷','x','-','+','/','*']:
        if event == '÷': event = '/'
        if event == 'x': event = '*'
        full_operations.append(''.join(typed_keys))
        typed_keys = []
        full_operations.append(event)

    if event == "Erase":

        if len(typed_keys)>0:
            typed_keys.pop()
        typed_equation = ''.join(typed_keys)
        window['Screen'].update(typed_equation)

    if event == "Clear":
        if len(typed_keys)>0:
            typed_keys = []
        typed_equation = ''.join(typed_keys)
        window['Screen'].update(typed_equation)
   
    if event == "=":
        full_operations.append(''.join(typed_keys))
        result = float(eval(''.join(full_operations)))
        full_operations = []
        typed_keys = list(str(round(result,6)))
        typed_equation = ''.join(typed_keys)
        window['Screen'].update(typed_equation)
        print(event)

window.close()

# %%



