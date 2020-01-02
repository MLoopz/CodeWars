public class Chocolate{
  public static int breakChocolate(int n, int m) {
    int breaks=0;
    if(n<=0&&m<=0){
      return breaks;
    }else{
      int chocolates=n*m;
      while(chocolates%2==0){
        breaks++;
      
      } 
      return breaks;
    }
    
  }