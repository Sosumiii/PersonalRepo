/*
 * Activity 3.6.1
 */
public class DogArray
{
  public static void main(String[] args)
  {
    Dog md1 = new Dog("Cooper");
    Dog md2 = new Dog("Micky");
    Dog md3 = null;

    Dog[] myDogs = {md1, md2, md3};

    Dog[] neighborsDogs;
    neighborsDogs = new Dog[3];
    neighborsDogs[0] = new Dog("Max");
    neighborsDogs[1] = new Dog("Bella");
    neighborsDogs[2] = new Dog("Cocoa"); // error: Our of bounds exeception
    
    System.out.println("Dog 1: " + myDogs[0].getName() + ". Dog 2: " + myDogs[2].getName() + ". Dog 2: " + myDogs[3].getName());

    //System.out.println(myDogs[2]);

  }
}