import java.io.*;
import java.util.StringTokenizer;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));   
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        
        int b = 0, c = 0, d = 0, count = 0 ;
        d = a;
        while (true) {
        	b = a/10 + a%10;
        	c = b%10 + (a%10)*10;
        	a = c;
        	count+=1;
        	if (d == a)
        		break;
        }
        System.out.println(count);
    }
}
