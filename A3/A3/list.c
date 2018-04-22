#include "assignment3.h"
#include <stdlib.h>
#include <stdio.h>

ListNodePtr reverselist(ListNodePtr);
void deallocateList(ListNodePtr);

ListNodePtr reverselist(ListNodePtr head){
    
    ListNodePtr current;
    if(head == NULL)
        return NULL;
    if(head->next == NULL)
        return head;
    current = reverselist(head->next);
    head->next->next = head;
    head->next = NULL;
    return current;
    
}

void deallocateList(ListNodePtr head){

    if(head != NULL)
        deallocateList(head->next);
    free(head);
}
