from dearpygui.core import *
from dearpygui.simple import *

def boton_callback(sender, data):
    log_info("¡Haz hecho clic en el botón!")

with window("Ventana Principal"):
    add_text("Hola mundo con Dear PyGui")
    add_button("Haz clic aquí", callback=boton_callback)
    add_input_text("Ingresa tu nombre", default_value="")
    add_slider_float("Volumen", default_value=0.5, max_value=1.0)

start_dearpygui()
