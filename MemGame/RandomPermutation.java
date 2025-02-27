import java.util.Random;

public class RandomPermutation 
{
    private static final Random rand = new Random();

    /**
     * The method below gets the specified length of a list and creates a randomized list of numbers ranging
     * from one to ten without repeating any numbers.
     * 
     * The initial conditions are that the list p is initialized and that the parameter randLength is valid.
     */
    public static String[] next(String[] p, int randLength)
    {
        int length = p.length;
        String[] r = new String[randLength];
        String[] temp = new String[length];

        // Copy elements from p to temp
        for (int i = 0; i < length; i++) {
            temp[i] = p[i];
        }

        for (int i = 0; i < randLength; i++)
        {
            int numSelect = rand.nextInt(length);
            r[i] = temp[numSelect];
            
            // Swap the selected element with the last element in the array
            temp[numSelect] = temp[length - 1];
            length--;
        }

        return r;
    }
}