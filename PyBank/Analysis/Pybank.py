import os
import csv

#abro el archivo desde el cual voy a sacar la información para hacer el analisis.
dataopen=os.path.join("C:/Users/sebat/ClassRepository/python-challenge/PyBank/Resources/budget_data.csv")

#start with -1 because i need to not plus the first row
date_count=0

#with this variable, i am atrying to calculate the net income and losses

list_change=[]
total_change=0
change=0
total_net_income=0
#with code, i am opening the csv file
with open(dataopen) as csvfile:
    #with this, i am saying that i dont want to considerer the first row, because it doesnt contains numbers
    next(csvfile)
    csvreader=csv.reader(csvfile,delimiter=",")
    
    #aca empiezo a ver fila por fila.    
    for row in csvreader:
        #con esto cuento los meses
        date_count+=1
        #con esto voy sumando los profit and losses, hay que agregar el float para que sepa que hay numero negativos.
        total_net_income=total_net_income+float(row[1])
        
        #con esto calculo la diferencia entre el anterior y el de ahora
        if len(list_change)!=0:
            change=round(int(-change+float(row[1])),)
            #con esto guardo la diferencia en un arreglo 
        list_change.append(float(change))
        #con esto guardo solo el dato anterior.
        change=float(row[1])
    
    #esto era de prueba para ir viendo como se iba armando el arreglo
    #print(list_change)

    #con este for voy a calcular la suma total de los changes
    for x in list_change:
       total_change=total_change+float(x)

    #aca calculo el promedio de los cambios.
    average=round(total_change/(date_count-1),2)
    
    #de prueba para ver si el calculo estaba bien.
    #print(average)    

# esto es para ir probando que resultado me va dando el calculo.
print(f"Total Month: {date_count}")
print(f"Total: ${round(int(total_net_income),0)}")
print(f"Average Change:${float(average)}")
print(f"Greatest Increase in profits: (${round(max(list_change),)})")
print(f"Greatest Decrease in profits: (${round(min(list_change),)})")

#con esto creo el texto en el repository con el analisis
dataout=os.path.join("C:/Users/sebat/ClassRepository/python-challenge/PyBank/analysis/Analysis_Pybank.txt")
with open(dataout,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Total Month: {date_count}"])
    csvwriter.writerow([f"Total: ${round(int(total_net_income),0)}"])
    csvwriter.writerow([f"Average Change:${float(average)}"])
    csvwriter.writerow([f"Greatest Increase in profits: (${round(max(list_change),)})"])
    csvwriter.writerow([f"Greatest Decrease in profits: (${round(min(list_change),)})"])