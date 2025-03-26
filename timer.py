import tkinter as tk
import time

# Başlangıç zamanı
start_time = time.time()

def create_timer(parent):
    """ Timer bölümünü oluşturur ve etiketi döndürür """
    section = tk.LabelFrame(parent, text="Time", fg="lime", bg="black", font=("Arial", 9),bd=2)
    section.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
    label = tk.Label(section, text="Veri Bekleniyor...", fg="white", bg="black", font=("Arial", 15), justify="center")
    label.pack(padx=10, pady=5, anchor='center')
    return label

def update_timer(label):
    """ Timer'ı günceller ve ekrana yazar """
    elapsed_time = int(time.time() - start_time)
    hours = elapsed_time // 3600
    minutes = (elapsed_time % 3600) // 60
    seconds = elapsed_time % 60

    datenow = time.strftime("%d/%m/%Y")
    timenow = time.strftime("%X")

    label.config(text=f"T + {hours:02}:{minutes:02}:{seconds:02}\n{datenow}\n{timenow}")
   

    # 1 saniyede bir güncelle
    label.after(1000, lambda: update_timer(label))
