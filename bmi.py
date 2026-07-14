

def calculate_bmi(weight,height):
    return round(weight / (height **2), 2)

def bmi_category(bmi):
   if bmi < 18.5: 
    
         return    "unrderweight" 
  
   elif bmi  < 24.9:
 
        return "normal"
  
   elif bmi < 30:

        return "overwheight"
    
   else:

       return "obese"   
    
print("--------------------------------------------------------")
print("                          BMI Calculator")
print("--------------------------------------------------------")
 
while True:

 weight=float(input("Enter your weight in kg").replace(",","."));

 height=float(input("Enter your height in m").replace(",","."));


 bmi = calculate_bmi(weight, height)

 if weight <= 0 or height <= 0:
        print("\nError: Weight and height must be greater than zero.")
        continue
 print("\n-----------------------BMI report----------------------------") 
 print("Weight",weight, "kg")
 print("Height",height, "m")
 print("BMI",bmi)
 print("category",bmi_category(bmi))


 answer =input("\n---------------would you like another calculation? (y/n)").lower()

 if answer !="y":

   print("\nThank you for using BMI Calculator!")
        
   break

