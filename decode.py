Dekod="mnbvcxyíűáélkjhgfdsaóüöúőpoiuztrewq"
print("Válassz az alábbi lehetőségek közül:")
print("1 = Kódol    2 = DeKódol")
szam = int(input("Kérem írja be a választott művelet számát: "))
if (szam == 1):
	szoveg = str(input("Kódolandó szöveg: "))
	def kodolt(szoveg):
		szoveg = szoveg.replace("a","2")
		szoveg = szoveg.replace("e","3")
		szoveg = szoveg.replace("o","4")
		szoveg = szoveg.replace("u","5")
		ujSzoveg = ""
		for x in range(len(szoveg)-1,-1,-1):
			ujSzoveg = ujSzoveg + szoveg[x]
		return ujSzoveg
	print(kodolt(szoveg))
elif (szam == 2):
	szoveg = str(input("DeKódolandó szöveg: "))
	def kodolt(szoveg):
		szoveg = szoveg.replace("2","a")
		szoveg = szoveg.replace("3","e")
		szoveg = szoveg.replace("4","o")
		szoveg = szoveg.replace("5","u")
		ujSzoveg = ""
		for x in range(len(szoveg)-1,-1,-1):
			ujSzoveg = ujSzoveg + szoveg[x]
		return ujSzoveg
	print(kodolt(szoveg))
else:
	print("nincs ilyen lehetőség")
	
	












	




