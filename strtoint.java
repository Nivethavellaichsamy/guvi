import java.util.*;
import java.lang.*;
import java.io.B;
class IntDemo {
public static void main(String[] args) throws IOException
{
BufferedReader b=new BufferedReader(new InputStreamReader(System.in));
String str1,str2;
int x,y;
System.out.println("Enter a string");
str1=b.readLine();
str2=b.readLine();
x= (Integer.valueOf(str1));
y=(Integer.valueOf(str2));
System.out.println("The SUM is "+(x+y));
System.out.println("Difference is "+(x-y));
}
}
