#include "lists.h"
/**
 * is_palindrome - check to see if data in a linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if not 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *front = NULL, *back = NULL, *backback = NULL;
	int x = 1;

	if (head)
	{
		if (*head)
		{
			front = *head;
			back = *head;
			while (back->next)
				{
				back = back->next;
				x++;
				}
			backback = back;
			if (back->n == front->n)
			{
				while (1)
				{
					if (front == back || front->next == back)
						return (1);
					if (front->n == back->n)
					{
						front = front->next;
						back = *head;
						while(back->next != backback)
							back = back->next;
						backback = back;
					}
					else
						break;
				}
			}
		}
	}
	return (0);
}