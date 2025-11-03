import sqlite3


def ShowYourMedication(Patient_Id,db_path="app.db"):
    """Shows all of your Medication including dosage, type, and side effects. """    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()    

    cursor.execute("""
    SELECT
        m.Med_id, 
        m.name, 
        m.dosage, 
        m.MedicationType, 
        d.first_name || ' ' || d.last_name AS doctor_name,
        p.date_of_prescription,
        s.description, 
        s.severity, 
        s.overdose
    FROM Prescriptions p
    JOIN Medication m ON p.Med_id = m.Med_id
    JOIN Doctors d ON p.doctor_id = d.doctor_id               
    LEFT JOIN side_effects s ON m.Med_id = s.Med_id
    WHERE p.patient_id = ?
    """, (Patient_Id,))
    
    results = cursor.fetchall()
    conn.close()
# Group data by medication
    meds = {}
    for med_id, name, dosage, med_type, doctor_name, presc_date, side_desc, side_sev, side_ovr in results:
        if med_id not in meds:
            meds[med_id] = {
                "name": name,
                "dosage": dosage,
                "type": med_type,
                "doctor": doctor_name,
                "date": presc_date,
                "side_effects": []
            }
        if side_desc and side_desc != 'none':
            meds[med_id]["side_effects"].append({
                "description": side_desc,
                "severity": side_sev,
                "overdose": side_ovr
            })
    
    # Print grouped results
    print(f"Medications for patient {Patient_Id}:")
    for med in meds.values():
        print(f"- {med['name']} ({med['type']}, {med['dosage']}mg), prescribed by Dr. {med['doctor']} on {med['date']}")
        if med['side_effects']:
            for se in med['side_effects']:
                print(f"   Side effect: {se['description']}, Severity: {se['severity']}, Overdose factor: {se['overdose']}")
    
    return meds



    
   