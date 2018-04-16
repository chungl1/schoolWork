#include <stdio.h>
#include <stdlib.h>

double dotproduct(int n, double x[], double y[]){

  double result=0, result1;
  int i = 0;

  while(i<n){
    result1 = x[i] * y[i];
    result += result1;
    i++;
    }
  return result;

}
