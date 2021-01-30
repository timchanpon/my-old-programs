/*
 * This was written when I was in 11th grade around October 2017.
 */

#include<stdio.h>
int main(void)
{
	float Am,Bm,Cm,m;
	float Axy,Bxy,Cxy;
	float N,n,a;
	float A,B,C;
	float g=9.8,skip,end;
	do{
		//A
		puts("***************\n<m of A>");
		scanf("%f",&Am);
		puts("<x or y(x:1 y:2)>");
		scanf("%f",&Axy);
		if(Axy==1){
			puts("<n>");
			scanf("%f",&n);
			A=Am*n*g;
		}
		else
			A=Am*g;
		//B
		puts("\n<m of B>");
		scanf("%f",&Bm);
		puts("<x or y(x:1 y:2)>");
		scanf("%f",&Bxy);
		if(Bxy==1&&n==0){
			puts("<n>");
			scanf("%f",&n);
			B=Bm*n*g;
		}
		else if(Bxy==1)
			B=Bm*n*g;
		else
			B=Bm*g;
		//C
		puts("\n<m of C>");
		scanf("%f",&Cm);
		if(Cm==0)
			goto skip;
		puts("<x or y(x:1 y:2)>");
		scanf("%f",&Cxy);
		if(Cxy==1&&n==0){
			puts("<n>");
			scanf("%f",&n);
			C=Cm*n*g;
		}
		else if(Cxy==1)
			C=Cm*n*g;
		else
			C=Cm*g;
		//N
		skip:
		puts("\n<N>");
		scanf("%f",&N);
		//a
		if(Cm==0){
			if(N==0){
				m=Am+Bm;
				a=(B-A)/m;
				printf("\n---------------\na=%.2f\n",a);
			}
			else if(N!=0){
				m=Am+Bm;
				a=(N-B-A)/m;
				printf("\n---------------\na=%.2f\n",a);
			}
		}
		else if(N!=0){
			m=Am+Bm+Cm;
			a=(N-C-B-A)/m;
			printf("\n---------------\na=%.2f\n",a);
		}
		else{
			m=Am+Bm+Cm;
			a=(C-B-A)/m;
			printf("\n---------------\na=%.2f\n",a);
		}
	puts("\n<Do you wanna continue(Yes:1 No:0)>");
	scanf("%f",&end);
	puts("");
	}while(end==1);
	puts("//end//");
	return 0;
}
