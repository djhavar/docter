class Doctor():
    
    def __init__(self):
        print("this is class doctor")
        
    def BMI(weight, height):
        bmi = weight/(height*height)
        print("your BMI is "+str(bmi))
        
    def heart_rates(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("great your heart rate is normal")
            
        else:
            print("Your heart rate does not seem normal, please visit the clinic")

class Patient(Doctor):
     def __init__(self,name,weight,height,heart_rates):
         self.patient_name = name
         self.patient_weight = weight
         self.patient_height = height 
         self.patient_heart_rates = heart_rates
         
     def healthCheck(self):
          print("\n Patient Name"+self.patient_name)
          Doctor.BMI(self.patient_weight,self.patient_height)
          Doctor.heart_rates(self.patient_heart_rates)
          
patient1 = Patient("michael", 30, 0.9144, 80)
patient1.healthCheck()
          
patient2 = Patient("jesse", 40, 1, 120)
patient2.healthCheck()

