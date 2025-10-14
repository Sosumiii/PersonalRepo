/*
 * Activity 3.7.3
 */
import java.util.ArrayList;

public class HorseBarnRunner
{
  public static void main(String[] args)
  {
    /* your code here */

    HorseBarn barn = new HorseBarn();
    ArrayList<Horse> barnSpaces = barn.getSpaces();

    int numSpaces = barnSpaces.size();
    /* for (int i = 0; i < numSpaces - 1; i++)
    {
      Horse h = barnSpaces.get(i);
      if (h.getName().equals("Patches"))
      {
        System.out.println("Bye bye " +  barnSpaces.remove(i));
        i--;
        numSpaces--;
      }

      else if (h.getName().equals("Lady"))
      {
        System.out.println("Bye bye " + barnSpaces.remove(i));
        i--;
        numSpaces--;
      }
    } */
    int i = 0;
    while (i < numSpaces)
    {
      Horse h = barnSpaces.get(i);
      if (h.getName().equals("Patches"))
      {
        System.out.println("Bye bye " +  barnSpaces.remove(i));
        i--;
        numSpaces--;
      }

      else if (h.getName().equals("Lady"))
      {
        System.out.println("Bye bye " + barnSpaces.remove(i));
        i--;
        numSpaces--;
      }
      i++;
    }

    System.out.println("");
    for (Horse horse : barnSpaces)
    {
      System.out.println(horse);
    }

  }
} 