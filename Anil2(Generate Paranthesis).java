class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        
        // start with open bracket and maintain count
        findAll("(",1,0,result,n);
        return result;
    }

    public void findAll(String current,int open,int close,List<String>result,int n){
        // Base case 
        // we can only add 1 open and 1 close or 2 open and 2 close
        // so 2*n
        if(current.length() == 2*n){
            result.add(current);
            return;
        }
        // check open is less than or equal to n
        if(open<n){
            findAll(current+"(",open+1,close,result,n);
        }

        if(close<open){
            findAll(current+")",open,close+1,result,n);
        }


    }
}
