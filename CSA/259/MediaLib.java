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
  public static String owner = "PLTW";

  public static String getOwner()
  {
    return owner;
  }
  
  public void changeOwner(String newOwner)
  {
    owner = newOwner;
  }

  public void addBook(Book b)
  {
    book = b;
  }

  public void addMovie(Movie m)
  {
    movie = m;
  }

  public void addSong(Song s)
  {
    song = s;
  }

  public void testBook(Book tester)
  {
    book = tester;
  }


  public String toString() 
  {
    String info = "";

    if (book != null)
    {
      info += book;
    }
    if (movie != null)
    {
      info += movie;
    }
    if (song != null)
    {
      info += song;
      return info;
    }
    else
    {
      return "";
    }
  }
}