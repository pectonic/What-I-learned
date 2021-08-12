from numpy import true_divide
import pandas as pd

#bu derste DataFrame yapisinda degisiklikler yapacagiz

students = {'Can':pd.Series(data=[20, 'M', 'Agriculture', 172], index=['age','gender', 'department', 'height']),
            'Miku':pd.Series(data=[21, 'F', 'Doctor', 170], index=['age','gender', 'department', 'height']),
            'Umit':pd.Series(data=[19, 'F', 'Streamer', 176], index=['age','gender', 'department', 'height'])
            }

df_students = pd.DataFrame(students)
print(df_students)
print()

# column alma 
""" df_students2 = pd.DataFrame(students, columns=['Can','Umit'])
print(df_students2) """

# index alma
""" df_students2 = pd.DataFrame(students, index=['age','department'])
print(df_students2) """

# her ikisini de alma
""" df_students2 = pd.DataFrame(students, columns=['Miku'] ,index=['department'])
print(df_students2) """

#peki varolan bir DataFrameden nasil cekecegiz
""" print(df_students['Can']) # tek boyutlu Series olarak geldi
print(df_students[['Can']]) #evet bu da 2 boyutlu bir DataFrame olarak geldi, tek fark bunun cift koseli parantezle yazilmis olmasi """

#birden fazla column almak istersek
""" print(df_students[['Can', 'Umit']])#evet iki column demek iki boyutlu DataFrame yapisi demek """

#loc ve iloc
""" print(df_students.loc['age']) # bize yaslari Series yapisi olarak dondurdu
print() 
print(df_students.loc[['age','department']]) #bize yaslari ve departmentleri DataFrame olarak dondurdu
print()
 """

#DF[col][row]
""" print(df_students['Can']['age']) 
print(df_students['Umit'][2]) # bu sekilde de calisir """

#yeni bir column ekleme
""" df_students['Kelek'] = [31, 'F', 'Sebze', 130]
print(df_students)
print()

    #ekleme yaparken toplama yapmak
df_students['Kelek2'] = df_students['Can'] + df_students['Kelek']
print(df_students) """

#yeni row ekleme
""" new_row = pd.DataFrame(data={'Can':'aydin','Miku':'japon','Umit':'demirkaya'},index=['surname'])
df_students = df_students.append(new_row)
print(df_students) """

#var olan column ve row'lari silme. pop > col ve drop > col-row
""" df_students.pop('Can')
print(df_students) """

""" df_students.drop(['Umit','Can'], axis=1 ,inplace=True) #kendine atayarak da yapabilirsin veya inplace parametresini kullanirsin
print(df_students)  """

df_students.drop('age', axis=0 ,inplace=True) #burada da row'lardan kurtulduk ve bu da coklu yapilabilir
print(df_students)