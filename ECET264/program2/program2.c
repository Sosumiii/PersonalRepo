////////////////////////////////////////////////////////////////////////////////
//
//  File Name  : program2.c
//
//  Programmer : Elvis Nguyen
//
//  Instructor : Jonathan Ormiston
//
//  Course     : ECET 264
//
//  Date Due   : January 26, 2026
//
//  Platform   : ASUS Vivobook S16 (Linux x64 6.18.4-1-MANJARO)
//
//  Compiler   : Microsoft Visual Studio Code v1.108.1
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

// User Defined Types 

// Function Prototypes 
//////////////////////////////////////////////////////////////////////////////// 
// 
//  Function Name : main
// 
//  Originated    : January 25, 2026
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
  //local variables
  int number = 5;
  //begin
  printf("Welcome to\nProgramming!\n");
  printf("the number is %d.\n", number);

  printf("Enter a new number: \n");
  scanf("%d", &number);
  printf("The new number you entered is %d!\n", number);
  return 0;
} //end function main

// Restore default warning level (pop from the stack)
#pragma warning(pop)

// end file program2.c

