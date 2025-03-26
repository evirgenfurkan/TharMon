import tkinter as tk
import random

def create_ambient_section(parent):
    """ Ortam bilgilerini gösteren bölüm """
    section = tk.LabelFrame(parent, text="Ambient Conditions", fg="lime", bg="black", font=("Arial", 9), bd=2)
    section.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    label = tk.Label(section, text="Veri Bekleniyor...", fg="white", bg="black", font=("Arial", 10), justify="left")
    label.pack(padx=10, pady=5, anchor='w')

    return label

def update_ambient(label):
    """ Ortam verilerini rastgele simüle et ve ekrana yazdır """
    temperature = random.randint(18, 25)
    pressure = round(random.uniform(0.8, 1.2), 2)
    humidity = random.randint(30, 60)
    oxygen = random.randint(19, 21)
    air_quality = random.randint(19, 221)

    label.config(text=f"Temperature:\t {temperature}°C\nPressure:\t {pressure} atm\nHumidity:\t {humidity}%\nOxygen:\t\t {oxygen}%\nAir Quality:\t {air_quality} ppm")

    # 1 saniyede bir güncelle
    label.after(1000, lambda: update_ambient(label))