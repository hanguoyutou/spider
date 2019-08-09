
with open('result.log','r') as f:
    answer = f.read()
    exp = "a\nb\nc\nd\ne\n"
    print(answer)
    print(exp)
    if answer == exp:
        print(100)
    else:
        print(0)