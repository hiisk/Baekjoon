import java.io.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));   
        int max = 0;
        int seq = 0;
        
        for(int i = 0; i< 9; i++) {
        	int tmp = Integer.parseInt(br.readLine());
        	if (tmp>max) {
        		max = tmp;
        		seq = i+1;
        	}
        }
        bw.write(max +"\n" + seq);
        bw.flush();
    }
}
