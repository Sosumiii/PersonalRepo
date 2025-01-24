/*
 * Activity 2.5.7
 */

public class Movie
{
    private String title;
    private String director;
    private double duration;

    public Movie(String t, String a, double d)
    {
        title = t;
        director = a;
        duration = d;
    }

    /*** Accessor methods ***/
    public String getTitle() {
        return title;
    }

    public String getDirector() {
        return director;
    }
    
    public double getDuration() {
        return duration;
    }
    
    public String toString() 
    {
        String info = "\"" + title + "\", directed by " + director + ". Length of movie: " + duration + " hours.";
        return info;
    }

    public Boolean equals(Movie m)
    {
        return (title.equals(m.title) && director.equals(m.director));
    }

}