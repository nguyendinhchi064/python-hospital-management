from tkinter import *
from PIL import ImageTk, Image

from src.domains.Employee import Employee
from src.domains.Doctor import Doctor
from src.domains.Room import Room
from src.domains.Patient import Patient
from src.methods.DoctorMethods import DoctorMethods
from src.methods.PatientMethods import PatientMethods
from src.methods.RoomMethods import RoomMethods
from src.methods.EmployeeMethods import EmployeeMethods
import database

def on_GUI_loaded():
  database.unzip_data()
  global doctors_list
  doctors_list = database.load_doctors()
  global workers_list
  workers_list = database.load_workers()
  global patients_list
  patients_list = database.load_patients()
  # global medicines_list
  # medicines_list = database.load_medicines()
  global pa_doc_list
  pa_doc_list = database.load_pa_doc()
  # global pa_med_list
  # pa_med_list = database.load_pa_med()
  
def on_exit():
  global doctors_list
  database.save_doctors(doctors_list)
  global workers_list
  database.save_workers(workers_list)
  global patients_list
  database.save_patients(patients_list)
  global medicines_list
  database.save_medicines(medicines_list)
  global pa_doc_list
  database.save_pa_doc(pa_doc_list)
  global pa_med_list
  database.save_pa_med(pa_med_list)
  database.zip_data()
  window.destroy()
  
global doctors_list
doctors_list = []
global workers_list
workers_list = []
global patients_list
patients_list = []
global medicines_list
medicines_list = []
global pa_doc_list
pa_doc_list = []
global pa_med_list
pa_med_list = []

window = Tk()

#TODO: GUI here

def main():
    on_GUI_loaded()
    window.protocol("WM_DELETE_WINDOW", on_exit)
    window.mainloop()

if __name__ == "__main__":
    main()