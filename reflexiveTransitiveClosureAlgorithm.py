import itertools
def createSet(sampleSet):
    newSet = set()
    for i in sampleSet:
        newSet.add(i)
    return newSet
def make_it_reflexive(alphabet,relation):
    newSet = createSet(relation)
    for i in alphabet:
        newSet.add((i,i))
    return newSet
def findAllTuplesOfIndex(index, alphabet):
    tupleOfIndex = set()
    for element in itertools.product(alphabet, repeat=index):
        tupleOfIndex.add(element)
    return list(tupleOfIndex)

def algorithm1(alphabet,relation):
    reflexive_closure = set()
    alphabet = list(alphabet)
    for index in range(len(alphabet)):
        tupleLength = index+1
        for tuple in findAllTuplesOfIndex(tupleLength, alphabet):
            if tupleLength == 1:
                reflexive_closure.add((tuple[0], tuple[0]))
            elif tupleLength == 2:
                if (tuple[0], tuple[1]) in relation:
                    reflexive_closure.add((tuple[0], tuple[1]))
            else:
                indexOfTraversing = 0
                done = False
                # traversing tuple with double indexing
                while indexOfTraversing+1 != tupleLength:
                    if (tuple[indexOfTraversing], tuple[indexOfTraversing+1]) in reflexive_closure:

                        # we cannot create a tuple with last index and null(lastIndex,null)
                        if indexOfTraversing+1 == tupleLength - 1:
                            done = True
                            break
                        indexOfTraversing += 1
                    # it breaks the path
                    else:
                        break
                if done:
                    reflexive_closure.add((tuple[0], tuple[tupleLength - 1]))

    return reflexive_closure



def algorithm2(alphabet,relation):
    newSet = make_it_reflexive(alphabet,relation)
    list_alphabet = sorted(list(alphabet))
    i,j,k = 0,0,0
    while(i < len(list_alphabet)):
        j = 0
        while (j < len(list_alphabet)):
            k = 0
            while (k < len(list_alphabet)):
                if ((list_alphabet[i],list_alphabet[j]) in newSet
                        and (list_alphabet[j],list_alphabet[k]) in newSet
                        and (list_alphabet[i],list_alphabet[k]) not in newSet ):
                    newSet.add((list_alphabet[i], list_alphabet[k]))
                    i,j,k= 0,0,0
                else: k+=1
            j+=1
        i+=1
    return newSet



def algorithm3(alphabet,relation):
    newSet = make_it_reflexive(alphabet,relation)
    for j in alphabet:
        for i in alphabet:
            for k in alphabet:
                if((i,j) in newSet and (j,k) in newSet and (i,k) not in newSet):
                    newSet.add((i,k))
    return newSet



def getAlphabeth():
    givenInput = input("Please enter member of alphabets with commas, (For example: 1,2,3,4,5)  :")
    return set(givenInput.split(","))

def getSample():
    relation = input("Please enter relations with a space (For example: 1,2 2,3 3,5)  :")
    relationList = relation.split(" ")
    relations = set()
    for i in relationList:
        relations.add(tuple(i.split(",")))
    return set(relations)


def main():
    print("Welcome to Reflexive Closure Algorithm Program")
    alphabet = getAlphabeth()
    sample = getSample()

    print("Result for first algorithm is: ")
    print(sorted(list(algorithm1(alphabet,sample))))
    print("Result for second algorithm is: ")
    print(sorted(list(algorithm2(alphabet,sample))))
    print("Result for third algorithm is: ")
    print(sorted(list(algorithm3(alphabet,sample))))

main()