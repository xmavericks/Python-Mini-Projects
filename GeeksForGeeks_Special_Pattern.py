# We are about to print pattern like this below:

G  
G e  
G e e  
G e e k  
G e e k s  
G e e k s F  
G e e k s F o  
G e e k s F o r  
G e e k s F o r G  
G e e k s F o r G e  
G e e k s F o r G e e  
G e e k s F o r G e e k  
G e e k s F o r G e e k s

# For this problem you need to think the logic on your on, and I must say that you can not find solution to this pattern anywhere on any website including GeeksForGeeks as well.

I will update the solution for this problem tomorrow.

---------------------Program: C++ ----------------------------------
#include <iostream>
using namespace std;

int main() {
    string name;
    cout << "Type your name: ";
    cin >> name;
    cout << "Your name is: " << name;

    for(int i = 0; i < name.length()+1; i++){
        for(int j = 1; j < i+1; j++){
            cout<< name[j-1]<< " ";
        }
        cout << "" << endl;
    }
    return 0;
}

-----------------------Output : C++ -------------------------------
Type your name: GEEKSFORGEEKS
Your name is: GEEKSFORGEEKS
G 
G E 
G E E 
G E E K 
G E E K S 
G E E K S F 
G E E K S F O 
G E E K S F O R 
G E E K S F O R G 
G E E K S F O R G E 
G E E K S F O R G E E 
G E E K S F O R G E E K 
G E E K S F O R G E E K S
