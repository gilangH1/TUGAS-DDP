def celcius_ke_fahrenheit(celcius):
    print(celcius*9/5+32)
celcius_ke_fahrenheit(0)


print('\n-----mencari bilangan genap-----')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('\n-----keterangan lulus dan tidak lulus-----')
# rata" nilai lulus 80
def skor(nilai):
    if nilai >= 80:
        print('lulus')
    else:
        print('tidak lulus')
        
skor(40)
skor(80)

print('\n-----mencatak bilngan gajil-----')
def bilangan_ganjil(ganjil):
    for i in range(1,ganjil+1,2):
        print(i,end='')
bilangan_ganjil(20)