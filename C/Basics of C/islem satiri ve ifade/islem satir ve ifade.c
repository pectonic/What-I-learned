#include <stdio.h>

void fonk(void)
{
  printf("C Programlama Dili");
}

int main(void)
{
  int id1 = 7;     // int bir değişken bildirimi yapılırken sabit bir değer değişkene atanır.
  int id2;         // int bir değişken bildirimi yapılır.
  int id3, id4;    // İki adet int değişken bildirimi yapılır.

  id2 = 21;        // Sabit bir değer int bir değişkene atanır.

  id3 = id1 + id2; // İki değişken değeri toplanarak int bir değişkene atanır.
  id4 = id3 + 35;  // Bir değişken değeri ve bir sabit değer toplanarak int bir değişkene atanır.

  printf("%d %d\n", id1, id2); // id1 ve id2 değişken değerleri ekrana yazılır.
  printf("%d %d\n", id3, id4); // id3 ve id4 değişken değerleri ekrana yazılır.

  fonk(); // Fonksiyon çağrısı yapılır.

  return 0;
}