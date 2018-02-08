#include <iostream>
using namespace std;

void Add(int &ref)
{
	ref += 1;
}

void Signed(int &ref)
{
	ref *= -1;
}

int main()
{
	int val = 10;
	Add(val);
	cout <<"After Add: "<<val<<endl;
	Signed(val);
	cout <<"After Signed: "<<val<<endl;
	return 0;
}
