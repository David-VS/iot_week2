import circle as c
import zwembad as z

#roept achterliggend de __init__functie op
cirkel1 = c.Circle(2)
cirkel2 = c.Circle(5)


print(cirkel1)
print(cirkel1.omtrek())
print(cirkel2.omtrek())

pool = z.Zwembad(straal_zwembad=3,breedte_pad=0.5)
print(pool.prijs_omheining())
print(pool.prijs_pad())
print(pool.totaal())
