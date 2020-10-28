import numpy as np


class M:
    def my_one(self):
        my_list = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9]
        ]

        np_arr = np.array(my_list)
        even = np.arange(0, 9, 2)
        odd = np.arange(1, 9, 2)
        print(f' arange : \neven num : {even} \nodd num : {odd}\n')

        # return one dimension array
        print(f'linspace : {np.linspace(0,5,10)}')

        print(f'\nidentity matrix {np.eye(4)}')

        # 0+ -> 1
        print(f'\n random matrix or array: \n{np.random.rand(5,5)}')

        # -0+
        print(f'\n random matrix or array: \n{np.random.randn(5)}')
        print(f'\n random array: \n{np.random.randint(1,100, 4)}\n')

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

    def slicing(self):

        #  indexing element from array
        arr = np.arange(0, 10)
        print(arr)

        print(arr[1:4])
        print(arr[3:])

        #! can broadcast tot the array, data will overwright it
        arr[:4] = 100
        print(arr, '\n')

        # matrix index
        arr_2d = np.array([
            np.random.randint(0, 50, 4),
            np.random.randint(0, 50, 4),
            np.random.randint(0, 50, 4)
        ])
        print(arr_2d)
        print(
            f'{arr_2d[0,2] } same is {arr_2d[0][2]}'
        )
        print(
            f' get top left corner of matrix: \n {arr_2d[:2, 1:]} \n'
        )

        #! conditional selection
        arr = np.random.randint(10, 50, 11)
        print(arr)
        print(
            f'conditional search:  {arr > 30}'
        )
        print(arr[arr > 30])  # put condition straight to array
        print(arr[arr < 30])

        arr_2d = np.random.randint(10, 30, 50).reshape(5, 10)
        print(
            f'\nbig 2d array : \n {arr_2d}'
        )

        chank = arr_2d[1:3, 3:5]  # first get rows and then cut column
        print(
            f'\ngrab chanck of it :\n {chank}'
        )

    def num_operations(self):
        print('numpy operations :  \n')

        arr = np.arange(0, 10)
        print(
            f' array + it self : {arr + arr}\n' +
            f'array * 3 : {arr * 3}\n' +
            # etc for regular
            f'sqrt or array : {np.sqrt(arr)}\n' +
            # log 0 is  -inf and must be undefined
            f'numpy will give warning instead of error like : {np.log(arr)}'
        )


if __name__ == "__main__":
    nn = M()
    nn.num_operations()
