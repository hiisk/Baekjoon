import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int tmp = 1;
        Stack<Integer> stack = new Stack<>();
        boolean flag = true;
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i<n; i++) {
        	int num = Integer.parseInt(br.readLine());
        	
        	while (tmp <= num) {
        		stack.push(tmp);
        		sb.append("+\n");
        		tmp+=1;
        	}
        	
        	if (stack.peek()== num) {
        		stack.pop();
        		sb.append("-\n");
        	}
        	else { 
        		System.out.println("NO");
        		flag = false;
        		break;
        	}
        }
        if (flag){
	        System.out.println(sb);
        }
    }
    
}