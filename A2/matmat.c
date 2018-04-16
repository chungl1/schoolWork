#include <stdio.h>
#include <stdlib.h>

void matrix_times_vector(int, int, double [], double [], double []);

void matrix_times_matrix(int m, int n, int p, double A[], double B[], double C[]){

  int i=0, j=0, k=0, h=0;
  double D[n], E[m];
  
  while(i<p){
    while(j<n){
      while(k<n*p){
        D[j] = B[k];
	k = k+p;
	j++;
      }
      matrix_times_vector(m, n, A, D, E);
      while(h<m*p){
        C[h] = E[i];
	i++;
	h = h+p;
      }
    }
  }
}
