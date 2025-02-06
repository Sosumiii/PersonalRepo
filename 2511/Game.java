/* 
 * Project 2.5.11
 * This program houses the game logic
 */
import java.util.Scanner;
import java.util.Random;

public class Game 
{
    public static void play()
    {
        Scanner sc = new Scanner(System.in);
        Random rn = new Random();

        System.out.println("Player 1: Please enter your name.");
        String p1Name = sc.nextLine();
        Player p1 = new Player(p1Name);

        System.out.println("Player 2: Please enter your name.");
        String p2Name = sc.nextLine();
        Player p2 = new Player(p2Name);

        System.out.println(p1);
        System.out.println(p2);
        
        Board b = new Board();

        int playerTurn = 0;//rn.nextInt(1);
        int choice = 0;

        boolean win = false;

        while (win != true);
        {
            System.out.println(b);

            if (playerTurn == 0)
            {
                while (choice >= (b.getNumOfSticks() / 2) || choice < 1)
                {
                    System.out.println(p1.getName() + ": Type in the amount of sticks you want to remove. \n It can not be 0 or a number greater than half of the amount still in the pile.");
                    choice = sc.nextInt();
                }
                
                win = true;
                
            }
        }


    }

}
