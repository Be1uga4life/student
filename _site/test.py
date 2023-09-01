from tabulate import tabulate
import os

something=[]
final=[]
dir = '/home/eroxyi/vscode/student/templates/tickets'
for f in os.listdir(dir):
	something.append(f)

final.append(something)
final=print(tabulate(final, tablefmt='html'))

print(final)
