import java.util.Scanner; //1 导包，找到scanner这个类在哪
        //地写在类定义的上面
public class ScannerDemol {
public static void main(String[] args){
        //创建扫描器对象
        Scanner sc = new Scanner(System.in);
        //获取键盘输入的整数
        System.out.println("请输入一个整数：");
        //变量num记录了键盘录入的数据
        int num = sc.nextInt();
        System.out.println("你输入的整数是："+num);




        //键盘录入练习
        //键盘输入数字并求和
        //需求 ；键盘录入两个整数 并求出它们的和
        Scanner sc1=new Scanner(System.in);
        System.out.println("请输入第一个数字：");
        int a=sc1.nextInt();
        System.out.println("请输入第二个数字：");
        int b=sc1.nextInt();
        System.out.println("你输入的两个整数的和是："+(a+b));
    }
    
}
