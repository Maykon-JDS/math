#include <iostream>
#include <windows.h>
#include <string>

using namespace std;

class Math{

    public: int base, valor ;

	public: void conversor_decimal_para_binario(){
		int decimal = valor;
		int divisor = base;
		string resultado = "";

		while(decimal > divisor){
			resultado = to_string(decimal % divisor) + resultado;
            decimal = decimal / divisor;
		}


        resultado = to_string(decimal % divisor) + resultado;
        resultado = to_string(decimal / divisor) + resultado;

        int limite = resultado.length();

        if(limite < 4){
            for(int i = 0; i < 4 - limite ; i++){
                resultado = to_string(0) + resultado;
            }
        }

        cout << resultado;

	}
};


int main(){
	Math *math = new Math();
	cout << "Digite qual sera a base: ";
	cin >> math->base;
    cout << "Digite qual sera o numero na base decimal: ";
    cin >> math->valor;
    math->conversor_decimal_para_binario();
	system("PAUSE > nul");
	return 0;
}
