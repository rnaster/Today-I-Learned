#include<iostream>
using namespace std;
int main(void)
{
	int num;
	while(num != -1)
	{
		cout<<"�Ǹ� �ݾ��� ���������� �Է�(-1 to end): ";
		cin>>num;
		if(num != -1)
		{
			cout<<"�̹� �� �޿�: "<<50 + num*0.12<<"����"<<endl; 	
		}
		else{cout<<"���α׷��� �����մϴ�.";}
	}
	return 0;
}
