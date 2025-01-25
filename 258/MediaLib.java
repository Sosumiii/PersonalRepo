/**
 * Activity 2.5.7
 * 
 * A MediaLib class for the MediaLibrary program
 */
public class MediaLib
{
  private Book book;
  private Movie movie;
  private Song song;
  private static int getNumEntries = 0;
  private static int countBook = 0;
  private static int countMovie = 0;
  private static int countSong = 0;
  public static String owner = "PLTW";

  public static String getOwner()
  {
    return owner;
  }
  
  public static void changeOwner(String newOwner)
  {
    owner = newOwner;
  }

  public static int getNumEntries()
  {
    // System.out.println("Test: Owner is " + owner);
    return getNumEntries;
  }
  public void addBook(Book b)
  {
    if (countBook == 0)
    {
      book = b;
      getNumEntries++;
      countBook++;
    }
    else
    {
      System.out.println("Cannot add more books.");
    }
  }

  public void addMovie(Movie m)
  {
    if (countMovie ==  0)
    {
      movie = m;
      getNumEntries++;
      countMovie++;
    }
    else
    {
      System.out.println("Cannot add more movies.");
    }
  }

  public void addSong(Song s)
  {
    if (countSong ==  0)
    {
      song = s;
      getNumEntries++;
      countSong++;
    }
    else
    {
      System.out.println("Cannot add more songs.");
    }
  }


  public void testBook(Book tester)
  {
    book = tester;
  }

  public String toString() 
  {
    if (book != null)
    {
      String info = "";
      info += book;
      return info;
    }
    else if (movie != null)
    {
      String info = "";
      info += movie;
      return info;
    }
    else if (song != null)
    {
      String info = "";
      info += song;
      return info;
    }
    else
    {
      return "";
    }
  }
}