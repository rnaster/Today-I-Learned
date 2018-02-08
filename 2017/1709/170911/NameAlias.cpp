#include<iostream>
using namespace std;
namespace AAA
{
	namespace BBB
	{
		namespace CCC
		{
			int num1;
			int num2;
		}
	}
}
int main()
{
	AAA::BBB::CCC::num1 = 20;
	AAA::BBB::CCC::num2 = 30;
	
	namespace ABC=AAA::BBB::CCC;
	using namespace ABC;
	cout<<num1<<endl;
	cout<<num2<<endl;
	return 0;
}
