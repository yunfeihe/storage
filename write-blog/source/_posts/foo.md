---
title: foo
date: 2018-09-13 08:46:21
tags:
---

# 链表的c语言实现
```c
#include<stdio.h>
#include <iostream> 
using namespace std;    
#include<iomanip>
#include<stdlib.h>
typedef int ElemType;
typedef struct LNode
{
	ElemType data;
	struct LNode *next;
}LNode,*LinkList;
void InitList(LinkList &L)
{
	L=(LNode*)malloc(sizeof(LNode));
	L->next=NULL;
}
void CreatList_L(LinkList &L,int n)
{   
	LinkList p;
	InitList(L);
	for(int i=n;i>0;--i)
	{
		p=(LNode*)malloc(sizeof(LNode));
		scanf("%d",&p->data);
	    p->next=L->next;
	    L->next=p;
	}
}
void TraverseList(LinkList m)	
{
	LinkList n;
	n=m->next;
    while(n!=NULL)
	{
		cout<<setw(2)<<n->data;
    	n=n->next;
	}
	    cout<<endl;
}
void Reserve(LinkList &L)
{       
	int i;
	LinkList p=L->next->next;
	LinkList q;
	LinkList t=L->next;
	while(p!=NULL)
	{
	q=p->next;
	p->next=L->next;
	L->next=p;
	p=q;
	}
	t->next=NULL;
	p=L->next;
    for(i=0;i<8;i++,p=p->next)
		cout<<setw(2)<<p->data;
	cout<<endl;
}
int main()
{
	LinkList L1;
	InitList(L1);
	cout<<"input 8 element:"<<endl;
	printf("elements:");
	CreatList_L(L1,8);
    printf("input elements:");
    TraverseList(L1);
	printf("reverse elements:");
    Reserve(L1);
    
    return 0;
}

```

# 删除指定值范围的节点
```c
#include <stdio.h>
#include <malloc.h>
#define NULL 0



typedef struct Node {
	int value;
	Node* next;
} Node;

Node* makeNode(int value) {
	Node* node = (Node*) malloc(sizeof(Node));
	node->value = value;
	node->next = NULL;
}

void toString(Node* head) {
	if(head->next == NULL) {
		printf("%d\n", head->value);
		return;
	}
	printf("%d -> ", head->value);
	toString(head->next);
}

int deleteBtween(Node* head, int min, int max) {
	Node* deletePoint = NULL;
	Node* beforeDeletePoint;
	Node* secondDeletePoint;
	if(head->value > min) {
		deletePoint = head;        // all nodes is greater than min then free all
	} else {
		beforeDeletePoint = head;
		while(beforeDeletePoint->next != NULL && beforeDeletePoint->next->value <= min) {  //find the pre-point of deletePoint
			beforeDeletePoint = beforeDeletePoint->next;
		}
		printf("beforeDeletePoint value: %d\n", beforeDeletePoint->value);
		if(beforeDeletePoint->next != NULL) {
			// "beforeDeletePoint->next != NULL" means nodes must have node needed to delete;
			deletePoint = beforeDeletePoint->next; 
			secondDeletePoint = deletePoint;
			while(secondDeletePoint->next != NULL && secondDeletePoint->next->value < max) {
				secondDeletePoint = secondDeletePoint->next;
			}
			printf("secondDeletePoint value: %d\n", secondDeletePoint->value);
			if(secondDeletePoint->next == NULL) {      //nodes after deletePoint is all smaller than max
				beforeDeletePoint->next = NULL;  //delete all nodes after deletePoint include deletePoint
			} else {
				beforeDeletePoint->next = secondDeletePoint->next;   //deleteNodes btween deletePoint and secondDeletePoint
				secondDeletePoint->next = NULL;
			}
		} 
	}
	while(deletePoint != NULL) {    //free space
		Node* temp = deletePoint->next;
		free(deletePoint);
		deletePoint = temp;
	}
	
}

int main() {
	Node* nodes[100];
	int i;
	int testLimit = 20;
	for(i = 0; i < testLimit; i++) {
		nodes[i] = makeNode(i);
	}
	for(i = 0; i < testLimit - 1; i++) {
		nodes[i]->next = nodes[i + 1];
	}
	toString(nodes[0]);
	deleteBtween(nodes[0], 10, 19);
	toString(nodes[0]);
	
}
```

# 就地逆序单链表
```c
#include <stdio.h>
#include <malloc.h>
#define NULL 0

typedef struct Node {
	int value;
	Node* next;
} Node;

Node* makeNode(int value) {
	Node* node = (Node*) malloc(sizeof(Node));
	node->value = value;
	node->next = NULL;
}

void toString(Node* head) {
	if(head->next == NULL) {
		printf("%d\n", head->value);
		return;
	}
	printf("%d -> ", head->value);
	toString(head->next);
}

Node* reverse(Node* head) {
	Node* na;
	Node* nb;
	na = head;
	nb = na->next;
	na->next = NULL; //make head node point at null
	
	while(nb != NULL) {
		Node* temp = nb->next;
//		printf("debug \n nb: %d\n", nb->value);
		nb->next = na;  //reverse na and nb
		na = nb;
		nb = temp;
	}
	return na;
}


int main() {
	Node* nodes[100];
	int i;
	int testLimit = 20;
	for(i = 0; i < testLimit; i++) {
		nodes[i] = makeNode(i);
	}
	for(i = 0; i < testLimit - 1; i++) {
		nodes[i]->next = nodes[i + 1];
	}
	toString(nodes[0]);
	Node* foo = reverse(nodes[0]);
	toString(foo);
	
}

```