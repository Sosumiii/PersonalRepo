/*
 * Activity 2.5.7
 *
 * A Book class for the MediaLibrary program
 */
public class Book
{
  private String title;
  private String author;
  private int rating;
  
  /*** Constructor ****/
  public Book(String t, String a)
  {
    title = t;
    author = a;
    rating = 0;

    System.out.println("Adding book " + t);
  }
  
   /*** Accessor methods ***/
  public String getTitle() {
    return title;
  }

  public String getAuthor() {
    return author;
  }
  
  public int getRating() {
    return rating;
  }
  
  public String toString() 
  {
    String info = "\"" + title + "\", written by " + author + ". ";
    if (rating != 0) 
    { 
      info += ", rating is " + rating;
    }
    return info;
  }

  public Boolean Equals(Book b)
  {
      //System.out.println("Checking book " + t);
      return (title.equals(b.title) && author.equals(b.author));
  }

  /* public String getInfo()
{
   return "The current book information is " + info;
} */


  /*** Mutator methods ***/
  public void setTitle(String t) {
    title = t;
  }

  public void setAuthor(String a) {
    author = a;
  }

  public int adjustRating(int newRating)
  {
    System.out.println("Adjusting rating by " + r);
    
    if (newRating > 10)
    {
      rating = 10;
      return rating;
    }
    else if (newRating < 0)
    {
      rating = 0;
      return rating;
    }
    else
    {
      rating = newRating;
      return rating;
    }
    
  }
}
