#include <iostream>
#include "Calculator.h"
using namespace std;

void Calculator::Init()
{
	add = 0, min = 0, mul = 0, div = 0;
};

double Calculator::Add(double num1, double num2)
{
	add++;
	return num1 + num2;
};

double Calculator::Min(double num1, double num2)
{
	min++;
	return num1 - num2;
};

double Calculator::Mul(double num1, double num2)
{
	mul++;
	return num1 * num2;
};

double Calculator::Div(double num1, double num2)
{
	div++;
	if(num2 == 0)
		{
			cout<<"0으로 나눌 수 없음!"<<endl;
			return 0;
		}
	else
		return num1 / num2;
};

void Calculator::ShowOpCount()
{
	cout<<"Addition: "<<add;
	cout<<"  Minus: "<<min;
	cout<<"  Multiplication: "<<mul;
	cout<<"  Division: "<<div<<endl;
};