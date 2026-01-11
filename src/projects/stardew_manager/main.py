from src.lote import lote, lotes

l = lotes()

l.create(lote("zanahoria", 200, 3))
l.create(lote("vino", 50, 1))

print("=== Día 0 ===")
print("Creciendo:", l.viewGrowing())
print("Listos:", l.viewReady())

l.passDay()
print("=== Día 1 ===")
print("Creciendo:", l.viewGrowing())
print("Listos:", l.viewReady())

l.passDay()
print("=== Día 2 ===")
print("Creciendo:", l.viewGrowing())
print("Listos:", l.viewReady())

l.passDay()
print("=== Día 3 ===")
print("Creciendo:", l.viewGrowing())
print("Listos:", l.viewReady())

cosecha = l.harvest(0)
print("Cosechado:", cosecha)
