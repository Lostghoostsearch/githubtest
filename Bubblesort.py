def bubble_sort(sequence):
    for i in range(0,len(sequence)):
        PA = 0
        PB = 1
        while PB<=len(sequence)-1:
            if sequence[PA]>sequence[PB]:
                HE = sequence[PA]
                LE = sequence[PB]
            elif sequence[PA]<sequence[PB]:
                HE= sequence[PB]
                LE = sequence[PA]
            elif sequence[PA]==sequence[PB]:
                HE=sequence[PA]
                LE = HE
            sequence[PA]=LE
            sequence[PB]=HE
            PA =PB
            PB =PB+1
    return sequence

ll = [4,1,3,9,20,21,6,21,14,25]

sort = bubble_sort(ll)
print(sort)
        
