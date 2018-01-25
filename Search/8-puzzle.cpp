#include <iostream>
#include <queue>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
using namespace std;
struct node{
 int m[3][3];
 int f;
 int g;
 bool operator < (const node &s)const{
  return f > s.f;
 }
 string s;
};
int ini[3][3] = {
 7, 2, 4,
 5, 0, 6,
 8, 3, 1
};
int goal[3][3] = {
 0, 1, 2,
 3, 4, 5,
 6, 7, 8
};
int distance(int m1[3][3], int m2[3][3], int n){
 int x1=0,x2=0;
 int y1=0,y2=0;
 for(int i=0;i<3;i++){
  for(int j=0;j<3;j++){
   if(m1[i][j]==n){
    x1 = i;
    y1 = j;
    break;
   }
  }
 }
 for(int i=0;i<3;i++){
  for(int j=0;j<3;j++){
   if(m2[i][j]==n){
    x2 = i;
    y2 = j;
    break;
   }
  }
 }
 return abs(x1-x2)+abs(y1-y2);
}
pair<int, int> findzero(int m[3][3]){
 int x,y;
 for(int i=0;i<3;i++){
  for(int j=0;j<3;j++){
   if(m[i][j]==0){
    x = i;
    y = j;
    break;
   }
  }
 }
 return make_pair(x, y);
}
bool mequal(int m1[3][3], int m2[3][3]){
 int num = 0;
 for(int i=0;i<3;i++){
  for(int j=0;j<3;j++){
   if(m1[i][j] == m2[i][j]){
    num++;
   }
  }
 }
 if(num==9)return true;
 else return false;
}
string makestring(int m[3][3]){
 string str;
 for(int i=0;i<3;i++){
  for(int j=0;j<3;j++){
   string temp;
   stringstream out1;
   out1 << m[i][j];
   temp = out1.str();
   str += temp;
  }
 }
 return str;
}
void outputStr(string s){
	for(int i=0;i<s.length();i+=9){
		int x=0;
		for(int j=0;j<3;j++){
			for(int k=0;k<3;k++){
				cout<<s[i+x]<<" ";
				x++;
			}
			cout<<endl;
		}
		cout<<endl;
	}
}
int main(){
 node start;
 for(int i=0;i<3;i++){
  for(int j=0;j<3;j++){
   start.m[i][j] = ini[i][j];
  }
 }
 start.f = 0; 
 start.g = 0;
 start.s = makestring(start.m);
 vector<node> visit;
 priority_queue<node> q;
 q.push(start);
 node jug;
 while(!q.empty()){
  jug = q.top();
  q.pop();
  visit.push_back(jug);	
  if(mequal(jug.m, goal)){
  	cout<<"Steps: ";
  	cout<<visit.size()<<endl;
  	cout<<endl;
   outputStr(jug.s);
   break;
  }
   //go left
  	if(findzero(jug.m).second!=0){
  	node cur = jug;
   	int i = findzero(jug.m).first;
   	int j = findzero(jug.m).second;
   	cur.m[i][j] = jug.m[i][j-1];
    cur.m[i][j-1] = 0;
   	cur.s = jug.s + makestring(cur.m);
   	int cost = 0;
   for(int i=0;i<3;i++){
    	for(int j=0;j<3;j++){
     		if(cur.m[i][j]!=0){
      			cost += distance(cur.m, goal, cur.m[i][j]);
     		}
    	}
   	}
   	cur.g = jug.g + 1;
   	cur.f = cost + cur.g;
   	int num = 0;
   	for(int i=0;i<visit.size();i++){
   		if(mequal(visit[i].m, cur.m))
   			num++;
	}
	if(num==0)
		q.push(cur);
  }
  //go right
  if(findzero(jug.m).second!=2){
  	node cur = jug;
   int i = findzero(jug.m).first;
   int j = findzero(jug.m).second;
   cur.m[i][j] = jug.m[i][j+1];
   cur.m[i][j+1] = 0;
   cur.s = jug.s + makestring(cur.m);
   int cost = 0;
   for(int i=0;i<3;i++){
    	for(int j=0;j<3;j++){
     		if(cur.m[i][j]!=0){
      			cost += distance(cur.m, goal, cur.m[i][j]);
     		}
    	}
   	}
   	cur.g = jug.g + 1;
   	cur.f = cost + cur.g;
   int num = 0;
   	for(int i=0;i<visit.size();i++){
   		if(mequal(visit[i].m, cur.m))
   			num++;
	}
	if(num==0)
		q.push(cur);
  }
  //go up
  if(findzero(jug.m).first!=0){
  	node cur = jug;
   int i = findzero(jug.m).first;
   int j = findzero(jug.m).second;
   cur.m[i][j] = jug.m[i-1][j];
   cur.m[i-1][j] = 0;
   cur.s = jug.s + makestring(cur.m);
   int cost = 0;
   for(int i=0;i<3;i++){
    	for(int j=0;j<3;j++){
     		if(cur.m[i][j]!=0){
      			cost += distance(cur.m, goal, cur.m[i][j]);
     		}
    	}
   	}
   	cur.g = jug.g + 1;
   	cur.f = cost + cur.g;
   int num = 0;
   	for(int i=0;i<visit.size();i++){
   		if(mequal(visit[i].m, cur.m))
   			num++;
	}
	if(num==0)
		q.push(cur);
  }
  //go down
  if(findzero(jug.m).first!=2){
  	node cur = jug;
   int i = findzero(jug.m).first;
   int j = findzero(jug.m).second;
   cur.m[i][j] = jug.m[i+1][j];
   cur.m[i+1][j] = 0;
   cur.s = jug.s + makestring(cur.m);
   int cost = 0;
   for(int i=0;i<3;i++){
    	for(int j=0;j<3;j++){
     		if(cur.m[i][j]!=0){
      			cost += distance(cur.m, goal, cur.m[i][j]);
     		}
    	}
   	}
   	cur.g = jug.g + 1;
   	cur.f = cost + cur.g;
   int num = 0;
   	for(int i=0;i<visit.size();i++){
   		if(mequal(visit[i].m, cur.m))
   			num++;
	}
	if(num==0)
		q.push(cur);
  }
 }
 return 0;
}
