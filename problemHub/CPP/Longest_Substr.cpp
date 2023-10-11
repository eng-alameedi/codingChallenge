#include <iostream>
#include <string>

using namespace std;

class Solutin {
public:
    int lengthOfLongestSubstring(string s) {
        string text {};
        int max_length {};
        int j {};
        int i {};
        while(j < s.length()) {
            if(text.find(s.at(j)) == text.npos) {
                text.push_back(s.at(j));
                ++j;
                max_length = max(max_length, j-i);
            } else {
                text.erase(0,1);
                ++i;
            }
        }
        return(max_length);
    }
};

int main(int argc, char **argv)
{
    cout << "= = = Program Started = = =" << endl;
    cout << "===========================" << endl;
    
    //string s = " ";
    //string s = "";
    string s = "abcabcbb";
    //string s = "bbbb";
    //string s = "pwwkew";
    //string s = "vdvf";
    
    Solutin sol;
    int count = sol.lengthOfLongestSubstring(s);
    
    cout << "The Length of Substring is: " << count << endl;
    
    cout << "===========================" << endl;
    cout << "= = = Program Started = = =" << endl;
    return 0;
}
/*
#include <iostream>
#include <string>
#include <unordered_set>

int lengthOfLongestSubstring(std::string s) {
    int n = s.length();
    int maxLength = 0;
    int i = 0, j = 0; // Initialize two pointers for the sliding window
    std::unordered_set<char> charSet;

    while (j < n) {
        if (charSet.find(s[j]) == charSet.end()) {
            charSet.insert(s[j]);
            j++;
            maxLength = std::max(maxLength, j - i); // Update the maximum length
        } else {
            charSet.erase(s[i]);
            i++;
        }
    }

    return maxLength;
}

int main() {
    std::string s = "pwwkew";
    int length = lengthOfLongestSubstring(s);

    std::cout << "Length of Longest Substring: " << length << std::endl;

    return 0;
}
*/