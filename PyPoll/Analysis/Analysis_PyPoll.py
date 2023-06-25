import os
import csv

#abro el archivo desde el cual voy a sacar la información para hacer el analisis.
dataopen=os.path.join("C:/Users/sebat/ClassRepository/python-challenge/PyPoll/Resources/election_data.csv")

#creo las variables que voy a utilizar para ir guardando los candidatos, los votos de cada uno, el porcentaje de cada uno y el total de votos
candidates=[]
votes=[]
votes_percentaje=[]
total_votes=0

with open(dataopen) as csvfile:
    #with this, i am saying that i dont want to considerer the first row, because it doesnt contains numbers
    
    next(csvfile)
    csvreader=csv.reader(csvfile,delimiter=",")
    
    #primero creamos la lista con los candidatos
    for row in csvreader:
        total_votes=total_votes+1
        #con este if, lo que vamos haciendo es ir creando a cada candidato en las listas.
        if not row[2] in candidates:
            candidates.append(str(row[2]))
            votes.append(0)
            #con esto, solo creo "la celda" del candidato en la lista de porcentajes, el cual sera calculado finalmente mas adelante.
            votes_percentaje.append(0)
        #con este for, lo que voy haciendo es ir sumando los votos de cada candidato.
        for x in candidates:
            if x==row[2]:
               votes[candidates.index(x)]= votes[candidates.index(x)]+1
    
    #esto es para ir verificando los datos que me van dando,
    print(total_votes)       
    print(candidates)
    print(votes)
    #print(len(candidates))
        
    #con este for, calculo y reemplazo los porcentajes finales para cada candidato
    for x in range(len(candidates)):
        votes_percentaje[x]=votes[x]/total_votes
    
    print(votes_percentaje)

#con esto calculo cual fue el candidato con mas fotos, y ademas veo en que celda de la lista se encuentra.
max_votes= max(votes_percentaje)
max_index= votes_percentaje.index(max_votes)

#A partir de aca, imprimo los resultados para compararlos con lo que sale en el assigment.
print(["Election Results"])
print(["-------------------------------------------------"])
print([f"Total Votes: {total_votes}"])
print(["-------------------------------------------------"])
for x in range(len(candidates)):
    print([f"{candidates[x]} : {round(votes_percentaje[x]*100,3)} % ({votes[x]})"])

print(["-------------------------------------------------"])
print([f"Winner: {candidates[max_index]}"])
print(["-------------------------------------------------"])

#con esto creo el texto en el repository con el analisis
dataout=os.path.join("C:/Users/sebat/ClassRepository/python-challenge/PyPoll/analysis/Analysis_PyPoll.csv")
with open(dataout,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------------------------------"])
    for x in range(len(candidates)):
        csvwriter.writerow([f"{candidates[x]} : {round(votes_percentaje[x]*100,3)} % ({votes[x]})"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Winner: {candidates[max_index]}"])
    csvwriter.writerow(["-------------------------------------------------"])
