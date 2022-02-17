file = open("Plik_do_generowania.sql","r")
sql_code = file.read()
 
fileC = open("constructors.csv", "r")
fileC.readline() 
 
i = 1
for line in fileC:

    L = line.split(",")
    name = L[2][1:-1]
    id = L[0]
    name = name.replace(" ", "-")
    name = "Kierowcy-" + name + ".sql"
    file2 = open(name, "w")
    t = sql_code.replace("<NUMBER>", id)
    file2.write(t)
    file2.close()
 
 
file.close()
 