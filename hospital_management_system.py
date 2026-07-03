import csv

while True:
    a = int(input("Enter who you want to deal with:-\n1.Patient\n2.Doctor\n3.exit\n"))
    if a ==1:
        print("Choose an option:- \n1.Enter new patient\n2.Search patient\n3.View all patients")
        b = int(input())
        if b == 1:
            patient_name = input("Enter patient name :")
            patient_age = input("Enter patient age :")
            patient_gender = input("Enter patient gender :")
            patient_issue = input("Issue faced by patient :")
            with open("doctors.csv", "r") as file:
                reader = csv.DictReader(file)

                found = False
                for row in reader:
                    if patient_issue == row["doctor_treats_issue"] :
                        doctor_name =row['doctor_name']
                        found = True
                        break

            if not found:
                print("Doctor not available.")  
            with open("patients.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([patient_name,patient_age,patient_gender,patient_issue,doctor_name])
            print("Patient successfully added!")    
        elif b == 2:
            search = input("Enter patient name : ")


            with open("patients.csv", "r") as file:
                reader = csv.DictReader(file)

                found = False
                for row in reader:
                    if search.lower() == row["patient_name"].lower(): 
                        print("\nPatient Found:")
                        print(f"Patient ID: {row['patient_id']}")
                        print(f"Name: {row['patient_name']}")
                        print(f"Age: {row['patient_age']}")
                        print(f"Gender: {row['patient_gender']}")
                        print(f"Issue: {row['patient_issue']}")
                        print(f"Doctor assigned:{row['doctor_name']}")
                        found = True
                        break
                if not found:
                    print("Patient not available")
                    
        elif b == 3:
            with open('patients.csv', "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    print(row["patient_name"])  
        else:
            print("invalid option")            
    elif a == 2:
        b = int(input("Choose an option:- \n1.Enter new doctor\n2.Search doctor\n3.View all doctors\n"))
        if b == 1:
            doctor_name = input("Enter doctor's name :")
            doctor_age = input("Enter doctor's age :")
            doctor_gender = input("Enter doctor's gender :")
            doctor_treats_issue = input("Doctor's speciality :")
            with open("doctors.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([doctor_name,doctor_age,doctor_gender,doctor_treats_issue])
                print("Doctor successfully added!")

        elif b == 2 :
            search = input("Name of the doctor: ")
            with open('doctors.csv', "r") as file:
                reader = csv.DictReader(file)

                found = False
                for row in reader:
                    if search.lower() == row["doctor_name"].lower(): 
                        print("\nDoctor Found:")
                        print(f"Name: {row['doctor_name']}")
                        print(f"Age: {row['doctor_age']}")
                        print(f"Gender: {row['doctor_gender']}")
                        print(f"Issue: {row['doctor_treats_issue']}")
                        found = True
                        break

                if not found:
                    print("Doctor not found.")
        elif b ==3 :
            with open('doctors.csv', "r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    print(row["doctor_name"])
        else:
            print("Invalid choice")             

    elif a == 3:
        print("Thank you for visiting Bhalla multispeciality hospital")
        break
    else:
        print("Invalid choice")


