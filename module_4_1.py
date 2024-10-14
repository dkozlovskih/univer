from fake_math import divide as div_fake
from true_math import divide as div_true

res = div_fake(23, 4)
res1 = div_fake(23, 0)
res2 = div_fake(23, 443)
res3 = div_true(654, 89765)
res4 = div_true(654, 0)
res5 = div_true(654, 85)
print(res)
print(res1)
print(res2)
print(res3)
print(res4)
print(res5)