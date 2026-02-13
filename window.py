from doctest import master

import os
import subprocess
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel
import ctypes
import sys
import os
import ipinfo
import requests
import tkinter as tk
from ipinfo import details
from main import rootmap
import tkintermapview
# Replace with your actual access token from ipinfo.io
ACCESS_TOKEN = 'cb0c0597827660'
city = ''
loc = ''
def get_ip_details_with_library(ip_address):
    """Fetches detailed geolocation using the ipinfo library."""
    handler = ipinfo.getHandler(ACCESS_TOKEN)
    try:
        global city
        global loc
        details = handler.getDetails(ip_address)
        print(f"IP Address: {details.ip}")
        print(f"City: {details.city}")
        print(f"Region: {details.region}")
        print(f"Country: {details.country_name}")
        print(f"Location (Lat/Lng): {details.loc}")
        print(f"Organization: {details.org}")
        city = details.city
        loc = details.loc
        # Access all details as a dictionary
        # print(details.all)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example:
get_ip_details_with_library(requests.get('https://api.ipify.org').text)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None,
        "runas",
        sys.executable,
        " ".join(sys.argv),
        None,
        1
    )
    sys.exit()

print("Запущено с правами администратора")
turn = False
val = 'not stated'
def turned():
    global turn
    global val
    if turn == False:
        val = cb.get()
        if val.lower() == 'fake(tls)':
            method = 'faketls.bat'
        elif val.lower() == 'simple fake':
            method = 'simplefake.bat'
        elif val.lower() == 'alt simple fake':
            method = 'simplefaketls.bat'
        status = 'On'
        subprocess.run(
            [method],
            shell=True,
            cwd="zapret/",
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        turn = True
        btn.configure(text='On',fg_color='#00ff62',hover_color='#25cf66')
    elif turn == True:
        subprocess.run(
            "taskkill /F /T /IM winws.exe",
            shell=True
        )
        turn = False
        status = 'Off'
        btn.configure(text='Off',fg_color='#fc5603',hover_color='#b85b2c')
    print(f'Status: {status}\n Method: {val}')
root = ctk.CTk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Discord Xray")
frame = CTkFrame(master=root, width=600, height=800)
frame.pack(padx=10, pady=20)
label = CTkLabel(master=frame,text="Xray DPI",font=("Arial",40,"bold"))
label.pack(padx=10, pady=20)
cb = ctk.CTkComboBox(master=frame, values=['Fake(TLS)','Simple Fake','ALT Simple Fake'])
cb.pack(padx=40, pady=20)
btn = ctk.CTkButton(master=frame, text="Off", command=turned,fg_color='#fc5603',hover_color='#b85b2c',corner_radius=10)
btn.pack(padx=40, pady=20)
btn2 = ctk.CTkLabel(master=frame,text='Your location',font=("Arial",20,"bold"))
btn2.pack(padx=40, pady=20)
map = tkintermapview.TkinterMapView(frame, width=500, height=600, corner_radius=0)

locat = loc.split(',')
print(locat[0], locat[1])
map.set_position(float(locat[0]), float(locat[1]))
map.set_zoom(8)
map.pack(padx=10, pady=20)




root.mainloop()