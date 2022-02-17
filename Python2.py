file = open("Plik_do-generowania-okrazen.sql","r")
sql_code = file.read()

 
i = 1950
while i<=2022:
    name = "Okrazenia-" + str(i) + ".sql"
    file2 = open(name, "w")
    t = sql_code.replace("<YEAR>", str(i))
    i += 1
    file2.write(t)
    file2.close()
    

 
file.close()
 