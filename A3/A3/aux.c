#include "assignment3.h"
#include <stdlib.h>
#include <stdio.h>
void generateRandomIntArray(int, int*, int);
void printArray(int, int*);
void printBSTinorder(TreeNodePtr);
void printList(ListNodePtr);

void generateRandomIntArray(int N, int *A, int NMAX){
    
    int count = 0;
    while(count<N){
        A[count] = rand() % (NMAX);
        count++;
    }
}

void printArray(int n, int *A){
    int i;
    for(i=0;i<n;i++){
        printf("%d ", A[i]);
    }
}

void printBSTinorder(TreeNodePtr root){

    if(root == NULL)
        return;
    printBSTinorder(root->left);
    printf("%d ", root->key);
    printBSTinorder(root->right);
       
    
}

void printList(ListNodePtr head){
    
    if(head == NULL)
        return;
    printf("%d ", head->key); 
    printList(head->next);
    
}

