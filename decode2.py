szoveg="proba"
"""
print(ord('A'))
print(ord('a'))
print()

kodolt=""

for x in range (0, len(szoveg)):
	kodolt+=str(ord(szoveg[x])*3+13)"""
karakterek="QWERTZUIOPŐÚÖÜÓASDFGHJKLÉÁŰÍYXCVBNMqwerztuiopőúasdfghjkléáűíyxcvbnmöüóÖÜÓ0123456789"
kodolo="9876543210ÓÜÖóüömnbvcxyíűáélkjhgfds2úőp4i5tzr3wqMNBVCXYÍŰÁÉLKJHGFDSAÓÜÖÚŐPOIUZTREWQ"
kodolt=""
for x in range (0, len(szoveg)):
	i=karakterek.index(szoveg[x])
	kodolt+=kodolo[i]
print(kodolt)