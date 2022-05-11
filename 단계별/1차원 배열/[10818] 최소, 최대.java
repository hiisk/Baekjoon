import java.io.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));   
        int num = Integer.parseInt(br.readLine());
        
        int max = -1000000, min = 1000000;
        String [] input = br.readLine().split(" ");
        
        for(int i = 0; i< num; i++) {
        	int tmp = Integer.parseInt(input[i]);
        	if (tmp>max)
        		max = tmp;
        	
        	if (tmp<min)
        		min = tmp;
        }
        bw.write(min+" "+ max);
        bw.flush();
    }
}
