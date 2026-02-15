////////////////////////////////////////////////////////////////////////////////
//
//  File Name  : program3.c
//
//  Programmer : Elvis Nguyen
//
//  Instructor : Jonathan Ormiston
//
//  Course     : ECET 264
//
//  Date Due   : February 13, 2026
//
//  Platform   : ASUS Vivobook S16 (Linux x64 6.18.8-1-MANJARO)
//
//  Compiler   : Microsoft Visual Studio Code v1.109.2
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
#include <math.h>
// Using Directives & Declarations

// Project Includes

// Constants

// User Defined Types 
#define PI 3.14159
// Function Prototypes 
//////////////////////////////////////////////////////////////////////////////// 
// 
//  Function Name : main
// 
//  Originated    : February 12, 2026
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
  float radius = 0.00; //in centimeters
  float height = 0.00; // in centimeters
  float curvedSurfaceArea = 0.00; //in centimeters squared
  float totalSurfaceArea = 0.00; //in centimeters squared

  //Begin
  printf("Enter the radius of the tin can in centimeters: ");
  scanf("%f", &radius);
  
  printf("Enter the height of the tin can in centimeters: ");
  scanf("%f", &height);

  //calculate the curved surface area of the tin can (tin required)
  curvedSurfaceArea = 2 * PI * radius * height;
  
  //calculate the total surface area of the tin can
  totalSurfaceArea = (2 * (PI * pow(radius, 2))) + curvedSurfaceArea;

  //display both the total amount of tin and paper required for the can
  printf("Amount of tin required: %.3f centimeters squared.\n", totalSurfaceArea);
  printf("Amount of paper required for the");
  printf(" label: %.3f centimeters squared.\n", curvedSurfaceArea);

  return 0;
} //end function main

// Restore default warning level (pop from the stack)
#pragma warning(pop)

// end file program3.c

