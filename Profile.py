import PySimpleGUI as sg
sg.theme("BluePurple")
sg.theme_text_color("#FFFFFF")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM    : 2210010468")],
                           [sg.Text("Nama   : SRI NOR EMILYANI")],
                           [sg.Text("Kelas  : 5O Reguler Banjarmasin")],
                           [sg.Text("Matkul : Pemrograman Visual 3")]
                          ],
                   size=(300,150),
                   font=("Comic", 12, "bold"))
window()
window.close()