#include <stdio.h>
#include <stdlib.h>

void fill_random(int, int, int, double [], double []);
void matrix_times_matrix(int, int, int, double [], double [], double []);
void check_result(int, int, int, double [], double [], double []);
double dotproduct(int, double [], double []);
void matrix_times_vector(int, int, double [], double [], double []);

int main(){

  int i;

  while(1){

    double A[i*i], B[i*i], C[i*i];
    
    fill_random(i, i, i, A, B);
    matrix_times_matrix(i, i, i, A,  B, C);
    check_result(i, i, i, A, B, C);

    i++;
    if(i>400)
      printf("i = %d \n",i);

  }
return 0;
}
