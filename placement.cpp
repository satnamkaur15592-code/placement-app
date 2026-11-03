#include <iostream>
using namespace std;

int main() {
    float cgpa;
    int iq;
    
    cout << "Enter CGPA: ";
    cin >> cgpa;
    
    cout << "Enter IQ: ";
    cin >> iq;
    
    if(cgpa >= 7.5 && iq >= 100) {
        cout << "Placement Ho Jayega! Congrats!";
    } else {
        cout << "Thoda Aur Mehnat Karni Padegi!";
    }
    return 0;
}
