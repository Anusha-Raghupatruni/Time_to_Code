public class Mainclass{

     public static void main(String []args){
        //Person p1 = new Person();//Person() is default constructor with no  arguments.
        //p1.age = 24;
        //p1.name = "Anu";
        
        //Person p2 = new Person(31,"Bhargav");
        //p2.age = 31;
        //p2.name = "Bhargav";
        
        //System.out.println(p1.age+" "+p1.name);//accessed properties
        //System.out.println(p2.age+" "+p2.name);

        //p1.eat();//behaviour accessed
        //p2.walk();
        //p2.walk(2);
        //System.out.println(Person.count);
        Developer d1 = new Developer(24,"Zayn");
        d1.walk();
     }
}

class Developer extends Person{
    public Developer(int age,String name){
        super(age, name);
    }
    
}


class Person {
    String name;
    int age;
    static int count;//property of class not object  .Static is used as class element
    
    public Person(){
        count++;
        System.out.println("Creating an object");
    }//constructers used to create new objects it prints twice as this is calling twice
    //public Person(int age, String name){
        //this();
        //this.name = name;
        //this.age = age;
    //}
    void walk(){
        System.out.println(name + " " + "is walking.");
        
    }
     
    void eat(){
        System.out.println(name + " " +"is eating.");
        
    }
     void walk(int steps){
        System.out.println(name + " " + "walked " + steps + " steps");
        
    }
     void dowork(){
        System.out.println("This Person is Working");
        
    }
}

