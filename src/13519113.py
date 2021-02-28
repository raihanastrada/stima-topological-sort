# Modul yang digunakan
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
        preq_node = [] # List kode matkul prerequisite
        char = f.read(1)
        while (char): # Selama bukan akhir file
            # Ambil kode matkul
            while(char != "," and char != "."):
                node += char
                char = f.read(1)
                # {EOP : char = "," or char = "." selesai mengambil kode matkul}

            if (char != "."): 
                # Jika terdapat matkul prerequisites, char = ","
                char = f.read(1)
                # Ambil kode matkul prerequisite
                while(char != "."):
                    if (char == ","):
                        preq_node.append(prerequisites)
                        prerequisites = ""
                        char = f.read(1)
                    else:
                        prerequisites += char
                        char = f.read(1)
                    # {EOP : char = "." selesai mengambil kode matkul prerequisites}
                preq_node.append(prerequisites)
                prerequisites = ""

            # Masukkan ke list graph
            graph_list.append([node,preq_node])
            node = ""
            preq_node = []
            
            # Ke next line
            char = f.read(1) 
            char = f.read(1) 
        # {EOP : not char, EOF}

    except:
        # Error message
        print("Tidak ditemukan file dengan nama tersebut\n")

    return graph_list

def find_zero_indegree(graph_list):
    # Mengembalikan list index matkul pada graph yang memiliki in-degree = 0
    zero_indegree = []
    for i in range(len(graph_list)):
        if (len(graph_list[i][1]) == 0):
            zero_indegree.append(i)
    return zero_indegree

def delete_node(idx_list,graph_list):
    for i in range(len(idx_list)):
        matkul = graph_list[idx_list[i]][0] # Mengambil kode matkul
        # Menghapus kode matkul pada setiap preq node pada graph_list
        neff = len(graph_list)
        j = 0
        while (j < neff):
            try:
                graph_list[j][1].remove(matkul)
                j += 1
            except:
                j += 1

    # Menghapus simpul pada graf
    while (len(idx_list) != 0):
        del graph_list[idx_list[0]]
        idx_list.pop(0)
        try:
            for i in range(len(idx_list)):
                idx_list[i] -= 1
        except:
            break

def topo_sort(graph_list,queue):
    idx_list = find_zero_indegree(graph_list) # Cari index matkul yang memiliki in-degree = 0
    for i in range(len(idx_list)):
        queue.append(graph_list[idx_list[i]][0]) # Masukkan matkul ke queue
    delete_node(idx_list,graph_list) # Proses mengurangi & mendelete node pada graf

def to_rome(number):
    # Mengembalikan angka romawi
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

def print_solusi(queue,sem):
    # Mencetak format solusi
    print("Semester",to_rome(sem),":",end="")
    for i in range(len(queue)):
        print(queue[i],end="")
        if (i != len(queue)-1):
            print(",",end="")
    
    while(len(queue) != 0):
        # Hapus elemen queue, karena sudah dicetak
        queue.pop(0)

# Main Program
if __name__ == "__main__":
    filename = str(input("Masukkan nama file: "))
    graph_list = get_files(filename)
    queue = [] # Matkul akan ditaruh di queue
    sem = 1
    while (len(graph_list) != 0):
        # Selama graf belum selesai diproses
        topo_sort(graph_list,queue)
        print_solusi(queue,sem)
        if(len(graph_list) != 0):
            print("")
        sem += 1
    # {EOP : len(graph_list) == 0, graf selesai diproses}
    print(".")