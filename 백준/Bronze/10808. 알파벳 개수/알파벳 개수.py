import sys

input = sys.stdin.readline
al_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'w', 'x', 'y', 'z']
word = list(input())

for i in range(len(al_list)):
    print(word.count(al_list[i]),end=" ")