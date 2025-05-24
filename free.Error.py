# python3
class GenomeAssembler:
    STR_LEN = 100

    def __init__(self, dataset):
        self.dataset = dataset
        self.n = len(self.dataset)

    def solve(self):
        next_s = [(0, None) for _ in range(self.n)]
        for i in range(self.n - 1):
            s1 = self.dataset[i]
            for j in range(i + 1, self.n):
                s2 = self.dataset[j]
                size_i, _ = next_s[i]
                size_j, _ = next_s[j]
                size_i = self.fbs(s1, s2, size_i)
                size_j = self.fbs(s2, s1, size_j)
                if size_i is not None:
                    next_s[i] = (size_i, j)
                if size_j is not None:
                    next_s[j] = (size_j, i)
        str_parts = [self.dataset[0]]
        ov_size, cur = next_s[0]
        while cur != 0:
            str_parts.append(self.dataset[cur][ov_size:])
            ov_size, cur = next_s[cur]
        s = "".join(str_parts)
        s = s[:-ov_size]
        return s

    @staticmethod
    def fbs(s1, s2, prev_ov):
        res = None
        for ov_size in range(GenomeAssembler.STR_LEN - 1, prev_ov, -1):
            if s2.startswith(s1[-ov_size:]):
                res = ov_size
                break
        return res

def run_test():
    dataset = [
        "gagtt", 
        "gtttt",  
        "tttat",  
        "tatcg",  
        "tcgct",  
        "gcttc",  
        "ttcca",  
        "agttt",  
        "cagag",  
    ]
    t = GenomeAssembler(dataset)
    result = t.solve()
    print(result)

def run_main():
    n_rows = 1618
    dataset = [input().strip()]
    for _ in range(n_rows - 1):
        s = input().strip()
        if s != dataset[-1]:
            dataset.append(s)
    t = GenomeAssembler(dataset)
    result = t.solve()
    print(result)

if __name__ == "__main__":
    run_main()