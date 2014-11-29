#! /usr/bin/env python3

import sys

sys.stdout = open('/Users/Gray/Desktop/muha.txt', 'w')

def read_fasta(file_path):
    with open(file_path) as inp:
        reads = []
        for line in inp:
            if line.startswith('>'):
                reads.append([[],[]])
                reads[-1][0].append(line.rstrip())
            elif not line.startswith('#'):
                reads[-1][1].append(line.rstrip())
    return tuple(((read[0][0], ''.join(read[1])) for read in reads))


seqs = read_fasta('/Users/Gray/Downloads/attemp3/second3/db_sorted.fasta')


clusters = {}

with open('/Users/Gray/Downloads/attemp3/second3/clusters.dmp') as inp:
    for line in inp:
        if line.startswith('#'):
            continue 
        seq_no, cluster = map(int, line.rstrip().split())
        if cluster not in clusters:
            clusters[cluster] = [seqs[seq_no - 1][0]]
        else:
            clusters[cluster].append(seqs[seq_no - 1][0])

#for cluster in clusters:
#    print(cluster)
#    print(clusters[cluster])

taxa = ['a_gambiae', 'c_quinquefasciatus', 'd_melanogaster', 'd_yakuba', 'd_erecta']

print('Description\tID\ta_gambiae\tc_quinquefasciatus\td_melanogaster\td_yakuba\td_erecta')

for cluster in clusters:
    temp = []
    for taxon in taxa:
        n = 0
        for component in clusters[cluster]:
            if component.endswith(taxon):
                n += 1
        temp.append(n)
#    if temp.count(0) < 4:
    if all(temp):
        print(seqs[cluster - 1][0], end='\t')
        print(cluster, end='\t')
        print('\t'.join(map(str, temp)))