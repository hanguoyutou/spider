import sys

with open('code.txt', 'r') as f:
    sys.stdout = open('result.log','w')
    s = f.read()
    try:
        exec(s)
    except Exception as e:
        print(e)
