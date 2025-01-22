/*
 * Project 2.4.6 Elvis Nguyen
 * Program: Pokemon Battle Simulation
 */

import java.util.Scanner;

public class MainPokemonBattle
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        
        while (PokemonBattleSubsystem.playerPokemonHealth > 0 && PokemonBattleSubsystem.pokemonHealth > 0)
        {
            System.out.println(PokemonBattleSubsystem.displayStatus() + "\nWhat would you like to do? \nAttack \nInventory");
            String choice = sc.nextLine();
            choice = choice.toLowerCase();
            System.out.println("|-----------------------------------|\n");

            if (!choice.equals("attack") && !choice.equals("inventory"))
            {
                System.out.println("Invalid choice.");
                System.out.println("|-----------------------------------|\n");
            }
            else if (choice.equals("attack"))
            {
                System.out.println("You have two attacks to choose from \nThunderbolt \nQuick Attack \nType \"back\" to exit this menu \n");
                String attackChoice = sc.nextLine();
                attackChoice = attackChoice.toLowerCase();

                if (!attackChoice.equals("thunderbolt") && !attackChoice.equals("quick attack") && !attackChoice.equals("back"))
                {
                    System.out.println("Invalid choice.");
                    System.out.println("|-----------------------------------|\n");
                }
                else if (attackChoice.equals("thunderbolt"))
                {
                    PokemonBattleSubsystem.attacks(attackChoice);
                    PokemonBattleSubsystem.enemyAttack();
                    System.out.println("|-----------------------------------|\n");
                }
                else if (attackChoice.equals("quick attack"))
                {
                    PokemonBattleSubsystem.attacks(attackChoice);
                    PokemonBattleSubsystem.enemyAttack();
                    System.out.println("|-----------------------------------|\n");
                }
                else if (attackChoice.equals("back"))
                {
                    System.out.println("|-----------------------------------|\n");
                }                
            }
            else if (choice.equals("inventory"))
            {
                System.out.println("Here are the items that are currently in your bag \n" + PokemonBattleSubsystem.displayInventory());
                System.out.println("");
                System.out.println("What would you like to choose? \nPotion \nStrong potion");
                String inventoryChoice = sc.nextLine();
                inventoryChoice = inventoryChoice.toLowerCase();

                if (!inventoryChoice.equals("potion") && !inventoryChoice.equals("strong potion"))
                {
                    System.out.println("Invalid choice.");
                    System.out.println("|-----------------------------------|\n");
                }
                else if (inventoryChoice.equals("potion"))
                {
                    PokemonBattleSubsystem.useItem(inventoryChoice);
                    PokemonBattleSubsystem.enemyAttack();
                    System.out.println("|-----------------------------------|\n");
                }
                else if (inventoryChoice.equals("strong potion"))
                {
                    PokemonBattleSubsystem.useItem(inventoryChoice);
                    PokemonBattleSubsystem.enemyAttack();
                    System.out.println("|-----------------------------------|\n");
                }
            }
        }

        if (PokemonBattleSubsystem.pokemonHealth <= 0)
        {
            PokemonBattleSubsystem.pokemonHealth = 0;
            System.out.println("Marowak has fainted, \nYou win!");
        }
        else if (PokemonBattleSubsystem.playerPokemonHealth <= 0)
        {
            PokemonBattleSubsystem.pokemonHealth = 0;
            System.out.println("Pikachu has fainted, \nYou lose!");

        }
    }
}