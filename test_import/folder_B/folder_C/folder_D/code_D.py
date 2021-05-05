'''

this is two parents up (grandparent folder)

'''


# import modules
import os
import sys




# append system path so that module from parent directory can be imported
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir) # moves a second folder up
sys.path.append(parentdir)


print()
print('the system path:')
print(sys.path)


# import from sibling folder
import folder_A.code_A as aa

print(aa.p)

