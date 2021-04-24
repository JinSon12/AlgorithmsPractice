public class TextileFactory {
    /*
     * Design an algorithm that determines the best return on the X*Y piece of
     * cloth.
     *
     * X, Y represent the dimensions of the cloth. For the i-th dress, a[i]*b[i] is
     * the dimension of the cloth needed to make it, and p[i] is its selling price.
     *
     * @returns The maximum sumed selling price of the dresses.
     */
    public static int clothCutting(int X, int Y, int[] a, int[] b, int[] p) {
        int dp[][] = new int[X+1][Y+1];

        dp = includeBaseCase(a, b, p, dp);

        // the base case => return 1, if some value is smaller than the base case, return 0.
        int minA= returnMin(a);
        int minB = returnMin(b);

        // size 0 would return value 0
        dp[0][0] = 0;

        for (int i =1; i <= X;i++) {
            for (int j = 1; j <= Y; j++) {

                int max = dp[i][j];
                int vertMax = 0;
                int horizMax = 0;
                // if Y-j > 0 && X - i > 0
                // cutting vertically :
                for (int v = 0; v <= j; v++) {
                    //    max = Math.max(max, dp[i][j] + dp[i][j] + dp[i][j] + dp[i][j]);
                    vertMax = Math.max(vertMax, dp[i][v] + dp[i][j - v]);
                }

                for (int h = 0; h <= i; h++) {
                    horizMax = Math.max(horizMax, dp[i - h][j] + dp[h][j]);
                }


                // compare the maximum of
                // 1) the value of the cloth dimension i,j if there exists a value
                // 2) the value of the maximum profit when cut horizontally, and vertically from 1~i, 1~j
                //    we already know that i=0, j=0 would result in 0 profit. (total size is 0)
                dp[i][j] = Math.max(max, Math.max(vertMax, horizMax));

            }
        }

        return dp[X][Y];
    }

    public static int[][] includeBaseCase(int[] arr1, int[] arr2, int[] profit, int[][] dp) {
        for(int i = 0; i < profit.length; i++) {
            int indX = arr1[i];
            int indY = arr2[i];
            dp[indX][indY] = profit[i];
        }
        return dp;
    }

    public static int returnMin(int[] arr) {
        int minVal = arr[0];
        for(int i = 1; i < arr.length; i++) {
            if (minVal > arr[i]) {
                minVal = arr[i];
            }
        }
        return minVal;
    }

    public static void main(String[] args) {
        /*
         * Example 1
         */
        {
            int X = 5;
            int Y = 4;
            // Dress 1: 2x2 cloth needed, worth $100
            // Dress 2: 1x1 cloth needed, worth $1
            int[] a = { 2, 1 };
            int[] b = { 2, 1 };
            int[] p = { 100, 1 };
            // The optimal way is to make 4 of the first dress,
            // and use the rest of the cloth to make the second.
            System.out.println(clothCutting(X, Y, a, b, p));
        }

        /*
         * Example 2
         */
        {
            int X = 4;
            int Y = 4;
            // Dress 1: 4x4 cloth needed, worth $15
            // Dress 2: 3x3 cloth needed, worth $30
            // Dress 3: 1x4 cloth needed, worth $10
            int[] a = { 4, 3, 1 };
            int[] b = { 4, 3, 4 };
            int[] p = { 15, 30, 10 };
            // Make 3x3 and 1x4.
            System.out.println(clothCutting(X, Y, a, b, p));
        }
    }
}
