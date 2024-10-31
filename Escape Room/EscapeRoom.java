/*
* Problem 1: Escape Room
* 
* V1.0
* 10/10/2019
* Copyright(c) 2019 PLTW to present. All rights reserved
*/
import java.util.Scanner;
/**
 * Create an escape room game where the player must navigate
 * to the other side of the screen in the fewest steps, while
 * avoiding obstacles and collecting prizes.
 */
public class EscapeRoom
{

      // describe the game with brief welcome message
      // determine the size (length and width) a player must move to stay within the grid markings
      // Allow game commands:
      //    right, left, up, down: if you try to go off grid or bump into wall, score decreases
      //    jump over 1 space: you cannot jump over walls
      //    if you land on a trap, spring a trap to increase score: you must first check if there is a trap, if none exists, penalty
      //    pick up prize: score increases, if there is no prize, penalty
      //    help: display all possible commands
      //    end: reach the far right wall, score increase, game ends, if game ended without reaching far right wall, penalty
      //    replay: shows number of player steps and resets the board, you or another player can play the same board
      // Note that you must adjust the score with any method that returns a score
      // Optional: create a custom image for your player use the file player.png on disk
    
      /**** provided code:
      // set up the game
      boolean play = true;
      while (play)
      {
        // get user input and call game methods to play 
        play = false;
      }
      */

  public static void main(String[] args) 
  {      
    // welcome message
    System.out.println("Welcome to EscapeRoom!");
    System.out.println("Get to the other side of the room, avoiding walls and invisible traps,");
    System.out.println("pick up all the prizes.\n");
    
    GameGUI game = new GameGUI();
    game.createBoard();

    // size of move
    int m = 60; 
    int j = 120;
    
    // individual player moves
    int px = 0;
    int py = 0; 
    
    int score = 0;

    game.setTraps(4);

    Scanner in = new Scanner(System.in);
    String[] validCommands = { "right", "left", "up", "down", "r", "l", "u", "d",
    "jump", "jr", "jumpleft", "jl", "jumpup", "ju", "jumpdown", "jd",
    "pickup", "p", "quit", "q", "replay", "help", "?", "c", "check"};
  
    // set up game
    boolean play = true;
    while (play)

      /* TODO: get all the commands working */
	  /* Your code here */
    
      { 
      //Primary control functions. VScode Recommends to switch them to switch cases. 
      String input = UserInput.getValidInput(validCommands);
      
      //Displays a list of valid commands.
      if (input.equals("help") || input.equals("?"))
      System.out.println("Here is a list of commands: \nMove right: right, 'r'\nMove left: left, l\nMove up: up, u\nMove down: down, d\nJump right: jr\nJump left: jumpleft, jl\nJump up: jumpup, ju\nJump down: jumpdown, jd\nPick up item: pickup, p\nQuit game: quit, q\nReplay game: replay\nDisplay help: help, ?\nCheck for traps and spring them if they are present: c, check");

      if (input.equals("quit"))
      {
        score += game.endGame();

        System.out.println("score=" + score);
        System.out.println("steps=" + game.getSteps());
      }

      //Checks for traps
      if (input.equals("check") || input.equals("c"))
      {
        game.isTrap(px+m, py);
        game.isTrap(px-m, py);
        game.isTrap(px, py+m);
        game.isTrap(px, py-m);
      }
      
      //Triggers the trap
      if (input.equals("Trigger") || input.equals("t"))
      {
        score += game.springTrap(px, py);
      }

      if (input.equals("replay"))
      {
        score += game.replay();
      }

      if (input.equals("pickup") || input.equals("p"))
      {
        score += game.pickupPrize();
      }

      //Standard Movement controls.
      if (input.equals("right") || input.equals("r"))
      {
        score += game.movePlayer(m, 0);
      }
      else if (input.equals("left") || input.equals("l")) 
      {
        score += game.movePlayer(-m, 0);
      }
      else if (input.equals("up") || input.equals("u")) 
      {
        score += game.movePlayer(0, -m);
      }
      else if (input.equals("down") || input.equals("d")) 
      {
        score += game.movePlayer(0, m);
      }

      //Jump moves the player one space further than the traditional movement commands.
      if (input.equals("jumpright") || input.equals("jr"))
      {
        score += game.movePlayer(j, 0);
      }
      else if (input.equals("jumpleft") || input.equals("jl")) 
      {
        score += game.movePlayer(-j, 0);
      }
      else if (input.equals("jumpup") || input.equals("ju")) 
      {
        score += game.movePlayer(0, -j);
      }
      else if (input.equals("jumpdown") || input.equals("jd")) 
      {
        score += game.movePlayer(0, j);
      }
    }

  

    score += game.endGame();

    System.out.println("score=" + score);
    System.out.println("steps=" + game.getSteps());
  }
}

        
