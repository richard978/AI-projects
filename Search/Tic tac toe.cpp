#include <cstdlib>
#include <iostream>
#include <time.h>
using namespace std;

#define x 'x'
#define o 'o'
#define empty '\0'

#define INFINITY INT_MAX

#define INPROGRESS 1
#define DRAW 0
#define WIN  (+INFINITY)
#define LOSE (-INFINITY)
#define DOUBLE 2


int maxSearch(char board[9], int alpha, int beta);
void PrintBoard(char board[9]);

int gameState(char board[9]){
	int state;
	static int table[][3] = {
		{0, 1, 2},
		{3, 4, 5},
		{6, 7, 8},
		{0, 3, 6},
		{1, 4, 7},
		{2, 5, 8},
		{0, 4, 8},
		{2, 4, 6},
	};
	char chess = board[0];
	for (char i = 1; i < 9; ++i){
		chess &= board[i];
	}
	bool isFull;
	if(chess == 0)
		isFull = 0;
	else
		isFull = 1;
	bool isFind = false;
	for (int i = 0; i < sizeof(table)/sizeof(int[3]);++i){
		chess = board[table[i][0]];
		int j;
		for (j = 1; j < 3; ++j)
			if (board[table[i][j]] != chess)
				break;
		if (chess != empty && j == 3){
			isFind = true;
			break;
		}
	}
	if (isFind)
		if(chess == o)
			state = WIN;
		else
			state = LOSE;
	else{
		if(isFull)
			return DRAW;
		else{
			int find[2] = {0};
			for (int i = 0; i < sizeof(table)/sizeof(int[3]); ++i){
				bool isEmpty = false;
				chess = 0xff;
				for (int j = 0; j < 3; ++j){
					if (board[table[i][j]] == empty && !isEmpty)
						isEmpty = true;
					else
						chess &= board[table[i][j]];
				}
				if ((chess == o || chess == x) && isEmpty){
					isFind = true;		
					if (chess == o)
						find[0]++;
					else
						find[1]++;
				}
			}
			if (find[0] > 1 && find[1] < 1)
				state = DOUBLE;
			else if (find[1] > 1 && find[0] < 1)
				state = -DOUBLE;
			else
				state = INPROGRESS;
		}
	}
	return state;
}

int minSearch(char board[9], int alpha, int beta){
	int state = gameState(board);
	if (state == DRAW) return 0;
	if (state != INPROGRESS) return state;
	int bestValue = +INFINITY;
	int value = alpha;
	for (int i = 0; i < 9&&value<beta; i++){
		if(board[i] == empty){
			board[i] = x;
			int tmp = maxSearch(board, value, beta);
			if(tmp < bestValue)
				bestValue = tmp;
			board[i] = empty;
		}
	}
	return bestValue;
}
int maxSearch(char board[9], int alpha, int beta){
	int state = gameState(board);
	if (state == DRAW) return 0;
	if (state != INPROGRESS) return state;
	int bestValue = -INFINITY;
	int value = beta;
	for(int i = 0; i < 9&&value>alpha; i++){
		if(board[i] == empty){
			board[i] = o;
			int tmp = minSearch(board, alpha, value);
			if(tmp > bestValue)
				bestValue = tmp;
			board[i] = empty;
		}
	}
	return bestValue;
}

int minimax(char board[9]){
	int bestValue = +INFINITY, index = 0;
	char move[9] = {0};
	for(int i = 0; i < 9; i++){
		if(board[i] == empty){
			board[i] = x;
			int value = maxSearch(board, -INFINITY, +INFINITY);
			if(value < bestValue){
				bestValue = value;
				index = 0;
				move[index] = i;
			}
			else if(value == bestValue){
				move[index++] = i;
			}
			board[i] = empty;
		}
	}
	srand((int)time(0));
	if(index > 0)
		index = rand() % index;
	return move[index];
}

void Print(char board[9]){
	for (int i = 0; i < 3; ++i){
		for (int j = 0; j < 3; ++j){
			if (board[i * 3 + j])
				cout<<board[i * 3 + j]<<" ";
			else
				cout<<"+ ";
		}
		cout<<endl;
	}
	cout<<endl;
}

int main(){
	char board[9] = {0};
	int state = INPROGRESS;
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<"+ ";
		}
		cout<<endl;
	}
	cout<<endl;
	while (state != WIN && state != LOSE && state != DRAW){
		int a, b;
		cout<<"Your turn; enter the coordinate:"<<endl;
		cin>>a>>b;
		if((a>2 || b>2) || board[a*3+b]){
			cout<<"You can't put chess here!"<<endl;
			cout<<endl;
			continue;
		}
		board[a*3+b] = o;
		state = gameState(board);
		Print(board);
		if(!board[minimax(board)]){
			cout<<"Computer's turn"<<endl;
			board[minimax(board)] = x;
			state = gameState(board);
			Print(board);
		}
		if (state == WIN || state == LOSE || state == DRAW)
			break;
	}
	switch (state){
	case WIN:
		printf("You Win!\n");
		break;
	case LOSE:
		printf("You Loose!\n");
		break;
	case DRAW:
		printf("Draw!\n");
		break;
	default:
		break;
	}
}
