import csv

def extraction(fichier):
    """extrait les donnees d'un fichier csv en enlevant les cases vides"""

    csv_file = open(fichier , "r")
    reader = csv.reader(csv_file , delimiter = ";")
    table = []
    for row in reader:
        row2 = list(filter(None , row))###/!\ enleve les cases vides
        table.append(row2)
        
    csv_file.close()
    return(table)