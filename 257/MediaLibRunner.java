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
    Book myBook = new Book("The Lord of the Rings", "Tolkien");

    System.out.println("Library: " + myLib);

    myLib.addBook(myBook);
    System.out.println("Library: " + myLib);


    int myRating = 5;
    myBook.adjustRating(myRating);
    System.out.println(myBook);


  }
}