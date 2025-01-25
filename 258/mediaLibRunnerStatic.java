/*
 * Activity 2.5.8
 */

public class mediaLibRunnerStatic
{
    public static void main(String[] args)
    {
        /* MediaLib.changeOwner("me");
        System.out.println(MediaLib.owner); */

        MediaLib myLib = new MediaLib();

        Book newBook1 = new Book("Title A", "Author A");
        myLib.addBook(newBook1);

        MediaLib myLib2 = new MediaLib();
        
        Movie newMovie = new Movie("Title C", "Director C", 1.45);
        myLib2.addMovie(newMovie);
        System.out.println(MediaLib.getNumEntries());

        Book newBook2 = new Book("Title B", "Author B");
        myLib.addBook(newBook2);
        
        Movie newMovie2 = new Movie("Title D", "Director D", 2.45);
        myLib2.addMovie(newMovie2);

        Song newSong = new Song("Title E", 4.45);
        myLib2.addMovie(newMovie2);
        System.out.println(MediaLib.getNumEntries());

        System.out.println(newSong + "\n" + myLib2);


                
    }
}