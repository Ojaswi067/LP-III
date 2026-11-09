#include<iostream>
using namespace std;

void non_rec(int n){
    int a,b,c;
    a=0;
    b=1;
    for(int i=0;i<n;i++){
    cout<<a<<" ";
    c=a+b;
    a=b;
    b=c;
    }
}
int rec(int n){
    if(n<=1)
        return n;
    return rec(n-2)+rec(n-1);
}

int main()
{
    int n;
    cout<<"enter the no.s upto which fibonaaci series to display: ";
    cin>>n;

    cout<<"Non recursive fib:";
    non_rec(n);

    cout<<"\nRecursive fib:";
    for (int i=0;i<n;i++){
        cout<<rec(i)<<" ";
    }
    return 0;
}