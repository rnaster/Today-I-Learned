#include<iostream>
using namespace std;
int main(void)
{
	int num;
	while(num != -1)
	{
		cout<<"판매 금액을 만원단위로 입력(-1 to end): ";
		cin>>num;
		if(num != -1)
		{
			cout<<"이번 달 급여: "<<50 + num*0.12<<"만원"<<endl; 	
		}
		else{cout<<"프로그램을 종료합니다.";}
	}
	return 0;
}
