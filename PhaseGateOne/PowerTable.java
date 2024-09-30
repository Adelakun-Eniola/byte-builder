public class PowerTable{
	public static void main(String [] args){
		System.out.printf("a\tb\ta**b");

		for(int index = 1; index <=5; index++){
			for(int jupi = 2; jupi <=6; jupi++){
				System.out.printf("%d \t %d \t %d ", index, jupi, Math.pow(index,jupi));
			}
			System.out.println();
		}
	}
}
