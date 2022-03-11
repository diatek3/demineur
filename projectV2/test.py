from dem import *
import os

os.system("")

table = TABLE(int(input("nombre de ligne : ")))

table.tabletostr()



running = True

while running:


    table.load(input("entrez la colonne et la ligne : "))


