/**
 * Activity 2.5.7
 * 
 * A MediaLib class for the MediaLibrary program
 */
public class MediaLib
{
  private Book book;
  private Movie movie;

  public void addBook(Book b)
  {
    book = b;
  }

  public void addMovie(Movie m)
  {
    movie = m;
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
    else
    {
      return "";
    }
  }
}