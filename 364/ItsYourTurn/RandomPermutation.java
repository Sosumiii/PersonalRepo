import java.util.Random;

public class RandomPermutation 
{
    private static final int[] p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    private static final Random rand = new Random();
    private static int length = p.length;

    /* 
     * The method below gets the specified length of a list and creates a randomized list of numbers ranging
     * from one to ten without repeating any numbers.
     * 
     * The initial conditions are that the list p is initialized and that the parameter randLength is valid.
     */
    public static int[] next(int randLength)
    {
        int[] r = new int[randLength];

        for (int i = 0; i < r.length; i++)
        {
            int numSelect = rand.nextInt(length);
            r[i] = p[numSelect];
            
            p[numSelect] = p[length - 1];
            length--;
            
        }

        return r;
    }
}
