import tkinter as tk
import random

def create_main_battery_section(parent):
    """ Batarya bilgilerini gösteren bölüm """
    section = tk.LabelFrame(parent, text="Main Battery Status", fg="lime", bg="black", font=("Arial", 9), bd=2)
    section.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

    main_battery_label = tk.Label(section, text="Loading...", fg="white", bg="black", font=("Arial", 10), justify="left")
    main_battery_label.pack(padx=10, pady=5, anchor='w')

    return main_battery_label

def create_aux_battery_section(parent):
    """ Batarya bilgilerini gösteren bölüm """
    section = tk.LabelFrame(parent, text="Aux Battery Status", fg="lime", bg="black", font=("Arial", 9), bd=2)
    section.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

    aux_battery_label = tk.Label(section, text="Loading...", fg="white", bg="black", font=("Arial", 10), justify="left")
    aux_battery_label.pack(padx=10, pady=5, anchor='w')

    return aux_battery_label

def update_main_battery(main_battery_label):

    main_soc = random.randint(0,100)
    main_voltage = random.randint(24, 30)
    main_current = random.randint(10, 20)
    main_temp = random.randint(30, 50)


    main_soc_line = f"State of Charge:\t {main_soc} %\n"
    main_voltage_line = f"Instant Voltage:\t {main_voltage} V\n"
    main_current_line = f"Instant Current:\t {main_current} A\n"
    main_temp_line = f"Temperature:\t {main_temp} °C\n"

    main_battery_label.config(text=f"{main_soc_line}{main_voltage_line}{main_current_line}{main_temp_line}")

    # 1 saniyede bir güncelle
    main_battery_label.after(1000, lambda: update_main_battery(main_battery_label))

def update_aux_battery(aux_battery_label):

    aux_soc = random.randint(0,100)
    aux_voltage = random.randint(12, 15)
    aux_current = random.randint(5, 10)
    aux_temp = random.randint(30,50)

    aux_soc_line = f"State of Charge:\t {aux_soc} %\n"
    aux_voltage_line =f"Instant Voltage:\t {aux_voltage} V\n"
    aux_current_line = f"Instant Current:\t {aux_current} A\n"
    aux_temp_line = f"Temperature:\t {aux_temp} °C"

    aux_battery_label.config(text=f"{aux_soc_line}{aux_voltage_line}{aux_current_line}{aux_temp_line}")

    # 1 saniyede bir güncelle
    aux_battery_label.after(1000, lambda: update_aux_battery(aux_battery_label))
