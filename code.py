import PySimpleGUI as sg
import os
import shutil

sg.theme('Reddit')

# Creating the application layout
layout = [
    [
        [sg.Text('Select a folder')],
        [sg.Input(size=(25, 1), key='file'),
         sg.FolderBrowse('Select Folder')],
        [sg.Button('Organize folder')],
        [sg.Output(size=(40, 5), key='output')],
        [sg.Text('Author: github.com/RyanKologeski')]
    ]
]

# Starting the window
window = sg.Window('Folder Organizer', layout, element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    # Test if the button to organize folder was clicked
    if event == 'Organize folder':
        path = values['file']
        print(
            f'Folder path: {path}\nOrganizing your folder, wait.')
        list_files = os.listdir(path)
        # Loop
        for file in list_files:
            # Check if it is a directory
            if(os.path.isdir(f'{path}\{file}')):
                pass
            else:
                corta = file.split('.')
                # checks if the file is of type image
                if((corta[-1] == 'png') or (corta[-1] == 'jpg') or (corta[-1] == 'jpeg') or
                        (corta[-1] == 'svg') or (corta[-1] == 'bmp') or (corta[-1] == 'gif')):
                    if not os.path.isdir(f'{path}\Files imagem'):
                        os.makedirs(f'{path}\Files imagem')
                    shutil.move(f'{path}\{file}',
                                f'{path}\Files imagem')
                # Checks other types files
                else:
                    if not os.path.isdir(f'{path}\Files {corta[-1]}'):
                        os.makedirs(f'{path}\Files {corta[-1]}')
                    shutil.move(f'{path}\{file}',
                                f'{path}\Files {corta[-1]}')
    sg.popup('Your folder is organized :)')
