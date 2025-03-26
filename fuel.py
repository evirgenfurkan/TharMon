import tkinter as tk
import random

def create_fuel_section(parent):
    """ Yakıt bilgilerini gösteren bölüm """
    section = tk.LabelFrame(parent, text="Fuel Status", fg="lime", bg="black", font=("Arial", 9), bd=2)
    section.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    label = tk.Label(section, text="Veri Bekleniyor...", fg="white", bg="black", font=("Arial", 10), justify="left")
    label.pack(padx=10, pady=5, anchor="w")

    return label

def update_fuel(label):
    """ Yakıt verilerini rastgele simüle et ve ekrana yazdır """
    fuel_level = random.randint(50, 100)
    fuel_pressure = round(random.uniform(1.1, 1.8), 2)
    fuel_temp = random.randint(-50, 50)

    label.config(text=f"Fuel Level:\t {fuel_level}%\nTank Pressure:\t {fuel_pressure} Bar\nFuel Temp:\t {fuel_temp}°C")

    # 1 saniyede bir güncelle
    label.after(1000, lambda: update_fuel(label))

