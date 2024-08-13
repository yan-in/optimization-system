import os
import subprocess
import webbrowser 
import tkinter as tk
from tkinter import PhotoImage
from customtkinter import *
from customtkinter import CTkButton, CTk, CTkLabel
from PIL import Image, ImageTk
#-------------------------
set_appearance_mode("dark-blue")  # Aparência da Janela
set_default_color_theme("dark-blue")
app = CTk()
app.geometry("600x550")
app.title("Optimization System")
app.resizable(width=False, height=False)
# Carrega a imagem do ícone
app.iconbitmap("F:/Documentos/teste/icon.ico")


# Adiciona uma label para exibir mensagens de status
status_label = CTkLabel(app, text="Bem Vindo ao Optimization System", font=('Verdana', 15,),height=12)
status_label.pack(pady=60)

# Função para deletar arquivos temporários
def temp_files():
    commands = r"""@echo off
echo Batch File
RD /S /Q %temp%
MKDIR %temp%
takeown /f "%temp%" /r /d y
takeown /f "C:\Windows\Temp" /r /d y
RD /S /Q C:\Windows\Temp
MKDIR C:\Windows\Temp
takeown /f "C:\Windows\Temp" /r /d y
takeown /f %temp% /r /d y
"""# Salva o comando em um arquivo temporário .bat
    batch_file_path = "temp_commands.bat"
    with open(batch_file_path, 'w') as file:
        file.write(commands)
    # Executa o arquivo batch
    try:
        subprocess.run(["cmd.exe", "/c", batch_file_path], shell=True)
        status_label.configure(text="Arquivos Temporários deletados")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")
# Função para deletar logs temporários
def log_files():
    commands = r"""@echo off
cd/
@echo
del *.log /a /s /q /f
"""
    
    # Salva o comando em um arquivo temporário .bat
    batch_file_path = "log_commands.bat"
    with open(batch_file_path, 'w') as file:
        file.write(commands)
    
    # Executa o arquivo batch
    try:
        subprocess.run(["cmd.exe", "/c", batch_file_path], shell=True)
        status_label.configure(text="Logs Temporários deletados")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")
#Função para deletar o Cache do Windows Update
def win_update_cache():
    commands = r'''@echo off
echo
net stop wuauserv
net stop UsoSvc
rd /s /q C:\\Windows\\SoftwareDistribution
md C:\\Windows\\SoftwareDistribution
'''
    # Salva o comando em um arquivo temporário .bat
    batch_file_path = "win_update_clear.bat"
    with open(batch_file_path, 'w') as file:
        file.write(commands)
    
    # Executa o arquivo batch
    try:
        subprocess.run(["cmd.exe", "/c", batch_file_path], shell=True)
        status_label.configure(text="Cache do Windows Update deletado")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")
#Função para Desligar as Atualizações Automaticas do Windows Update
def off_win_update():
    commands = r'''@echo off
echo Batch File 
taskkill -F -FI "IMAGENAME eq SystemSettings.exe"
net stop wuauserv
net stop UsoSvc
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v "DoNotConnectToWindowsUpdateInternetLocations" /t REG_DWORD /d "1" /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v "SetDisableUXWUAccess" /t REG_DWORD /d "1" /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU" /v "NoAutoUpdate" /t REG_DWORD /d "1" /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v "ExcludeWUDriversInQualityUpdate" /t REG_DWORD /d "1" /f
gpupdate /force
echo Deleting Windows Update Files
rd s q "C:\Windows\SoftwareDistribution"
md "C:\Windows\SoftwareDistribution"
net start wuauserv
net start UsoSvc
echo Windows Updates Are Successfully Disabled!
'''
    # Salva o comando em um arquivo temporário .bat
    batch_file_path = "off_win_update.bat"
    with open(batch_file_path, 'w') as file:
        file.write(commands)
    
    # Executa o arquivo batch
    try:
        subprocess.run(["cmd.exe", "/c", batch_file_path], shell=True)
        status_label.configure(text="As atualizações automáticas do Windows update foram desligadas")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")
def off_latency_bcd():
    commands = r'''@echo off
echo Disable Dynamic Tick
echo Disable High Precision Event Timer (HPET)
echo Disable Synthetic Timers
@echo
bcdedit /set disabledynamictick yes
bcdedit /deletevalue useplatformclock
bcdedit /set useplatformtick yes
'''
    # Salva o comando em um arquivo temporário .bat
    batch_file_path = "bcd.bat"
    with open(batch_file_path, 'w') as file:
        file.write(commands)
    
    # Executa o arquivo batch
    try:
        subprocess.run(["cmd.exe", "/c", batch_file_path], shell=True)
        status_label.configure(text="As funções de latência foram desabilitadas com sucesso")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")

# Função para desativar o Cortana
def disable_cortana():
    commands = r'''@echo off
echo Desativando Cortana
reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v "AllowCortana" /t REG_DWORD /d 0 /f
echo Cortana foi desativado com sucesso!
'''
    # Salva o comando em um arquivo temporário .bat
    batch_file_path = "disable_cortana.bat"
    with open(batch_file_path, 'w') as file:
        file.write(commands)
    
    # Executa o arquivo batch
    try:
        subprocess.run(["cmd.exe", "/c", batch_file_path], shell=True)
        status_label.configure(text="Cortana foi desativado com sucesso")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")

def game_bar():
    text = r'''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\System\GameConfigStore]
"GameDVR_Enabled"=dword:00000000

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\GameDVR]
"AppCaptureEnabled"=dword:00000000'''

    reg_file_path = "disable_gamebar.reg"
    with open(reg_file_path, 'w') as file:
        file.write(text)
    
    # Executa o arquivo batch
    try:
        subprocess.run(["regedit.exe", "/s", reg_file_path], shell=True)
        status_label.configure(text="Gamer Bar foi desabilitado com sucesso")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")

def off_xbox_services(): 
    text = r'''Windows Registry Editor Version 5.00                                                                                                                                                                                     youtube.com/AdamxYT

;Registry File 
;Disable Xbox Live Game Save
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XblGameSave]
"Start"=dword:00000004

;Disable Xbox Live Networking Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XboxNetApiSvc]
"Start"=dword:00000004

;Disable Xbox Accessory Management Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XboxGipSvc]
"Start"=dword:00000004

;Disable Xbox Live Auth Manager
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\XblAuthManager]
"Start"=dword:00000004
'''
    
    reg_file_path = "disable_xbox_services.reg"
    with open(reg_file_path, 'w') as file:
        file.write(text)
    
    # Executa o arquivo batch
    try:
        subprocess.run(["regedit.exe", "/s", reg_file_path], shell=True)
        status_label.configure(text="O xbox services foi desabilitado com sucesso")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")

def off_donw_maps():
    text = r'''Windows Registry Editor Version 5.00                                                                                                                                                                                     youtube.com/AdamxYT

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MapsBroker]
"Start"=dword:00000004
    '''

    reg_file_path = "disable_donw_maps.reg"
    with open(reg_file_path, 'w') as file:
        file.write(text)
    
    # Executa o arquivo batch
    try:
        subprocess.run(["regedit.exe", "/s", reg_file_path], shell=True)
        status_label.configure(text="Gerenciador de Mapas desabilitado com sucesso")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")

def off_blue(): 
    text = r'''Windows Registry Editor Version 5.00                                                                                                                                                                                     youtube.com/AdamxYT

;Registry File 
;Disable Bluetooth Audio Gateway Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BTAGService]
"Start"=dword:00000004

;Disable Bluetooth Support Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\bthserv]
"Start"=dword:00000004''' 
    
    reg_file_path = "disable_blue.reg"
    with open(reg_file_path, 'w') as file:
        file.write(text)
    # Executa o arquivo batch
    try:
        subprocess.run(["regedit.exe", "/s", reg_file_path], shell=True)
        status_label.configure(text="Bluetooth foi Desabilitado com sucesso")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")

def off_printer(): 
    text = r'''Windows Registry Editor Version 5.00                                                                                                                                                                                     youtube.com/AdamxYT

;Registry File 
;Disable Print Spooler
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Spooler]
"Start"=dword:00000004

;Disable Printer Extensions and Notifications
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PrintNotify]
"Start"=dword:00000004''' 
    
    reg_file_path = "off_printer.reg"
    with open(reg_file_path, 'w') as file:
        file.write(text)
    # Executa o arquivo batch
    try:
        subprocess.run(["regedit.exe", "/s", reg_file_path], shell=True)
        status_label.configure(text="Serviço de Impressão foi Desabilitado com sucesso")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")

def off_extra(): 
    text = r'''Windows Registry Editor Version 5.00                                                                                                                                                                                    
;Registry File 
;Disable Windows Biometric Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WbioSrvc]
"Start"=dword:00000004

;Disable Windows Font Cache Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\FontCache]
"Start"=dword:00000004

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\FontCache3.0.0.0]
"Start"=dword:00000004

;Disable Graphics performance monitor service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\GraphicsPerfSvc]
"Start"=dword:00000004

;Disable Windows Image Acquisition (WIA)
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\stisvc]
"Start"=dword:00000004

;Disable Windows Error Reporting Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WerSvc]
"Start"=dword:00000004

;Disable Program Compatibility Assistant Service
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\PcaSvc]
"Start"=dword:00000004

;Disable Windows Event Collector
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Wecsvc]
"Start"=dword:00000004''' 
    
    reg_file_path = "off_extra.reg"
    with open(reg_file_path, 'w') as file:
        file.write(text)
    # Executa o arquivo batch
    try:
        subprocess.run(["regedit.exe", "/s", reg_file_path], shell=True)
        status_label.configure(text="Serviços extras foram desabilitados com sucesso")
    except Exception as e:
        status_label.configure(text=f"Ocorreu um erro: {e}")

def donate():
    new=2
    url="https://livepix.gg/yaano"
    webbrowser.open(url,new=new)

def discord():
    new=2
    url="https://discord.gg/fbVE35uxsb"
    webbrowser.open(url,new=new)

def github():
    new=2
    url="https://github.com/yan-in"
    webbrowser.open(url,new=new)

def sobre():
    sobre_text = """Optimization System

O Optimization System é uma ferramenta poderosa projetada para otimizar e aprimorar o desempenho do seu sistema Windows. Com uma interface intuitiva e funções específicas, ele permite limpar arquivos temporários, desativar serviços desnecessários e otimizar o registro do sistema de forma rápida e eficaz. Ideal para usuários que desejam um controle total sobre a performance do seu computador.

Principais Recursos:
- Limpeza de arquivos temporários e logs.
- Desativação de serviços que impactam a latência.
- Otimização do Windows Update.
- Desabilitação de funcionalidades como Cortana, Game Bar e serviços do Xbox.

Aproveite o máximo do seu sistema com o Optimization System!

Ass: Yan Dos Santos Epifânio
"""

    # Cria o arquivo .txt e escreve o conteúdo
    file_path = "sobre_optimization_system.txt"
    with open(file_path, 'w') as file:
        file.write(sobre_text)
    
    # Abre o arquivo após criar
    os.startfile(file_path)    

# Personalização dos botões e chamada das funções
btn = CTkButton(master=app, text="Limpar Arquivos Temporários", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02",font=('Verdana', 13), 
                command=temp_files, width=250)
btn1 = CTkButton(master=app, text="Remover Logs Temporários", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=log_files, width=250)
btn2 = CTkButton(master=app, text="Limpar Cache do Windows Update", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=win_update_cache, width=250)
btn3 = CTkButton(master=app, text="Desativar o Windows Update", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=off_win_update, width=250)
btn4 = CTkButton(master=app, text="Desabilitar Latência BCD", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=off_latency_bcd, width=250)
btn5 = CTkButton(master=app, text="Desativar Cortana", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=disable_cortana, width=250)
reg6 = CTkButton(master=app, text="Desativar Bluetooth", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=off_blue, width=250)
reg7 = CTkButton(master=app, text="Desativar Game Bar", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=game_bar, width=250)
reg8 = CTkButton(master=app, text="Desativar Serviços Xbox", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=off_xbox_services, width=250)
reg9 = CTkButton(master=app, text="Desativar Serviços de Impressão", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=off_printer, width=250)
reg10 = CTkButton(master=app, text="Desativar Gerenciador de Mapas", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=off_donw_maps, width=250)
reg11 = CTkButton(master=app, text="Desativar Serviços extras inuteis", 
                corner_radius=8, fg_color="#ff7600",text_color=("black"),
                hover_color="#7c0a02", font=('Verdana', 13),
                command=off_extra, width=250)
# Novos botões
btn_donate = CTkButton(master=app, text="Doação", 
                       corner_radius=8, fg_color="#28a745",text_color=("white"),
                       hover_color="#19692c", font=('Verdana', 13),
                       width=250, command=donate)
btn_discord = CTkButton(master=app, text="Discord", 
                        corner_radius=8, fg_color="#7289DA",text_color=("white"),
                        hover_color="#4e5f9e", font=('Verdana', 13),
                        width=250, command=discord)
btn_github = CTkButton(master=app, text="GitHub", 
                       corner_radius=8, fg_color="#24292e",text_color=("white"),
                       hover_color="#161b22", font=('Verdana', 13),
                        width=250, command=github)

# Botão "Sobre"
btn_about = CTkButton(master=app, text="Sobre", 
                      corner_radius=8, fg_color="#6c757d",text_color=("white"),
                      hover_color="#565e64", font=('Verdana', 13),
                     width=250,command=sobre)

# Posicionamento dos novos botões
btn_donate.place(x=35, y=435)
btn_discord.place(x=35, y=470)
btn_github.place(x=310, y=435)
btn_about.place(x=310, y=470)
# Posição dos botões alinhada à esquerda
btn.place(x=20, y=165)
btn1.place(x=20, y=200)
btn2.place(x=20, y=235)
btn3.place(x=20, y=270)
btn4.place(x=20, y=305)
btn5.place(x=20, y=340)
reg6.place(x=330, y=165)
reg7.place(x=330, y=200)
reg8.place(x=330, y=235)
reg9.place(x=330, y=270)
reg10.place(x=330, y=305)
reg11.place(x=330, y=340)
# Inicializa a interface gráfica

app.mainloop()



