import PySimpleGUI as sg
import os
import shutil


class TelaPython:
    def __init__(self) -> None:
        layout = [
            [sg.Text('Caminho Absoluto da Pasta que Deseja Organizar:')],
            [sg.Input(key='caminho', do_not_clear=False)],
            [sg.Button('Organizar Pasta')],
            [sg.Output(size=(50, 5), key='output')],
            [sg.Text('Author: github.com/RyanKologeski')]
        ]
        # Window
        self.janela = sg.Window("Organizador de Pasta").layout(layout)

    def Iniciar(self):
        i = 0
        while True:
            # Extract data from screen
            event, self.values = self.janela.Read()
            # Check if the organize folder button was clicked
            if(event == 'Organizar Pasta'):
                self.janela.FindElement('output').Update('')
                caminho = self.values['caminho']
                print(
                    f'Caminho da pasta: {caminho}\nOrganizando sua pasta, aguarde.')
                # Scan files from absolute path
                lista_arquivos = os.listdir(caminho)
                for arquivo in lista_arquivos:
                    # Check if it is a directory
                    if(os.path.isdir(f'{caminho}\{arquivo}')):
                        pass
                    else:
                        corta = arquivo.split('.')
                        # checks if the file is of type image
                        if((corta[-1] == 'png') or (corta[-1] == 'jpg') or (corta[-1] == 'jpeg') or
                           (corta[-1] == 'svg') or (corta[-1] == 'bmp') or (corta[-1] == 'gif')):
                            if not os.path.isdir(f'{caminho}\Arquivos imagem'):
                                os.makedirs(f'{caminho}\Arquivos imagem')
                            shutil.move(f'{caminho}\{arquivo}',
                                        f'{caminho}\Arquivos imagem')
                        # Checks other types files
                        else:
                            if not os.path.isdir(f'{caminho}\Arquivos {corta[-1]}'):
                                os.makedirs(f'{caminho}\Arquivos {corta[-1]}')
                            shutil.move(f'{caminho}\{arquivo}',
                                        f'{caminho}\Arquivos {corta[-1]}')
            # Checks if the application was closed
            elif event == sg.WIN_CLOSED or event == ' ':
                break
            else:
                pass
            print('\nSua pasta foi organizada :)')


tela = TelaPython()
tela.Iniciar()
