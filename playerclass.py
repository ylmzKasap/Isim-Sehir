import os

oyunKategorileri = ['İsim', 'Şehir', 'Hayvan']
kategoriNumaralari = {kategori: index for index, kategori in enumerate(oyunKategorileri)}
oyuncular = ['Mahmut', 'Nisa', 'Memin']
MahmutCevap = ['Yılmaz', 'Adana', 'At']


class yarismaci:
    def __init__(self, name, kategoriListesi):
        self.name = name
        self.puan = 0
        self.kategoriler = kategoriListesi
        self.tablo = [[kategori] for kategori in kategoriListesi]


    def cevapla(self, kategori, cevap):
        indexNumber = 1
        while True:
            try:
                getattr(self, f'{kategori}_{indexNumber}')
                indexNumber += 1
            except AttributeError:
                break
        setattr(self, f'{kategori}_{indexNumber}', cevap)
        self.tablo[kategoriNumaralari[kategori]].append(cevap)


    def puanVer(self, kategori, cevap, puan):
        setattr(self, f'{kategori}_{cevap}', puan)


nesne = {}
for oyuncu in oyuncular:
    nesne[oyuncu] = yarismaci(oyuncu, oyunKategorileri)

nesne['Nisa'].cevapla('Hayvan', 'Eşek')
nesne['Nisa'].cevapla('Hayvan', 'Dana')
nesne['Nisa'].cevapla('Hayvan', 'Öküz')
print(nesne['Nisa'].tablo)

"""
for kategori in kategoriler:
    for name in oyuncular:
        print(f'\n{name.title()} {kategori.lower()} için ne diyor?')
"""
