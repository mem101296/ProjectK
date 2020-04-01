/*This will be used for C programming*/

#include <stdio.h> //declares library to import.
#include <math.h> //imports math library
  int main(void){
    char start[]={'s','t','a','r','t','i','n','g'};
    int i = 0;
      //start == "Hello";
      //for (i=0; i<6; i++){ //loops until i = 6
        //printf("Hello\n"); // prints hello

//}

while (start[i] != '\0')
  {
      printf("%c\n", start[i]);
      i++;
  }
return 0;
  }
