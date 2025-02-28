/*
 * Activity 3.6.4
 */
public class StandardArrayAlgorithms
{
  public static void main(String[] args)
  {
    int[] goals = {1, 2, 0, 3, 2, 4, 2, 1, 1};
    
    /* double sum = 0;
    for (int i = 0; i < goals.length; i++)
    {
      sum += goals[i];
    }
    double avg = sum / goals.length;

    System.out.println("Avg Goals: " + avg);

    int max = goals[1];
    int min = goals[1];

    for (int g = 0; g < goals.length; g++)
    {
      if (goals[g] > max)
      {
        max = goals[g];
      } 

      if (goals[g] < min)
      {
        min = goals[g];
      }
    } */

    /* System.out.println("Max: " + max);
    System.out.println("Min: " + min); */

    /* 
     * The algorithm below requires there to be a list of 10 values. Any list comtaining greater than 10 variables will not be counted by the algorithm.
     */
    /* int[] goalCounter = new int[10];
    
    for (int g : goals)
    {
      if (g >= 0 && g <=9)
      {
        goalCounter[g]++;
      }
    }

    for (int i = 0; i <= 9; i++)
    {
      System.out.println(goalCounter[i]);
    } */

    Player[] players = {new Player("Alex", 21), new Player("Aiden", 21),
                    new Player("Bobbie", 21), new Player("Blaine", 21),
                    new Player("Chris", 21), new Player("Charlie", 21) };

    int i = 0;
    boolean hasValue = false;
    boolean allHaveValue = true;

    /* while (hasValue == false)
    {
      if (hasValue == false || i < players.length)
      {
        hasValue = true;
        System.out.println("Property Found.");
      }
      i++;
    } */

    while (allHaveValue == true && i < players.length)
    {
      if (!(players[i].getAge() == 21))
      {
        allHaveValue = false;
        System.out.println("Not all of the players are 21 years old.");
      }
      i++;
    }

    if (allHaveValue == true)
    {
      System.out.println("All of the players are 21 years old.");
    }
    
    
    
  }

  
}