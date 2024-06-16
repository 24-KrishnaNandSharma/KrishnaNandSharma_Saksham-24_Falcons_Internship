from matplotlib import pyplot as plt
Disease=['Common Cold','Diabetes','Hypertension (High Blood Pressure)','Asthma','Pneumonia','Arthritis','Migraine'] #Data lies on the X-asix  
Patient=[60,75,79,40,58,89,40]#Data lies on the Y-axis 
plt.pie(Patient, labels=Disease,autopct='%0.1f%%')
plt.show()