
def who_wins(q):
    organs = ["pancreas", "brain", "skin", "stomach", "heart", "lungs"]
    if q in organs:
        return "correct"
    else:
        return "wrong"
    
time = input("name an organ:\n")
print(who_wins(time))