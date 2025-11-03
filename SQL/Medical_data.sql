


CREATE TABLE IF NOT EXISTS Doctors(
    doctor_id INTEGER PRIMARY Key AUTOINCREMENT,
    first_name TEXT NOT NULL CHECK(LENGTH(first_name) > 1),
    last_name TEXT NOT null CHECK(LENGTH(last_name) > 1),
    department TEXT NOT NULL,
    phone TEXT CHECK (LENGTH(phone) >= 7)

);





CREATE TABLE IF NOT EXISTS Medication(    
    Med_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT  NOT NULL,
    dosage real DEFAULT 0.0 CHECK (dosage>=0 AND dosage<10000),
    MedicationType TEXT NOT NULL CHECK (MedicationType in('tablet','Injection','liquid'))
    
);




CREATE TABLE IF NOT EXISTS  side_effects(
    side_effect_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Med_id INTEGER NOT NULL,
    description TEXT DEFAULT 'none',
    severity INTEGER not null DEFAULT 0 CHECK(severity>0),
    overdose INTEGER not null DEFAULT 1  CHECK(overdose>0),
    FOREIGN KEY(Med_id)REFERENCES Medication(Med_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Patients(
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT CHECK (gender in('Male','Female','Other')),
    first_name TEXT NOT NULL CHECK(LENGTH(first_name) > 1),
    last_name TEXT NOT NULL CHECK(LENGTH(last_name) > 1),
    date_of_birth DATE NOT NULL,
    email TEXT UNIQUE COLLATE NOCASE NOT null,
    phone TEXT not null CHECK (LENGTH(phone) >= 7),
    address TEXT not null,
    STATUS TEXT NOT NULL CHECK(STATUS IN ('active','discharged','deceased')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    

CREATE TABLE IF NOT EXISTS Patient_Doctor(
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    PRIMARY KEY (patient_id, doctor_id),
    FOREIGN KEY(patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY(doctor_id) REFERENCES Doctors(doctor_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Prescriptions(
    pharmacy_id INTEGER PRIMARY key AUTOINCREMENT,
    doctor_id INTEGER NOT NULL,
    patient_id INTEGER not NULL,
    Med_id INTEGER NOT NULL,
    STATUS TEXT NOT NULL CHECK(STATUS IN ('active', 'inactive', 'discontinued')),
    date_of_prescription DATE DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(patient_id) REFERENCES Patients(patient_id)
    ON DELETE CASCADE
    on UPDATE CASCADE,
    FOREIGN KEY(doctor_id) REFERENCES Doctors(doctor_id) ON DELETE CASCADE on UPDATE CASCADE,
    FOREIGN KEY(Med_id) REFERENCES Medication(Med_id) ON DELETE CASCADE on UPDATE CASCADE
);



