
#include <stdlib.h>
#include <stdio.h>
#include "assignment3.h"

TreeNodePtr createBSTnode(int);
TreeNodePtr insertNodeIntoBST(TreeNodePtr, const TreeNodePtr);
TreeNodePtr insertArrayintoBST(int, int*);
ListNodePtr convertBSTtoLinkedList(TreeNodePtr);
void deallocateBST(TreeNodePtr);

TreeNodePtr createBSTnode(int key){

    TreeNodePtr nNode = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    nNode->key = key;
    nNode->right = nNode->left = NULL;
    return nNode;

}

TreeNodePtr insertNodeIntoBST(TreeNodePtr root, const TreeNodePtr z){
    
    if(root == NULL){
        root = createBSTnode(z->key);
        return root;
    }
    else if(z->key < root->key)
        root->left = insertNodeIntoBST(root->left, z);  
    else 
        root->right = insertNodeIntoBST(root->right, z);
       
}
    
TreeNodePtr insertArrayIntoBST(int n, int *A){
    
    TreeNodePtr root = createBSTnode(*A);
    int count = 1;
    while(count<n){
        root = insertNodeIntoBST(root, createBSTnode(A[count]));
        count++;   
    }
    return root;
}
    
ListNodePtr convertBSTtoLinkedList(TreeNodePtr root){
    
    ListNodePtr l, m, r, first;
    l = r = NULL;
    m = (struct ListNode *)malloc(sizeof(struct ListNode));
    
    if(root->left != NULL)
        l = convertBSTtoLinkedList(root->left);
    if(root->right != NULL)
        r = convertBSTtoLinkedList(root->right);  
    
    m->key = root->key;
    m->next = r;
    if(root->left == NULL)
        return m;   
    
    first = l;
    while(first->next){
        first = first->next;
    }
    first->next = m;
    return l;
}
void deallocateBST(TreeNodePtr root){
        
    if(root != NULL){
        if(root->right != NULL){
            deallocateBST(root->right);
        }
        if(root->left != NULL){
            deallocateBST(root->left);
        }
    }
    free(root);
}
