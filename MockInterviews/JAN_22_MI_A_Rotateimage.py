"""
ST: 10:21

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Ex 1)
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

[0,0], [0,1], [0,2]
[2,0], [1,0], [0,0]


# messing around with the matrix

1 2 3	  7 4 1
4 5 6 ->8 5 2
7 8 9   9 6 3


1 2 3	   7 8 9
4 5 6 -> 4 5 6
7 8 9		 1 2 3

1			4
2			3
3			2
4 		1

1 4 7 step 1 (transpose)
2 5 8
3 6 9

7 4 1 step 2 (reflect)
8 5 2
9 6 3


=== swap
int temp = x;
x = y;
y = temp;

ex2)
input = [[]]
output = [[]]


Constraints:
len:
1 <= n <= 20

n == m

n * m
-1000 <= matrix[n][m] <= 1000

Approach:
- rotate right by once (90)

- space = copyMat
	- same as inp arr

 bL's [r][c] = len(matrix), [0]
 tL = 0, 0
 tR = 0, len(mat[0])
 bR = len(ma), len(ma[0])

 										changing val
# bottomL => topL (reduce row --1)
# topL => topR		(increase col ++1)
# topR => botR 		(increase row ++1)
# botR => botL 		(reduce col --1)

# traverse thru inp matrix
for i in range(len(matrix)):
	for j in range(len(matrix[0])):
  	find the appropriate value from copyMat
    - keep track of the dir
    - depend dir
    	- find switch els
      - if TL: (bL => TL )
      	newr, newc = len(mat), 0
      	mat[i][j] = copyArr[newr][newc]
        newr -= 1
      - if TR (Tl -> TR):
      	newr, newc = copyMat[0], copyMat[0]
        mat[i][j] = copyArr[newr][newc]
        newc += 1
      - if BR (TR -> BR):
      	newr, newc = copyMat[]

    change the value of the input matrix


def transpose(mat):
	tranposeMatr = []

  for c in range(len(mat[0])):
  	row = []
  	for r in range(len(mat)):
    	row.append(mat[r][c])

    newMatr.append(row)

  return transposeMatr

def reflect(mat):
	# for each row of the transpose Matr
  # reverse the row and return

  for r in range(len(mat)):
  	# reversed row
    tempr = r[::-1]
    r = tempr

  return mat


1 2 3	  7 4 1
4 5 6 ->8 5 2
7 8 9   9 6 3

1 4 7 step 1 (transpose)
2 5 8
3 6 9

7 4 1 step 2 (reflect)
8 5 2
9 6 3

"""
# TC: O(n*m)
# SC: O(n*m)


class Solution:
  def reflect(self, mat):  # [[1,4,7], [2, 5, 8], [3,6,9]]
    # for each row of the transpose Matr
    # reverse the row and return

    for r in range(len(mat)):
      # reversed row
      tempr = r[::-1]  # [7,4,1],
      								# [8,5,2],
        							# [9,6,3]
      r = tempr

  # swap method instead of transpose arr
  def transpos(self, mat):
    	tranposeMatr = []  # [[1,4,7], [258], [3,6,9]]

      for c in range(len(mat[0])): 
        row = [] 			# [1,4,7]
        for r in range(len(mat)): 
          row.append(mat[r][c]) # [0][0] = 1, [1][0] = 4, [1][1] = 7

        tranposeMatr.append(row)
        
        """
        for (int i = 0; i < mat.length; i++) { // row
        	for (int j = i + 1; i < mat.length; j++) // elements in the row {
          	int temp = mat[j][i];
            matrix[j][i] = matrix[i][j];
            matrix[i][j] = temp;
          }
        }
        
        """

      return transposeMatr 
    
	def rotate90(self, mat): 
    mat = self.transpose(mat)
    self.reflect(mat)

  

