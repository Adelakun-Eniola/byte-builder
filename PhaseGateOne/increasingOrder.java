import java.util.Scanner;
public class increasingOrder{
	public static void main(String [] args){
		Scanner input = new Scanner(System.in);
		System.out.println("Enter A Number:");
		int num1 = input.nextInt();
	
		System.out.println("Enter Second Number:");
		int num2 = input.nextInt();
	
		System.out.println("Enter Third Number:");
		int num3 = input.nextInt();

	
		
		int sumTotal = num1 + num2+ num3;

		int highest = num1;
		
		if (num2 > num1) highest = num2;
		if (num3 > highest) highest = num3;
		
		
		
		int smallest = num1;

		if (num2 < num1) smallest = num1;
		if (num3 < num1) smallest = num3;

		int mid = sumTotal - highest - smallest;
		
		System.out.printf("%d  %d %d", smallest, mid, highest);


	
	}

}