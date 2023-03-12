import pyautogui
import mysql.connector
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="estudiantes_db"
)
def guardar_formulario():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    fecha_nacimiento = fecha_nacimiento_entry.get()
    carrera = carrera_combobox.get()

    # Insertar los datos del formulario en la base de datos
    cursor = db.cursor()
    sql = "INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, carrera) VALUES (%s, %s, %s, %s)"
    val = (nombre, apellido, fecha_nacimiento, carrera)
    cursor.execute(sql, val)
    db.commit()
    db.close()

    pyautogui.alert(text="Los datos se han guardado correctamente.", title="Formulario", button='OK')


formulario_window = Tk()
formulario_window.title("Formulario")

# Crear los campos de entrada del formulario
nombre_label = ttk.Label(formulario_window, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5)
nombre_entry = ttk.Entry(formulario_window)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)

apellido_label = ttk.Label(formulario_window, text="Apellido:")
apellido_label.grid(row=1, column=0, padx=5, pady=5)
apellido_entry = ttk.Entry(formulario_window, width=12, background='darkblue', foreground='white')
apellido_entry.grid(row=1, column=1, padx=5, pady=5)

fecha_nacimiento_label = ttk.Label(formulario_window, text="Fecha de nacimiento:")
fecha_nacimiento_label.grid(row=2, column=0, padx=5, pady=5)
fecha_nacimiento_entry = DateEntry(formulario_window)
fecha_nacimiento_entry.grid(row=2, column=1, padx=5, pady=5)

carrera_label = ttk.Label(formulario_window, text="Carrera:")
carrera_label.grid(row=3, column=0, padx=5, pady=5)
carrera_combobox = ttk.Combobox(formulario_window, values=["Informática", "Administración", "Contabilidad"])
carrera_combobox.grid(row=3, column=1, padx=5, pady=5)


guardar_boton = ttk.Button(formulario_window, text="Guardar", command=guardar_formulario)
guardar_boton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Limpiar


formulario_window.mainloop()
