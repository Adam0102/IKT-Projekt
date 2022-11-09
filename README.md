# Programnév: KKFood

#   A programunk egy ételrendelős oldalhoz fog hasonlítani, amiben meg lehet adni, hogy személyesen venné-e át vagy pedig kiszállítsuk. Amennyiben kiszállítsuk, akkor milyen címre kérné (ezt elmenti egy file-ba és a következő rendelésnél előhívható). Mindezek után ki tudja választani, hogy mit szeretne enni, pl.: melegszendvics, leves, főétel, desszert, stb.(ezeket 'ittfogyasztás' lehetőség alatt is lehetséges) Lesznek menüs kaják is, és itallap is elérhető lesz. Megtekinthetőek lesznek az eddigi rendelések is illetve a paraméterek árai, összesített árai és kosármódosításra is lehetőséget ad(az ár is vele változik). A lényeg az lesz, hogy átlátható legyen a program működésé, és könnyen kezelhető. 

# FELADATOK:
# A program indítása és a név megadása után az ügyfél megtudja, hogy regisztrált/belépő felhasználó. Nevét, telefonszámát adatok.csv file-ban kezeli a program. Belépés után az ügyfél egy menüvel találkozik,ahol eldöntheti a menü pontjai alapján fogyasztásának lehetőségét.(helybenfogyasztás -> itt maradok,hozzák ki /elvitel -> értemegyek, elhozom). Mindkét opció esetén: itallap és étlap közti választási lehetőség adott. Az ételeket/italokat kategória alapján választhatja ki, melyeket kiválasztásuk után kosárba helyezhet. A kosárt megtekintheti, módsíthatja, akár a vásárlást be is fejezheti fizetés után.


## user adatok.csv tartalma:
- id
- név
- telefonszám

## etelek.csv tartalma:
- id
- név
- leírás
- ár
- kategória

## ital.csv tartalma:
- id
- név
- leírás
- ár
- kategória

### Étel kategória lehet:
- leves
- főétel
- tészta
- menü
- desszert
- pizza

### Ital kategória lehet:
- szénsavas
- szénsavmentes
- alkoholos
- alkoholmentes

## rendelés.csv tartalmazza:
- id
- user id
- étel id
- rendelés dátuma
- ár

## kosar.csv tartalmazza:
- rendelés 
- megrendelendő étel/ital
- összeg