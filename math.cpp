#include <iostream>
#include <windows.h>
#include <string>

using namespace std;

class Math{
	public: void conversor_decimal_para_binario(int decimal){
		string resultado = "";
		int binario = 2;

		while(decimal > binario){
			resultado = to_string(decimal % binario) + resultado;
            decimal = decimal / binario;
		}


        resultado = to_string(decimal % binario) + resultado;
        resultado = to_string(decimal / binario) + resultado;

		cout << resultado;
	}
};


int main(){
	Math *math = new Math();
    math->conversor_decimal_para_binario(2);
	system("PAUSE > nul");
	return 0;
}
