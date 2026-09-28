public class VariableTest {
    //the main entrance of the program
    public static void main(String[]args){
        //1 车站问题
        //一开始没有乘客
        int count =0;
        //第一站，上去一个乘客
        count=count+1;
        //第二站，上去两个乘客，下来一位乘客
        count=count+2-1;
        //第三站，上去两位乘客，下来一位乘客
        count=count+2-1;
        //第四站，下来一位乘客
        count=count-1;
        //第五站，上去一位乘客
        count=count+1;
        //最终人数
        System.out.println(count);
        

        //输出老师信息
        String name="黑马谢广坤";
        int age=18;
        char sex='男';
       double height=180.1;
       boolean married=false;
       
        System.out.println("姓名："+name);
        System.out.println("年龄："+age);
        System.out.println("性别："+sex);
        System.out.println("身高："+height);
        System.out.println("是否结婚："+married);

        //3输出电影信息
        String names ="送初恋回家";
        String people="刘鑫 张玉提 高媛";
        int time=2020;
        double scores=9.0;
        System.out.println("电影名称："+names);
        System.out.println("演员："+people);
        System.out.println("上映年份："+time);
        System.out.println("评分："+scores);

        //4输出商品信息
        String brand="华为";
        double prices=5299.00;
        System.out.println("手机品牌："+brand);
        System.out.println("手机价格："+prices);
    }
}
