import time
import numpy as np

#burada numpy ile python hiz karsilastirmasi yapiyoruz

start_time_np = time.time() #simdiki zamani degisgene atiyoruz ki daha sonra gecen zamani bulmak icin, time.time() bize kullanildigi zamani verir

x = np.arange(1000000) 
x ** 2

time_np = time.time() - start_time_np # bu kod satiri bize numpy ile ne kadar surede 1m sayisinin karesini alacagini verecek



start_time_py = time.time()

y = range(1000000) 

[i ** 2 for i in y] #ustteki islemi py'de bu sekilde yapiyoruz 

time_py = time.time() - start_time_py # bu kod ise ayni islemi python ile hesaplama hizini verecek 

print(time_py/time_np) #bu kod satiri Numpy'in python'dan kac kat daha hizli oldugunu verecektir. Bende 110 kat daha hizli cikti ama izledigim videoda 240 kat daha hizli cikti... Vardir devletin bi bildigi 🦍🦍🦍. Ve tabii ki bu sonuc surekli degiscektir, videoyu devam ettirdigimde de adamin sonucu ortalama 110 katlara dustu vesselam kardesim



