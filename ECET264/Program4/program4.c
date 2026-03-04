////////////////////////////////////////////////////////////////////////////////
//
//  File Name  : program4.c
//
//  Programmer : Elvis Nguyen
//
//  Instructor : Jonathan Ormiston
//
//  Course     : ECET 264
//
//  Date Due   : March 6, 2026
//
//  Platform   : ASUS Vivobook S16 (Linux x64 6.18.12-1-MANJARO)
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
#define gravitationalConstant 32.17
#define PI 3.14159
#define THETA_MAX PI/2
#define THETA_MIN 0.00
#define GROUND_LEVEL 0.00
// Function Prototypes 
//////////////////////////////////////////////////////////////////////////////// 
// 
//  Function Name : main
// 
//  Originated    : February 18, 2026
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
  double theta = 0.00; //angle in radians
  double distance = 0.00; // in feet
  double velocity = 0.00; //in feet per second

  //breaking down calculations into two sections due to character limit
  double heightCalc1 = 0.00;
  double heightCalc2 = 0.00;

  double time = 0.00; //in seconds
  double height = 0.00; //in feet

  //Begin
  printf("Enter the angle of the projectile in radians (between 0 and PI/2): ");
  scanf("%lf", &theta);

  if ((theta > THETA_MAX) || (theta <= THETA_MIN)) {
    printf("the angle, %.3f, is invalid (has to be a value between 0 and pi/2).", theta);
    return 0;
  }
  
  else {
    printf("Enter the distance in feet: ");
    scanf("%lf", &distance);

    if (distance <= 0) {
      printf("the distance, %.3lf, is invalid (has to be a number greater than 0).", distance);
      return 0;
    }

    else {
      printf("Enter the velocity of the projectile in feet per second: ");
      scanf("%lf", &velocity);

      if (velocity <= 0) {
        printf("the velocity, %3lf, is invalid (has to be a number greater than 0).", velocity);
        return 0;
      }

      else {
        //calculate the time of flight
        time = distance / (velocity * cos(theta));
        
        //calculate the height
        heightCalc1 = velocity * sin(theta) * time;
        heightCalc2 = (gravitationalConstant * (pow(time, 2) / 2));

        height = heightCalc1 - heightCalc2;

        /*display both the total flight time and height of the projectile if
          the final height is greater than ground level */
        
        if (height >= GROUND_LEVEL) {
          printf("Total flight time: %.3lf seconds.\n", time);
          printf("Total height when it reaches the target: %.3lf feet.\n", height);
        }
        else {
          printf("The projectile has struck the ground instead of the target.");
        }

        return 0;
      }
    }
  }
  
} //end function main

// Restore default warning level (pop from the stack)
#pragma warning(pop)

// end file program4.c

