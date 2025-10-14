/*
 * Project 1.3.8
 */

import java.util.Scanner;
 
public class Project138 {

    public static void main(String args[]) {
        
        Scanner sc = new Scanner(System.in);

        System.out.println("Please enter your name:");
        String playerName = sc.nextLine();

        System.out.println("You are about to enter a cave. \n You bring a flashlight and some \n food with you on your expedition. \n Within the cave, there are two paths \n to head down from. \n What path will you choose? \n Type 1 or 2.");
        Integer pathOption = sc.nextInt();

        if (pathOption == 1)
        {
            System.out.println("You have entered the first path. \n Suddenly, some rocks behind you collapse \n into the entrance and now you are trapped. \n What will you try first? \n 1. Try to reach out for help. \n 2. Keep exploring the cave.");
            Integer firstChoice = sc.nextInt();

            if (firstChoice == 1)
            { 
                System.out.println("You have tried reaching out for help. \n Unfortunately, the rocks prove too big for \n any meaningful noise to excape. \n Your phone also has no reception either. \n What will you do next? \n 1. Wait near the entrance and hope that help arrives. \n 2. Kick the rocks.");
                Integer secondChoice = sc.nextInt();

                if (secondChoice == 1)
                {
                    System.out.println("You chose to wait for help. \n While you are waiting, \n you rummage through your bag for anything \n that could be of use. \n You find an emergency light in your bag. \n You also find a small pickaxe. \n which item do you use? \n 1. The emergency light. \n 2. the pickaxe.");
                    Integer thirdChoice = sc.nextInt();

                    if (thirdChoice == 1)
                    {
                        System.out.println("You have used the emergency light. \n The light dimmly shines through the cracks in the rock. \n A few hours later, a hitchhiker crosses by \n and notices your flashing light. \n He calls for rescue and you end up getting saved.");
                        System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + ", has gotten trapped in the local caves. \n" + playerName + " was rescued by a passing hitchhiker.");
                    }
                    else if (thirdChoice == 2)
                    {
                        System.out.println("You chose to use the axe on the rock. \n there is a significant chance that the rocks might crumble \n upon you, but you start making like Minecraft Steve and start swinging. \n The rocks come crashing down and you are left unscathed. \n you quickly find your way back to civilization.");
                        System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + ", has gotten trapped in the local caves. \n" + playerName + " has simply dug out of the cave using a handy pickaxe.");
                    }
                }
                
                while ((secondChoice != 1) && (secondChoice == 2))
                {
                    System.out.println("Kicking the rock did nothing.");
                    System.out.println("You have tried reaching out for help. \n Unfortunately, the rocks prove too big for \n any meaningful noise to excape. \n Your phone also has no reception either. \n What will you do next? \n 1. Wait near the entrance and hope that help arrives. \n 2. Kick the rocks.");
                    secondChoice = sc.nextInt();

                    if (secondChoice == 1)
                    {
                        System.out.println("You chose to wait for help. \n While you are waiting, \n you rummage through your bag for anything \n that could be of use. \n You find an emergency light in your bag. \n You also find a small pickaxe. \n which item do you use? \n 1. The emergency light. \n 2. the pickaxe.");
                        Integer thirdChoice = sc.nextInt();

                        if (thirdChoice == 1)
                        {
                            System.out.println("You have used the emergency light. \n The light dimmly shines through the cracks in the rock. \n A few hours later, a hitchhiker crosses by \n and notices your flashing light. \n He calls for rescue and you end up getting saved.");
                            System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + ", has gotten trapped in the local caves. \n" + playerName + "was rescued by a passing hitchhiker.");
                        }
                        else if (thirdChoice == 2)
                        {
                            System.out.println("You chose to use the axe on the rock. \n there is a significant chance that the rocks might crumble \n upon you, but you start doing like cavecraft Steve and start swinging. \n The rocks come crashing down and you are left unscathed. \n you quickly find your way back to civilization.");
                            System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + ", has gotten trapped in the local caves. \n" + playerName + "has simply dug out of the cave using a handy pickaxe.");
                        }
                    }
                }
                
                

            }
            else if (firstChoice == 2)
            {
                System.out.println("You wander around the cave and eventually find yourself inside of the second path. \n You realize that the entrance to the second path is wide open. \n Do you 1. exit the cave or 2. continue exploring?");
                Integer secondChoice = sc.nextInt();

                if (secondChoice == 1)
                {
                    System.out.println("You have decided to exit the cave and report your findings.");
                    System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + " has reported a cave with a collapsed entrance. \n Please do not visit the cave for your safety.");
                }
                else if (secondChoice == 2)
                {
                    System.out.println("You enter the second path. \n as you walk further into the cave, you find all sorts of ores that you could bring back and sell. \n You either 1. pick them up and shove them into your bag or \n 2. Leave them where they are and continue exploring.");
                    Integer thirdChoice = sc.nextInt();
        
                    if (thirdChoice == 1)
                    {
                        System.out.println("You greedily picked the ores up and shoved them into your bag. \n You continue to travel further into the cave for 2 hours. \n You then enter a room containing what seemed like thousands of ores. \n You 1. stay and try to collect as many ores as you can or 2. move on.");
                        Integer fourthChoice = sc.nextInt();
        
                        if (fourthChoice == 1)
                        {
                            System.out.println("You stayed and started picking the ores up. \n You eventually pass out due to exhaustion. \n Fortunutely for you, another adventurer passed by and carried you to safety.");
                            System.out.print("The local newspaper reads: \n An adventurer, " + playerName + ", was found unconscious in the local cave. \n A bunch of ores were found on their person. \n The ores were seized and the adventurerer was labeled greedy.");
                        }
        
                        else if (fourthChoice == 2)
                        {
                            System.out.println("You ignored the room and walked further into the cave. \n Eventually you found a secret room with gold spread every inch of said room. \n you bring as many pieces of gold that you could carry back into civilization.");
                            System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + ", has suddenly found themselves a millionare after a fateful exploration in the caves.");
                        }
                    }
                    else if (thirdChoice == 2)
                    {
                        System.out.println("You ignored the ores. \n You continue to travel further into the cave for 2 hours. \n You then enter a room containing what seemed like thousands of ores. \n You 1. stay and try to collect as many ores as you can or 2. move on.");
                        Integer fourthChoice = sc.nextInt();
        
                        if (fourthChoice == 1)
                        {
                            System.out.println("You stayed and started picking the ores up. \n You eventually pass out due to exhaustion. \n Fortunutely for you, another adventurer passed by and carried you to safety.");
                            System.out.print("The local newspaper reads: \n An adventurer, " + playerName + ", was found unconscious in the local cave. \n A bunch of ores were found on their person. \n The ores were seized and the adventurerer was labeled greedy.");
                        }
        
                        else if (fourthChoice == 2)
                        {
                            System.out.println("You ignored the room and walked further into the cave. \n Eventually you found a secret room with gold spread every inch of said room. \n you bring as many pieces of gold that you could carry back into civilization.");
                            System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + ", has suddenly found themselves a billionare after a fateful exploration in the caves.");
                        }
                    }
                }
            }
        }

        else if (pathOption == 2)
        {
            System.out.println("You enter the second path. \n as you walk further into the cave, you find all sorts of ores that you could bring back and sell. \n You either 1. pick them up and shove them into your bag or \n 2. Leave them where they are and continue exploring.");
            Integer firstChoice = sc.nextInt();

            if (firstChoice == 1)
            {
                System.out.println("You greedily picked the ores up and shoved them into your bag. \n You continue to travel further into the cave for 2 hours. \n You then enter a room containing what seemed like thousands of ores. \n You 1. stay and try to collect as many ores as you can \n or 2. move on.");
                Integer secondChoice = sc.nextInt();

                if (secondChoice == 1)
                {
                    System.out.println("You stayed and started picking the ores up. \n You eventually pass out due to exhaustion. \n Fortunutely for you, another adventurer passed by and carried you to safety.");
                    System.out.print("The local newspaper reads: \n An adventurer, " + playerName + ", was found unconscious in the local cave. \n A bunch of ores were found on their person. \n The ores were seized and the adventurerer was labeled greedy.");
                }

                else if (secondChoice == 2)
                {
                    System.out.println("You ignored the room and walked further into the cave. \n Eventually you found a secret room with gold spread every inch of said room. \n you bring as many pieces of gold that you could carry back into civilization.");
                    System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + ", has suddenly found themselves a millionare after a fateful exploration in the caves.");
                }
            }
            else if (firstChoice == 2)
            {
                System.out.println("You ignored the ores. \n You continue to travel further into the cave for 2 hours. \n You then enter a room containing what seemed like thousands of ores. \n You 1. stay and try to collect as many ores as you can \n or 2. move on.");
                Integer secondChoice = sc.nextInt();

                if (secondChoice == 1)
                {
                    System.out.println("You stayed and started picking the ores up. \n You eventually pass out due to exhaustion. \n Fortunutely for you, another adventurer passed by and carried you to safety.");
                    System.out.print("The local newspaper reads: \n An adventurer, " + playerName + ", was found unconscious in the local cave. \n A bunch of ores were found on their person. \n The ores were seized and the adventurerer was labeled greedy.");
                }

                else if (secondChoice == 2)
                {
                    System.out.println("You ignored the room and walked further into the cave. \n Eventually you found a secret room with gold spread every inch of said room. \n you bring as many pieces of gold that you could carry back into civilization.");
                    System.out.print("The local newspaper reads: \n Local adventurer, " + playerName + ", has suddenly found themselves a billionare after a fateful exploration in the caves.");
                }
            }

        }
    }
}
