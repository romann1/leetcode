def reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[0:-1])


print(f'hello -> {reverse("hello")}')
print(f'h -> {reverse("h")}')
print(f'ab -> {reverse("ab")}')
print(f'\'\' -> {reverse("")}')


