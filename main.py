def fake_bin(x):
    y = ""
    for i in range(len(x)):
        if int(x[i]) < 5:
            y += "0"
        else:
            y += "1"
    return y

if fake_bin("45385593107843568") == "01011110001100111":
    print(True)
