public class VariableDemo3 {
    public static void main(String[] args){
        //byte
        byte b1=10;
        System.out.println(b1);
        //short
        short s1=20;
        System.out.println(s1);
        //int
        int i1=30;
        System.out.println(i1);
        //long
        //如果要定义long类型的变量，必须在数字后面加上L或者l
        //建议是用大写
        long l1=99999999990L;
        System.out.println(l1);

        //float
        //如果要定义float类型的变量，必须在数字后面加上F或者f
        //建议是用大写
        float f1=3.14F;
        System.out.println(f1);
        //double
        double d1=3.14;
        System.out.println(d1);
        //char
        char c1='男';
        System.out.println(c1);
        //boolean
        //boolean类型的变量值只能是true或者false
        boolean flag=true;
        System.out.println(flag);
        /*整数和小数取值范围大小关系：
        double > float > long > int > short > byte
        */
    }
}
