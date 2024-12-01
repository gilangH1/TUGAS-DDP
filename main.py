import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'luas persegi{sisi}*{sisi} = {luas}')
    print(f'keliling persegi adalah {keliling}')
    
def l_persegi_panjang (panjang,lebar):
    luas=panjang*lebar
    keliling=2*(panjang+lebar)
    print(f'luas persegi panjang{panjang}*{lebar}={luas}')
    print(f'keliling persegi panjang adalah{keliling}')
    
def l_segitiga(alas,tinggi,):
    luas =(alas*tinggi)/2
    print(f'luas segitiga{alas}*{tinggi}={luas}')
    
def l_lingkaran(jari):
    luas = 3.14 * (jari*jari)**2
    keliling = 3.14 * (jari*jari)*2
    print(f'luas lingkaran{jari}*{jari}={luas}')
    print(f'keliling lingkaran adalah {keliling}')
    
def l_layang_layang(panjang,lebar):
    luas = (panjang*lebar)/2
    keliling =2*(panjang+lebar)
    print(f'luas layang layang{panjang}*{lebar}=luas')
    print(f'keliling layang layang adalah{keliling}')
    