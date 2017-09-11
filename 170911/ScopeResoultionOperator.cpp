#include <iostream>
using namespace std;
int val = 100;
int SimpleFunc()
{
	int val = 20;
	val += 3;
	cout<<val<<" : 지역변수"<<endl;
	::val += 99;
	cout<<::val<<" : 전역변수"<<endl; 
}
int main()
{
	SimpleFunc();
	return 0;
}
