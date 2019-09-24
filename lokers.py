from collections import OrderedDict
input_loker = OrderedDict()
lokers = OrderedDict()

# fungsi untuk menambah jumlah loker
def init(values):
    for i in range(0,int(values)):
        result = 'loker'
        lokers[i+1] = result
    print ('Berhasil membuat loker dengan jumlah %s' % len(lokers))

# fungsi untuk menambah loker isi
def inputs(values):
    loker_tersedia = []
    terkecil = ""
    try:
        for k in lokers:
            if lokers[k] == "loker":
                loker_tersedia.append(k)
                if min(loker_tersedia) == k:
                    terkecil = k
        # print (min(lokers))
        tipe_identitas , no_identitas = values.split(" ")
        lokers[int(terkecil)] =  (tipe_identitas , no_identitas)
        # print(lokers)
        print ("Kartu identitas tersimpan di loker nomor"+" "+ str(terkecil))
    except:
        print ('Maaf loker sudah penuh')

# fungsi untuk menampilkan semua loker
def status():
    # print(lokers)
    print ("{:<8} {:<15} {:<10}".format('no loker','tipe identitas','no identitas'))
    for k in lokers :
        print ("{:<8} {:<15} {:<10}".format( str(k), lokers[k][0], lokers[k][1] ))

# fungsi untuk untuk mengosongkan loker
def leave(values):
    try:
        i = 0
        for key in lokers.keys():
            if i == int(values)-1:
                key_to_delete = key
            i = i + 1
        if key_to_delete in lokers:
            lokers[key_to_delete] = 'loker'
        # print(lokers)
        print("Loker nomor %s berhasil dikosongkan" % values)
    except:
        print("Loker nomor tidak ditemukan" )

# fungsi akan menampilkan nomor loker berdasar nomor identitas
def find(values):
    nomor_loker = []
    for k in lokers:
        if lokers[k][1] == values:
            nomor_loker.append(k)
    if len(nomor_loker) == 0:
        print ("Nomor identitas tidak ditemukan")
    else:
        print ("Kartu identitas tersebut berada di loker nomor %s " % nomor_loker)

# fungsi untuk mencari daftar nomor identitas sesuai tipe identitas yang dicari
def search(values):
    result=[]
    for k in lokers:
        if lokers[k][0] == values:
            result.append(lokers[k][1])

    if len(result) == 0:
        print ('Pencarian tidak ditemukan')
    else:
        print(*result, sep = ", ")

# fungsi untuk menampilkan menu
def show_menu(infunc=input):
    print ("[x] Exit")
    # print ("\n")
    # menu = infunc("PILIH MENU> ")
    # print ("\n")

    if "init" in menu:
        xdel , data = menu.split(' ',1)
        init(data)
    elif "input" in menu:
        xdel , data = menu.split(' ',1)
        inputs(data)
    elif "status" in menu:
        status()
    elif "leave" in menu:
        xdel , data = menu.split(' ',1)
        leave(data)
        xdel , data = menu.split(' ',1)
    elif "find" in menu:
        xdel , data = menu.split(' ',1)
        find(data)
    elif "search" in menu:
        xdel , data = menu.split(' ',1)
        search(data)
    elif menu == "x":
        exit()
    else:
        print ("Salah pilih!")

## TESTING LEWAT COMMAND LINE
if __name__ == "__main__":
    while(True):
        show_menu()

# TESTING OTOMATIS
show_menu(lambda prompt: "init 5")
show_menu(lambda prompt: "input SIM 12345")
show_menu(lambda prompt: "input KTP 34710")
show_menu(lambda prompt: "input KTP 35770")
show_menu(lambda prompt: "input KTP 24710")
show_menu(lambda prompt: "input SIM 98775")
show_menu(lambda prompt: "status")
show_menu(lambda prompt: "input SIM 87214")
show_menu(lambda prompt: "leave 3")
show_menu(lambda prompt: "input SIM 87214")
show_menu(lambda prompt: "find 34710")
show_menu(lambda prompt: "search SIM")
show_menu(lambda prompt: "find 99999")
