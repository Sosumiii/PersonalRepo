/* 
 * Activity 2.5.8
 */

public class Song
{
    private String song = "";
    private double rating = 0.0;

    public Song(String s, double r)
    {
        song = s;
        rating = r;
    }
    
    /*** Accessor methods ***/
    public String getSong() {
        return song;
    }

    public double getRating() {
        return rating;
    }
       
    public String toString() 
    {
        String info = "\"" + song + "\", and the rating is " + rating + ".";
        return info;
    }

    public Boolean equals(Song s)
    {
        return (song.equals(s.song) && rating == s.rating);
    }

}