# The game life

Proposal for exercise of the discipline Programming II



Rules:

* Any living cell with less than two neighboring living cells dies, due to low population;
* Any living cell with more than three neighboring living cells dies, due to high population;
* Any living cell with two or three living cells next door remains alive for the next generation;
* Any dead cell with exactly three neighboring living cells turns into a living cell;

You will also have to think about:

- How to represent the Game area in an easy way to test;
- What 'value' will cells outside the Game area have. Or will the Game have no area limit?





ANOTANDO OS PASSOS PARA N ESQUECER QUANDO FOR TERMINAR!!!!

 

**neighborhood calculation**

Create a function that returns the result of the neighbors amount:



top_left_diagonal = current - 1 column - 1 row

left = current - 1 column

bottom_left_diagonal = current - 1 column + 1 row



top_right_diagonal = current + 1 column - 1 row

right = current + 1 column

bottom_right_diagonal = current + 1 column + 1 column



up = current - 1 row

down = current + 1 line



neighbors_amount = top_left_diagonal + left + bottom_left_diagonal + top_right_diagonal + bottom_right_diagonal + up + down



Inside start method, create conditional statements to check if the wihch rule will be executed:



Living cell 

neighbors_amount < 2:

​	 current = 0

neighbors_amount > 3: 

​	current = 0

neighbors_amount == 2

​	pass



Dead cell

neighbors_amount == 3:

​	current = 1