

## Proje 1
[22,27,16,2,18,6] -> Insertion Sort

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.
Time Complexity: Average case: Aradığımız sayının ortada olması,Worst case: Aradığımız sayının sonda olması, Best case: Aradığımız sayının dizinin en başında olması.
Dizi sıralandıktan sonra 18 sayısı hangi case kapsamına girer? Yazınız.


[7,3,5,8,2,9,4,15,6] dizisinin Insertion Sort'a göre ilk 4 adımını yazınız.

### Öncelikle [22,27,16,2,18,6] listesi için aşamlar şu sekildedir. 
1- n adet elemanlı listeden en küçük değer sahip olanı bul ve başa at ve kontrol edileceklerden çıkar. 
2- n tane elemanlı listeden en küçüğünü bulduğum için şimdi n-1 elemanlı bir listemiz var. Bundan sonra sonuca ulaşana kadar her adımda eleman sayısından 1 çıkartarak devam edeceğiz.
3- Sonuç Insertion Sort için n + (n-1) + (n-2) + ... + 1 adımlarına sahip olacağız. 

Big-O notation: (n*(n+1))/2 = (n^2+n)/2 yani Big-O = O(n^2)

18 sayısı bizim için Average case'ye girer.


### [7,3,5,8,2,9,4,15,6] listesinin ilk dört aşaması:
1- En küçüğü bul
2- en küçüğü başa yerleştir
3- en küçüğü listeye almayacak şekilde geri kalanlardan en küçüğü bul
4- Bulunan sayıyı en küçüğün yanına koy




## Proje 2
Proje 2
[16,21,11,8,12,22] -> Merge Sort

Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.

### Aşamalar:
1- N elemanlı listenin hepsi bir eleman kalana kadar bölünür
2- sonra yan yana olanlar sıralanarak birleştirilir. 
3- Birleştirilenler kendi aralarında da sıralanarak birleştirilir. 
4- Bu işlemi n/2 kere yaparak bu işlemi bitiriyorum. Sıralama falan derken bu 2^x=n mantığına geliyor.

Big-O notetion: n/2 işlemi n(O) + (2^x = n işlemi O(logn)) = O(nlogn) 



## Proje 3
Proje 3
[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.

### Aşamalar: 
1- Root: 4 solunda: [0,1,2,3] ve sağında = [5,6,7,8,9] var
2- [0,1,2,3] için 1 root olur, solunda = [0] ve sağında [2,3] ||| [5,6,7,8,9] için 7 root olur, solunda = [5,6] ve sağında [8,9] olur ve ağacımız oluşur


