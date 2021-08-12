from numpy import product
import pandas as pd

#pandasin en cok kullanilan 2 boyutlu veri yapisi olan DataFrame. Bir veriyi cagirmak icin x ve y dimension ozelligini kullanacagiz yani cift babagul

#iste DataFrame olusturma yontemlerinden bir tanesi
""" 
students = [
    {
        'name':'Can',
        'age':'20',
        'gender':'M'
    },
    {
        'name':'Ali',
        'age':'14',
        'gender':'M'
    },
    {
        'name':'Esma',
        'age':'17',
        'gender':'F'
    }
]

print(students)
print(type(students))
print()

df_students = pd.DataFrame(students)
print(df_students)
print(type(df_students))
 """

#DataFrame olusturmak icin farkli yol deneyelim, bu sefer dict kullanarak

""" students = {
    'name':['can','ali','esma'],
    'age':[20,14,18],
    'gender':['M','M','F']
}

print(students)
print(type(students))
print()

df_students = pd.DataFrame(students)
print(df_students)
print(type(df_students))  """

#farkli bir yontem olan sadece listelerden list of list taktigi ile DataFrame olusturacagiz

""" list_of_list = [
    ['ahmet','ali','esma'],
    [20,14,18],
    ['M','M','F']
]

print(list_of_list)
print(type(list_of_list))
print()

df_list_of_list = pd.DataFrame(list_of_list)
print(df_list_of_list)
print(type(df_list_of_list)) """

#simdi tek stundan olusan bi DataFrame olusturalim

""" names = ['can','ali','esma']
print(names)
print(type(names))
print()

df_names = pd.DataFrame(names)
print(df_names)
print(type(df_names)) """

#simdi iki boyut nasil belirlenir onla ilgili ornek gosterecegim

""" students = {'name':'can','age':20}
print(students)
print(type(students))
print()

se_students = pd.Series(students) # hatasiz oluyor cunku tanimladigimiz olusturdugumuz dict tek boyutlu
df_students = pd.DataFrame(students) #"If using all scalar values, you must pass an index" hatasi aliyoruz yani diyor ki amina koydugum ben iki yolluyum sen bana tek boyutlunun verisini veriyorsun, tek boyut istiyorsan Series kullan 🤬🤬
 """

#simdi dict kullanarak hem satir hem stun indexli ile bir DataFrame olusturalim

""" students = {'Can':pd.Series(data=[20, 'M', 'Agriculture'], index=['age','gender', 'department']),
            'Miku':pd.Series(data=[21, 'F', 'Doctor'], index=['age','gender', 'department'])}
print(students)
print(type(students))
print()


df_students = pd.DataFrame(students)
print(df_students) """

#simdi PANDAS'in EN GUCLU taraflarindan birini gosterecegim, bu guc OLMAYAN VERILERLE CALISABILIYOR olmasidir. MAAAAAN cok havali la 😎

students = {'Can':pd.Series(data=[20, 'M', 'Agriculture', 172], index=['age','gender', 'department', 'height']),
            'Miku':pd.Series(data=[21, 'F', 'Doctor', 60], index=['age','gender', 'department', 'weight'])}

df_students = pd.DataFrame(students)
print(df_students) #MAAA MAAAN olmayan veriler yuzunden hata vermiyor onlarin NaN olarak bos oldugunu belirtiyor, cok guzel be. Huzur ke