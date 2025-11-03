import sqlite3

def seed_data(db_path="app.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # --- Doctors ---
    cursor.execute("SELECT COUNT(*) FROM Doctors;")
    if cursor.fetchone()[0] == 0:
        doctors = [
            ("Gregory", "House", "Diagnostics", "5551234"),
            ("Meredith", "Grey", "Surgery", "5555678"),
            ("John", "Watson", "General Practice", "5554321"),
        ]
        cursor.executemany("""
            INSERT INTO Doctors (first_name, last_name, department, phone)
            VALUES (?, ?, ?, ?);
        """, doctors)

    # --- Medications ---
    cursor.execute("SELECT COUNT(*) FROM Medication;")
    if cursor.fetchone()[0] == 0:
        medications = [
            ("Ibuprofen", 200, "tablet"),
            ("Amoxicillin", 500, "tablet"),
            ("Morphine", 10, "Injection"),
        ]
        cursor.executemany("""
            INSERT INTO Medication (name, dosage, MedicationType)
            VALUES (?, ?, ?);
        """, medications)

    # --- Side Effects ---
    cursor.execute("SELECT COUNT(*) FROM side_effects;")
    if cursor.fetchone()[0] == 0:
        side_effects = [
            (1, "Nausea", 2, 1),
            (2, "Allergic rash", 3, 1),
            (3, "Drowsiness", 1, 1),
        ]
        cursor.executemany("""
            INSERT INTO side_effects (Med_id, description, severity, overdose)
            VALUES (?, ?, ?, ?);
        """, side_effects)

    # --- Patients ---
    cursor.execute("SELECT COUNT(*) FROM Patients;")
    if cursor.fetchone()[0] == 0:
        patients = [
            ( "Male", "John", "Wick", "1980-03-10", "wilson@example.com", "5552222", "123 Main St", "active"),
            ( "Female", "Sarah", "Connor", "1975-05-12", "sarahc@example.com", "5553333", "456 Elm St", "active"),
        ]
        cursor.executemany("""
            INSERT INTO Patients  (gender, first_name, last_name, date_of_birth, email, phone, address, STATUS)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, patients)
    
    cursor.executemany(""" INSERT INTO Patient_Doctor (patient_id, doctor_id) 
        VALUES (?, ?) """, [ (1, 1), # John Wick has Alice Smith 
                            (1, 2), # John Wick also has Bob Johnson 
                            (2, 2) # Sarah Connor has Bob Johnson 
                            ])


    # --- Prescriptions ---
    cursor.execute("SELECT COUNT(*) FROM Prescriptions;")
    if cursor.fetchone()[0] == 0:
        prescriptions = [
            (1, 1,'active', 1),  # Doctor 1 → Patient 1 → Medication 1
            (2, 2,'active', 2),  # Doctor 2 → Patient 2 → Medication 2
        ]
        cursor.executemany("""
            INSERT INTO Prescriptions (doctor_id, patient_id, STATUS ,Med_id)
            VALUES (?, ?, ?,?);
        """, prescriptions)

    conn.commit()
    conn.close()
    print("Sample data inserted successfully (if tables were empty).")