# prints biggest in each cluster from blastclust output

import sys, getopt

def read_fasta(source_file):
    f = open(source_file, "r")
    d = {}
    key = ""
    for line in f:
        s = line.strip()
        if s[0:1] == '>':
            key = s.replace('>', '')
            d[key] = ''
        else:
            d[key] += s
    return d

def print_biggest_from_clusters(clust_file, d):
    f = open(clust_file, "r")

    for line in f:
        prot_ids = line.replace('\n', '').split(' ')

        max_len = 0

        found = False
        for prot_id in prot_ids:
            if prot_id in d.keys():
                cur_prot = d[prot_id]
                if max_len < len(cur_prot):
                    max_len = len(cur_prot)
                    res_prot_id = prot_id
                    found = True

        if found:
            print('>' + res_prot_id)
            print(d[res_prot_id])


source_file = ''
clust_result_file = ''


try:
    opts, args = getopt.getopt(sys.argv[1:], "f:c:")
except getopt.GetoptError:
    exit(2)

if len(opts) < 2:
    print('clust_to_exo.py -f <from_clust> -c <clust_result>')
    exit(1)

for opt, arg in opts:
    if opt == '-h':
        print('clust_to_exo.py -f <from_clust> -c <clust_result>')
        sys.exit()
    elif opt in "-f":
        source_file = arg
    elif opt in "-c":
        clust_result_file = arg

d = read_fasta(source_file)
print_biggest_from_clusters(clust_result_file, d)