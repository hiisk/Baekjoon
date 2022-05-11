import java.io.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));   
        
        int [] arr = new int[10];
        int tmp = Integer.parseInt(br.readLine())* Integer.parseInt(br.readLine()) * Integer.parseInt(br.readLine());
        String str = String.valueOf(tmp);
        
        for(int i=0; i< str.length(); i++) {
        	arr[(str.charAt(i) - 48)]++;
        }
        for(int i = 0; i<10; i++) {
        	bw.write(arr[i]+"\n");
        }
        bw.flush();
    }
}
