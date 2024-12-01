import math

def l_kubus(sisi):
    luas = sisi*sisi*sisi*sisi*sisi*sisi
    print(f'luas kubus{sisi}*{sisi} {sisi}*{sisi}*{sisi}*{sisi}= {luas}')
    
def l_balok(panjang,lebar,tinggi):
    luas = 2 * panjang * lebar + panjang * tinggi + lebar * tinggi
    keliling=2*(panjang+lebar)
    print(f'luas persegi panjang 2*{panjang*lebar}+{panjang*tinggi}{lebar*tinggi}={luas}')
    
def l_limas(alas,jumlah_sisi_tegak):
    luas =(alas+jumlah_sisi_tegak)
    print(f'luas alas{alas}+{jumlah_sisi_tegak}={luas}')
    
def l_kerucut(alas,selimut):
    luas = alas + selimut
    print(f'luas kerucut{alas}+{selimut}={luas}')
    
def l_tabung(jari,tingi):
    luas_permukaaan= 3.14*jari*jari + 2*3.14*jari*tingi
    print(f'luas permukaan tabung 3.14*{jari*jari} + 2*3.13{jari*tingi}={luas_permukaaan}')