#include<iostream>
namespace BestComImp1
{
	void SimpleFunc(void);
}
namespace ProgComImp1
{
	void SimpleFunc(void);
}
int main()
{
	BestComImp1::SimpleFunc();
	ProgComImp1::SimpleFunc();
	return 0;
}
void BestComImp1::SimpleFunc()
{
	std::cout<<"BestCom�� ������ �Լ�"<<std::endl;
}
void ProgComImp1::SimpleFunc()
{
	using namespace std;
	cout<<"ProgCom�� ������ �Լ�"<<endl;
}
