////////////////////////////////////////////////////////////////////////////////
//
//  File Name  : program8.c
//
//  Programmer : Elvis Nguyen
//
//  Instructor : Jonathan Ormiston
//
//  Course     : ECET 264
//
//  Date Due   : May 1, 2026
//
//  Platform   : IBM PC (Windows 11 25H2)
//
//  Compiler   : Microsoft Visual Studio Code v1.118.1
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
#define MAX_FILENAME_LENGTH 100
#define MAX_AUTOS 4

// User Defined Types
typedef struct
{
    int month;
    int day;
    int year;
} DATE_TYPE;

typedef struct
{
    double capacity;
    double level;
} TANK_TYPE;

typedef struct
{
    char make[25];
    char model[25];
    int odometer;
    DATE_TYPE manufactureDate;
    DATE_TYPE purchaseDate;
    TANK_TYPE tank;
} AUTO_TYPE;

// Function Prototypes
DATE_TYPE ScanDate(FILE *file);
TANK_TYPE ScanTank(FILE *file);
AUTO_TYPE ScanAuto(FILE *file);

void PrintDateLong(DATE_TYPE date);
void PrintAuto(AUTO_TYPE automobile);

char *GetMonthName(int month);

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : main
//
//  Originated    : April 30, 2026
//
//  Abstract      : This function is where the main program is executed.
//
//  Parameters    : None
//
//  Return Value  : Returns an int value of 0.
//
//  Misc. I/O     : Prompts user for file name, reads automobile records,
//                  and displays formatted automobile information.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
int main(void)
{
    // Local variables
    char filename[MAX_FILENAME_LENGTH];
    FILE *file;
    AUTO_TYPE automobiles[MAX_AUTOS];
    int i;

    // Begin
    printf("Enter the automobile input file name: ");
    scanf("%99s", filename);

    file = fopen(filename, "r");

    if (file == NULL)
    {
        printf("Error: File could not be opened.\n");
        return 0;
    }

    if (fgetc(file) == EOF)
    {
        printf("Error: File is empty.\n");
        fclose(file);
        return 0;
    }

    rewind(file);

    for (i = 0; i < MAX_AUTOS; i++)
    {
        automobiles[i] = ScanAuto(file);
    }

    fclose(file);

    for (i = 0; i < MAX_AUTOS; i++)
    {
        PrintAuto(automobiles[i]);
    }

    return 0;
} // end function main

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : ScanDate
//
//  Originated    : April 30, 2026
//
//  Abstract      : This function reads one date from the input file and
//                  stores the values into a DATE_TYPE structure.
//
//  Parameters    : file - pointer to opened input file
//
//  Return Value  : Returns a DATE_TYPE structure.
//
//  Misc. I/O     : Reads date information from the file.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
DATE_TYPE ScanDate(FILE *file)
{
    // Local variables
    DATE_TYPE date;

    // Begin
    fscanf(file, "%d%d%d",
           &date.month,
           &date.day,
           &date.year);

    return date;
} // end function ScanDate

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : ScanTank
//
//  Originated    : April 30, 2026
//
//  Abstract      : This function reads tank information from the input file
//                  and stores the values into a TANK_TYPE structure.
//
//  Parameters    : file - pointer to opened input file
//
//  Return Value  : Returns a TANK_TYPE structure.
//
//  Misc. I/O     : Reads tank data from the file.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
TANK_TYPE ScanTank(FILE *file)
{
    // Local variables
    TANK_TYPE tank;

    // Begin
    fscanf(file, "%lf%lf",
           &tank.capacity,
           &tank.level);

    return tank;
} // end function ScanTank

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : ScanAuto
//
//  Originated    : April 30, 2026
//
//  Abstract      : This function reads one automobile record from the input
//                  file and stores the values into an AUTO_TYPE structure.
//
//  Parameters    : file - pointer to opened input file
//
//  Return Value  : Returns an AUTO_TYPE structure.
//
//  Misc. I/O     : Reads automobile data from the file.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
AUTO_TYPE ScanAuto(FILE *file)
{
    // Local variables
    AUTO_TYPE automobile;

    // Begin
    fscanf(file, "%s%s%d",
           automobile.make,
           automobile.model,
           &automobile.odometer);

    automobile.manufactureDate = ScanDate(file);
    automobile.purchaseDate = ScanDate(file);
    automobile.tank = ScanTank(file);

    return automobile;
} // end function ScanAuto

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : GetMonthName
//
//  Originated    : April 30, 2026
//
//  Abstract      : This function converts a numeric month value into the
//                  corresponding month name.
//
//  Parameters    : month - numeric month value
//
//  Return Value  : Returns pointer to month name string.
//
//  Misc. I/O     : None
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
char *GetMonthName(int month)
{
    // Begin
    switch (month)
    {
        case 1:  return "January";
        case 2:  return "February";
        case 3:  return "March";
        case 4:  return "April";
        case 5:  return "May";
        case 6:  return "June";
        case 7:  return "July";
        case 8:  return "August";
        case 9:  return "September";
        case 10: return "October";
        case 11: return "November";
        case 12: return "December";
        default: return "Unknown";
    }
} // end function GetMonthName

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : PrintDateLong
//
//  Originated    : April 30, 2026
//
//  Abstract      : This function displays a date in long format.
//
//  Parameters    : date - date structure to display
//
//  Return Value  : None
//
//  Misc. I/O     : Displays output to terminal.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
void PrintDateLong(DATE_TYPE date)
{
    // Begin
    printf("%s %d, %d",
           GetMonthName(date.month),
           date.day,
           date.year);
} // end function PrintDateLong

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : PrintAuto
//
//  Originated    : April 30, 2026
//
//  Abstract      : This function displays one automobile record in the
//                  required assignment output format.
//
//  Parameters    : automobile - automobile structure to display
//
//  Return Value  : None
//
//  Misc. I/O     : Displays output to terminal.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
void PrintAuto(AUTO_TYPE automobile)
{
    // Local variables
    double percent;

    // Begin
    percent = (automobile.tank.level /
               automobile.tank.capacity) * 100.0;

    printf("=============================================================\n");

    printf("Make: %-10s", automobile.make);
    printf("Model: %-10s", automobile.model);
    printf("Odometer: %d\n", automobile.odometer);

    printf("-------------------------------------------------------------\n");

    printf("Manufactured on ");
    PrintDateLong(automobile.manufactureDate);

    printf("    Purchased on ");
    PrintDateLong(automobile.purchaseDate);
    printf("\n");

    printf("Fuel capacity is %.0f gallons",
           automobile.tank.capacity);

    printf("    Current fuel level is %.1f%%\n",
           percent);

    printf("=============================================================\n\n");
} // end function PrintAuto

// Restore default warning level
#pragma warning(pop)

// end file program8.c