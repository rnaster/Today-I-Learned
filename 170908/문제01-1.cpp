#include<iostream>
using namespace std;
int main(void)
{
	int num, result;
	for(int i = 1; i <= 5; i++)
	{
		cout<<i<<"��° ���� �Է�: ";
		cin>>num;
		result += num;
	}
	cout<<"�հ�: "<<result;
	return 0;
}
