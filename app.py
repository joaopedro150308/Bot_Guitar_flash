import pyautogui
import webbrowser
from time import sleep
import keyboard


def apertar_tecla(tecla):
    pyautogui.press(tecla)


def fechar():
    pyautogui.click(113, 240, duration=2)
    sleep(1)
    pyautogui.hotkey('ctrl', 'w')
    pyautogui.alert(text='Fim do programa', title='Fim', button='Ok')

# Abrir ou não o navegador
abrir_ou_nao = pyautogui.confirm(text='Deseja abrir o jogo desde o navegardo?',
                                 title='Abrir ou iniciar', buttons=['Sim, abrir navegardo', 'Não, já esta aberto'])
if abrir_ou_nao == 'Sim, abrir navegador':
    # Abrir site
    webbrowser.open_new_tab(
        'https://guitarflash.com/?lg=pt&_gl=1*1pjiznc*_ga*MTIzNDcwNDAzOC4xNzE2MDY0MTkx*_ga_37GXT4VGQK*MTcxNzEwODgyNy40LjEuMTcxNzExMDI1NS4wLjAuMA..')
    sleep(20)
    # Maximizar
    apertar_tecla('f11')
    sleep(3)
    # Clickar em jogar
    pyautogui.click(626, 445, duration=1.5)
    sleep(15)
    # Clickar em nivel 1
    pyautogui.click(1237, 921, duration=2)
    sleep(5)
elif abrir_ou_nao == 'Não, já esta aberto':
    comecar = pyautogui.confirm(text='Para iniciar a automação clique na música que deseja, em seguida aperter em iniciar.',
                                title='Comaçar automação', buttons=['Cancelar', 'Iniciar'])
    if comecar == 'Cancelar':
        pyautogui.alert(text='Automação cancelada.',
                        title='Cancelando', button='Ok')
        sleep(1)
        fechar()

    elif comecar == 'Iniciar':
        pyautogui.click(113, 240, duration=2)
        sleep(1)
        pyautogui.scroll(2000)
        sleep(1)
        pyautogui.scroll(-400)
        sleep(5)
        pyautogui.click(712, 406, duration=1.5)
        sleep(5)
        pyautogui.click(576, 798, duration=1.5)

        while not keyboard.is_pressed('1') == True:
            # Verde
            if pyautogui.pixelMatchesColor(678, 840, (0, 152, 0)) == True:
                apertar_tecla('a')
                sleep(0.05)
            # Vermelho
            if pyautogui.pixelMatchesColor(814, 841, (255, 0, 0)) == True:
                apertar_tecla('s')
                sleep(0.05)
            # Amarelo
            if pyautogui.pixelMatchesColor(942, 842, (244, 244, 2)) == True:
                apertar_tecla('j')
                sleep(0.05)
        pyautogui.alert(text='Programa finalizado!',
                        title='Volte sempre!', button='Ok')
