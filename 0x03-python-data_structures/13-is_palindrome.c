#include "lists.h"
/**
 * is_palindrome - check to see if data in a linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if not 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *front = NULL, *back = NULL, *backback = NULL;
	listint_t *fast = NULL, *slow = NULL;

	if (!(head || *head))
		return (0);
	slow = *head;
	fast = *head;
	while (fast && slow)
	{
		if (fast == slow)
		{
			slow = *head;
			while (1)
			{
				slow = slow->next;
				fast = fast->next;
				if (fast->next == slow->next)
				{
					break;
				}
			}
		}
		if (fast->next)
			fast = fast->next->next;
		slow = slow->next;

	}
	front = *head;
	if (fast == NULL || slow == NULL)
	{
		back = *head;
		while (back->next)
			back = back->next;
	}
	else
		back = fast;
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
				back = front;
				while(back->next != backback)
					back = back->next;
				backback = back;
			}
			else
				break;
		}
	}
	return (0);
}
