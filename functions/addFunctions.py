import sqlite3

def addMedication(name,dosage,MedicationType,db_path="app.db"):
    """Adds a Medication to the list of Medications you can pick from"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        
        cursor.execute("""
        INSERT INTO Medication (name,dosage,MedicationType)
        VALUES(?,?,?);""",(name,dosage,MedicationType))
    
        conn.commit()
        print(f"Medication {name} added successfully.")


    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return
    finally:
        conn.close()


def addDoctor(first_name, last_name, department, phone, db_path="app.db"):
    """adds a new Doctor to the Doctors table"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Doctors (first_name, last_name, department, phone)
            VALUES (?, ?, ?, ?);
        """, (first_name, last_name, department, phone))
        conn.commit()
        print(f"Doctor {first_name} {last_name} added successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def addPatient(gender, first_name, last_name, dob, email, phone, address, status="active", db_path="app.db"):
    """adds a Patient to the Patients table"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Patients (gender, first_name, last_name, date_of_birth, email, phone, address, STATUS)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (gender, first_name, last_name, dob, email, phone, address, status))
        conn.commit()
        print(f"Patient {first_name} {last_name} added successfully.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def addSideEffect(med_id, description, severity, overdose, db_path="app.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        # Validate medication exists
        cursor.execute("SELECT 1 FROM Medication WHERE id = ?;", (med_id,))
        if not cursor.fetchone():
            print(f"Error: Medication ID {med_id} does not exist.")
            return
        cursor.execute("""
            INSERT INTO side_effects (Med_id, description, severity, overdose)
            VALUES (?, ?, ?, ?);
        """, (med_id, description, severity, overdose))
        conn.commit()
        print(f"Side effect added for Medication ID {med_id}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


def setDoctor(patient_id, doctor_id, db_path="app.db"):
    """sets a  relashinship between a Patient and Doctor"""
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
        cursor.execute("""
            INSERT OR IGNORE INTO Patient_Doctor (patient_id, doctor_id)
            VALUES (?, ?);
        """, (patient_id, doctor_id))
        conn.commit()
        print(f"Doctor {doctor_id} linked to Patient {patient_id}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()