file = open("Plik_do_generowania.sql","r")
sql_code = file.read()
 
fileC = open("constructors.csv", "r")
fileC.readline()  #ignorowanie naglowka pliku
 
i = 1
for line in fileC:
	#napis = '4,"renault","Renault","French","http://en.wikipedia.org/wiki/Renault_in_Formula_One"\n'
    L = line.split(",")
    name = L[2][1:-1]
    id = L[0]
    name = name.replace(" ", "-")
    name = "Kierowcy-" + name + ".sql"
    # print(name)
    #file2 = open(f"ala{i}.sql", "w")  # ala1.sql  ala2.sql
    file2 = open(name, "w")  # ala1.sql  ala2.sql
    t = sql_code.replace("<NUMBER>", id)
    file2.write(t)
    file2.close()
 
 
file.close()
 