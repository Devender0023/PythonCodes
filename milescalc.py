dist = input("Enter the number of kilometers you ran today? ")
print("ok, you said you ran " + str(dist) +" kms.") 
miles = float(dist)/1.60934
print(f"You ran {round(miles, 2)} miles today.")
