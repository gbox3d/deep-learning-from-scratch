#%% 모듈 준비 
import numpy as np

#%% batch test

# x = [[1,2,3],[4,5,6]]
w = [2,4,8]

print(np.dot([1,1,1],w))
print(np.dot([2,2,2],w))


# %%
# print(np.dot([[1,1,1]],w))
print(np.dot([[1,1,1],[2,2,2]],w))

# %%
