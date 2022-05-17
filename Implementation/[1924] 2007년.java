import java.util.*;

class Main{
    public static void main(String[] args){
        
        int x, y, tmp = 0;
        Scanner scan = new Scanner(System.in);
        String[] week = new String[]{"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int [] month = new int[]{31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        x = scan.nextInt();
        y = scan.nextInt();
        
        for (int i = 0; i<x-1; i++) {
        	tmp += month[i];
        }
        tmp+=y;
        System.out.println(week[tmp%7]);
    }
    
}