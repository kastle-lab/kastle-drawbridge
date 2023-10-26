patients = []

def addPatient():
     global patients
     f = input("Enter the first name of the patient: ")
     l = input("Enter the last name of the patient: ")
     a = int(input("Enter the age of the patient: "))
     w = int(input("Enter the weight of the patient: "))
     p = {'firstName': f, 'lastName': l, 'age': a, 'weight': w}
     patients.append(p)
     
def displayPatients():
     print("")
     print("Patients Currently In Hospital: ")
     for patient in patients:
         print(patient['lastName']+',', patient['firstName'], "- Age:", patient['age'])
         print("")
     
def main():
     while True:
         addPatient()
         displayPatients()
         
if __name__ == "__main__":
     main()
