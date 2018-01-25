#include <iostream>
#include <queue>
#include <sstream>
using namespace std;

class nodes{
public:
	pair<int, int> p;
	int first;
	int second;
	string s;
	int fcost;
	bool operator < (const nodes &s)const{
		return fcost > s.fcost;
	}
};
int visit[20][20];

string makestring(int a, int b){
	std::stringstream out1;
	std::stringstream out2;
	string t1, t2, str;
	out1 << a;
	t1 = out1.str();
	out2 << b;
	t2 = out2.str();
	str = "(" + t1 + "," + t2 + ")";
	return str;
}
int main()
{
	int counter = 0;
	ios::sync_with_stdio(false);
	//pair<int,int> cap,ini,final;
	nodes cap, ini, final;
	ini.p.first = 0, ini.p.second = 0; 
	ini.fcost = 0;
	ini.s = makestring(ini.p.first, ini.p.second);
	//Input initial values
	cout << "Enter the capacity of 2 jugs\n";
	cin >> cap.p.first >> cap.p.second;
	//input final values
	cout << "Enter the required jug config\n";
	cin >> final.p.first >> final.p.second;
	//Using BSF to find the answer
	priority_queue<nodes> q;
	q.push(ini);
	nodes jug;
	while (!q.empty()){
		//Base case
		jug = q.top();
		q.pop();
		visit[jug.p.first][jug.p.second] = 1;
		if (jug.p.first == final.p.first){// && jug.p.second == final.p.second){
			string str;
			if (jug.p.second != 0){
				str = makestring(jug.p.first, 0);
			}
			jug.s += str;
			cout << jug.s << endl;
			// counter++;
			// if(counter==5)
			break;
		}
		nodes temp = jug;
		//Fill 1st Jug
		if (jug.p.first<cap.p.first){
			temp.p = make_pair(cap.p.first, jug.p.second);
			temp.s = jug.s + makestring(temp.p.first, temp.p.second);
			int cost = abs(ini.p.first - temp.p.first) + abs(ini.p.second - temp.p.second);
			int dist = abs(final.p.first - temp.p.first) + abs(final.p.second - temp.p.second);
			temp.fcost = cost + dist;
			if (!visit[temp.p.first][temp.p.second])
				q.push(temp);
		}
		//Fill 2nd Jug
		if (jug.p.second<cap.p.second){
			temp.p = make_pair(jug.p.first, cap.p.second);
			temp.s = jug.s + makestring(temp.p.first, temp.p.second);
			int cost = abs(ini.p.first - temp.p.first) + abs(ini.p.second - temp.p.second);
			int dist = abs(final.p.first - temp.p.first) + abs(final.p.second - temp.p.second);
			temp.fcost = cost + dist;
			if (!visit[temp.p.first][temp.p.second])
				q.push(temp);
		}
		//Empty 1st Jug
		if (jug.p.first>0){
			temp.p = make_pair(0, jug.p.second);
			temp.s = jug.s + makestring(temp.p.first, temp.p.second);
			int cost = abs(ini.p.first - temp.p.first) + abs(ini.p.second - temp.p.second);
			int dist = abs(final.p.first - temp.p.first) + abs(final.p.second - temp.p.second);
			temp.fcost = cost + dist;
			if (!visit[temp.p.first][temp.p.second])
				q.push(temp);
		}
		//Empty 2nd Jug
		if (jug.p.second>0){
			temp.p = make_pair(jug.p.first, 0);
			temp.s = jug.s + makestring(temp.p.first, temp.p.second);
			int cost = abs(ini.p.first - temp.p.first) + abs(ini.p.second - temp.p.second);
			int dist = abs(final.p.first - temp.p.first) + abs(final.p.second - temp.p.second);
			temp.fcost = cost + dist;
			if (!visit[temp.p.first][temp.p.second])
				q.push(temp);
		}
		//Pour from 1st jug to 2nd until its full
		if (jug.p.first>0 && (jug.p.first + jug.p.second) >= cap.p.second){
			temp.p = make_pair((jug.p.first - (cap.p.second - jug.p.second)), cap.p.second);
			temp.s = jug.s + makestring(temp.p.first, temp.p.second);
			int cost = abs(ini.p.first - temp.p.first) + abs(ini.p.second - temp.p.second);
			int dist = abs(final.p.first - temp.p.first) + abs(final.p.second - temp.p.second);
			temp.fcost = cost + dist;
			if (!visit[temp.p.first][temp.p.second])
				q.push(temp);
		}
		//Pour from 2nd jug to 1st until its full
		if (jug.p.second>0 && (jug.p.first + jug.p.second) >= cap.p.first){
			temp.p = make_pair(cap.p.first, (jug.p.second - (cap.p.first - jug.p.first)));
			temp.s = jug.s + makestring(temp.p.first, temp.p.second);
			int cost = abs(ini.p.first - temp.p.first) + abs(ini.p.second - temp.p.second);
			int dist = abs(final.p.first - temp.p.first) + abs(final.p.second - temp.p.second);
			temp.fcost = cost + dist;
			if (!visit[temp.p.first][temp.p.second])
				q.push(temp);
		}
		//Pour all water from 1st to 2nd
		if (jug.p.first>0 && (jug.p.first + jug.p.second) <= cap.p.second){
			temp.p = make_pair(0, jug.p.first + jug.p.second);
			temp.s = jug.s + makestring(temp.p.first, temp.p.second);
			int cost = abs(ini.p.first - temp.p.first) + abs(ini.p.second - temp.p.second);
			int dist = abs(final.p.first - temp.p.first) + abs(final.p.second - temp.p.second);
			temp.fcost = cost + dist;
			if (!visit[temp.p.first][temp.p.second])
				q.push(temp);
		}
		//Pour all water from 2nd to 1st
		if (jug.p.second>0 && (jug.p.first + jug.p.second) <= cap.p.first){
			temp.p = make_pair(jug.p.first + jug.p.second, 0);
			temp.s = jug.s + makestring(temp.p.first, temp.p.second);
			int cost = abs(ini.p.first - temp.p.first) + abs(ini.p.second - temp.p.second);
			int dist = abs(final.p.first - temp.p.first) + abs(final.p.second - temp.p.second);
			temp.fcost = cost + dist;
			if (!visit[temp.p.first][temp.p.second])
				q.push(temp);
		}
	}
	return 0;
}