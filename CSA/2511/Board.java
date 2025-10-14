/* 
 * Project 2.5.11
 * This program is responsible for setting up the board and game pieces
 */
import java.util.Random;

public class Board 
{
    Random rn = new Random();
    int max = 50, min = 10;
    private int numOfSticks = (rn.nextInt(max - min + 1) + min);

    public int getNumOfSticks()
    {
        return numOfSticks;
    }

    public void removeSticks(int num)
    {
        numOfSticks = numOfSticks - num;
    }
    
    public String toString()
    {
        String info = "";
        info += "Amount of sticks: ";
        info += numOfSticks;
        
        return info;
    }
}
