#include <iostream>  
#include <vector>  
#include <algorithm>  
using namespace std;  

vector<int> curDom[81];
int state[81] = {0};

int a[9][9] = {  
  {0,2,0,0,0,0,0,0,0},  
  {0,0,0,6,0,0,0,0,3},  
  {0,7,4,0,8,0,0,0,0},  
  {0,0,0,0,0,3,0,0,2},  
  {0,8,0,0,4,0,0,1,0},  
  {6,0,0,5,0,0,0,0,0},  
  {0,0,0,0,1,0,7,8,0},  
  {5,0,0,0,0,9,0,0,0},  
  {0,0,0,0,0,0,0,4,0}  
};  

void print(){  
for(int i=0;i<9;i++){  
       for(int j=0;j<9;j++){  
           cout<<a[i][j]<<" ";  
       }  
       cout<<endl;  
   }  
   cout<<endl;  
}


bool judge(int x,int y){  
   for(int i=0;i<9;i++){  
       if(a[x][i]==a[x][y]&&i!=y)  
       return false;  
   }  
   for(int i=0;i<9;i++){  
       if(a[i][y]==a[x][y]&&i!=x)  
       return false;  
   }  
   for(int i=x/3*3;i<x/3*3+3;i++){  
       for(int j=y/3*3;j<y/3*3+3;j++){  
           if(a[i][j]==a[x][y]&&(i!=x||j!=y))  
           return false;  
       }
   }
   return true;  
}

bool backtrack(int m){
	int row = m/9;
	int col = m%9;
	if(m>=81)
		return true;
	if(a[row][col]==0){
		for(int i=1;i<=9;i++){
			a[row][col]=i;
			if(judge(row,col))
				if(backtrack(m+1))
					return true;
			a[row][col]=0;
		}
	}
	else
		return backtrack(m+1);
	return false;
}

void dom(int d, int i, int j){
	vector<int> tmp;
	for(int k=0;k<curDom[i*9+j].size();k++){
		tmp.push_back(curDom[i*9+j][k]);
	}
	curDom[i*9+j].clear();
	for(int k=0;k<tmp.size();k++){
		if(tmp[k]!=d){
			curDom[i*9+j].push_back(tmp[k]);
		}
	}
}
void changeDom(int m){
	int row = m/9;
	int col = m%9;
	for(int i=m+1;i<81;i++){
		if(a[i/9][i%9] == 0){
			a[i/9][i%9] = a[row][col];
			if(!judge(i/9,i%9))
				dom(a[row][col],i/9,i%9);
			a[i/9][i%9] = 0;
		}
	}
}
bool findValue(int v, vector<int> t){
	for(int i=0;i<t.size();i++){
		if(t[i] == v)
			return true;
	}
	return false;
}
int tmp;
void forwardchecking(int m){

	//print();
	int row = m/9;
	int col = m%9;
	if(m>=81)
		return;
	if(a[row][col]==0){
		if(!curDom[m].empty()){
		for(int i=1;i<=9;i++){
			if(findValue(i,curDom[m])){
				a[row][col]=i;
				dom(i,m/9,m%9);
				tmp=m;
				break;
			}
		}
		changeDom(m);
		forwardchecking(m+1);
		}
		else{
			a[tmp/9][tmp%9] = 0;
		}
	}
	else
		forwardchecking(m+1);
}

void init(){
	for(int i=0;i<9;i++){
		for(int j=0;j<9;j++){
			if(a[i][j]==0){
				for(int k=1;k<=9;k++)
					curDom[i*9+j].push_back(k);
			}
		}
	}
	for(int i=0;i<9;i++){
		for(int j=0;j<9;j++){
			if(a[i][j]==0){
				for(int k=1;k<=9;k++){
					a[i][j] = k;
					if(!judge(i,j))
						dom(k,i,j);
					a[i][j] = 0;
				}
			}
		}
	}
}
int main(){
	init();
	cout<<"Initial: "<<endl;
	print();
	cout<<endl;
	forwardchecking(0);
	//backtrack(0);
	cout<<"After: "<<endl;
	print();
	return 0;
}


 
