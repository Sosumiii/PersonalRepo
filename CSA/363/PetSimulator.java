/*
 * Activity 3.6.3
 */
public class PetSimulator
{
  public static void main(String[] args)
  {
    // create an array that can hold up to 10 pets (does not require looping)
    Pet[] pets = {new Pet("Billy", 2), new Pet("Whiskers", 1), new Pet("Micky", 2), new Pet("Loaf", 1), new Pet("Miggie", 2), new Pet("Luna", 1), new Pet("Kobe", 2), new Pet("Pika", 1), new Pet("Max", 2), new Pet("Lily", 1)};
    // adopt (create and name) four pets, two cats, two dogs (does not require looping)
    Pet myFirstDog = pets[0];
    Pet mySecondDog = pets[2];

    Pet myFirstCat = pets[1];
    Pet mySecondCat = pets[3];

    Pet[] myPets = {myFirstDog, mySecondDog, myFirstCat, mySecondCat};
    Pet[] myDogs = {myFirstDog, mySecondDog};
    Pet[] myCats = {myFirstCat, mySecondCat};

    // first things first, feed your pets
    for (Pet p : myPets)
    {
        p.feed();
    }

    // next, make yourself the owner of all of your new pets
    for (Pet p : myPets)
    {
        p.setOwner("Elvis");
    }

    // your dogs make some noise, take them for a walk
    for (Pet d : myDogs)
    {
        d.walk();
    }

    // when you get back, your cats make some noise
    for (Pet c : myCats)
    {
        c.makeNoise();
    }
    // give all of your pets a treat
    for (Pet p : myPets)
    {
        p.giveTreat();
    }
    // groom your cats
    for (Pet c : myCats)
    {
        c.groom();
    }
    // grooming is done, play with all pets
    for (Pet c : myCats)
    {
        c.play();
    }

    // whew, that was tiring, all pets nap and get fed
    for (Pet p : myPets)
    {
        p.feed();
        p.sleep();
    }

    System.out.println("--- MY PETS ---");
    // show the state of all of your pets
    for (Pet p : myPets)
    {
        System.out.println(p + ", ");
    }
    
    // You decide to get a couple of pets for your friend (does not require looping)
    Pet friendsFirstDog = pets[4];
    Pet friendsSecondDog = pets[6];

    Pet friendsFirstCat = pets[5];
    Pet friendsSecondCat = pets[7];
    
    // set the owner of the new pets to your friends name
    Pet[] friendsPets = {friendsFirstDog, friendsSecondDog, friendsFirstCat, friendsSecondCat};

    System.out.println("--- FRIEND'S PETS ---");
    for (Pet p : friendsPets)
    {
        System.out.println(p + ", ");
    }
    
    System.out.println("--- MY PETS ---");
    // show the state of all of your pets
    for (Pet p : myPets)
    {
        System.out.println(p + ", ");
    }
  }
}