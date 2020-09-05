public class Solution {
    public ArrayList<Integer> rotateArray(ArrayList<Integer> A, int B) {
        ArrayList<Integer> ret = new ArrayList<Integer>();
        int size = A.size();
        int index = B % A.size(); 
        for (int i = 0; i < size; i++) {
            if (i == size-1) {
                size = B % A.size(); 
                i = 0; 
                index = 0; 
            }
            ret.add(A.get(i));
            index++; 
        }
        return ret;
    }
}
