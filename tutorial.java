import java.awt.*;
import java.sql.SQLOutput;
import java.util.Date;

public class Main {
    public static void main(String[] args) {
        int ages = 30, temp = 20;
        int tte = 20;
        int myAge = 30;
        int herAge = myAge;
        System.out.println(herAge);
        System.out.println("Hello world!");
        //types in java
        // byte = 1 //short = 2
        //int = 4 //long = 8
        //float 4 for decimal numbers //double = 8
        // char = 2 //boolean = 2
        //int viewsCount = 123_456_789; //long viewsCounts = 3_123_456_789L;
        //float price = 10.99F; //char letter = 'A'; // ='' for single charater
        //boolean isEligible = false;
       // byte age = 30;
        //Date now = new Date();
        //System.out.println(now);
        //byte x = 1;
        //byte y = x;
        //x = 2;
        //System.out.println(y);

        //ref types
        Point point1 = new Point(1, 1);
        Point point2 = point1;
        point1.x = 2;
        System.out.println(point2);
        
        //Write a Java program to print 'Hello' on screen and then print your name on a separate line.
        import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input = new Scanner (System.in);
        System.out.println("Input you first name: ");
        String fname = input.next();
        System.out.println("Input your last name: ");
        String lname = input.next();
        System.out.println();
        System.out.println("Hello \n"+fname+" "+lname);
    }
}
    }
}
