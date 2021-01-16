/*
* This is the first program I wrote all by myself
* when I was in 11th grade around July 2017.
*/

#include <stdio.h>
#include <math.h>
int main(void)
{
	int y,w;
	float a,pm,pm2,v,v0,t,s,x;
	a=9.8;
	do{
	do{
		printf("----------\n0 - end\n1 - v,v0\n2 - v,t\n3 - v,s\n4 - v0,t\n5 - v0,s\n6 - t,s\n\n");
		scanf("%d",&y);
		if(y>6)
			printf("\nnothing\n");
	}while(y>6);
	if(y!=0)
		do{
			printf("\n<down:1 up:-1>\n");
			scanf("%f",&pm);
			if((pm!=1)&&(pm!=-1))
				printf("nothing\n");
		}while((pm!=1)&&(pm!=-1));
		pm2=pm*-1;
	switch(y){
		case 1:
			printf("<v>\n");
			scanf("%f",&v);
			printf("<v0>\n");
			scanf("%f",&v0);
			t=(v*pm+v0*pm2)/a;
			s=v0*t+pm*a*t*t/2;
			printf("\nt=%.2f\ns=%.2f\n",t,s);
			break;
		case 2:
			printf("<v>\n");
			scanf("%f",&v);
			printf("<t>\n");
			scanf("%f",&t);
			v0=v+pm2*a*t;
			s=v0*t+pm*a*t*t/2;
			printf("\nv0=%.2f\ns=%.2f\n",v0,s);
			break;
		case 3:
			printf("<v>\n");
			scanf("%f",&v);
			printf("<s>\n");
			scanf("%f",&s);
			x=pm2*2*a*s+v*v;
			t=(pm*v+pm2*sqrtf(x))/a;
			printf("\nv0=%.2f\nt=%.2f\n",sqrtf(x),t);
			break;
		case 4:
			printf("<v0>\n");
			scanf("%f",&v0);
			printf("<t>\n");
			scanf("%f",&t);
			v=v0+pm*a*t;
			s=v0*t+pm*a*t*t/2;
			printf("\nv=%.2f\ns=%.2f\n",v,s);
			break;
		case 5:
			printf("<v0>\n");
			scanf("%f",&v0);
			printf("<s>\n");
			scanf("%f",&s);
			x=v0*v0+pm*2*a*s;
			t=(pm*pm*sqrtf(x)+pm2*v0)/a;
			printf("\nv=%.2f\nt=%.2f\n",pm*sqrtf(x),t);
			break;
		case 6:
			printf("<t>\n");
			scanf("%f",&t);
			printf("<s>\n");
			scanf("%f",&s);
			v0=pm2*a*t/2+s/t;
			v=v0+pm*a*t;
			printf("\nv=%.2f\nv0=%.2f\n",v,v0);
			break;
	}
	if(y!=0)
		printf("\nok?\n");
		scanf("%d",&w);
	}while(y!=0);
	printf("\n//end//\n");
	return 0;
}
