import random
import textwrap


def word_preprocess(item,line_index):
    if len(item) <= 1:
        raise Exception("Invalid word item: {} @ line {}".format(item,line_index))
    item_clean = [i for i in item if i != ""] if len(item) > 2 else item
    if len(item_clean) > 2:
        raise Exception("Invalid word item: {}".format(item_clean))
    
    try:
    	item_clean[-1] = int(item_clean[-1])
    except:
    	print(item_clean)
    
    if not isinstance(item_clean[-1],int):
        raise Exception(f"invalid format found in {line_index} line")

    return item_clean


def read_data(path):
    freader = open(path, "r")
    words_collection = list()
    for line_index,line in enumerate(freader):
        item = line.strip().split("---")
        
        item_clean = word_preprocess(item,line_index)
        words_collection.append(item_clean)

    freader.close()
    return sorted(words_collection, key=lambda x: x[1])


def bs_find_index(array,value):
    length = len(array)
    start = 0
    end = length - 1
    while (end-start)>1:
        mid = start + (end - start)//2
        if array[mid][1] > value:
            end = mid
        else:
            start = mid
    return start


def execute_learning(words_collection,end_point):
    ifcont = "Y"
    reviewed = set()
    delted = set()
    while ifcont in ['Y', 'y', "", "yes"]:
        curr_index = random.randint(0,end_index)
        if curr_index not in reviewed:
            print (curr_index)
            print (textwrap.fill(words_collection[curr_index][0]))
            words_collection[curr_index][1] += 1
            reviewed.add(curr_index)
            ifdelete = input("If Delete:")
            if ifdelete in ['Y', 'y', 'yes']:
            	_ = words_collection.pop(curr_index)
            ifcont = input("If Continue?")
        else:
            continue
    print("Total sentences reviewed today is {}".format(len(reviewed)))

    return words_collection


if __name__ == "__main__":
    file_path = "./words_collection.txt"
    words_collection = read_data(file_path)
    count_treshold = int(input("Less than?"))
    end_index = bs_find_index(words_collection, count_treshold)
    words_collection = execute_learning(words_collection, end_index)

    fwrite = open(file_path, "w")
    for item in words_collection:
        fwrite.write("---".join([str(i) for i in item]) + "\n")
    fwrite.close()
