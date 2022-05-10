import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
                int a, b;
                a = sc.nextInt();
                b = sc.nextInt();
                if (b >= 45)
                    System.out.println(a+" "+(b-45));
                else {
                    if (a == 0){
                        a = 23;
                        b += 15;}
                    else{
                        a--;
                        b += 15;}
                    System.out.println(a+" "+b);
        }
    }
}
