import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="hatice",
  password="Plmoplmo14*",
  database="baseloc"
)

print(mydb)

mycursor = mydb.cursor()


# partie création et insertions :



mycursor.execute("CREATE TABLE Loyer (id_loyer int not null auto_increment primary key,type_logement varchar(3),mt_loyer smallint,frais smallint)")


sql = "INSERT INTO Loyer (type_logement,mt_loyer,frais) values (%s, %s,%s)"
val = [
('t1',450,30),
('t2',500,30),
('t3',600,30),
('t4',750,30),
('t1b',475,30)
]
mycursor.executemany(sql, val)
mydb.commit()



mycursor.execute("CREATE TABLE Individu(id_individu int not null auto_increment primary key,nom varchar(55) not null,prenom varchar(55) not null,date_naissance date,num_tel1 char(10),num_tel2 char(10))")

sql = "INSERT INTO Individu (nom,prenom,date_naissance,num_tel1)VALUES (%s, %s,%s, %s)"
val = [
('Thomas','Charles','19750202','0612326545'),
('Dudemaine','Marc','19600131','0678541232'),
('Chabert','Eric','19450504','0698563214'),
('Monatigne','Martha','19820615','0785422526'),
('Pullman','Lucie','19870916','0695658965')
]
mycursor.executemany(sql, val)
mydb.commit()
mycursor.execute("SELECT * FROM Individu")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)



cursor.execute("CREATE TABLE Commune (id_commune int not null auto_increment primary key,nb_habitant int,distance_agence smallint,nom_commune varchar(50) not null,cp char(5))")

sql = "INSERT INTO Commune (nb_habitant, distance_agence,nom_commune, cp)  values (%s,%s,%s,%s)"
val = [
(17565, 12,'Faches-Thumesnil','59255'),
(2104,20,'Capinghem','59160'),
(4068,12,'Hallennes-lez-Haubourdin','59320'),
(40246,8,'Marcq-en-Baroeul','59700'),
(21405,10,'Mons-en-Baroeul','59370')
]
mycursor.executemany(sql, val)
mydb.commit()

mycursor.execute("SELECT * FROM Commune")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)
mycursor.execute("CREATE TABLE Logement (id_logement int not null auto_increment primary key,id_loyer int,superficie smallint,adresse varchar(255),id_commune int not null,CONSTRAINT fk_commune_id_commune FOREIGN KEY (id_commune) REFERENCES Commune(id_commune))")

sql = "INSERT INTO  Logement (id_loyer,superficie,adresse,id_commune) values (%s,%s,%s,%s)"
val = [
(1, 25, '25 rue du molinel' ,1),
(2,35,'35 rue de Paris',2),
(4,60,'3 rue du port',3),
(3,65,'87 avenue de la République', 4),
(5,135,'15 boulevard Montebello',5)
]
mycursor.executemany(sql, val)

mydb.commit()
mycursor.execute("SELECT * FROM Logement")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)



mycursor.execute("CREATE TABLE Location(id_location int not null auto_increment primary key,id_logement int not null,id_individu int not null,date_debut date,date_fin date, FOREIGN KEY (id_logement) REFERENCES Logement(id_logement) ,FOREIGN KEY (id_individu) REFERENCES Individu(id_individu))")

sql = "INSERT INTO Location (id_logement,id_individu, date_debut, date_fin) values (%s,%s,%s,%s)"
val=[
(1,1,'20181201','20200202'),
(2,1,'20200203','20220202'),
(3,2,'20160601','20200530'),
(4,5,'20200101','20201231'),
(5,4,'20190201','20231231')
]

mycursor.executemany(sql, val)

mydb.commit()
mycursor.execute("SELECT * FROM Location")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)





#Partie Update

sql = "UPDATE Individu  SET prenom = %s WHERE id_individu= %s"
val = ("Martin",1)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
mycursor.execute("SELECT * FROM Individu where id_individu = 1")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)

sql = "UPDATE Loyer SET mt_loyer = %s WHERE id_loyer= %s"
val = (800,1)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
mycursor.execute("SELECT * FROM Loyer WHERE id_loyer= 1")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)


sql = "UPDATE Commune SET distance_agence = %s WHERE id_commune= %s"
val = (8,1)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
mycursor.execute("SELECT * FROM Commune WHERE id_commune= 1")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)


sql = "UPDATE Logement SET superficie = %s WHERE id_logement= %s"
val = (8,1)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
mycursor.execute("SELECT * FROM Logement WHERE id_logement= 1")

myresult = mycursor.fetchall()

for x in myresult:
 print(x)

sql = "UPDATE Location SET date_debut = %s WHERE id_logement= %s"
val = ('20190101',1)

mycursor.execute(sql, val)

# partie suppression:

sql = "DELETE FROM Loyer WHERE  id_loyer =1"

mycursor.execute(sql)