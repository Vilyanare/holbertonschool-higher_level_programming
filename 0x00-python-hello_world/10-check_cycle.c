#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast = list, *slow = list;

	if (list)
	{
		while (fast->next && slow->next)
		{
			if (fast->next->next)
			{
				fast = fast->next->next;
				slow = slow->next;
			}
			else
				break;
			if (fast == slow)
				return (1);
		}
	}
	return (0);
}