import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); 
        
//       N, N_arr 입력
        int N = Integer.parseInt(br.readLine());
        int[] N_arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int cnt = st.countTokens();
        
        for(int i=0; i<cnt; i++) {
            N_arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(N_arr);
        
//        M, M_arr 입력
        int M = Integer.parseInt(br.readLine());
        
        st = new StringTokenizer(br.readLine());
        cnt = st.countTokens();
        
//        리스트 정렬
        
        for (int i = 0; i<cnt; i++) {
        	int tmp = Arrays.binarySearch(N_arr, Integer.parseInt(st.nextToken()));
        	if (tmp < 0)
        		bw.write("0\n");
        	else
        		bw.write("1\n");
        }
        bw.flush();
    }
    
}
