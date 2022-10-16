//Write a program in C to insert a new node at the beginning of a Singly Linked List.
#include<stdio.h>

#include<stdlib.h>
struct node{
    int num;
    struct node *nextptr;

    
}*stnode;

void createNodeList(int n);
void NodeInsertatBegin(int num);
void displayList();

int main()
{
    int n,num;
    printf("Input the nnumber of nodes : ");
    scanf("%d", &n);
    createNodeList(n);
    printf("\n Data entered in the list are : \n");
    displayList();
    printf("\n Input data to insert at the begining of the list : \n");
    scanf("%d",&num);
    NodeInsertatBegin(num);
    printf("\n Data after inserted in the list are : \n");
    displayList();
    return 0;


}
void createNodeList(int n)
{
    struct node *fnNode, *tmp;
    int num,i;
    stnode = (struct node *)malloc(sizeof(struct node));
    if(stnode == NULL) 
    {
        printf("Memory can not be allocated. ");

    }
    else{
        printf("Input data for node 1 : ");
        scanf("%d",&num);
        stnode->num = num;
        stnode->nextptr = NULL;
        tmp = stnode;

        for(i=2;i<=n;i++)
        {
            fnNode = (struct node *)malloc(sizeof(struct node));
            if(fnNode == NULL)
            {
                printf("Memory can not be allocated. ");
                break;

            }
            else{
                printf("Input data for node %d :",i);
                scanf(" %d",&num);
                fnNode->num = num;
                fnNode->nextptr = NULL;
                tmp->nextptr = fnNode;
                tmp = tmp->nextptr;
            }
        }
    }
}
void NodeInsertatBegin(int num)
{
    struct node *fnNode;
    fnNode = (struct node*)malloc(sizeof(struct node));
    if(fnNode == NULL)
    {
        printf("Memory can not be allocated.");
    }
    else
    {
        fnNode->num = num;
        fnNode->nextptr = stnode;
        stnode = fnNode;
    }
}
void displayList()
{
    struct node *tmp;
    if(stnode == NULL)
    {
        printf(" No data found in the list.");

    }
    else{
        tmp = stnode;
        while(tmp!=NULL)
        {
            printf("Data = %d\n",tmp->num);
            tmp = tmp->nextptr;
        }
    }
}