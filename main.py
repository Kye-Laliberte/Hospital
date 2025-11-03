from functions.db_setup import  initialize_database
from functions.seed_data import seed_data
from functions.MedicationDef import ShowYourMedication
def main():

    initialize_database()
    print("Database initialized.")
    #seed_data()
    ShowYourMedication(1,'app.db')
    return

if __name__ == "__main__":  
    main()   