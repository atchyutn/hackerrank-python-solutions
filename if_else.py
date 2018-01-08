'''
Solution for If-else statement in python 3
'''

if __name__ == '__main__':
    n = int(input())
    
    if (n%2 != 0) or n in range(6,21):
      print("Weird")
    else:
      print("Not Weird")

