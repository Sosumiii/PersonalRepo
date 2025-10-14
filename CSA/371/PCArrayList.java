import java.util.ArrayList;
import java.util.Scanner;

public class PCArrayList 
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> pcPartList = new ArrayList<String>();
        pcPartList.add("Processor");
        pcPartList.add("Graphics Card");
        pcPartList.add("Memory");

        String userInput = "";

        while (!userInput.equals("q"))
        {
            System.out.println(pcPartList);
            System.out.println("Would you like to (a)dd, (i)nsert, (r)emove, re(p)lace, or (q)uit?");
            userInput = sc.nextLine();
            
            if (userInput.equals("a"))
            {
                
            }

            else if (userInput.equals("i"))
            {
                
            }

            else if (userInput.equals("r"))
            {
                
            }

            else if (userInput.equals("p"))
            {
                
            }

            else if (userInput.equals("q"))
            {
                System.out.println("Exiting program.");
            }

            else
            {
                System.out.println("Incorrect input");
            }
            

        }

    }
    
}
