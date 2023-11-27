#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
*check_cycle -  checks if list is cyclical
*@list : apointer to alist
*Return: 1 if it's cycle, 0 if not
*/

int check_cycle(listint_t *list)
{
listint_t *nextone, *after_next;

nextone = list;
after_next = list;
while (after_next && after_next->next)
{
nextone = nextone->next;
after_next = after_next->next->next;
if (nextone == after_next)
return (1);
}
return (0);
}
