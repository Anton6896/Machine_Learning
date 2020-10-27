import numpy as np


def my_one():
    my_list = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9]
    ]

    np_arr = np.array(my_list)
    even = np.arange(0, 9, 2)
    odd = np.arange(1, 9, 2)
    print(f' arange : \neven num : {even} \nodd num : {odd}\n')

    print(f'linspace : {np.linspace(0,5,10)}')  # return one dimension array

    print(f'\nidentity matrix {np.eye(4)}')

    # 0+ -> 1
    print(f'\n random matrix or array: \n{np.random.rand(5,5)}')

    # -0+
    print(f'\n random matrix or array: \n{np.random.randn(5)}')
    print(f'\n random matrix or array: \n{np.random.randint(1,100, 4)}\n')

    # max min
    ranarr = np.random.randint(0, 50, 10)
    # get position
    print(f'position of max value from ranarr : {ranarr.argmax()}')
    print(f'max value from ranarr : {ranarr.max()}')

    # reshape method
    arr = np.arange(25)
    print(
        f'reshape : this: {arr} to : \nthis :  {arr.reshape(5,5)} '
    )
    print(arr.shape)  # return the shape of the arr 
    # arr.dtype  for data type in array 


if __name__ == "__main__":
    my_one()
