# python 3
import sys

def build_kmers(n, reads):
    return [read[i:i+n] for read in reads for i in range(len(read)-n+1)]

def is_eulerian(n, reads):
    kmers = set(build_kmers(n, reads))
    prefixes = {k[:-1] for k in kmers}
    suffixes = {k[1:] for k in kmers}
    return prefixes == suffixes

def main():
    reads = sys.stdin.read().strip().split()
    for length in range(len(reads[0]), 1, -1):
        if is_eulerian(length, reads):
            print(length)
            break

if __name__ == '__main__':
    main()