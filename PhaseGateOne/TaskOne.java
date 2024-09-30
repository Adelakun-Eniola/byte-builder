import java.util.Scanner;
public class TaskOne{
	public static void main(String [] args){
		Scanner scan = new Scanner(System.in);
		System.out.println("Enter A Number Between 0 And 1000");
		int numberEntered = scan.nextInt();
		
		int xtract_one = numberEntered % 10;
		int new_value = numberEntered /10;
		int xtract_two = numberEntered %10;
		int new_value_two = numberEntered /10;


		int total = xtract_one + xtract_two + new_value_two;
		System.out.println(total);
	
	}

}