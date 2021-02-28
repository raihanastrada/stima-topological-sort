import os

def get_files(filename):
    # Membaca file dan mengembalikan list graph
    cur_path = os.path.dirname(__file__)
    fpath = os.path.join(cur_path, '..\\test\\'+filename)
    graph_list = []
    try:
        f = open(fpath, "r")
        node = "" # Kode matkul
        prerequisites = "" # Kode matkul prerequisite
        adjacent_node = [] # List kode matkul prerequisite
        char = f.read(1)
        while (char):
            # Ambil kode matkul
            while(char != "," and char != "."):
                node += char
                char = f.read(1)
                # {EOP : char = "," or char = "." selesai mengambil kode matkul}

            if (char != "."): # Jika terdapat matkul prerequisites, char = ","
                char = f.read(1)
                # Ambil kode matkul prerequisite
                while(char != "."):
                    if (char == ","):
                        adjacent_node.append(prerequisites)
                        prerequisites = ""
                        char = f.read(1)
                    else:
                        prerequisites += char
                        char = f.read(1)
                    # {EOP : char = "." selesai mengambil kode matkul prerequisites}
                adjacent_node.append(prerequisites)
                prerequisites = ""

            # Masukkan ke list graph
            graph_list.append([node,adjacent_node])
            node = ""
            adjacent_node = []
            
            # Ke next line
            char = f.read(1) 
            char = f.read(1) 
        # {EOP : not char, EOF}

    except:
        # Error message
        print("Tidak ditemukan file dengan nama tersebut\n")

    return graph_list

def find_zero_indegree(graph_list):
    # Mengembalikan index matkul pada graph yang memiliki in-degree = 0
    for i in range(len(graph_list)):
        if (len(graph_list[i][1]) == 0):
            return i

def delete_node(idx,graph_list):
    matkul = graph_list[idx][0]
    # Menghapus kode matkul pada setiap adjacent node pada graph_list
    neff = len(graph_list)
    i = 0
    while (i < neff):
        try:
            graph_list[i][1].remove(matkul)
            i += 1
        except:
            i += 1

    # Menghapus simpul pada graph_list[idx]
    del graph_list[idx]


def topo_sort(graph_list, queue):
    idx = find_zero_indegree(graph_list) # Cari index matkul yang memiliki in-degree = 0
    queue.append(graph_list[idx][0]) # Masukkan matkul ke prioQueue
    delete_node(idx,graph_list) # Proses pada graf

def to_rome(number):
    switcher = {
        1: "I    ",
        2: "II   ",
        3: "III  ",
        4: "IV   ",
        5: "V    ",
        6: "VI   ",
        7: "VII  ",
        8: "VIII ",
    }
    return switcher.get(number,"nothing")

def print_solusi(queue):
    # Menampilkan hasil topo sort dengan format dibagi per semester
    n = len(queue) // 8 # dibagi 8 semester
    if(n == 0): 
        # Jika matkul kurang dari 8
        for i in range(len(queue)):
            print("Semester",to_rome(i+1),":",end="")
            print(queue[i],end="")
            if (i != len(queue)-1):
                print("")

    else:
        idx = 0 # Index queue yang akan diprint
        remain = len(queue)%8 # Sisa matkul, jumlah matkul tidak dapat dibagi rata
        for i in range(1,9):
            print("Semester",to_rome(i),":",end="")
            for j in range(idx,idx+n):
                print(queue[j],end="")
                if(j != idx+n-1):
                    print(",",end="")

            idx += n
            if(remain != 0):
                # Jika terdapat sisa
                print(","+str(queue[idx]),end="") # Tambah 1 matkul pada semester
                remain -= 1 # Sisa dikurangi
                idx += 1
            if (i != 8):
                print("")
    print(".")

# Main Program
if __name__ == "__main__":
    filename = str(input("Masukkan nama file: "))
    graph_list = get_files(filename)
    queue = [] # Hasil topo sort akan ditaruh di queue
    while (len(graph_list) != 0):
        # Selama graf belum selesai diproses
        topo_sort(graph_list, queue)
    # {EOP : len(graph_list) == 0, graf selesai diproses}
    print_solusi(queue)