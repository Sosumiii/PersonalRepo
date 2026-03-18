////////////////////////////////////////////////////////////////////////////////
//
//  File Name  : program5.c
//
//  Programmer : Elvis Nguyen
//
//  Instructor : Jonathan Ormiston
//
//  Course     : ECET 264
//
//  Date Due   : March 13, 2026
//
//  Platform   : ASUS Vivobook S16 (Linux x64 6.18.12-1-MANJARO)
//
//  Compiler   : Microsoft Visual Studio Code v1.111.0
//
////////////////////////////////////////////////////////////////////////////////

// Eliminate deprecation warnings for the older, less secure functions
// Needed for Microsoft Visual Studio 2005 (MSVC++ version 8) or later
#define _CRT_SECURE_NO_DEPRECATE
// Save default warning level (push to the stack)
#pragma warning(push)
// Disable Microsoft Visual C++ WARNING C6031 - Return value ignored: 'scanf'
#pragma warning(disable: 6031)

// Compiler Includes
#include <stdio.h>

// Using Directives & Declarations

// Project Includes

// Constants
#define PERIOD '.'
#define QUESTION '?'
#define EXCLAMATION '!'

#define SPACE ' '
#define TAB '\t'
#define NEWLINE '\n'

#define QUOTE_CHARACTER '"'

// User Defined Types 

// Function Prototypes 
//////////////////////////////////////////////////////////////////////////////// 
// 
//  Function Name : main
// 
//  Originated    : March 18, 2026
// 
//  Abstract      : This function is where the main program is executed.
// 
//  Parameters    : None
// 
//  Return Value  : It returns a int value of 0.
// 
//  Misc. I/O     : None
// 
//  Revisions     :
// 
//////////////////////////////////////////////////////////////////////////////// 
int main(void) {
  //Local variables
  char filename[100];
  FILE *file;

  int wordCount = 0;
  int sentenceCount = 0;

  int inWord = 0;

  char curr;
  char next;
  char next2;

  int prev = 0;

  //Begin
  printf("Enter the name of the text file: ");
  scanf("%99s", filename);

  file = fopen(filename, "r");

  if (file == NULL) {
    printf("Error: File could not be opened.\n");
    return 0;
  }

  // Check if file is empty
  if (fgetc(file) == EOF) {
    printf("Error: File is empty.\n");
    fclose(file);
    return 0;
  }

  rewind(file);

  // Processing loop
  //fgetc is used instead of fscanf since the program scans for individual characters insteads of the whole word. 
  while ((curr = fgetc(file)) != EOF) {

    // Word detection
    if ((curr >= 'A' && curr <= 'Z') ||
        (curr >= 'a' && curr <= 'z') ||
        (curr >= '0' && curr <= '9')) {
      if (!inWord) {
        wordCount++;
        inWord = 1;
      }
    }

    // End of word
    if (curr == SPACE || curr == TAB) {
        inWord = 0;
    } 
    else if (curr == NEWLINE) {
      if (prev != '-') {
        inWord = 0;
      }
    }

    // Sentence detection
    if (curr == PERIOD || curr == QUESTION || curr == EXCLAMATION) {
      sentenceCount++;    // count sentence
      inWord = 0;         // reset for next sentence

      next = fgetc(file);
      while (next == SPACE || next == TAB) next = fgetc(file);

      if (next == QUOTE_CHARACTER) {
        next = fgetc(file); // skip quote
      }

      if (next != EOF) {
        ungetc(next, file);
      }
    }

    prev = curr;
  }

  fclose(file);

  // Output
  printf("Word Count: %d\n", wordCount);
  printf("Sentence Count: %d\n", sentenceCount);

  return 0;
} //end function main

// Restore default warning level (pop from the stack)
#pragma warning(pop)

// end file program5.c

