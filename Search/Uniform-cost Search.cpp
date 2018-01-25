#include<iostream>  
#include<queue>  
#include<stack>
#include<string>
#define INF 10000
using namespace std;  

int edge[7][7] = {
	0, 140, INF, INF, INF, INF, INF,
	140, 0, 99, 80, INF, INF, INF,
	INF, 99, 0, INF, INF, INF, 211,
	INF, 80, INF, 0, 146, 97, INF,
	INF, INF, INF, 146, 0, 138, INF,
	INF, INF, INF, 97, 138, 0, 101,
	INF, INF, 211, INF, INF, 101, 0
};
int visit[7]; 
int dist;
int pre[7];
string str[7] = {"Arad", "Sibiu", "Fagaras", "Rimmicu Vilcea", "Craiova", "Pitesti", "Bucharest"};

struct node{
	int city;
	int cost;
	node(){}
	node(int mcity, int mcost){
		city = mcity;
		cost = mcost;
	}
	bool operator > (const node &s)const{
		return cost<s.cost;
	}
	bool operator < (const node &s)const{
		return cost>s.cost;
	}
	bool operator == (const node &s)const{
		return cost==s.cost;
	}
};
void UCS(int start, int end){
	priority_queue<node> q;
	q.push(node(start,0));
	node CurNode;
	stack<int> chr1, chr2;
	while(!q.empty()){
		int temp;
		CurNode = q.top();
		q.pop();
		visit[CurNode.city] = true;
		if(CurNode.city==end){
			int e = end;
			cout<<"Nodes are: "<<endl;
			cout<<start<<" ";
			while(pre[e]!=start){
				chr1.push(pre[e]);
				chr2.push(pre[e]);
				e = pre[e];
			}
			while(!chr1.empty()){
				cout<<chr1.top()<<" ";
				chr1.pop();
			}
			cout<<end<<endl;
			cout<<"Cities are: "<<endl;
			cout<<str[start]<<" ";
			while(!chr2.empty()){
				cout<<str[chr2.top()]<<" ";
				chr2.pop();
			}
			cout<<str[end]<<endl;
			cout<<"Total cost is: "<<endl;
			cout<<CurNode.cost<<endl;
			break;
		}
		for(int i=0;i<7;i++){
			if(edge[CurNode.city][i]!=INF && visit[i]==false){
				pre[i] = CurNode.city;
				temp = CurNode.cost+edge[CurNode.city][i];
				q.push(node(i,temp));
			}
		}
	}
	if(q.empty())
		cout<<"Failed"<<endl;
}

int main(){
	UCS(0,6);
	return 0;
}
