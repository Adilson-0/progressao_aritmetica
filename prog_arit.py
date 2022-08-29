# Arial * Courier * Comic, * Fixedsys * Times * Verdana * Helvetica
import PySimpleGUI as sg
from time import sleep
sg.theme("DarkGrey13")

#script de cálculo
def desc_val(a1, raz, n):
    an = a1+(n-1)*raz
    sn = ((a1+an)*n)/2
    return an, sn

def escrever(a1, raz, n):
    ptermo = a1
    pa = [a1]
    for i in range(n):
        ptermo = ptermo + raz
        pa.append(ptermo)
    return pa

#layouts
def menu():
    opcoes = [
        [sg.Push(), sg.Button("DESCOBRIR ALGUM VALOR"), sg.Button("VALORES DA EQUAÇÃO", size=(25, 1))],
        [sg.Push(), sg.Button("ESCREVER P.A"), sg.Push()]
    ]

    layout = [
        [sg.Push(), sg.Text("CALCULADOR DE P.A", font=('bolder', 17)), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text("escolha uma das operações abaixo para prosseguir:", font=12), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Frame("", opcoes), sg.Push()]
    ]
    return sg.Window("menu", layout=layout, finalize=True, size=(500, 200))

def desc_val_main():
    opcoes = [
        [sg.Push(), sg.Text("PRIMEIRO NÚMERO -->"), sg.Spin([i for i in range(0, 999)], initial_value=0, size=(6,6), key="a1"), sg.Push()],
        [sg.Push(), sg.Text("RAZÃO DA P.A -->"), sg.Spin([i for i in range(0, 999)], initial_value=0, size=(6,6), key="raz"), sg.Push()],
        [sg.Push(), sg.Text("NÚMERO A SER ALCANÇADO -->"), sg.Spin([i for i in range(0, 999)], initial_value=0, size=(6,6), key="n"), sg.Push()],
    ]
    layout = [
        [sg.Push(), sg.Text("DESCOBRIR VALOR EM UMA P.A", font=('bolder', 17)), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Frame("", layout=opcoes), sg.Push()],
        [sg.Push(), sg.Output(size=(25, 7)), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button("MENU"), sg.Button("CALCULAR"), sg.Push()]
    ]
    return sg.Window("descobrir valor", layout=layout, finalize=True, size=(500, 330))

def escrev_pa():
    opcoes = [
        [sg.Push(), sg.Text("PRIMEIRO NÚMERO -->"), sg.Spin([i for i in range(0, 999)], initial_value=0, size=(6,6), key='a12'), sg.Push()],
        [sg.Push(), sg.Text("RAZÃO DA P.A -->"), sg.Spin([i for i in range(0, 999)], initial_value=0, size=(6,6), key='raz2'), sg.Push()],
        [sg.Push(), sg.Text("NÚMERO A SER ALCANÇADO -->"), sg.Spin([i for i in range(0,999)], initial_value=0, size=(6,6), key='n2'), sg.Push()]
    ]

    layout = [
        [sg.Push(), sg.Text("ESCREVER UMA P.A", font=('bolder', 17)), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Frame("", layout=opcoes), sg.Push()],
        [sg.Push(), sg.Output(size=(25, 7)), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button("MENU"), sg.Button("CALCULAR"), sg.Push()]
    ]
    return sg.Window("escrever P.A", layout=layout, finalize=True, size=(500, 330))

janela1, janela2, janela3 = menu(), None, None

while True:
    janela, evento, valor = sg.read_all_windows()
    if evento == sg.WINDOW_CLOSED:
        break
    elif janela == janela1 and evento == "DESCOBRIR ALGUM VALOR":
        janela1.close()
        janela2 = desc_val_main()
    elif janela == janela1 and evento == "ESCREVER P.A":
        janela1.close()
        janela3 = escrev_pa()
    elif janela == janela2 and evento ==  "MENU":
        janela2.close()
        janela1 = menu()
    elif janela == janela3 and evento == "MENU":
        janela3.close()
        janela1 = menu()
    elif janela == janela2 and evento == "CALCULAR":
        vals = desc_val(valor['a1'], valor['raz'], valor['n'])
        print(f"a1 = {vals[0]}\nsn = {vals[1]}")
        print("-------------------\n")
    elif janela == janela3 and evento == "CALCULAR":
        vals2 = escrever(valor['a12'], valor['raz2'], valor['n2'])
        print(f"P.A --> {vals2}")
        print("-------------------------------------------\n")