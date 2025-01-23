/*
 * Activity 2.5.7
 * 
 * The runner for the MediaLibrary program
 */
public class MediaLibRunner
{
  public static void main(String[] args)
  {
    System.out.println("Welcome to your Media Library");
    MediaLib myLib = new MediaLib();
    
    /*Book myBook = new Book("The Lord of the Rings", "Tolkien");
    myLib.addBook(myBook);

    Book myBook2 = new Book("The Lord of the Rings", "Tolkien");
    myLib.addBook(myBook2);
    
    System.out.println(myBook.Equals(myBook2)); */

    //System.out.println(myBook2.title); //Will produce an error as this line attempts to access a variable that is set to private.

    //System.out.println(myLib.bookEquals(myBook2.getAuthor(), myBook2.getTitle()));

    Movie myMovie = new Movie("Iron Man", "Jon Favreau", 2.1);
    Movie myMovie2 = new Movie("Avengers: Endgame", "Anthony Russo and Joe Russo", 3.02);
    Movie myMovie3 = new Movie("Iron Man", "Jon Favreau", 2.1);


    myLib.addMovie(myMovie);
    System.out.println(myLib);
    
    myLib.addMovie(myMovie2);
    System.out.println(myLib);

    System.out.println(myMovie.equals(myMovie2));
    System.out.println(myMovie.equals(myMovie3));



    

    
    



  }
}