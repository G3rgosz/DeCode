Dekod="mnbvcxyíűáélkjhgfdsaóüöúőpoiuztrewq"
print("Válassz az alábbi lehetőségek közül:")
print("1 = Kódol    2 = DeKódol")
szam = int(input("Kérem írja be a választott művelet számát: "))
if (szam == 1):
	szoveg = str(input("Kódolandó szöveg: "))
	v=""
	karakterek="QWERTZUIOPŐÚÖÜÓASDFGHJKLÉÁŰÍYXCVBNMqwerztuiopőúasdfghjkléáűíyxcvbnmöüóÖÜÓ0123456789"
	kodolo="9876543210ÓÜÖóüömnbvcxyíűáélkjhgfds2úőp4i5tzr3wqMNBVCXYÍŰÁÉLKJHGFDSAÓÜÖÚŐPOIUZTREWQ"
	for x in range (0, len(szoveg)):
		i=karakterek.index(szoveg[x])
		v+=kodolo[i]
	def kodolt(v):
		v = v.replace("a","2")
		v = v.replace("e","3")
		v = v.replace("o","4")
		v = v.replace("u","5")
		ujSzoveg = ""
		for x in range(len(v)-1,-1,-1):
			ujSzoveg = ujSzoveg + v[x]
		return ujSzoveg
	print(kodolt(v))
elif (szam == 2):
	szoveg = str(input("DeKódolandó szöveg: "))
	v = ""
	karakterek="QWERTZUIOPŐÚÖÜÓASDFGHJKLÉÁŰÍYXCVBNMqwerztuiopőúasdfghjkléáűíyxcvbnmöüóÖÜÓ0123456789"
	kodolo="9876543210ÓÜÖóüömnbvcxyíűáélkjhgfds2úőp4i5tzr3wqMNBVCXYÍŰÁÉLKJHGFDSAÓÜÖÚŐPOIUZTREWQ"
	for x in range (0, len(szoveg)):
		i=kodolo.index(szoveg[x])
		v+=karakterek[i]
	def kodolt(v):
		v = v.replace("2","a")
		v = v.replace("3","e")
		v = v.replace("4","o")
		v = v.replace("5","u")
		ujSzoveg = ""
		for x in range(len(v)-1,-1,-1):
			ujSzoveg = ujSzoveg + v[x]
		return ujSzoveg
	print(kodolt(v))
else:
	print("nincs ilyen lehetőség")
	
	












	




