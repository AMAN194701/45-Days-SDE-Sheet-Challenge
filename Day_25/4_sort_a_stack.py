def insert(stack, temp):
    # Base case:
    # If the stack is empty or the top element is smaller than
    # or equal to temp, insert temp
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return

    # remove the top element
    val = stack.pop()
    # recursively insert temp into the remaining stack
    insert(stack, temp)
    # Put the removed element back
    stack.append(val)


def sortStack(stack):
    # Base case: If stack is empty, return
    if stack:
        # Remove the top element
        temp = stack.pop()

        # sort the remaining stack
        sortStack(stack)

        # insert the removed element in sorted order
        insert(stack, temp)


stack = [4, 1, 3, 2]
sortStack(stack)
print("Sorted Stack:", stack)