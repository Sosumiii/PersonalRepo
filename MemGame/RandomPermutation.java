import java.util.Random;

public class RandomPermutation 
{

    private static final Random rand = new Random();
    /* 
     * The method below gets the specified length of a list and creates a randomized list of numbers ranging
     * from one to ten without repeating any numbers.
     * 
     * The initial conditions are that the list p is initialized and that the parameter randLength is valid.
     */
    public static String[] next(String[] p, int randLength)
    {
        int length = p.length;
        String[] r = new String[randLength];

        for (int i = 0; i < r.length; i++)
        {
            int numSelect = rand.nextInt(length);
            r[i] = p[numSelect];
            
            p[numSelect] = p[length - 1];
            length--;

            //System.out.println(r[i]); //debug
            
        }

        return r;
    }
}