#include<iostream>
namespace BestComImp1
{
	using namespace std;
	void SimpleFunc(void)
	{
		cout<<"BestCom�� ������ �Լ�"<<endl;
	}
}
namespace ProgComImp1
{
	using namespace std;
	void SimpleFunc(void)
	{
		cout<<"ProgCom�� ������ �Լ�"<<endl;
	}
}
int main()
{
	BestComImp1::SimpleFunc();
	ProgComImp1::SimpleFunc();
	return 0;
}
