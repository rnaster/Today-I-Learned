#include<iostream>
namespace BestComImp1
{
	using namespace std;
	void SimpleFunc(void)
	{
		cout<<"BestCom이 정의한 함수"<<endl;
	}
}
namespace ProgComImp1
{
	using namespace std;
	void SimpleFunc(void)
	{
		cout<<"ProgCom이 정의한 함수"<<endl;
	}
}
int main()
{
	BestComImp1::SimpleFunc();
	ProgComImp1::SimpleFunc();
	return 0;
}
