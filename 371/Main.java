import java.util.ArrayList;
public class Main 
{

    public static void main(String[] args)
    {
        ArrayList<Person> people = new ArrayList();
        people.add(new Person("Alice", 25, "blue"));
        people.add(new Person("Bob", 30, "green"));
        people.add(new Person("Charlie", 35, "red"));
        people.add(new Person("David", 40, "yellow"));
        
        System.out.println(people);
    }

}
