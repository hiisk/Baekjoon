import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); 
        Stack<Integer> stack = new Stack<>();
        
        int num = Integer.parseInt(br.readLine());
        int sum = 0;
        
        for (int i = 0; i <num; i++) {
        	int tmp = Integer.parseInt(br.readLine());
        	if (tmp>0) stack.push(tmp);
        	else stack.pop();
        }
        

    	while (!stack.empty()) {
    		sum += stack.pop();
        }
    	bw.write(sum+"");
    	
        bw.flush();
        bw.close();
    }
    
}