import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
                int a, sum = 0;
                a = sc.nextInt();
                for (int i=1; i<a+1; i++){
                    sum+=i;
                }
                System.out.println(sum);
    }
}
