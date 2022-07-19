from audioop import avg


score = {
'python': 80,
'django': 89,
'web': 83,
}
 
#1
score['algorithm'] = 90 

#2
score.update({'python' : 85})

#3
value = score.values()
print(sum(value)/len(value))