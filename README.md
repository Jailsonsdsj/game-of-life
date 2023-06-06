# The game of life

Proposal for project of the discipline Programming II. The project consists in recreate the game of life, created by mathematical Jhwon Horton Conway in 1970. 

According to wikipedia, the game can be described as:

> "a cellular automaton [...]. It is a zero-player game, 2 meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine."



## Rules

* Any living cell with less than two neighboring living cells dies, due to low population;
* Any living cell with more than three neighboring living cells dies, due to high population;
* Any living cell with two or three living cells next door remains alive for the next generation;
* Any dead cell with exactly three neighboring living cells turns into a living cell;

You will also have to think about:

- How to represent the Game area in an easy way to test;
- What 'value' will cells outside the Game area have. Or will the Game have no area limit?



## How to run

Just download the main.py file and execute in you personal computer (you need python 3 installed)



## Methods

Creating a board and passing the number of generation

```python
game = board(25)
```

Defining the initial cells

```
data = "c1, d2, b3, c3, d3"
```

Input data into board

```
game.input(data)
```

Start simulator

```
game.start()
```





 

