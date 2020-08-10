#!/usr/bin/env python
# coding: utf-8

# ### Rock Paper Scissors Game

# In[6]:


import random, sys

print('ROCK, PAPER, SCISSORS')

w = 0

t = 0

l = 0

print(f'{w} Wins, {t} Ties, {l} Losses')
      
print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')

move = input()
      
while True:
    
    if move == 'r':
        player = 'Rock'
        
    elif move == 'p':
        player = 'Paper'
        
    elif move == 's':
        player = 'Scissors'
        
    elif move == 'q':
        sys.exit()
    
    options = ['Rock', 'Paper', 'Scissors']
    selection = random.choice(options)
    
    if player == 'Rock' and selection == 'Paper':
        print(f'{player} versus...')
        print(selection)
        print('You lose!')
        l = l+1
        
    elif player == 'Scissors' and selection == 'Rock':
        print(f'{player} versus...')
        print(selection)
        print('You lose!')
        l = l+1
        
    elif player == 'Paper' and selection == 'Scissors':
        print(f'{player} versus...')
        print(selection)
        print('You lose!')
        l = l+1
    
    elif player == 'Rock' and selection == 'Scissors':
        print(f'{player} versus...')
        print(selection)
        print('You Win!')
        w = w+1
        
    elif player == 'Paper' and selection == 'Rock':
        print(f'{player} versus...')
        print(selection)
        print('You Win!')
        w = w+1
    
    elif player == 'Scissors' and selection == 'Paper':
        print(f'{player} versus...')
        print(selection)
        print('You Win!')
        w = w+1
    
    elif player == selection:
        print(f'{player} versus...')
        print(selection)
        print('It\'s a tie!')
        t = t+1
        
    print(f'{w} Wins, {t} Ties, {l} Losses')
    
    move = input()


# In[ ]:




