import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        //创建一个Scanner对象
/*  Scanner sc=new Scanner(System.in);
        //从键盘接收一个整数
        System.out.println("请输入一个三位数：");
        int a=sc.nextInt();
        System.out.println(a%10);
        System.out.println(a/10%10);
        System.out.println(a/100%10);
        /*
       个位数：数值%10
       十位数：数值/10%10
       百位数：数值/100%10
       千位数：数值/1000%10
        */

       /*隐式转换：
       1 .当数据类型不一样时，java会自动将范围小的数据类型转换为范围大的数据类型
       2 .byte->short->int->long->float->double
       3 .数据类型不一样，不能进行计算，需要转成一样的数据类型 转的时候是小的转为大的
       4.byte、short、char三种类型在计算时都会被提升为int类型
       */

/* 

       //约会类题目
       //1键盘录入两个整数，表示你和对象的时髦度（0-10）
       //如果你的时髦程度大于对象的时髦程度，则输出：你更时髦，去约会吧！ 输出True 否则false
       Scanner sc1=new Scanner(System.in);
       System.out.println("请输入你的时髦度：");
        int a1=sc1.nextInt();
        System.out.println("请输入对象的时髦度：");
        int b1=sc1.nextInt();
       // if (a1>b1){System.out.println("true");}else {System.out.println("false");}
        boolean result=a1>b1;
        System.out.println(result);


        //数字6
        Scanner sc2=new Scanner(System.in);
        System.out.println("请输入一个整数：");
        int a2=sc2.nextInt();
        System.out.println("请输入一个整数：");
        int b2=sc2.nextInt();
        boolean result2=(a2==6||b2==6||(a2+b2)%6==0);
        System.out.println(result2);
*/

        //两只老虎
        Scanner sc3=new Scanner(System.in);
        System.out.println("请输入第一只老虎的体重：");
        int a3=sc3.nextInt();
        System.out.println("请输入第二只老虎的体重：");
        int b3=sc3.nextInt();
      // boolean value= a3==b3?true:false;
      String value=a3==b3?"相等":"不相等";
        System.out.println(value);

    }
    
}
