class Solution {
public:
    string reverseWords(string &s){
        stringstream ss(s);
        string curr_word, answer;
        while(ss >> curr_word){
            answer = curr_word + " " + answer;
        }
        return answer.substr(0, size(answer)-1);  
    }
};
