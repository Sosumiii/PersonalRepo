public class Person 
{
    private String name;
    private int age;
    private String favoriteColor;
    
    public Person(String name, int age, String favoriteColor)
    {
        this.name = name;
        this.age = age;
        this.favoriteColor = favoriteColor;

    }
    
    public String getName()
    {
        return name;
    }
    
    public int getAge()
    {
        return age;
    }

    public String getFavoriteColor()
    {
        return favoriteColor;
    }
    
    public String toString()
    {
        return name + " " + age + " " + favoriteColor;
    }
}
