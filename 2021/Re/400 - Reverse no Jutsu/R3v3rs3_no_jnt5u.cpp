#include<bits/stdc++.h>
#include<windows.h>
using namespace std;

int check(string ninjutsu){
			if( ninjutsu.length()==32 &&
                ninjutsu[0x1c]         == 'r' &&
                ninjutsu[18/9]         == 'P' &&
                ninjutsu[14]           == '0' &&
                ninjutsu[21+2*10+2-22] == '_' &&
                ninjutsu[3]  		   == 'C' &&
                ninjutsu[24]           == 'i' &&
                ninjutsu[18/6*10]      == 'm' &&
                ninjutsu[6]            == 'B' &&
                ninjutsu[9]            == '3' &&
                ninjutsu[10]    	   == 'x' &&
                ninjutsu[12]           == '_' &&
                ninjutsu[5]            == 'U' &&
                ninjutsu[16]           == 'j' &&
                ninjutsu[23]           == '4' &&
                ninjutsu[17]           == 'n' &&
                ninjutsu[4]            == 'L' &&
                ninjutsu[18+9-2+2-9]   == 't' &&
                ninjutsu[20]           == 'u' &&
                ninjutsu[0]            == 'I' &&
                ninjutsu[22]           == 'K' &&
                ninjutsu[7]            == '{' &&
                ninjutsu[11]           == 'Y' &&
                ninjutsu[0x1b]         == '4' &&
                ninjutsu[13]           == 'n' &&
                ninjutsu[5*5]          == '_' &&
                ninjutsu[8]            == 's' &&
                ninjutsu[26]           == 'h' &&
                ninjutsu[1]            == 'S' &&
                ninjutsu[29]           == '3' &&
                ninjutsu[15]           == '_' &&
                ninjutsu[21*2-23]      == '5' &&
                ninjutsu[31]           == '}') 
	return 1;
    return 0;
}

int main(){
	cout <<"Ban da tim thay nhung gi Deku Haha can chu\n\n\n";
	string ninjutsu;
	getline(cin,ninjutsu);
	system("cls");
	if(check(ninjutsu)) cout << "\n\n\n								Deku Haha chac chan se rat cam kich truoc tam long hao hiep cua ban giup han tim duoc cam thuat >>_<<";
	else cout << "\n\n\n								Deku Haha guc nga khi biet do khong phai thu han can ~..~"; 
}


