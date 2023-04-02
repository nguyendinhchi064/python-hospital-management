from tkinter import *
from tkinter import ttk
from tk import *
from src.domains.Person import *
from src.domains.Doctor import *
from src.domains.classConnection import *
import utils

def clear_entry(entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry):
    # Delete all Warnings
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=0,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=1,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=2,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=3,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=4,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=5,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=6,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=7,sticky="w")
    
    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gender_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    

    # Set selected_doctor to -1
    global selected_doctor
    selected_doctor = -1
    
def doc_add(doctors_list, doctor_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry):
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=0,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=1,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=2,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=3,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=4,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=5,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=6,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=7,sticky="w")
    
    id = id_entry.get()
    name = name_entry.get()
    gender = gender_entry.get()
    dob = dob_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    
# Validation
    valid_check = 0
# Validate genderer
    if len(gender) == 0:
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="EMPTY", font=("Work Sans", 14, "bold")).grid(column=6,row=2,sticky="w")
        valid_check += 1
    elif utils.invalid_gender(gender) == 1:
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="INVALID", font=("Work Sans", 14, "bold")).grid(column=6,row=2,sticky="w")
        valid_check += 1 
    # Validate Date of Birth
    if len(dob) == 0:
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="EMPTY", font=("Work Sans", 14, "bold")).grid(column=6,row=3,sticky="w")
        valid_check += 1
    elif utils.invalid_dob(dob) == 1:
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="INVALID", font=("Work Sans", 14, "bold")).grid(column=6,row=3,sticky="w")
        valid_check += 1
    # Validate Phone:
    if len(phone) != 0:
        if utils.invalid_phone(phone) == 1:
            Label(entry_frame, bg="#ceede8", fg="#7C809B", text="INVALID", font=("Work Sans", 14, "bold")).grid(column=6,row=4,sticky="w")
            valid_check += 1

    # If All Valid
    if valid_check == 0:
        # Add to doctors_list
        new_doc = doctors_list(id, name, gender, dob)
        if len(phone) > 0:
            new_doc.set_phone(phone)
        if len(email) > 0:
            new_doc.set_email(email)
        doctors_list.append(new_doc)

        # Display on Treeview
        doctor_tree.insert(parent="", index = "end", iid=id, text="", values=(id, name, gender, dob))

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        gender_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        
def doc_remove(doctors_list, doctor_tree, pa_doc_list):
    if len(doctor_tree.selection())>0:
        selected_doc = doctor_tree.selection()[0]
        doctor_id = doctor_tree.item(selected_doc, "values")[0]
        for classConnection in pa_doc_list:
            if classConnection.get_DoctorID() == doctor_id:
                pa_doc_list.remove(classConnection)
        
        for doctor in doctors_list:
            if doctor.get_id()== doctor_id:
                doctors_list.remove(doctor)
                break
        doctor_tree.delete(selected_doc)

        
def doc_update(doctors_list, pa_doc_list, doctor_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry):
    global selected_doctor
    if selected_doctor != -1:
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=0,sticky="w")
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=1,sticky="w")
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=2,sticky="w")
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=3,sticky="w")
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=4,sticky="w")
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=5,sticky="w")
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=6,sticky="w")
        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=7,sticky="w")
        
        id = id_entry.get()
        name = name_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
    
        # Validation
        valid_check = 0
        
        #Validate ID
        if len(id) == 0:
            Label(entry_frame, bg="#ceede8", fg="#7C809B", text="EMPTY", font=("Work Sans", 14, "bold")).grid(column=6,row=0,sticky="w")
            valid_check += 1
        elif utils.invalid_id(id, "D-") == 1:
            Label(entry_frame, bg="#ceede8", fg="#7C809B", text="INVALID", font=("Work Sans", 14, "bold")).grid(column=6,row=0,sticky="w")
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if id != doctor_tree.item(selected_doctor, "values")[0]:
                for doctor in doctors_list:
                    if doctor.get_id() == id:
                        Label(entry_frame, bg="#ceede8", fg="#7C809B", text="ID already exist", font=("Work Sans", 14, "bold")).grid(column=6,row=0,sticky="w")
                        valid_check += 1
                        break
        
        # Validate Name
        if len(name) == 0:
            Label(entry_frame, bg="#ceede8", fg="#7C809B", text="EMPTY", font=("Work Sans", 14, "bold")).grid(column=6,row=1,sticky="w")
            valid_check += 1

        # Validate genderer
        if len(gender) == 0:
            Label(entry_frame, bg="#ceede8", fg="#7C809B", text="EMPTY", font=("Work Sans", 14, "bold")).grid(column=6,row=2,sticky="w")
            valid_check += 1
        elif utils.invalid_gender(gender) == 1:
            Label(entry_frame, bg="#ceede8", fg="#7C809B", text="INVALID", font=("Work Sans", 14, "bold")).grid(column=6,row=2,sticky="w")
            valid_check += 1

        # Validate Date of Birth
        if len(dob) == 0:
            Label(entry_frame, bg="#ceede8", fg="#7C809B", text="EMPTY", font=("Work Sans", 14, "bold")).grid(column=6,row=3,sticky="w")
            valid_check += 1
        elif utils.invalid_dob(dob) == 1:
            Label(entry_frame, bg="#ceede8", fg="#7C809B", text="INVALID", font=("Work Sans", 14, "bold")).grid(column=6,row=3,sticky="w")
            valid_check += 1
        
        # Validate Phone:
        if len(phone) != 0 and phone != "_":
            if utils.invalid_phone(phone) == 1:
                Label(entry_frame, bg="#ceede8", fg="#7C809B", text="INVALID", font=("Work Sans", 14, "bold")).grid(column=6,row=4,sticky="w")
                valid_check += 1


        # If All Valid
        if valid_check == 0:
            for doctor in doctors_list:
                if doctor.get_id() == doctor_tree.item(selected_doctor, "values")[0]:
                    doctor.set_id(id)
                    doctor.set_name(name)
                    doctor.set_gender(gender)
                    doctor.set_dob(dob)
                    if len(phone) > 0:
                        doctor.set_phone(phone)
                    elif len(phone) == 0:
                        doctor.set_phone("_")
                    if len(email) > 0:
                        doctor.set_email(email)
                    elif len(email) == 0:
                        doctor.set_email("_")
                    break
            
            for classConnection in pa_doc_list:
                if classConnection.get_DoctorID() == doctor_tree.item(selected_doctor, "values")[0]:
                    classConnection.set_DoctorID(id)
                    
            
            doctor_tree.item(selected_doctor, text="", values = (id, name, gender, dob))
            selected_doctor = -1
        
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            gender_entry.delete(0, END)
            dob_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            


def doc_select(doctors_list, doctor_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry, phone_entry, email_entry):
    # Delete all Warnings
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=0,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=1,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=2,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=3,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=4,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=5,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=6,sticky="w")
    Label(entry_frame, bg="#ceede8", fg="#7C809B", text="                   ", font=("Work Sans", 14, "bold")).grid(column=6,row=7,sticky="w")
    
    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gender_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    

    # Show Selected Doctor Info
    if len(doctor_tree.selection())>0:
        global selected_doctor
        selected_doctor = doctor_tree.selection()[0]
        doc_id = doctor_tree.item(selected_doctor, "values")[0]
        for doctor in doctors_list:
            if doctor.get_id()== doc_id:
                id_entry.insert(0, doctor.get_id())
                name_entry.insert(0, doctor.get_name())
                gender_entry.insert(0, doctor.get_gender())
                dob_entry.insert(0, doctor.get_dob())
                phone_entry.insert(0, doctor.get_phone())
                email_entry.insert(0, doctor.get_email())
                
                break

def patients_assignment(doc_subwin, doctor_tree, pa_doc_list, patients_list, assigned_patients_list, unassigned_patients_list):
    if selected_doctor != -1:    
        doc_pa_subwin = Toplevel(doc_subwin)
        doc_pa_subwin.geometry("1920x1080")
        icon = PhotoImage(file = "images\Hospital_icon.png")
        doc_pa_subwin.iconphoto(False, icon)
        doc_pa_subwin.title("Patients Assignment")
        Frame(doc_pa_subwin, bg="#ceede8").place(x=0, y=0 ,width=1200/2, height=800)
        Label(doc_pa_subwin, text="ASSIGNED PATIENTS", bg="#ceede8", fg="white", font=("Work Sans", 20, "bold")).place(x=50,y=50,width=1200/2-100,height=50)
        Label(doc_pa_subwin, text="UNASSIGNED PATIENTS",bg="#ceede8", fg="white", font=("Work Sans", 20, "bold")).place(x=1200/2+50,y=50,width=1200/2-100,height=50)

        # Create list of assigned and unassigned patients for selected doctor
        assigned_patients_list.clear()
        unassigned_patients_list.clear()

        doctor_id = doctor_tree.item(selected_doctor, "values")[0]
        temp_list = []
        for classConnection in pa_doc_list:
            if classConnection.get_DoctorID() == doctor_id:
                temp_list.append(classConnection)
        for patient in patients_list:
            check = 0
            for classConnection in temp_list:
                if patient.get_id() == classConnection.get_PatientID():
                    check += 1
                    break
            if check == 0:
                unassigned_patients_list.append(patient)
            else:
                assigned_patients_list.append(patient)
        temp_list.clear()

        # Unassigned treeview
        # create Treeview
        unassigned_patients_tree = ttk.Treeview(doc_pa_subwin, selectmode="browse", show="headings")

        # define columns
        unassigned_patients_tree["columns"] = ("ID", "Name", "genderer", "Date of Birth")

        # Format columns
        unassigned_patients_tree.column("#0", width=0, stretch=NO)
        unassigned_patients_tree.column("ID", anchor="center", width=75)
        unassigned_patients_tree.column("Name",anchor="w", width=150)
        unassigned_patients_tree.column("genderer",anchor="center", width=75)
        unassigned_patients_tree.column("Date of Birth",anchor="center", width=125)

        # Create Headings
        unassigned_patients_tree.heading("#0", text="")
        unassigned_patients_tree.heading("ID", text="ID", anchor="center", command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "ID", False))
        unassigned_patients_tree.heading("Name", text="Name", anchor="center", command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "Name", False))
        unassigned_patients_tree.heading("genderer", text="genderer", anchor="center", command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "genderer", False))
        unassigned_patients_tree.heading("Date of Birth", text="Date of Birth", anchor="center", command= lambda: utils.sort_people_list_by_column(unassigned_patients_tree, unassigned_patients_list, "Date of Birth", False))

        unassigned_patients_tree.bind("<Motion>", "break")

        # Insert Data
        global unassigned_patients_count
        unassigned_patients_count = 0
        for patient in unassigned_patients_list:
            unassigned_patients_tree.insert(parent="", index = "end", iid=patient.get_id(), text="", values=(patient.get_id(), patient.get_name(), patient.get_gender(), patient.get_dob()))
            unassigned_patients_count += 1

        unassigned_patients_tree.place(x=1200/2+50, y=100, height=800-300, width=1200/2-100)

        #==========================================================================================
        # Assigned treeview
        assigned_patients_tree = ttk.Treeview(doc_pa_subwin, selectmode="browse", show="headings")

        # define columns
        assigned_patients_tree["columns"] = ("ID", "Name", "genderer", "Date of Birth")

        # Format columns
        assigned_patients_tree.column("#0", width=0, stretch=NO)
        assigned_patients_tree.column("ID", anchor="center", width=75)
        assigned_patients_tree.column("Name",anchor="w", width=150)
        assigned_patients_tree.column("genderer",anchor="center", width=75)
        assigned_patients_tree.column("Date of Birth",anchor="center", width=125)

        # Create Headings
        assigned_patients_tree.heading("#0", text="")
        assigned_patients_tree.heading("ID", text="ID", anchor="center", command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "ID", False))
        assigned_patients_tree.heading("Name", text="Name", anchor="center", command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "Name", False))
        assigned_patients_tree.heading("genderer", text="genderer", anchor="center", command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "genderer", False))
        assigned_patients_tree.heading("Date of Birth", text="Date of Birth", anchor="center", command= lambda: utils.sort_people_list_by_column(assigned_patients_tree, assigned_patients_list, "Date of Birth", False))

        assigned_patients_tree.bind("<Motion>", "break")

        # Insert Data
        global assigned_patients_count
        assigned_patients_count = 0
        for patient in assigned_patients_list:
            assigned_patients_tree.insert(parent="", index = "end", iid=patient.get_id(), text="", values=(patient.get_id(), patient.get_name(), patient.get_gender(), patient.get_dob()))
            assigned_patients_count += 1

        assigned_patients_tree.place(x=50, y=100, height=800-300, width=1200/2-100)

        # ===============================================================================
        # Count
        Label(doc_pa_subwin, text=f"COUNT: {assigned_patients_count}", anchor="e", bg="#ceede8", fg="black", font=("Work Sans", 16, "bold")).place(x=1200/4+50,y=800-150,width=200,height=50)
        Label(doc_pa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor="e",fg="black", font=("Work Sans", 16, "bold")).place(x=1200/4*3+50,y=800-150,width=200,height=50)

        # ===============================================================================
        # Buttons
        assign_patient_button = Button(doc_pa_subwin, text="ASSIGN PATIENT", font=("Work Sans", 16, "bold"), fg="white", bg="#ceede8", relief="ridge",
            activebackground="#ceede8", activeforeground="white", command=lambda: assign_patient(doc_pa_subwin, 1200, 800, unassigned_patients_tree, assigned_patients_tree, unassigned_patients_list, assigned_patients_list, patients_list, doctor_id, pa_doc_list))
        assign_patient_button.place(x=1200/2+50, y=800-150, width=250, height=50)

        unassign_patient_button = Button(doc_pa_subwin, text="UNASSIGN PATIENT", font=("Work Sans", 16, "bold"), fg="#ceede8", relief="ridge",
            activebackground="#ceede8", activeforeground="white", command=lambda: unassign_patient(doc_pa_subwin, 1200, 800, unassigned_patients_tree, assigned_patients_tree, unassigned_patients_list, assigned_patients_list, patients_list, doctor_id, pa_doc_list))
        unassign_patient_button.place(x=50, y=800-150, width=250, height=50)

def assign_patient(doc_pa_subwin, unassigned_patients_tree, assigned_patients_tree, unassigned_patients_list, assigned_patients_list, patients_list, doctor_id, pa_doc_list):
    if len(unassigned_patients_tree.selection())>0:
        selected_unassigned_patient = unassigned_patients_tree.selection()[0]
        patient_id = unassigned_patients_tree.item(selected_unassigned_patient, "values")[0]

        pa_doc_list.append(pa_doc_list(patient_id, doctor_id))

        global unassigned_patients_count
        global assigned_patients_count
        
        assigned_patients_tree.insert(parent="", index = "end", iid=patient_id, text="", values=(unassigned_patients_tree.item(selected_unassigned_patient, "values")))
        unassigned_patients_tree.delete(selected_unassigned_patient)
        
        for patient in patients_list:
            if patient.get_id()==patient_id:
                assigned_patients_list.append(patient)
                break

        for patient in unassigned_patients_list:
            if patient.get_id()==patient_id:
                unassigned_patients_list.remove(patient)
                break
    
        unassigned_patients_count -= 1
        assigned_patients_count += 1
        # ===============================================================================
        # Count
        Label(doc_pa_subwin, text=f"COUNT: {assigned_patients_count}", anchor="e", bg="#ceede8", fg="black", font=("Work Sans", 16, "bold")).place(x=1200/4+50,y=800-150,width=200,height=50)
        Label(doc_pa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor="e",fg="black", font=("Work Sans", 16, "bold")).place(x=1200/4*3+50,y=800-150,width=200,height=50)

def unassign_patient(doc_pa_subwin, unassigned_patients_tree, assigned_patients_tree, unassigned_patients_list, assigned_patients_list, patients_list, doctor_id, pa_doc_list):
    if len(assigned_patients_tree.selection())>0:
        selected_assigned_patient = assigned_patients_tree.selection()[0]
        patient_id = assigned_patients_tree.item(selected_assigned_patient, "values")[0]

        for classConnection in pa_doc_list:
            if classConnection.get_PatientID() == patient_id and classConnection.get_DoctorID() == doctor_id:
                pa_doc_list.remove(classConnection)
    
        global unassigned_patients_count
        global assigned_patients_count

        unassigned_patients_tree.insert(parent="", index = "end", iid=patient_id, text="", values=(assigned_patients_tree.item(selected_assigned_patient, "values")))
        assigned_patients_tree.delete(selected_assigned_patient)

        for patient in patients_list:
            if patient.get_id()==patient_id:
                unassigned_patients_list.append(patient)
                break

        for patient in assigned_patients_list:
            if patient.get_id()==patient_id:
                assigned_patients_list.remove(patient)
                break

        unassigned_patients_count += 1
        assigned_patients_count -= 1
        # Count
        Label(doc_pa_subwin, text=f"COUNT: {assigned_patients_count}", anchor="e", bg="#ceede8", fg="#2FDBED", font=("Work Sans", 16, "bold")).place(x=1200/4+50,y=800-150,width=200,height=50)
        Label(doc_pa_subwin, text=f"COUNT: {unassigned_patients_count}", anchor="e",bg="#ceede8", fg="#2FDBED", font=("Work Sans", 16, "bold")).place(x=1200/4*3+50,y=800-150,width=200,height=50)

def doc_press(window, doctors_list, patients_list, pa_doc_list):
    global selected_doctor
    selected_doctor = -1

    doc_subwin = Toplevel(window)
    doc_subwin.geometry("1920x1080")
    icon = PhotoImage(file = "images\Hospital_icon.png")
    doc_subwin.iconphoto(False, icon)
    doc_subwin.title("Doctors Information Management")
    Frame(doc_subwin, bg="#ceede8").place(x=0, y=0 ,width=1200/2, height=800)
    
    assigned_patients_list = []
    unassigned_patients_list = []

    #=====================================================================================
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
        background = "silver",
        foreground = "black",
        rowheight = 25,
        font=("Work Sans", 12),
        fieldbackground = "silver"
        )
    style.configure("Treeview.Heading", font=("Work Sans", 16,"bold"))
    
    style.map("Treeview", background=[("selected", "#ceede8")])

    # Create TreeView List
    doctor_tree = ttk.Treeview(doc_subwin, selectmode="browse", show="headings")

    # Define columns
    doctor_tree["columns"] = ("ID", "Name", "genderer", "Date of Birth")

    # Format columns
    doctor_tree.column("#0", width=0, stretch=NO)
    doctor_tree.column("ID", anchor="center", width=75)
    doctor_tree.column("Name",anchor="w", width=150)
    doctor_tree.column("genderer",anchor="center", width=75)
    doctor_tree.column("Date of Birth",anchor="center", width=125)

    # Create Headings
    doctor_tree.heading("#0", text="")
    doctor_tree.heading("ID", text="ID", anchor="center", command= lambda: utils.sort_people_list_by_column(doctor_tree, doctors_list, "ID", False))
    doctor_tree.heading("Name", text="Name", anchor="center", command= lambda: utils.sort_people_list_by_column(doctor_tree, doctors_list, "Name", False))
    doctor_tree.heading("genderer", text="genderer", anchor="center", command= lambda: utils.sort_people_list_by_column(doctor_tree, doctors_list, "genderer", False))
    doctor_tree.heading("Date of Birth", text="Date of Birth", anchor="center", command= lambda: utils.sort_people_list_by_column(doctor_tree, doctors_list, "Date of Birth", False))

    doctor_tree.bind("<Motion>", "break")
    
    # Insert Data
    for doctor in doctors_list:
        doctor_tree.insert(parent="", index = "end", iid=doctor.get_id(), text="", values=(doctor.get_id(), doctor.get_name(), doctor.get_gender(), doctor.get_dob()))
        
    doctor_tree.place(x=1200/2+50, y=50, height=800-250, width=1200/2-100)


    #=========================================================================================
    
    # Doctor Control
    Label(doc_subwin, bg="#ceede8", fg="white", text="DOCTORS MANAGEMENT", font=("Work Sans", 20, "bold")).place(x=50, y=25, width=1200/2-100, height=50)
    Frame(doc_subwin, bg="#7C809B").place(x=50, y=85, width=1200/2-100, height=2)
    entry_frame = Frame(doc_subwin, bg="#ceede8")
    entry_frame.place(x=50, y=100, width=1200/2-100, height=800/2)
    Frame(doc_subwin, bg="#7C809B").place(x=50, y=350, width=1200/2-100, height=2)
    Label(doc_subwin, text="  - Entries marked with " * " must not be empty ", anchor="w", bg="#ceede8", fg="white", font=("Work Sans", 12, "bold")).place(x=50, y=360, height=30)
    Label(doc_subwin, text="  - ID must be   D-xxx  ", anchor="w", bg="#ceede8", fg="white", font=("Work Sans", 12, "bold")).place(x=50, y=385, height=30)
    Label(doc_subwin, text="  - genderer must be  M  or  F  ", anchor="w", bg="#ceede8", fg="white", font=("Work Sans", 12, "bold")).place(x=50, y=410, height=30)
    Label(doc_subwin, text="  - Date of Birth must be  dd/mm/yyyy  ", anchor="w", bg="#ceede8", fg="white", font=("Work Sans", 12, "bold")).place(x=50, y=435, height=30)
    Label(doc_subwin, text="  - Phone & Salary must be numbers ", anchor="w", bg="#ceede8", fg="white", font=("Work Sans", 12, "bold")).place(x=50, y=460, height=30)


    # Column 0: ( * )
    Label(entry_frame, bg="#ceede8", fg="red", text="( * )", font=("Work Sans", 14, "bold")).grid(column=0, row=0)
    Label(entry_frame, bg="#ceede8", fg="red", text="( * )", font=("Work Sans", 14, "bold")).grid(column=0, row=1)
    Label(entry_frame, bg="#ceede8", fg="red", text="( * )", font=("Work Sans", 14, "bold")).grid(column=0, row=2)
    Label(entry_frame, bg="#ceede8", fg="red", text="( * )", font=("Work Sans", 14, "bold")).grid(column=0, row=3)
    
    # Column 1: |
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=1, row=0)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=1, row=1)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=1, row=2)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=1, row=3)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=1, row=4)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=1, row=5)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=1, row=6)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=1, row=7)

    # Column 2: Atribute
    Label(entry_frame, bg="#ceede8", fg="white", text=" - ID - ", font=("Work Sans", 14, "bold")).grid(column=2, row=0)
    Label(entry_frame, bg="#ceede8", fg="white", text=" - Name - ", font=("Work Sans", 14, "bold")).grid(column=2, row=1)
    Label(entry_frame, bg="#ceede8", fg="white", text=" - genderer - ", font=("Work Sans", 14, "bold")).grid(column=2, row=2)
    Label(entry_frame, bg="#ceede8", fg="white", text=" - DoB - ", font=("Work Sans", 14, "bold")).grid(column=2, row=3)
    Label(entry_frame, bg="#ceede8", fg="white", text=" - Phone - ", font=("Work Sans", 14, "bold")).grid(column=2, row=4)
    Label(entry_frame, bg="#ceede8", fg="white", text=" - Email - ", font=("Work Sans", 14, "bold")).grid(column=2, row=5)
    Label(entry_frame, bg="#ceede8", fg="white", text=" - Dept - ", font=("Work Sans", 14, "bold")).grid(column=2, row=6)
    Label(entry_frame, bg="#ceede8", fg="white", text=" - Salary - ", font=("Work Sans", 14, "bold")).grid(column=2, row=7)

    # Column 3: |
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=3, row=0)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=3, row=1)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=3, row=2)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=3, row=3)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=3, row=4)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=3, row=5)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=3, row=6)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=3, row=7)
    
    # Column 4: Entries
    id_entry = Entry(entry_frame)
    id_entry.grid(column=4,row=0)

    name_entry = Entry(entry_frame)
    name_entry.grid(column=4,row=1)

    gender_entry = Entry(entry_frame)
    gender_entry.grid(column=4,row=2)

    dob_entry = Entry(entry_frame)
    dob_entry.grid(column=4,row=3)

    phone_entry = Entry(entry_frame)
    phone_entry.grid(column=4,row=4)

    email_entry = Entry(entry_frame)
    email_entry.grid(column=4,row=5)

    dept_entry = Entry(entry_frame)
    dept_entry.grid(column=4,row=6)

    salary_entry = Entry(entry_frame)
    salary_entry.grid(column=4,row=7)

    # Column 5: |
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=5, row=0)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=5, row=1)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=5, row=2)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=5, row=3)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=5, row=4)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=5, row=5)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=5, row=6)
    Label(entry_frame, bg="#ceede8", fg="white", text=" | ", font=("Work Sans", 14, "bold")).grid(column=5, row=7)

    # Buttons
    select_doctor_button = Button(doc_subwin, text="SELECT",anchor="center",font=("Work Sans", 12,"bold"), bg="#ceede8",fg="white", relief="ridge",
        activebackground="#ceede8", activeforeground="white", command=lambda: doc_select(doctors_list, doctor_tree, entry_frame, id_entry, name_entry, gender_entry, dob_entry,phone_entry,email_entry,dept_entry,salary_entry))
    select_doctor_button.place(x=1200/2+50, y=800-75-85, width=150, height=50)

    patients_assignment_button = Button(doc_subwin, text="PATIENTS ASSIGNMENT",anchor="center",font=("Work Sans", 12,"bold"), fg="#ceede8", relief="ridge",
        activebackground="#ceede8", activeforeground="white", command=lambda: patients_assignment(doc_subwin, doctor_tree, 1200, 800, pa_doc_list, patients_list, assigned_patients_list, unassigned_patients_list))
    patients_assignment_button.place(x=50,y=800-75-85, width=1200/2-100, height=50)