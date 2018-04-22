#include <stdio.h>
#include <stdlib.h>

void fill_random(int, int, int, double [], double []);
void matrix_times_matrix(int, int, int, double [], double [], double []);
void check_result(int, int, int, double [], double [], double []);
double dotproduct(int, double [], double []);
void matrix_times_vector(int, int, double [], double [], double []);

int main(){

  int m, n, p;
  
  //Enter m, n, p
  printf("Enter m, n, p: ");
  scanf("%d%d%d",& m, &n, &p);

  double A[m*n], B[n*p], C[m*p];
  // fill A and B with random numbers
  fill_random(m, n, p, A, B);
  
  // Computer C = A*B
  matrix_times_matrix(m, n, p, A, B, C);

  // Check the result
  check_result(m, n, p, A, B, C);

  return 0;

}
