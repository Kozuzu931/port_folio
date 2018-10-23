public class Practice2_3 {
    public static void main(String[] args) {
        System.out.println("ようこそ占いの館へ");
        System.out.print("あなたの名前を入力してください。: ");
        String name = new java.util.Scanner (System.in).nextLine();

        System.out.print("あなたの年齢を入力してください。: ");
        String ageString = new java.util.Scanner (System.in).nextLine();
        int age = Integer.parseInt(ageString);

        int fortune = new java.util.Random().nextInt(4);
        fortune += 1;

        System.out.println("占いの結果が出ました！");
        String result = age + "歳の" + name + "さん、あなたの運勢は";
        switch (fortune) {
            case 1:
                System.out.println(result + "大吉です");
                break;
            
            case 2:
                System.out.println(result + "中吉です");
                break;

            case 3:
                System.out.println(result + "吉です");
                break;

            case 4:
                System.out.println(result + "凶です");
                break;
            
            default:
                System.out.println(result + "私どもの力では占うことができませんでした……。");
                break;
        }


            

                
        

    }
}