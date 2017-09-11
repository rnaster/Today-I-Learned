#include<iostream>
using namespace std;
int main(void)
{
	int num, result;
	for(int i = 1; i <= 5; i++)
	{
		cout<<i<<"번째 정수 입력: ";
		cin>>num;
		result += num;
	}
	cout<<"합계: "<<result;
	return 0;
}
