#include <iostream>
using namespace std;
int val = 100;
int SimpleFunc()
{
	int val = 20;
	val += 3;
	cout<<val<<" : ��������"<<endl;
	::val += 99;
	cout<<::val<<" : ��������"<<endl; 
}
int main()
{
	SimpleFunc();
	return 0;
}
