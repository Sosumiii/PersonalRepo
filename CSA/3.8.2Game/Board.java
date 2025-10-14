/** 
 * A game board of NxM board of tiles.
 * 
 *  @author PLTW
 * @version 2.0
 */
import java.util.*;
/** 
 * A Board class for concentration
 */
public class Board
{  
  private static String[] tileValues = {"lion", "lion",
                                        "penguin", "penguin",
                                        "dolphin", "dolphin",
                                        "fox", "fox",
                                        "monkey", "monkey",
                                        "turtle", "turtle"}; 
  private Tile[][] gameboard = new Tile[3][4];

  /**  
   * Constructor for the game. Creates the 2D gameboard
   * by populating it with card values
   * 
   */
  public Board()
  {
   
    /* your code here */ 
    int count = 0;

    for (int i = 0; i < gameboard.length; i++)
      for (int j = 0; j < gameboard[0].length; j++)
      {
        gameboard[i][j] = new Tile(tileValues[count]);
        count++;
      }

    // shuffle the tiles
    ArrayList<Tile> tileList = new ArrayList<>();
    for (int i = 0; i < gameboard.length; i++) {
      for (int j = 0; j < gameboard[0].length; j++) {
        tileList.add(gameboard[i][j]);
      }
    }
    ArrayList<Tile> shuffledTiles = RandomPermutation.next(tileList);
    for (int i = 0; i < gameboard.length; i++) {
      for (int j = 0; j < gameboard[0].length; j++) {
        gameboard[i][j] = shuffledTiles.get(i * gameboard[0].length + j);
      }
    }

  }

 /** 
   * Returns a string representation of the board, getting the state of
   * each tile. If the tile is showing, displays its value, 
   * otherwise displays it as hidden.
   * 
   * Precondition: gameboard is populated with tiles
   * 
   * @return a string represetation of the board
   */
  public String toString()
  {
 
    /* your code here */
    for (int i = 0; i < gameboard.length; i++)
    {
      for (int j = 0; j < gameboard[0].length; j++)
      {
        if (gameboard[i][j].isShowingValue())
        {
          System.out.print(gameboard[i][j] + "\t");
        }
        
        else
        {
          System.out.print(" ____ ");
        }
      }
      System.out.println("");
    }
    return "";
  }

  /** 
   * Determines if the board is full of tiles that have all been matched,
   * indicating the game is over.
   * 
   * Precondition: gameboard is populated with tiles
   * 
   * @return true if all tiles have been matched, false otherwse
   */
  public boolean allTilesMatch()
  {
    /* your code  here */
    int count = 0;

    for (int i = 0; i < gameboard.length; i++)
      for (int j = 0; j < gameboard[0].length; j++)
      {
        if (gameboard[i][j].matched())
        {
          count++;
        }
      }
    
    if (count == 6)
    {
      return true;
    }

    else
    {
      return false;
    }
      
  }

  /** 
   * Sets the tile to show its value (like a playing card face up)
   * 
   * Preconditions:
   *   gameboard is populated with tiles,
   *   row values must be in the range of 0 to gameboard.length,
   *   column values must be in the range of 0 to gameboard[0].length
   * 
   * @param row the row value of Tile
   * @param column the column value of Tile
   */
  public void showValue (int row, int column)
  {
   
    /* your code here */
    gameboard[row][column].show();
  }  

  /** 
   * Checks if the Tiles in the two locations match.
   * 
   * If Tiles match, show Tiles in matched state and return a "matched" message
   * If Tiles do not match, re-hide Tiles (turn face down).
   * 
   * Preconditions:
   *   gameboard is populated with Tiles,
   *   row values must be in the range of 0 to gameboard.length,
   *   column values must be in the range of 0 to gameboard[0].length
   * 
   * @param row1 the row value of Tile 1
   * @param col1 the column value of Tile 1
   * @param row2 the row value of Tile 2
   * @param col2 the column vlue of Tile 2
   * @return a message indicating whether or not a match occured
   */
  public String checkForMatch(int row1, int col1, int row2, int col2)
  {
    String msg = "";

     /* your code here */
     if (gameboard[row1][col1].equals(gameboard[row2][col2]))
     {
      msg = "Matched";
     }

     else
     {
      msg = "No Match";
      gameboard[row1][col1].hide();
      gameboard[row2][col2].hide();
     }
    
     return msg;
  }

  /** 
   * Checks the provided values fall within the range of the gameboard's dimension
   * and that the tile has not been previously matched
   * 
   * @param rpw the row value of Tile
   * @param col the column value of Tile
   * @return true if row and col fall on the board and the row,col tile is unmatched, false otherwise
   */
  public boolean validateSelection(int row, int col)
  {

    /* your code here */
    if (row <= gameboard.length - 1 && col <= gameboard[0].length - 1)
    {
      return true;
    }

    else
    {
      return false;
    }
    
  }

}
