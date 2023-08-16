from plyer import notification
import tkinter as tk
from tkinter import messagebox
import time
import os
from win10toast import ToastNotifier
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from gtts import gTTS


# Display another message box using tkinter
msg_box = messagebox.showinfo('Error', 'System has been destroyed', icon='error')
time.sleep(1)

# Show Windows toast notification
toaster = ToastNotifier()
title = "Windows Defender"
message = "WARNING WINDOWS SYSTEM HAS BEEN DESTROYED: a malicious malware has destroyed your computer, the system will expire in 20 seconds. Sorry."
icon = ("windows.png")  # Replace with the actual icon path
toaster.show_toast(title, message, icon_path=icon, duration=100)

time.sleep(2)

# Display a message box using tkinter
msg_box = messagebox.showinfo('Error', 'System has been destroyed', icon='error')


# Pause for a few seconds
time.sleep(4)

def adjust_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices[0].Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume_range = volume.GetVolumeRange()

    # Aumenta il volume del 30%
    new_volume = min(current_volume + 0.3, volume_range[1])
    volume.SetMasterVolumeLevelScalar(new_volume, None)





# Convert text to speech
text = "il tuo sistema è appena stato hackerato, il sistema verrà distrutto entro 1 minuto, buona fortuna!"
tts = gTTS(text, lang='it')
output_file = "output.mp3"
tts.save(output_file)
os.system(f'start {output_file}')



time.sleep(0)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


html_content = '''
<html>
<head>
<title>BSOD</title>
</head>
<body bgcolor="#FF0000" scroll="no">
<font face="Lucida Console" size="4" color="#FFFFFF">
<p>A problem has been detected and windows has been shutdown to prevent damage to your computer.</p>
<p>Error: SYS_DESTROYED</p>
<p>WARNING.</p>
<p>-------------------------------------------------------------------------------------------------------------------------</p>
<p>Technical information:</p>
<p>*** you can't use your computer again</p>
<p>*** a potent malware has destroyed your computer</p>
<p>your system has been destroyed</p>
<p>Physical component are unavable.</p>
<p>-------------------------------------------------------------------------------------------------------------------------</p>
<p>Contact your system administrator or technical support group.</p>
<p>please restart your computer.</p>
</font>
</body>
</html>
'''

# Scrivi il contenuto HTML nel file
with open('bsod.html', 'w') as file:
    file.write(html_content)

# Scrivi il contenuto HTML nel file
with open('bsod.html', 'w') as file:
    file.write(html_content)

# Configura il driver per Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-fullscreen")  # Apri a schermo intero

# Avvia il browser e apri il file HTML
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://fakeupdate.net/win8/bsod.html')  # Inserisci il percorso assoluto del file bsod.html

time.sleep(5)  # Attendiamo 5 secondi per far sì che la pagina si carichi completamente

# Chiudi il browser dopo un ritardo
time.sleep(10)  # Attendi 10 secondi prima di chiudere il browser
driver.quit()   # Chiudi il browser



time.sleep(50000)



StopAsyncIteration 


