/*
 * Project 2.4.6 Elvis Nguyen
 * Pokemon Battle Subsystem
 */
import java.util.Random;

public class PokemonBattleSubsystem
{
    //initialize class level variables
    public static int playerPokemonHealth = 100;
    public static int pokemonHealth = 100;
    public static int potionAmt = 4;
    public static int strongPotionAmt = 2;
    public static int antidoteAmt = 3;
    
    public static int useItem(String item) //This method is used when the user wants to select an item.
    {
        int potionValue = 15;
        int strongPotionValue = 25;
        int antidoteValue = 1;

        while (!item.equals("potion") && !item.equals("strong") && !item.equals("antidote"))
        {
            System.out.println("Invalid input.");
        }

        if (item.equals("potion"))
        {
            if (potionAmt > 0)
            {
                System.out.println("A potion was used.");
                potionAmt--;
                return potionValue;
            }
            else
            {
                System.out.println("There are no more potions.");
                return 0;
            }
        }
        else if (item.equals("strong potion"))
        {
            if (strongPotionAmt > 0)
            {
                System.out.println("A strong potion was used.");
                strongPotionAmt--;
                return strongPotionValue;
            }
            else
            {
                System.out.println("There are no more strong potions.");
                return 0;
            }
        }
        else if (item.equals("antidote"))
        {
            if (strongPotionAmt > 0)
            {
                System.out.println("An antidote was used.");
                antidoteAmt--;
                return antidoteValue;
            }
            else
            {
                System.out.println("There are no more antidotes.");
                return 0;
            }
        }
        else
        {
            System.out.println("Exiting item menu");
            return 0;
        }
            
    }

    public static int attacks(String playerAttack) //This method is used whenever the player wants to make an attack (based on some of Pikachu's common attacks)
    {
        int quickAttackValue = 25;
        int thunderBoltValue = 35;

        Random rn = new Random();

        while (!playerAttack.equals("quick attack") && !playerAttack.equals("thunderbolt"))
        {
            System.out.println("Invalid input.");
        }

        if (playerAttack.equals("quick attack"))
        {
            if (rn.nextInt(100) > 20)
            {
                System.out.println("Attack failed");

                return 0;
            }
            else
            {
                System.out.println("Pikachu used quick attack.");
                return quickAttackValue;
            }
        }

        if (playerAttack.equals("thunderbolt"))
        {
            if (rn.nextInt(100) > 20)
            {
                System.out.println("Attack failed");
                return 0;
            }
            else
            {
                System.out.println("Pikachu used Thunderbolt.");
                return thunderBoltValue;
            }
        }

        return 0;

    }

    public static String displayStatus()
    {
        return "Marowak Health: " + pokemonHealth + "\nYour Pikachu's Health: " + playerPokemonHealth;
    }

    public static String displayInventory()
    {
        return "Strong potion: " + strongPotionAmt + "\nPotion: " + potionAmt + "\nAntidotes: " + antidoteAmt;
    }

    public static int enemyAttack()
    {
        int boneRushValue = 25;
        int falseSwipeValue = 10;

        Random rn = new Random();

        int attackValue = rn.nextInt(2);

        if (attackValue == 0)
        {
            if (rn.nextInt(100) > 20)
            {
                System.out.println("Attack failed");

                return 0;
            }
            else
            {
                System.out.println("Marowak used used bone rush.");
                return boneRushValue;
            }
        }

        if (attackValue == 1)
        {
            if (rn.nextInt(100) > 20)
            {
                System.out.println("Attack failed");

                return 0;
            }
            else
            {
                System.out.println("Marowak used used false swipe.");
                return falseSwipeValue;
            }
        }

        
        return 0;
    }
    


}