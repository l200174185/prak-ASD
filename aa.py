a = [10,51,2,18,4,31,13,5,23,64,29]
#swap
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


#cariposisiyangterkecil
def cariPosisiYangTerkecil(A,n,k):
    po = n
    for i in range(n+1, k):
        if A[i] < A[po]:
            po = i
    return po

def bubbleSort2(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)




##bubble sort
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j].nim > A[j+1].nim:
                swap(A,j,j+1)
    for k in A:
        print("Urutan nim dengan cara bubble "+ str(k.nim))

#selectionSort(A)
def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        inde = cariPosisiYangTerkecil(A,i,n)
        if inde != i:
            swap(A,i,inde)

#insertion Sort
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1] :##--> cari posisi yang tepat
            A[pos] = A[pos-1] # --> dan geser ke kanan terus
            pos = pos - 1 # nilai nilai yang lebih besar
        A[pos] = nilai # --> Pada posisi ini temptkan nilai element ke i

#soal mahasiswa
class MhsTIF(object):    
    def __init__(self, nama, nim, kota,us):
            self.nama = nama
            self.nim = nim
            self.kotaTinggal=kota
            self.uangSaku=us
    def __str__(self):
            s = self.nama + ',NIM '+ str(self.nim) \
                + '. Tinggal di ' + self.kotaTinggal \
                + '. Uang saku Rp ' + str(self.uangSaku) \
                + ' tiap bulannya.'
            
c1 = MhsTIF("Kukuh",26,"Pati",286000)
c2 = MhsTIF("Pratama",29,"Magelang",652000)
c3 = MhsTIF("Putri",77,"Wonosobo",124000)
c4 = MhsTIF("Ayuk",31,"Blora",441000)
c5 = MhsTIF("Onican",12,"Rembang",299000)
c6 = MhsTIF("Shifa",63,"Banjarmasin",357000)
c7 = MhsTIF("Yusuf",55,"Makassar",314000)

ar = [c1,c2,c3,c4,c5,c6,c7]


ar1 = [12,4,1,3,9,34,32,11,14]
ar2 = [15,23,12,16,25,28,30,34]
c = ar1+ar2
