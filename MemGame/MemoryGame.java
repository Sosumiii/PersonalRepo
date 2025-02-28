import java.util.Scanner;

/**
 * Project 3.6.5
 *
 * The Memory Game shows a random sequence of "memory strings" in a variety of buttons.
 * After wathcing the memory strings appear in the buttons one at a time, the
 * player recreates the sequence from memory.
 */
public class MemoryGame
{
  public static void main(String[] args) {

    // Create the "memory strings" - an array of single character strings to 
    // show in the buttons, one element at a time. This is the sequence
    // the player will have to remember.

    // Create the game and gameboard. Configure a randomized board with 3 buttons.
    // (Later, you can change options to configure more or less buttons
    // and turn randomization on or off.)
    boolean play = true;
    MemoryGameGUI gui = new MemoryGameGUI();
    Scanner sc = new Scanner(System.in);

    String user; //= sc.nextLine();

    //user = user.replaceAll("[^a-zA-Z]", "");
    //user = user.toLowerCase();

    System.out.println("Type one letter then press enter and repeat");

    String[] letters = {new String(user = sc.nextLine().toLowerCase()), new String(user = sc.nextLine().toLowerCase()), new String(user = sc.nextLine().toLowerCase()), new String(user = sc.nextLine().toLowerCase()), new String(user = sc.nextLine().toLowerCase())};

    user = user.replaceAll("[^a-zA-Z]", "");
    //user = user.toLowerCase();

    gui.createBoard(3, true);


    
    int rounds = 1;
    int score = 0;
    double time = 2.0;

    String[] r = RandomPermutation.next(letters, letters.length);

    //gui.createBoard(5, true);

    // Play the game until user wants to quit.
    while (play)
    {
      String n = "";

      for (String r1 : r) {
          n += r1;
      }
      
      System.out.println(n);
      String guess = gui.playSequence(r, time);

      if (guess == null)
      {
        play = false;
        break;
      }


      guess = guess.replaceAll("[^a-zA-Z]", "");
      guess = guess.toLowerCase();

      if (guess.equals(n))
      {
        gui.matched();
        score++;
        play = gui.playAgain();
        if (play)
        {
          rounds++;
          time -= 0.2;
          r = RandomPermutation.next(letters, letters.length);
        }

      }

      else if (guess.equals(""))
      {
        gui.tryAgain();
      }

      else
      {
        gui.tryAgain();
        rounds++;
      }
      
    }

    gui.showScore(score, rounds);
    gui.quit();
    


      // Create a new array that will contain the randomly ordered memory strings.

      // Create a list of randomly ordered integers with no repeats, the length
      // of memory strings. Use it to create a random sequence of the memory strings.
      // - OR -
      // Overload the next method in RandomPermutation to create a random sequence 
      // of the memory strings, passed as a parameter.

      // Play one sequence, delaying half a second for the strings to show
      // in the buttons. Save the player's guess. 
      // (Later, you can speed up or slow down the game.)

      // Determine if player's guess matches all elements of the random sequence.
      
        // Cleanup the guess - remove commas and spaces. Refer to a new String method 
        // replace to make this easy.
        
        // iterate to determine if guess matches sequence

        // If match, increase score, and signal a match, otherwise, try again.

      // Ask if user wants to play another round of the game 
      // and track the number of games played.
   
    // When done playing, show score and end the game.
  }
}