#include "lists.h"

/**
 * revlist - reverse a listint_t list
 * @head: head of listint_t list
 * Return: address to head of reversed list
 */
listint_t *revlist(listint_t *head)
{
	listint_t *slow = head, *temp = NULL;
	int x = 1;

	while (slow)
	{
		slow = slow->next;
		x++;
	}
	x /= 2;
	for (; x > 0; x--)
		head = head->next;
	slow = head;
	while (head)
	{
		temp = head->next;
		head->next = (x > 0) ? slow:NULL;
		slow = head;
		head = temp;
		x++;
	}
	return (slow);
}
/**
 * is_palindrome - check to see if data in a linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if not 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *front = NULL, *back = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	front = *head;
	back = revlist(*head);
	if (back == NULL || front == NULL)
		return (1);
	while (back->n == front->n)
	{
		if (back->next == NULL || front->next == NULL)
			return (1);
		back = back->next;
		front = front->next;

	}
	return (0);
}
