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
    
    public static void useItem(String item) //This method is used when the user wants to select an item.
    {
        int potionValue = 15;
        int strongPotionValue = 25;

        if (item.equals("potion"))
        {
            if (potionAmt > 0 && playerPokemonHealth < 100)
            {
                System.out.println("A potion was used. \n");
                potionAmt--;
                playerPokemonHealth += potionValue;
                if (playerPokemonHealth > 100)
                {
                    playerPokemonHealth = 100;
                }
            }
            else if (potionAmt == 0)
            {
                System.out.println("There are no more potions. \n");
            }
            else if (playerPokemonHealth == 100)
            {
                System.out.println("Pikachu is at full health. \n");
            }
        }
        else if (item.equals("strong potion"))
        {
            if (strongPotionAmt > 0 && playerPokemonHealth < 100)
            {
                System.out.println("A strong potion was used.");
                strongPotionAmt--;
                playerPokemonHealth += strongPotionValue;
                if (playerPokemonHealth > 100)
                {
                    playerPokemonHealth = 100;
                }
            }
            else if (strongPotionAmt == 0)
            {
                System.out.println("There are no more strong potions.");
            }
            else if (playerPokemonHealth == 100)
            {
                System.out.println("Pikachu is at full health");
            }
        }
    }

    public static void attacks(String playerAttack) //This method is used whenever the player wants to make an attack (based on some of Pikachu's common attacks)
    {
        int quickAttackValue = 15;
        int thunderBoltValue = 20;

        Random rn = new Random();

        int genNum1 = rn.nextInt(100); //added to ensure that randomly generated numbers are differentiated.
        //System.out.println(genNum1); //debug

        if (playerAttack.equals("quick attack"))
        {
            if (genNum1 < 10)
            {
                System.out.println("Pikachu's attack missed!");
            }
            else
            {
                System.out.println("Pikachu used quick attack.");
                pokemonHealth -= quickAttackValue;
            }
        }

        if (playerAttack.equals("thunderbolt"))
        {
            if (genNum1 < 10)
            {
                System.out.println("Pikachu's attack missed!");
            }
            else
            {
                System.out.println("Pikachu used Thunderbolt.");
                pokemonHealth -= thunderBoltValue;
            }
        }

    }

    public static String displayStatus()
    {
        return "Marowak's Health: " + pokemonHealth + "\nYour Pikachu's Health: " + playerPokemonHealth;
    }

    public static String displayInventory()
    {
        return "Strong potion: " + strongPotionAmt + "\nPotion: " + potionAmt;
    }

    public static void enemyAttack()
    {
        int boneRushValue = 25;
        int falseSwipeValue = 12;

        Random rn = new Random();

        int attackValue = rn.nextInt(2);
        int genNum2 = rn.nextInt(100); //added to ensure that randomly generated numbers are differentiated.
        //System.out.println(genNum2); //debug

        if (attackValue == 0)
        {
            if (genNum2 < 10)
            {
                System.out.println("Marowak's attack missed!\n");;
            }
            else
            {
                System.out.println("Marowak used used bone rush.\n");
                playerPokemonHealth -= boneRushValue;
            }
        }

        else
        {
            if (genNum2 < 10)
            {
                System.out.println("Marowak's attack missed!\n");
            }
            else
            {
                System.out.println("Marowak used false swipe.\n");
                playerPokemonHealth -= falseSwipeValue;
            }
        }
    }
}