public class Accumul {
    
    public static String accum(String s) {
        // your code
        String solution="";
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j <= i; j++) {
                if (j==0){
                    if(i!=0) solution+="-";
                    solution+=String.valueOf(s.charAt(i)).toUpperCase();
                } 
                else{
                    solution+=String.valueOf(s.charAt(i)).toLowerCase();
                }
            }  
        }
        return solution;
    }

    public static void main(String[] args) {
        System.out.println(accum("abcd"));//"A-Bb-Ccc-Dddd"
        System.out.println(accum("RqaEzty"));//"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
        System.out.println(accum("cwAt"));//"C-Ww-Aaa-Tttt"
    }
}