import sqlite3

def gitDoctor(doctor_id,db_path="app.db"):
    """Retrives one Doctors infermatin"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        # find if there is a Doctor 
        cursor.execute("""SELECT doctor_id, first_name, last_name,department,phone 
        FROM Doctors
        WHERE doctor_id=?;""",(doctor_id,))
        
        find=cursor.fetchone()

        if not find:
            print(f"No Doctor with {doctor_id} as ID")
            
        
        return find
    
    except sqlite3.error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()


def gitMedication(med_id,db_path="app.db"):
    """Retrives one Medication infermatin"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        #find where the cursor Medication if is
        cursor.execute("""SELECT med_id, name, dosage,MedicationType 
        FROM Medication
        WHERE med_id=?;""",(med_id,))
        
        find=cursor.fetchone()
        # find if there is a Medication
        if not find:
            print(f"No  with Medication {med_id} as ID")

        return find
    
    except sqlite3.error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()


def gitPatients(patient_id,db_path="app.db"):
    """Retrives one patient infermatin"""
    conn =sqlite3.connect(db_path)
    cursor=conn.cursor()

    try:
            
        cursor.execute("""SELECT patient_id,gender,first_name,last_name,date_of_birth,email,
                           phone,address,STATUS,created_at 
                       FROM Patients WHERE patient_id=?""",(patient_id,))
            
        val=cursor.fetchone()
        if not val:
            print(f"no patient with{patient_id}")

        return val
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()



def gitDoctors(db_path="app.db"):
    """ all doctors from the database and return them as a list of tuples."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT doctor_id, first_name, last_name, department, phone
            FROM Doctors;
        """)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()
