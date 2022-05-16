import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = 10;
        List<Integer> list = new ArrayList<>();
        
        for (int i = 0; i<n; i++) {
        	int num = Integer.parseInt(br.readLine());
        	
        	list.add(num%42);
        	
        list = list.stream().distinct().collect(Collectors.toList());
        }
        if (list.size()>0){
        	System.out.println(list.size());
        }
        else	System.out.println(1);
    }
    
}