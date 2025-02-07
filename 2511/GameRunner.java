/* 
 * Project 2.5.11
 * Main game runner
 * This file executes the main game.
 */
import java.util.Scanner;
 public class GameRunner 

{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String replay = "y";

        while (replay.equals("y"))
        {
            Game.play();

            System.out.println("----------------------\nWould you like to play again?\nType y or n.");
            replay = sc.next();

            while (!replay.equals("y") && !replay.equals("n"))
            {
                System.out.println("----------------------\nInvalid choice. Please try again. \n Type y or n");
                replay = sc.next();
            }

        }
        
        System.out.println("Thanks for playing!");
    }
}
