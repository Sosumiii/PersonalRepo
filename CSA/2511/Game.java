/* 
 * Project 2.5.11
 * This program houses the game logic
 */
import java.util.Random;
import java.util.Scanner;

public class Game 
{
    public static void play()
    {
        Scanner sc = new Scanner(System.in);
        Random rn = new Random();

        System.out.println("Player 1: Please enter your name. \n----------------------");
        String p1Name = sc.nextLine();
        Player p1 = new Player(p1Name);

        System.out.println("Player 2: Please enter your name. \n----------------------");
        String p2Name = sc.nextLine();
        Player p2 = new Player(p2Name);

        System.out.println(p1);

        System.out.println(p2);
        boolean win = false;
        
        Board b = new Board();

        int playerTurn = rn.nextInt(2);

        while (!win)
        {
            System.out.println("---------------------- \n" + b);

            if (b.getNumOfSticks() == 1)
            {
                win = true;
                if (playerTurn == 1)
                {
                    System.out.println("---------------------- \n" + p1.getName() + " has won the game of Nim. \nScore: " + p1.getScore());
                    break;
                }
                else
                {
                    System.out.println("---------------------- \n" + p2.getName() + " has won the game of Nim. \nScore: " + p2.getScore());
                    break;
                }
            }

            if (playerTurn == 0)
            {
                int choice = 0;

                while (choice > (b.getNumOfSticks() / 2) || choice < 1)
                {
                    System.out.println("---------------------- \n" + p1.getName() + ": Type in the amount of sticks you want to remove. \n It can not be 0 or a number greater than half of the amount still in the pile.");
                    choice = sc.nextInt();
                }

                b.removeSticks(choice);
                p1.setScore(1);
                playerTurn = 1;

            }

            else if (playerTurn == 1)
            {
                int choice = 0;

                while (choice > (b.getNumOfSticks() / 2) || choice < 1)
                {
                    System.out.println("---------------------- \n" + p2.getName() + ": Type in the amount of sticks you want to remove. \n It can not be 0 or a number greater than half of the amount still in the pile.");
                    choice = sc.nextInt();
                }

                b.removeSticks(choice);
                p2.setScore(1);
                playerTurn = 0;
            }

        }


    }
}
