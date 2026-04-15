////////////////////////////////////////////////////////////////////////////////
//
//  File Name  : program6.c
//
//  Programmer : Elvis Nguyen
//
//  Instructor : Jonathan Ormiston
//
//  Course     : ECET 264
//
//  Date Due   : April 5, 2026
//
//  Platform   : IBM PC (Windows 11 25H2)
//
//  Compiler   : Microsoft Visual Studio Code v1.113.0
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
#define MAX_FILENAME_LENGTH 100
#define MAX_VALUES 1000

// User Defined Types

// Function Prototypes
int GetInput(const char filename[], double values[], int maxSize);
void SortValues(double values[], int count);

double FindSum(const double values[], int count);
double FindMean(double sum, int count);
double FindMedian(const double values[], int count);
double FindMin(const double values[], int count);
double FindMax(const double values[], int count);
double FindStandardDeviation(const double values[], int count, double mean);

void DisplayStats(double minValue, double maxValue, double mean, double median,
                  double stdDev);

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : main
//
//  Originated    : April 5, 2026
//
//  Abstract      : This function is where the main program is executed.
//
//  Parameters    : None
//
//  Return Value  : It returns a int value of 0.
//
//  Misc. I/O     : Prompts the user for a file name and displays the resulting
//                  statistics to the terminal screen.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
int main(void)
{
    // Local variables
    char filename[MAX_FILENAME_LENGTH];
    double values[MAX_VALUES];
    FILE *file;
    int count;

    double sum;
    double mean;
    double median;
    double minValue;
    double maxValue;
    double stdDev;

    // Begin
    printf("Enter the name of the text file: ");
    scanf("%99s", filename);

    file = fopen(filename, "r");

    if (file == NULL)
    {
        printf("Error: File could not be opened.\n");
        return 0;
    }

    if (fscanf(file, "%lf", &values[0]) != 1)
    {
        printf("Error: File is empty.\n");
        fclose(file);
        return 0;
    }

    fclose(file);

    count = GetInput(filename, values, MAX_VALUES);

    if (count <= 0)
    {
        printf("Error: No valid numeric data was read from the file.\n");
        return 0;
    }

    SortValues(values, count);

    sum = FindSum(values, count);
    mean = FindMean(sum, count);
    median = FindMedian(values, count);
    minValue = FindMin(values, count);
    maxValue = FindMax(values, count);

    if (count == 1)
    {
        stdDev = 0.0;
    }
    else
    {
        stdDev = FindStandardDeviation(values, count, mean);
    }

    DisplayStats(minValue, maxValue, mean, median, stdDev);

    return 0;
} // end function main

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : GetInput
//
//  Originated    : April 4, 2026
//
//  Abstract      : This function opens the specified file and reads numeric
//                  values from it, storing them into an array.
//
//  Parameters    : filename - name of the input text file
//                  values   - array used to store numeric values
//                  maxSize  - maximum number of values the array can hold
//
//  Return Value  : Returns the total number of values successfully read
//                  from the file.
//
//  Misc. I/O     : Reads data from the input text file.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
int GetInput(const char filename[], double values[], int maxSize)
{
    // Local variables
    FILE *file;
    int count = 0;

    // Begin
    file = fopen(filename, "r");

    if (file == NULL)
    {
        return 0;
    }

    while (count < maxSize && fscanf(file, "%lf", &values[count]) == 1)
    {
        count++;
    }

    fclose(file);

    return count;
} // end function GetInput

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : SortValues
//
//  Originated    : April 4, 2026
//
//  Abstract      : This function sorts the values in ascending order using
//                  a bubble sort algorithm.
//
//  Parameters    : values - array of numeric values
//                  count  - number of values in the array
//
//  Return Value  : None
//
//  Misc. I/O     : None
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
void SortValues(double values[], int count)
{
    // Local variables
    int i;
    int j;
    double temp;

    // Begin
    for (i = 0; i < count - 1; i++)
    {
        for (j = 0; j < count - 1 - i; j++)
        {
            if (values[j] > values[j + 1])
            {
                temp = values[j];
                values[j] = values[j + 1];
                values[j + 1] = temp;
            }
        }
    }
} // end function SortValues

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : FindSum
//
//  Originated    : April 4, 2026
//
//  Abstract      : This function calculates the sum of all values in the array.
//
//  Parameters    : values - array of numeric values
//                  count  - number of values in the array
//
//  Return Value  : Returns the total sum of the values.
//
//  Misc. I/O     : None
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
double FindSum(const double values[], int count)
{
    // Local variables
    int i;
    double sum = 0.0;

    // Begin
    for (i = 0; i < count; i++)
    {
        sum += values[i];
    }

    return sum;
} // end function FindSum

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : FindMean
//
//  Originated    : April 4, 2026
//
//  Abstract      : This function calculates the mean value using the sum
//                  of the dataset and the total number of values.
//
//  Parameters    : sum   - sum of all values
//                  count - number of values in the dataset
//
//  Return Value  : Returns the mean value.
//
//  Misc. I/O     : None
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
double FindMean(double sum, int count)
{
    // Local variables

    // Begin
    return sum / count;
} // end function FindMean

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : FindMedian
//
//  Originated    : April 4, 2026
//
//  Abstract      : This function calculates the median value of a sorted
//                  array of numeric values.
//
//  Parameters    : values - sorted array of numeric values
//                  count  - number of values in the array
//
//  Return Value  : Returns the median value.
//
//  Misc. I/O     : None
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
double FindMedian(const double values[], int count)
{
    // Local variables
    double median;

    // Begin
    if (count % 2 == 1)
    {
        median = values[count / 2];
    }
    else
    {
        median = (values[(count / 2) - 1] + values[count / 2]) / 2.0;
    }

    return median;
} // end function FindMedian

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : FindMin
//
//  Originated    : April 4, 2026
//
//  Abstract      : This function determines the minimum value from a sorted
//                  array of numeric values.
//
//  Parameters    : values - sorted array of numeric values
//                  count  - number of values in the array
//
//  Return Value  : Returns the minimum value.
//
//  Misc. I/O     : None
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
double FindMin(const double values[], int count)
{
    // Local variables
    double minValue;

    // Begin
    minValue = values[0];

    return minValue;
} // end function FindMin

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : FindMax
//
//  Originated    : April 5, 2026
//
//  Abstract      : This function determines the maximum value from a sorted
//                  array of numeric values.
//
//  Parameters    : values - sorted array of numeric values
//                  count  - number of values in the array
//
//  Return Value  : Returns the maximum value.
//
//  Misc. I/O     : None
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
double FindMax(const double values[], int count)
{
    // Local variables
    double maxValue;

    // Begin
    maxValue = values[count - 1];

    return maxValue;
} // end function FindMax

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : FindStandardDeviation
//
//  Originated    : April 5, 2026
//
//  Abstract      : This function calculates the sample standard deviation
//                  of the dataset using the mean value.
//
//  Parameters    : values - array of numeric values
//                  count  - number of values in the array
//                  mean   - mean value of the dataset
//
//  Return Value  : Returns the standard deviation value.
//
//  Misc. I/O     : None
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
double FindStandardDeviation(const double values[], int count, double mean)
{
    // Local variables
    int i;
    double difference;
    double sumSquares = 0.0;
    double stdDev;

    // Begin
    for (i = 0; i < count; i++)
    {
        difference = values[i] - mean;
        sumSquares += difference * difference;
    }

    stdDev = sqrt(sumSquares / count);

    return stdDev;
} // end function FindStandardDeviation

////////////////////////////////////////////////////////////////////////////////
//
//  Function Name : DisplayStats
//
//  Originated    : April 4, 2026
//
//  Abstract      : This function displays the calculated statistical values
//                  to the terminal screen.
//
//  Parameters    : minValue - minimum value in the dataset
//                  maxValue - maximum value in the dataset
//                  mean     - mean value
//                  median   - median value
//                  stdDev   - standard deviation value
//
//  Return Value  : None
//
//  Misc. I/O     : Displays output to the terminal.
//
//  Revisions     :
//
////////////////////////////////////////////////////////////////////////////////
void DisplayStats(double minValue, double maxValue, double mean, double median,
                  double stdDev)
{
    // Local variables

    // Begin
    printf("\nMinimum Value      : %.2f\n", minValue);
    printf("Maximum Value      : %.2f\n", maxValue);
    printf("Mean Value         : %.2f\n", mean);
    printf("Median Value       : %.2f\n", median);
    printf("Standard Deviation : %.2f\n", stdDev);
} // end function DisplayStats

// Restore default warning level (pop from the stack)
#pragma warning(pop)

// end file program6.c