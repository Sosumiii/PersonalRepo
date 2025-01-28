/*
 * Activity 2.5.8
 */

public class Song
{
    private String title;
    private double rating;

    public Song(String t, double r)
    {
        title = t;
        rating = r;
    }

    public Song(String t)
    {
        title = t;
    }

    /*** Accessor methods ***/
    public String getTitle() {
        return title;
    }

    public double getRating() {
        return rating;
    }
    
    public String toString() 
    {
        String info = "\"" + title + "\", and the rating is " + rating + ". ";
        return info;
    }

    public Boolean equals(Song s)
    {
        return (title.equals(s.title) && rating == s.rating);
    }

}