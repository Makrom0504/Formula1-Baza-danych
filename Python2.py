file = open("Plik_do-generowania-okrazen.sql","r")
sql_code = file.read()

 
i = 1950
while i<=2022:
	#napis = '4,"renault","Renault","French","http://en.wikipedia.org/wiki/Renault_in_Formula_One"\n'
    name = "Okrazenia-" + str(i) + ".sql"
    # print(name)
    #file2 = open(f"ala{i}.sql", "w")  # ala1.sql  ala2.sql
    file2 = open(name, "w")  # ala1.sql  ala2.sql
    t = sql_code.replace("<YEAR>", str(i))
    i += 1
    file2.write(t)
    file2.close()
    

 
file.close()
 