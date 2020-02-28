### Reverse Integer

```python

class Solution:
    def reverse(self, x: int) -> int:
        re_in = [i for i in str(x)]
        return "".join(sorted(re_in, reverse=True))
# '-'부호가 뒤로 가버림

```

```python
class Solution:
    def reverse(self, x: int) -> int:
        re_in = [i for i in str(x)]
        re_x = ''
        # if re_in.index('0'):
        #             
        # del re_x[del_x]
        # del re_in.value('0')
        # for i in range(len(re_in)):
        #     if re_in[i] == '0':
        #         del re_in[i]
        if re_in[0] == '-' or re_in[0] == '+':
            # re_x.append(re_in[0])
            re_x = re_in[0]
            del re_in[0]
            # return "".join(sorted(re_in, reverse=True))
            re_in.append(re_x)
            re_in.reverse()
            return "".join(re_in)
        else:
            return "".join(sorted(re_in, reverse=True))
        print(re_in)
        print(re_x)

#  0이 들어가있을경우 pop해주는거 실패
```