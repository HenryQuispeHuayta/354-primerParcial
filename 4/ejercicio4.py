# from collections import Iterator
from kanren import run, var, eq, Relation, facts, conde

a = var()
b = var()

padre = Relation()
madre = Relation()
hijo = Relation()
hija = Relation()
hermano = Relation()
hermana = Relation()
esposo = Relation()
esposa = Relation()
padres = Relation()

facts(padre,('Enrique','Henry'),('Enrique','Lady'),('Juan','Susan'),('Juan','Claudia'),('Valentin','Jose'),('Carlos','Marcelo'),('Carlos','Oscar'),('Javier','Samuel'),('Javier','Rebeca'),('Abuelo1','Enrique'),('Abuelo1','Paola'),('Abuelo1','Valentin'),('Abuelo2','Elena'),('Abuelo2','Juana'),('Abuelo2','Javier'))
facts(madre,('Elena','Henry'),('Elena','Lady'),('Paola','Susan'),('Paola','Claudia'),('Tia1','Jose'),('Juana','Marcelo'),('Juana','Oscar'),('Crecencia','Samuel'),('Crecencia','Rebeca'),('Abuela1','Enrique'),('Abuela1','Paola'),('Abuela1','Valentin'),('Abuela2','Elena'),('Abuela2','Juana'),('Abuela2','Javier'))
facts(hijo,('Henry','Enrique'),('Henry','Elena'),('Jose','Valentin'),('Jose','Tia1'),('Marcelo','Carlos'),('Marcelo','Juana'),('Oscar','Carlos'),('Oscar','Juana'),('Samuel','Javier'),('Samuel','Crecencia'),('Enrique','Abuelo1'),('Valentin','Abuelo1'),('Enrique','Abuela1'),('Valentin','Abuela1'),('Javier','Abuelo2'),('Javier','Abuela2'))
facts(hija,('Lady','Enrique'),('Lady','Elena'),('Susan','Juan'),('Susan','Paola'),('Claudia','Juan'),('Claudia','Paola'),('Rebeca','Javier'),('Rebeca','Crecencia'),('Paola','Abuelo1'),('Paola','Abuela1'),('Elena','Abuelo2'),('Elena','Abuela2'),('Juana','Abuelo2'),('Juana','Abuela2'))
facts(hermano,('Henry','Lady'),('Marcelo','Oscar'),('Oscar','Marcelo'),('Samuel','Rebeca'),('Enrique','Paola'),('Enrique','Valentin'),('Valentin','Enrique'),('Valentin','Paola'),('Javier','Elena'),('Javier','Juana'))
facts(hermana,('Lady','Henry'),('Susan','Claudia'),('Claudia','Susan'),('Rebeca','Samuel'),('Paola','Enrique'),('Paola','Valentin'),('Elena','Juana'),('Elena','Javier'),('Juana','Elena'),('Juana','Javier'))
facts(esposo,('Enrique','Elena'),('Juan','Paola'),('Valentin','Tia1'),('Carlos','Juana'),('Javier','Crecencia'))
facts(esposa,('Elena','Enrique'),('Paola','Juan'),('Tia1','Valentin'),('Juana','Carlos'),('Crecencia','Javier'))
padres.add_fact(padre)
padres.add_fact(madre)

def abuelo(x,y):
  c = var()
  return conde((padre(x,c), padre(c,y)),(padre(x,c), madre(c,y)))

def abuela(x,y):
  c = var()
  return conde((madre(x,c), madre(c,y)),(madre(x,c), padre(c,y)))

def hijos(x,y):
  c = var()
  return conde((madre(y,x), esposa(y,c),padre(c,x)), (padre(y,x), esposo(y,c),madre(c,x)))

def primos(x,y):
  c = var()
  d = var()
  return conde((padre(c,x), hermano(c,d), padre(d,y)),(padre(c,x), hermano(c,d), madre(d,y)),(madre(c,x), hermana(c,d), padre(d,y)),(madre(c,x), hermana(c,d), madre(d,y)))

def tio(x,y):
  c = var()
  d = var()
  return conde((hermano(x,c), padre(c,y)), (esposo(x,d), hermana(d,c), padre(c,y)), (hermano(x,c), madre(c,y)), (esposo(x,d), hermana(d,c), madre(c,y)))

def tia(x,y):
  c = var()
  d = var()
  return conde((hermana(x,c), padre(c,y)), (esposa(x,d), hermano(d,c), padre(c,y)), (hermana(x,c), madre(c,y)), (esposa(x,d), hermano(d,c), madre(c,y)))


# print(run(1,a,padre(a,'Henry')))
print(run(1,a,tio(a,'Henry')))