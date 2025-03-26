import tkinter as tk
from timer import create_timer, update_timer
from ambient import create_ambient_section, update_ambient
from fuel import create_fuel_section, update_fuel
from battery import create_main_battery_section, update_main_battery, create_aux_battery_section, update_aux_battery

# Ana pencereyi oluştur
root = tk.Tk()
root.title("TharMon")
# root.attributes('-fullscreen', True)

# ESC tuşuna basıldığında tam ekrandan çık
def exit_fullscreen(event=None):
    root.attributes('-fullscreen', False)

root.bind("<Escape>", exit_fullscreen)

# Ana frame
frame = tk.Frame(root, bg="black")
frame.pack(expand=True, fill="both")

## Zamanlayıcı oluştur ve başlat
timer_label = create_timer(frame)
update_timer(timer_label)

# Bölümleri ekle ve güncelle
ambient_label = create_ambient_section(frame)
update_ambient(ambient_label)

fuel_label = create_fuel_section(frame)
update_fuel(fuel_label)

main_battery_label = create_main_battery_section(frame)
update_main_battery(main_battery_label)

aux_battery_label = create_aux_battery_section(frame)
update_aux_battery(aux_battery_label)

# Ana döngüyü başlat
root.mainloop()
