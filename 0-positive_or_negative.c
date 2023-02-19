#include <stdlib.h>
#include <time.h>
#include <stdio.h>
/* more header goes there */

/* betty style doc for function goes ther */
/**
 * main -Entry point
 * printing with n variable
 * Return: Always 0 (success)
 */
int main(void)
{
	int n;

	srand(time(0));
	n = rand() - RAND_MAX / 2;
	/* your code goes here */
	if (n > 0)
		printf("%d is positive/n", n);
	else if (n == 0)
		printf("%d is zero/n", n);
	else
		printf("%d is negative/n", n);
	return (0);
}
