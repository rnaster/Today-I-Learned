#include<iostream>
namespace Hybrid
{
	using namespace std;
	void HybFunc()
	{
		cout<<"So simple function!"<<endl;
		cout<<"In namespace Hybrid!"<<endl;
	}
}
int main()
{
	using Hybrid::HybFunc;
	HybFunc();
	return 0;
}
