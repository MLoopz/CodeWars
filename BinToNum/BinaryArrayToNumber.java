
import java.util.*;

public class BinaryArrayToNumber {

    public static int ConvertBinaryArrayToInt(List<Integer> binary) {
        // Your Code
        int solution=0;
        for (int i=0; i<binary.size(); i++) {
            solution+=(int) (binary.get(i)*Math.pow(2, (binary.size()-1)-i));
        }
        return solution;
    }
    public static void main(String[] args) {
        int[] arr={0, 1, 0, 1};
        ArrayList<Integer> l = new ArrayList<Integer>();
        for (Integer integer : arr) {
            l.add(integer);
        }
        System.out.println(ConvertBinaryArrayToInt(l));
    }
}