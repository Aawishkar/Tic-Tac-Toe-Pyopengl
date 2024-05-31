/**@file my.c
 * @brief a program to play Tic Tac Toe
 * @author: Aawishkar tiwari
 * @date; 08/17/2021
*/


#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<windows.h>
#include<conio.h>

/*Declaring Function called introduction which displays the introduction of the game.*/
void introduction();

/*Declaring Function called board which prints the board where the game is played.*/
void board();

/*Declaring Function called win_verification which checks the win or draw condtion of the game.*/
int win_verification();

/*Declaring Function called againstfriend where the input is taken from the user and game is played.*/
void againstfriend();

/*Declaring Function called delay which delays the display time.*/
/*The argument that taken by the function is the second of screen delay.*/
void delay(float t);

/*Declaring Function called rules which displays the rules of the game.*/
void rules();

/*Declaring Function called endgame which displays the details after the game ends.*/
void endgame();

/*Declaring a array named move.*/
char move[10]={'0','1','2','3','4','5','6','7','8','9'};

/*Variable declaration*/
char ch;


/*Defining the introduction function.*/
void introduction(){

    system("CLS");            /*Clearing the screen.*/


    SetConsoleOutputCP(CP_UTF8);        /*Syntax for printing TIC TAC TOE.*/

    /*Title bar.*/
    printf("\t████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗\n");
    printf("\t╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝\n");
    printf("\t   ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗  \n");
    printf("\t   ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝  \n");
    printf("\t   ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗\n");
    printf("\t   ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝ ╚══════╝\n");
    

    delay(1);               /*Calling the dealy fumction.*/
    printf("## Enjoy the game.\n");
    printf("## Lets get started.\n\n");
}

/*Defining the board function.*/
void board(){
    system("CLS");

    /*Drawing board and leaving places for assigning value.*/
	printf("     |     |     \n");
	printf("  %c  |  %c  |  %c  \n",move[1],move[2],move[3]);
	printf("_____|_____|_____\n");
	printf("     |     |     \n");
	printf("  %c  |  %c  |  %c  \n",move[4],move[5],move[6]);
	printf("_____|_____|_____\n");
	printf("     |     |     \n");
	printf("  %c  |  %c  |  %c  \n",move[7],move[8],move[9]);
	printf("     |     |     \n");
}


/*Defining the main function.*/
int main(){


    introduction();             /*Calling function named introduction. */
    delay(3);
    system("CLS");

    /*Assigning the values in the board.*/
    int k =1;
    for( int i = 49; i<=57;i=i+1){
        move[k]=i;
        k=k+1;
    }

    
    int against;            /*Declaring variable.*/

    /*Menu bar.*/
    menu:

		printf("GAME:\n");
        delay(1);
		printf("1. Start Game.\n");
		printf("2. Rules.\n");
		printf("3. I dont want to play. This is boring.\n");



        delay(1);

		printf("Enter Your Choice=\n");     /*Taking choice from user and storing in against.*/
        scanf("%d",&against);

        if(against==1){
            system("CLS");

            againstfriend();            /*Calling function named againstfriend.*/
        }

        else if(against==2){
            system("CLS");

            rules();                     /*Calling function named rules.*/
        }

        else if(against==3){
            system("CLS");

            endgame();                   /*Calling function named endgame*/    
            end();
        }

        else{
            printf("##INVALID CHOICE");

            delay(2);
            system("CLS");
            goto menu;                  /*If wrong input is provided then going to menu again.*/
        }
}


/*Defining the againstfriend function.*/
void againstfriend(){


    char player1[16], player2[16];          /*Array declaration named player1 and player2.*/

    printf ("* Enter player-1 name:\n ");   /*Taking input from user and storing in player1.*/
	scanf("%s",&player1);
    delay(0.8);
	printf ("%s's symbol is 'X'.\n\n", player1);

    delay(1.8);
    system("CLS");

	printf ("* Enter player-2 name: \n");    /*Taking input from user and storing in player2*/
	scanf ("%s",&player2);
    delay(0.8);
	printf ("%s's symbol is 'O'.\n\n", player2);

    delay(1.8);

    /*Variable declarations.*/
    char mark;                                          
    int player=1,i,place;
    char *name;

    do
    {

		board();                    /*Calling the function named board.*/


        /*Determing the players turn.*/
        if(player%2==0){
            player=1;
        }
        else{
            player=2;
        }
    
        if(player==1){
            name=player2;
        }
        else{
            name=player1;
        }



		printf("%s, enter the choice : ",name);     /*Taking information from user and assigning in place.*/
		scanf("%d",&place);
        
        /*providing the symbol for player1 and player2.*/
        if(player==2){
            mark='X';
        }
        else{
            mark='O';
        }



        /*Marking the place provided by the player.*/
		if(place == 1 && move[1] == '1'){
			move[1] = mark;
		}
        else if(place == 2 && move[2] == '2'){
			move[2] = mark;
        }
		else if(place == 3 && move[3] == '3'){
			move[3] = mark;
        }
		else if(place == 4 && move[4] == '4'){
			move[4] = mark;
        }
		else if(place == 5 && move[5] == '5'){
			move[5] = mark;
        }
		else if(place == 6 && move[6] == '6'){
			move[6] = mark;
        }
		else if(place == 7 && move[7] == '7'){
			move[7] = mark;
        }
		else if(place == 8 && move[8] == '8'){
			move[8] = mark;
        }
		else if(place == 9 && move[9] == '9'){
			move[9] = mark;
        }
		else {
			printf("Invalid option !");
            player--;
            getch();
			
        }
        i = win_verification();         /*Calling function named win_verification.*/

	}while(i==-1);                      /*Repeating the do while condition until the value of i is -1.*/

    board();                            /*Calling the function named board.*/

    /*Displaying which player won the game.*/
	if(i==1){
		printf("%s won",name);
	}

    /*Displaying game draw if no one wins.*/
	else {
		printf("==>Game draw");
	}


    delay(0.8);



    again:

    printf("\nDo you want to play again(y/n)?");
    getchar();                                      /*Taking the input from user.*/

    ch=getchar();


    if(ch=='Y'||ch=='y'){
        main();                                     /*Calling main function if information satisfies.*/
    }

    else if(ch=='N'||ch=='n'){                      
        endgame();                                  /*Calling endgame function if information satisfies.*/
        delay(3);
        end();                                      /*End condition.*/
    }
    else{
        printf("INVALID CHOICE");
        delay(2);
        goto again;                                 /*If provided information is wrong it goes to again*/
    }


}


/*Defining the win_verification function.*/
int win_verification(){

    /*Checks for the information from user for win or draw and
     if someone wins it returns 1 or returns 0 when game is draw or returns -1 when nothing happens.*/
    if(move[1] == move[2] && move[2] == move[3]){
		return 1;
    }
	else if (move[4] == move[5] && move[5] == move[6]){
		return 1;
    }
	else if(move[7] == move[8] && move[8] == move[9]){
		return 1;
    }
	else if(move[1] == move[4] && move[4] == move[7]){
		return 1;
    }
	else if(move[2] == move[5] && move[5] == move[8]){
		return 1;
    }
	else if(move[3] == move[6] && move[6] == move[9]){
		return 1;
    }
	else if(move[1] == move[5] && move[5] == move[9]){
		return 1;
    }
	else if(move[3] == move[5] && move[5] == move[7]){
		return 1;
    }
	else if(move[1] != '1' && move[2] != '2' && move[3] != '3' && move[4] !='4' && move[5] != '5' && move[6] != '6' && move[7] != '7' && move[8] != '8' && move[9] != '9'){
		return 0;
    }
	else{
		return -1;
    }
}


/*Defining the delay function.*/
void delay(float t){

    /*Starting point of the time.*/
    clock_t start=0;
    start=clock();

    while((clock()-start)<(t*1000));

}


/*Defining the rules function.*/
void rules(){

    /*Rules for the game.*/
    delay(0.8);
    printf("1. The game is played on a grid that's 3 squares by 3 squares.\n");

    delay(0.8);
    printf("2.You are X, your friend is O or vice versa. Players take turns putting their marks in empty squares.\n");

    delay(0.8);
    printf("3.The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n");
    
    delay(0.8);
    printf("4.When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n");

    delay(3);
    main();                     /*Calling the main function.*/
}


/*Defining the endgame function.*/
void endgame(){
    system("CLS");

    /*Displaying information after the game ends*/
    delay(1);
    printf("Thanks for playing.\n");

        
    delay(1);
    printf("Hope you enjoyed it.\n");


    delay(3);
    system("CLS");
    printf("\t\tGame name : Tic Tac Toe\n");
    delay(1);
    printf("\t\tDeveloper : Aawishkar Tiwari\n");
    delay(1);
    printf("\t\tDepartment : Computer Engineering\n");
    delay(3);
    system("CLS");
}





