/*
* This was written when I was in 11th grade around July 2017.
*/

#include<stdio.h>
int main(void)
{
	int p,bp,np,vp,t,s,e,ns,ne;
	int sh,sm,eh,em,end;
	/*bp*/
	puts("<基本時給は？>");
	scanf("%d",&bp);
	bp/=60;
	/*np*/
	puts("\n<夜間手当は？>");
	scanf("%d",&np);
	np=np/60+bp;
	/*ns,ne*/
	if(np-bp!=0){
		puts("\n<何時から何時まで？(00:00-00:00)>");
		scanf("%d:%d-%d:%d",&sh,&sm,&eh,&em);
		ns=sh*60+sm;
		if(sh>eh)
			ne=(24+eh)*60+em;
		else
			ne=eh*60+em;
	}
	/*vp*/
	puts("\n<休日手当はいくら？>");
	scanf("%d",&vp);
	vp/=60;
	do{
		/*s,e*/
		puts("\n-------------------------\n<勤務時間は？(00:00-00:00)>");
		scanf("%d:%d-%d:%d",&sh,&sm,&eh,&em);
		s=sh*60+sm;
		if(sh>eh)
			e=(24+eh)*60+em;
		else
			e=eh*60+em;
		/*t,p*/
		t=e-s;
		if(e<ns||ne<s)
			p=t*bp;
		else if(s<ns&&ns<e)
			p=(ns-s)*bp+(e-ns)*np;
		else if(ns<s&&s<e&&e<ne)
			p=t*np;
		else if(s<ne&&ne<e)
			p=(e-ne)*bp+(ne-s)*np;
		else if(s<ns&&ne<e)
			p=((ns-s)+(e-ne))*bp+(ne-ns)*np;
		else{
			puts("\nfuck");
			goto end;
		}
		/*result*/
		printf("\n勤務時間 = %d時間 %d分\n",t/60,t%60);
			printf("平日給料 = %d円\n",p);
			printf("休日給料 = %d円\n",p+t*vp);
		/*end*/
		puts("\n<続ける？(はい:1 いいえ:他の数字)>");
		scanf("%d",&end);
	}while(end==1);
	end:
	puts("\n//終わり//");
	return 0;
}
