import java.util.*; 
public class script {
  public static int sortDesc(final int num) {
    
    //Your code
    ArrayList<Integer> lista= new ArrayList<Integer>();
    String numberStr="";
    int temp=num;
    int res=0;
    while(temp>10){
      
      res=temp%10;
      temp=temp/10;
      lista.add(res);
    
    }
    lista.add(temp);
    lista.sort(Collections.reverseOrder());
    for (int number : lista) 
    { 
      numberStr+=""+number+"";
    }
    return Integer.parseInt(numberStr);
  }
  public static void main(String[] args){
      System.out.println(sortDesc(2101));
  }
}