public class StrongestEvenNumber {

    public static int strongestEven(int n, int m) {
        int solution=0;
        long maxZeros=0;
        long zeros=0;
        String binary="";
        for (int i = n; i <=m; i++) {
            if(i%2==0){
                binary=Integer.toBinaryString(i);
                zeros=Integer.valueOf(binary.substring(binary.lastIndexOf("1"),binary.length()-1).length());
                
                if(zeros>maxZeros) {
                    maxZeros=zeros;
                    solution=i;
                }
                i++;
            }
            
        }
        return solution; 
    }

 public static void main(String[] args) {
    //System.out.println(strongestEven(0,0));//192
    //System.out.println(strongestEven(1,2));//2
    //System.out.println(strongestEven(5,10));//8
    //System.out.println(strongestEven(48,56));//48
    //System.out.println(strongestEven(129,193));//192
    System.out.println(strongestEven(509989925,1113831035));//192
 }
}