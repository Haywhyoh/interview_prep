str = '([)]'
lst = list(str)
dict = {'{':'}', '(':')', '[':']'}
dict2 = {'}':'{', ')':'(', ']':'['}

queue = []
for i in lst:
    if i in dict.keys():
        queue.append(i)
        continue
    if dict2[i] in queue:
        queue.remove(dict2[i])
    else:
        queue.append(i)
    print(queue)
if len(queue) == 0:
    print('True')
else:
    print('False')


def isValid(self, s: str) -> bool:
        lst = list(s)
        dict = {'{':'}', '(':')', '[':']'}
        dict2 = {'}':'{', ')':'(', ']':'['}

        queue = []
        for i in range(len(lst)):
            if lst[i] in dict.keys():
                queue.append(lst[i])
                continue
            if dict2[lst[i]] in queue and lst[i - 1] == dict2[lst[i]]:
                queue.remove(dict2[lst[i]])
            else:
                queue.append(lst[i])
        if len(queue) == 0:
            return True
        else:
            return False
