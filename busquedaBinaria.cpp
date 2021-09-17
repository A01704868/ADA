#include <iostream>

using namespace std;

//busqueda binaria
int busquedaBin(int lista[], int n, int clave){
    int central, bajo, alto, valorCentral;
    bajo = 0;
    alto = n-1;

    while(bajo<=alto){
        central = (bajo+alto)/2;//indice de elemento central
        valorCentral = lista[central];//valor del indice central
        if(clave == valorCentral){
            return central;//encontrado, regresa valor
        }else if(clave<valorCentral){
            alto = central--;//ir a sublista inferior
        }else{
            bajo = central++;//ir a sublista superior
        }

    }//while
    return -1;//no se encontro el valor
}//funcion

int main() {
	int arreglo[] = {17, 24, 29, 36, 53, 58, 59, 62, 97};
	int n = sizeof(arreglo);
	int central = busquedaBin(arreglo, n, 59);

	if(central != -1){
            cout<<"El indice de n es: "<<central;
	}else{
	    cout<<"El numero no se encuentra en el arreglo";
	}
	return 0;
}
