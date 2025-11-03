import sqlite3
from addFunctions import addDoctor,setDoctor
def addPrescription(patient_id, doctor_id, med_id, db_path="app.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:

        # Validate patient exists
        cursor.execute("SELECT 1 FROM Patients WHERE id = ?;", (patient_id,))
        if not cursor.fetchone():
            print(f"Error: Patient ID {patient_id} does not exist.")
            return
         # Validate doctor exists
        cursor.execute("SELECT 1 FROM Doctors WHERE id = ?;", (doctor_id,))
        if not cursor.fetchone():
            print(f"Error: Doctor ID {doctor_id} does not exist.")
            return
        # Validate medication exists
        cursor.execute("SELECT 1 FROM Medication WHERE id = ?;", (med_id,))
        if not cursor.fetchone():
            print(f"Error: Medication ID {med_id} does not exist.")
            return
        

        cursor.execute("""SELECT 1 FROM Patient_Doctor WHERE patient_id = ? AND doctor_id = ?;""",(patient_id,doctor_id))
        if not cursor.fetchone():
            print("This Doctor is not currently listed to this patient.")
            setDoctor(patient_id,doctor_id,db_path)
            print("Doctor has now been add your listing")

        cursor.execute("""
            INSERT INTO Prescriptions (doctor_id, patient_id, Med_id)
            VALUES (?, ?, ?);""",(doctor_id,patient_id,med_id))
        
        conn.commit()

        print("Prescription successfully added.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

    