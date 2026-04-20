//Elvis Nguyen
//Program 7

#include <stdio.h>
#include <string.h>

int main(void){
  //local variables
  char string1[100] = "";
  char string2[100] = "";
  
  int numOfWords;
  int cmpResults;
  //begin
  printf("Please enter a string: ");
  scanf("%s", string1);

  numOfWords = strlen(string1);

  printf("The number of characters in the word %s is %d.\n", string1, numOfWords);

  printf("Enter another string: ");
  scanf("%s", string2);

  cmpResults = strcmp(string1, string2);
  
  if (cmpResults < 0)
    {
        printf("%s is less than %s\n", string1, string2);
    }
  else if (cmpResults > 0)
    {
        printf("%s is greater than %s\n", string1, string2);
    }
  else
    {
        printf("%s is equal to %s\n", string1, string2);
    }

  return 0;
}