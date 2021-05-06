#include <iostream>
#include <string>
using namespace std;

class Glass
{
    int nakami;

    public :
    Glass():nakami(10){}
    Glass(int x) :nakami(x){}
    void Dasu(int);
};

void Glass::Dasu(int x)
{
    if(nakami >= x)
    {
        nakami -= x;
        cout << "Current left in glass is" << nakami << endl;
    }
    else 
    {
        cout << "Current left is " << nakami << " So can't put it outside" << endl;
    }
}

int main()
{
    int x;
    Glass glass2;
    cout << "how much ? " << endl;
    cin >> x;
    glass2.Dasu(x);
    cout << "FIN" << endl;

    cout << "Please type how much water is the glass  ?" << endl;
    cin >> x;
    Glass glass(x);
    cout << "How much water do you put outside per onetime ?" << endl;
    cin >> x;
    glass.Dasu(x);
    cout << "FIN" << endl;

}