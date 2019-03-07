DNA = 'GATGGAACTTGACTACGTAAATT'
ans = list(DNA)
answer = []
for i in ans:
    if ord(i) == 65:
        answer.append('A')
    elif ord(i) == 67:
        answer.append('C')
    elif ord(i) == 71:
        answer.append('G')
    elif ord(i) == 84:
        answer.append('U')
actual = ''.join(answer)
print(actual)