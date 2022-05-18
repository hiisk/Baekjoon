import java.io.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st = br.readLine();
        
        for(int i = 0; i<st.length()/10+1; i++) {
        	if (i == st.length()/10)	System.out.println(st.substring(10*i,st.length()%10+10*i));
        	else System.out.println(st.substring(10*i,10+10*i));
        }
    }
    
}