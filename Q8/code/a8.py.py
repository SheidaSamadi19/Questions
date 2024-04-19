# Authors : Sheida Samadi , Baran Farrokhian

#first class: Educational Institiute

class Educational_Institiute :
    def __init__(self,room):
        self.room = room

# second class: students 
class students:  
    def __init__(self,name,gender,grade, id_num):
        self.name = name
        self.gender = gender
        self.grade = grade
        self.id_num = id_num

# creating Educational Institiute classes as objects 
Class_1 = Educational_Institiute(room = "physics")
Class_2 = Educational_Institiute(room = "chemistry")
Class_3 = Educational_Institiute(room = "mathematics")
Class_4 = Educational_Institiute(room = "computer")
Class_5 = Educational_Institiute(room = "biology")


# creating the 20 students as objects 
student_1 = students(name="Gabriel", gender="male", grade="diploma" ,id_num="02546")
student_2 = students(name="Adrian", gender="male", grade="diploma" ,id_num="35462")
student_3 = students(name="Alex", gender="male", grade="diploma" ,id_num="78165")
student_4 = students(name="Janet", gender="female", grade="diploma" ,id_num="84329")
student_5 = students(name="Lucy", gender="female", grade="diploma" ,id_num="21872")
student_6 = students(name="Luka", gender="male", grade="diploma" ,id_num="15462")
student_7 = students(name="Sakura", gender="female", grade="diploma" ,id_num="46856")
student_8 = students(name="Dazai", gender="male", grade="diploma" ,id_num="18756")
student_9 = students(name="Angel", gender="male", grade="diploma" ,id_num="13586")
student_10= students(name="Juliette", gender="female", grade="diploma" ,id_num="74185")
student_11= students(name="Romeo", gender="male", grade="diploma" ,id_num="96345")
student_12= students(name="Violet", gender="female", grade="diploma" ,id_num="75325")
student_13= students(name="Charlotte",gender ="female", grade="diploma" ,id_num="15634")
student_14= students(name="Jack", gender="male", grade="diploma" ,id_num="98719")
student_15= students(name="Carmen", gender="female", grade="diploma" ,id_num="83548")
student_16= students(name="Harold", gender="male", grade="diploma" ,id_num="02464")
student_17= students(name="Barbara", gender="female", grade="diploma" ,id_num="83218")
student_18= students(name="Nelson", gender="male", grade="diploma" ,id_num="24593")
student_19= students(name="Daniella", gender="female", grade="diploma" ,id_num="42860")
student_20= students(name="Berthana", gender="female", grade="diploma" ,id_num="12756")

print( student_1.__dict__,Class_2.__dict__,Class_1.__dict__,Class_5.__dict__)
print( student_2.__dict__,Class_4.__dict__,Class_3.__dict__,Class_1.__dict__)
print( student_3.__dict__,Class_1.__dict__,Class_2.__dict__,Class_3.__dict__)
print( student_4.__dict__,Class_5.__dict__,Class_1.__dict__,Class_4.__dict__)
print( student_5.__dict__,Class_4.__dict__,Class_3.__dict__,Class_1.__dict__)
print( student_6.__dict__,Class_5.__dict__,Class_1.__dict__,Class_4.__dict__)
print( student_7.__dict__,Class_5.__dict__,Class_2.__dict__,Class_1.__dict__)
print( student_8.__dict__,Class_3.__dict__,Class_5.__dict__,Class_4.__dict__)
print( student_9.__dict__,Class_4.__dict__,Class_2.__dict__,Class_3.__dict__)
print(student_10.__dict__,Class_3.__dict__,Class_5.__dict__,Class_1.__dict__)
print(student_11.__dict__,Class_2.__dict__,Class_3.__dict__,Class_5.__dict__)
print(student_12.__dict__,Class_1.__dict__,Class_2.__dict__,Class_3.__dict__)
print(student_13.__dict__,Class_3.__dict__,Class_2.__dict__,Class_5.__dict__)
print(student_14.__dict__,Class_2.__dict__,Class_1.__dict__,Class_4.__dict__)
print(student_15.__dict__,Class_5.__dict__,Class_3.__dict__,Class_4.__dict__)
print(student_16.__dict__,Class_2.__dict__,Class_5.__dict__,Class_1.__dict__)
print(student_17.__dict__,Class_1.__dict__,Class_2.__dict__,Class_4.__dict__)
print(student_18.__dict__,Class_3.__dict__,Class_5.__dict__,Class_2.__dict__)
print(student_19.__dict__,Class_4.__dict__,Class_2.__dict__,Class_5.__dict__)
print(student_20.__dict__,Class_4.__dict__,Class_2.__dict__,Class_1.__dict__)

