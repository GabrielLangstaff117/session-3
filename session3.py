
numa = (int(input("number")))
numb = (int(input("number")))
numc = (int(input("number")))

def fractional (numa,numb):
    return numa/numb  -  numa//numb

def if_even (num):
   return (num // 2) == 0

def largest_first (numa, numb, numc):
    return numa> numb and numb > numc

def add_multiply (numa, numb, numc):
    return (numa + numb) * numc

def concat(numa, numb, numc):
    return  int(str(numa) + str(numb) + str(numc))

def flip(numa, pos):
    return numa ^ (1 << pos)

def age(iamx, numa):
    age = int(iamx[5:7]) + numa
    return str(age)

