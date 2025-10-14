/*
 * Activity 3.7.2
 */
import java.util.ArrayList;

public class ArrayListExample
{  
   public static void main(String args[])
   {  
      ArrayList<String> animalList = new ArrayList<String>();  
      animalList.add("Dog");
      animalList.add("Cat");
      animalList.add("Rabbit");
      animalList.add("Frog");
      animalList.add("Horse");
      animalList.add("Cow");
      
      // isplaying elements
      System.out.println(animalList);
      
      /* your code here */ 
      animalList.add("Bird");
      animalList.add(3, "Snake");

      for (int i = 0; i < animalList.size(); i++)
      {
        if ((i == 2) || (i == 3) || (i == 5))
        {
            System.out.println(animalList.get(i));
        }
      }

      animalList.remove(4);

      System.out.println(animalList.size());
      // display elements
      System.out.println(animalList);
   }  
}