#include<iostream>

namespace BestComImp1
{
	void SimpleFunc();
	void PrettyFunc();
}
namespace ProgComImp1
{
	void SimpleFunc();
}
int main()
{
	BestComImp1::SimpleFunc();
	return 0;
}
void BestComImp1::SimpleFunc()
{
	using namespace std;
	cout<<"BestCom이 정의한 함수"<<endl;
	PrettyFunc();
	ProgComImp1::SimpleFunc();
}
void BestComImp1::PrettyFunc()
{
	using namespace std;
	cout<<"So Prettry!!"<<endl;
}
void ProgComImp1::SimpleFunc()
{
	using namespace std;
	cout<<"ProgCom이 정의한 함수"<<endl;
}
