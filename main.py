from functions.db_setup import  initialize_database
from functions.addFunctions import addMedication 
from functions.getFunctions import gitDoctor
from functions.seed_data import seed_data
from functions.MedicationDef import ShowYourMedication
from functions.viewTools import viewTable
def main():
    tables=["Doctors","Medication","side_effects","Patients","Patient_Doctor","Prescriptions"]
    initialize_database()
    print("Database initialized.")
    #seed_data()
    #addMedication("Flu_Shot",15,"Injection")
    #ShowYourMedication(1,'app.db')
    test =gitDoctor(1)

    
    
    viewTable(tables[3])
    #print(test)
    return

if __name__ == "__main__":  
    main()   