#include<iostream>
using namespace std;

int SimpleFunc(int a)
{
	return a + 1;
}
int SimpleFunc(void)
{
	return 10;
}
int main()
{
	cout<<SimpleFunc(3)<<endl;
	cout<<SimpleFunc()<<endl;
	return 0;
}
