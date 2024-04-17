def main():
    string = (input())
    condition = verification_string(string, 0)
    if condition:
        print('SI', end='')
    else:
        print('NO', end='')
def verification_string(string, i):
    if i >= len(string):
        return True
    if string[0].isdigit(): 
        return False
    if string[i] == ' ' or (string[i] != '_' and not(string[i].isalnum())):
        return False
    return verification_string(string, i+1)   
main()