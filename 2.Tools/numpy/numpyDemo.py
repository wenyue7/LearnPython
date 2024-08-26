import numpy as np

def numpyDemo():
    print('#================================================')
    print("hello world")
    arr = np.array([[1,2,3], [2,3,4]])
    print(arr)
    print(type(arr))
    print('number of dim:', arr.ndim)
    print('shape:', arr.shape)
    print('size:', arr.size)

    print('#================================================')
    a32 = np.array([1,23,456], dtype=int)
    print(a32.dtype)
    a64 = np.array([1,23,456], dtype=np.int64)
    print(a64.dtype)
    f64 = np.array([1,23,456], dtype=float)
    print(f64.dtype)
    print('\n')

    print('#================================================')
    z = np.zeros((3, 4))
    print(z)
    print(z.dtype)
    print()

    one = np.ones((3, 4), dtype=int)
    print(one)
    print(one.dtype)
    print()

    emt = np.empty((3, 4), dtype=int)
    print(emt)
    print(emt.dtype)
    print()

    ran = np.arange(12).reshape((3,4))
    print(ran)
    print(ran.dtype)
    print()

    li = np.linspace(1, 10, 6).reshape(2, 3)
    print(li)
    print(li.dtype)
    print('\n')

    print('#================================================')
    a = np.array([10,20,30,40])
    b = np.arange(4)
    print(a)
    print(b)
    print()

    print(a+b)
    print(a-b)
    print(a*b)
    print()

    print(a**b)
    print()

    print(10*np.sin(a))
    print()

    print(b<3)
    print()

    print('#================================================')
    a = np.array([[1,2], [3,4]])
    b = np.arange(4).reshape(2, 2)
    print(a)
    print(b)
    print()

    print(a * b)
    print(np.dot(a, b)) #矩阵乘法，或下面：
    print(a.dot(b))
    print()

    print('#================================================')
    a = np.random.random((2, 4))
    print(a)
    print(np.sum(a))
    print(np.min(a))
    print(np.max(a))
    print()

    print(np.sum(a, axis=1))  #返回每一行的和。 axis=1代表行
    print(np.min(a, axis=0))  #返回每一列的最小值。 axis=0代表列
    print(np.mean(a, axis=1))  #返回每一行的平均值

    print('#================================================')
    A = np.arange(2, 14).reshape(3, 4)
    print(A)

    print(np.argmin(A)) #最小索引
    print(np.argmax(A)) #最大索引
    print()

    print(A.mean())
    print(np.median(A)) #中位数
    print(A.cumsum()) #累加值
    print(np.diff(A)) #相邻差值
    print()

    print('#================================================')
    A = np.array([[1,0], [0,3]])
    print(A)
    print(A.nonzero()) #分别输出非零元素的行和列值
    print(np.sort(A)) #逐行排序后的矩阵
    print(np.sort(A, axis=0)) #逐列排序的矩阵
    print(np.sort(A).nonzero())
    print()

    B = np.arange(14, 2, -1).reshape(3, 4)
    print(B)
    print(B.transpose()) #转置
    print((B.T).dot(B))  #转置
    print()

    print(np.clip(B, 5, 9))  #B中将范围限定，大于9的数都为9，小于5的都为5，之间的数不变
    print()

    print('#================================================')
    A = np.arange(3, 7)
    print(A)
    print(A[2])
    print()

    B = np.arange(3, 15).reshape(3, 4)
    print(B)
    print(B[2])
    print(B[2][1])
    print(B[2, 1])
    print()

    print(B[2, 2:])
    print(B[1:, 2:])
    print()

    for row in B:
        print(row)
    print()

    for col in B.T:
        print(col)
    print()

    print(B.flatten())
    for elm in B.flat:
        print(elm)

    print('#================================================')
    #矩阵合并
    A = np.array([1,1,1])
    B = np.array([2,2,2])
    C = np.vstack((A, B, A, B))
    print(C)
    print(A.shape, (A.T).shape)
    print(C.shape)
    print()

    D = np.hstack((A, B))
    print(D)
    print()

    print(A[np.newaxis, :])
    print(A[:, np.newaxis])
    print(np.hstack((A[:, np.newaxis], B[:, np.newaxis])))
    print()


    print(np.stack((A,B), axis=0))
    print(np.stack((A,B), axis=1))
    #print(np.concatenate((A,B,B,A), axis=0))
    #print(np.concatenate((A,B,B,A), axis=1))

    print('#================================================')
    A = np.arange(12).reshape(3, 4)
    print(A)
    print(np.split(A, 2, axis=1))
    print(np.split(A, 3, axis=0))
    print()

    print(np.array_split(A, 3, axis=1)) #不等分割
    print()

    print(np.hsplit(A, 2))
    print(np.vsplit(A, 1))

    print('#================================================')
    A = np.arange(4)
    B = A
    C = B
    D = A.copy()
    print(A, B, C, D)
    A[0] = 5
    print(A, B, C, D)
    print(id(A), id(B), id(C), id(D)) #id返回指针的值（内存地址）
    print()


def main():
    numpyDemo()

if __name__ == "__main__":
    main()
