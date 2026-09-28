public class VariableDemol {
    //主入口
    public static void main(String[] args){
        //变量的定义(变量名不能重复)
        //数据类型 变量名 = 变量值;(before using the variable,we must define it first.)
        //整数
        int age = 18;
        System.out.println(age);
//小数
        double num = 3.15;
        System.out.println(num);
        //evovle to calculate
        int b=20;
        int c=10;
        System.out.println(b+c);
        //revise the value of variable
        b=23;
        System.out.println(b);

        //notice:in the sentence ,you can define one or more variables.
        int x=10,y=20,z=30;
        System.out.println(x);
        System.out.println(y);
        System.out.println(z);
        //以后再定义变量时，请直接赋值，不要把赋值分开来写
        System.out.println(12*4);
        //整数参与计算 结果只能得到整数
        System.out.println(12/4);
        //小数参与计算 结果可能是不精确的
        System.out.println(12.0/4);
        //取余数
        System.out.println(12%4);
        //代码中若有小数参与计算 则结果有可能不准确
        System.out.println(1.01+1.1);
        System.out.println(12.0+23.3);

        int a=10;//++,--单独写一行结果都是一样的
        a++;
        System.out.println(a);
        ++a;
        System.out.println(a);
        a--;
        System.out.println(a);
        --a;
        System.out.println(a);

        //后++ 先用后加  先++ 先加后用
        //+= 这些底层上都隐含着一个强制类型转换
        /*int a=10;
        a+=b;
        本质上就是a=(int)(a+b);*/

        //^  异或运算 相同为false,不同为true
//!  取反运算 逻辑非  取反的感叹号不要写多次 要么不写  要么只写一个  !a

/*1.&&   逻辑与运算  都为true 为true
   有一个为false 为false
   2.|| 逻辑或运算  有一个为true 为true
   都为false 为false
   3.注意:短路逻辑运算符具有短路效果
   即 当左边的表达式能确定最终结果时，那么右边就不会参与运算了
*/

/*三元运算符 条件1?表达式1:表达式2
   1.如果条件1为true 则表达式1执行
   2.如果条件1为false 则表达式2执行
*/



//三元运算符练习
 int h1=150;
 int h2=210;
 int h3=165;
 int maxHeight=(h1>h2?h1:h2)>h3?(h1>h2?h1:h2):h3;
 System.out.println(maxHeight);
//  int one =h1>h2?h1:h2;
//  int max=one>h3?one:h3;
//  System.out.println(max);
//小括号优先于所有
    }
}

