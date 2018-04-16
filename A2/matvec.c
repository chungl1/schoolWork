#include <stdio.h>
#include <stdlib.h>

double dotproduct(int, double [], double []);

void matrix_times_vector(int m, int n , double A[], double x[], double y[]){

  int i = 0, j = 0, k = 0;
  double B[n];

  while(i<m*n){
    while(k<m){
      while(j<n){
        B[j] = A[i];
	i++;
	j++;
      }
      y[k] = dotproduct(n, B, x);
      k++;
      j = 0;
    }
  }
}
