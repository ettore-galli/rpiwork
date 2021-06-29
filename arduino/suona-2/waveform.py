import math

N=128
M=256
wave = [int(N + N*math.sin(2*math.pi*i/M)) for i in range(M)]
print(wave)

#pulses = [1 if i <= value else 0 for value in wave for i in range(2*N)]
#print(pulses)
#print(len(pulses))