import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
                int a, b, c;
                a = sc.nextInt();
                b = sc.nextInt();
                c = sc.nextInt();
                if (a == b && b == c) 
                    System.out.println(10000+a*1000);
                else if (a == b || b == c)
                    System.out.println(1000+b*100);
                else if (a == c)
                    System.out.println(1000+a*100);
                else
                    System.out.println(100*Math.max(Math.max(a,b),c));
    }
}
