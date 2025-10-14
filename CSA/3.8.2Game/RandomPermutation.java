import java.util.ArrayList;
import java.util.Random;

public class RandomPermutation 
{
    private static final Random rand = new Random();

    /* 
     * The method below takes an ArrayList of Horses and returns a randomly ordered version of it.
     */
    public static ArrayList<Tile> next(ArrayList<Tile> tiles)
    {
        ArrayList<Tile> shuffledTiles = new ArrayList<>(tiles);
        for (int i = shuffledTiles.size() - 1; i > 0; i--)
        {
            int j = rand.nextInt(i + 1);
            Tile temp = shuffledTiles.get(i);
            shuffledTiles.set(i, shuffledTiles.get(j));
            shuffledTiles.set(j, temp);
        }
        return shuffledTiles;
    }
}
