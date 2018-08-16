#!/usr/bin/env python3


from math import *

samples = 1024

beta = pi * 0.3 * sqrt(2 / log(2))

def erfint(normalised_time): # normalised time goes from 0 to 1 to represent 0 to T_b
    erfi = normalised_time * erf(beta * normalised_time) + (1 / ( beta *sqrt(pi))) * exp(-((beta*normalised_time)**2))
    return erfi


def traj_one(t):
    return 0.5 * pi * (erfint(t-1) -1)

def traj_two(t):
    return 0.5 * pi * (erfint(t) - erfint(0.0) - erfint(t-1) + 1 - t)

def traj_three(t):
    return 0.5 * pi * (erfint(t) - erfint(0.0))

def traj_seven(t):
    return 0.5 * pi * t


ph_1 = open("phase_1.txt",'w')
ph_2 = open("phase_2.txt",'w')
ph_3 = open("phase_3.txt",'w')
ph_7 = open("phase_7.txt",'w')




def fixup_phase_one(t):
    return (-traj_one(t))

def fixup_phase_two(t):
    return traj_two(t) + 2 * (sqrt(log(2)/(2*pi))/(4*0.3))

def fixup_phase_three(t):
    return traj_three(t) + 2 * (sqrt(log(2)/(2*pi))/(4*0.3))

def fixup_phase_seven(t):
    return traj_seven(t)


#### MASTER CURVES ####

def master_curve_one(t):
    return sin(fixup_phase_one(t))

def master_curve_two(t):
    return sin(fixup_phase_two(t))

def master_curve_three(t):
    return sin(fixup_phase_three(t))

def master_curve_seven(t):
    return sin(fixup_phase_seven(t))



for i in range(0,samples+1):  # from zero (inclusive) to 64 (EXCLUSIVE)
    time = i/samples        # time from 0 to 1 (to represent real time 0 to T_b)
    print (time, master_curve_one(time), file=ph_1)
    print (time, master_curve_two(time), file=ph_2)
    print (time, master_curve_three(time), file=ph_3)
    print (time, master_curve_seven(time), file=ph_7)

    

