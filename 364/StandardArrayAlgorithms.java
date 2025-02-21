/*
 * Activity 3.6.4
 */
public class StandardArrayAlgorithms
{
  public static void main(String[] args)
  {
    int[] goals = {1, 2, 0, 3, 2, 4, 2, 1, 0, 2, 0, 1, 3, 2};
    
    double sum = 0;
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
    }

    System.out.println("Max: " + max);
    System.out.println("Min: " + min);

    
    
  }

  
}