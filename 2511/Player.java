/* 
 * Project 2.5.11
 * Game of Nim Player Class
 * Elvis Nguyen
 */
public class Player 
{
    private static int playerTurn = 0;
    private String playerName = "";
    private int playerScore = 0;

    public Player(String name)
    {
        this.playerName = name;
        this.playerScore = 0;
    }

    public String toString()
    {
        String info = "";
        info += "Welcome to the game of nim, ";
        info += this.playerName;
        
        return info;
    }

    public String getName()
    {
        return this.playerName;
    }

    public int getScore()
    {
        return this.playerScore;
    }

    public int getTurn()
    {
        return playerTurn;
    }

    public void setName(String name)
    {
        this.playerName = name;
    }

    public void setScore(int score)
    {
        this.playerScore += score;
    }

}
