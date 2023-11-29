import nltk
import sys
import math
import pickle
from nltk import word_tokenize
from nltk.util import ngrams
from nltk import cluster
from collections import Counter
from statistics import mean
import networkx as nx
import sys
import csv

# def buildVector(iterable1, iterable2):
#     counter1 = Counter(iterable1)
#     counter2= Counter(iterable2)
#     all_items = set(counter1.keys()).union( set(counter2.keys()) )
#     vector1 = [counter1[k] for k in all_items]
#     vector2 = [counter2[k] for k in all_items]
#     return vector1, vector2
def cosine_similarity(l1, l2):

    vec1 = Counter(l1)
    vec2 = Counter(l2)
    
    # print(len(vec1))
    # print(len(vec2))  
    
    # print("Vec 1 : ", vec1)
    # print("Vec 2: ", vec2)

    intersection = set(vec1.keys()) & set(vec2.keys())
    
    # print(intersection)
    
    # for x in intersection:
    #     if(vec1[x] > 10):
    #         print(vec1[x].key())
    #         print(vec2[x].key())
    
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0

    return float(numerator) / denominator


# Could be changed to include rightmost minimum too
def get_min(get_key = lambda x: x):
    def rightmost_minimum(l):
        minimum = float('inf')
        minimum_index = -1
        pos = 0

        
        while(pos < len(l)):
            if (get_key(l[pos]) < minimum):
                minimum = get_key(l[pos])
                minimum_index = pos
            pos += 1
        
        return l[minimum_index]
    return rightmost_minimum

# Have used the inbuilt hash function (Should try a self defined rolling hash function)
def winnowing(kgrams, k, t):
    modified_min_func = get_min(lambda key_value: key_value[0])
    
    document_fingerprints = []
    
    # print(kgrams)
    hash_table = [ (hash(kgrams[i]) , i)  for i in range(len(kgrams)) ]
    # print(len(hash_table))
    
    window_length = t - k + 1
    window_begin = 0
    window_end = window_length
    
    minimum_hash = None

    while (window_end < len(hash_table)):
        window = hash_table[window_begin:window_end]
        window_minimum = modified_min_func(window)
        
        if(minimum_hash != window_minimum):
            # print(window_minimum)
            document_fingerprints.append(window_minimum[0]) #not taking positions into consideration
            minimum_hash = window_minimum

        window_begin = window_begin + 1
        window_end = window_end + 1

    return document_fingerprints

def generate_kgrams(data, k):
    for text in data :
        token = nltk.word_tokenize(text)
        kgrams = ngrams(token, k)
        lst_kgrams = list(kgrams)
        # print("Kgrams : ", lst_kgrams)
        return lst_kgrams


# only conversion to lowercase for now
def preprocess(document):
    preprocessed_document = []
    for item in document :
        item = item.lower()
        preprocessed_document.append(item) 
    return preprocessed_document

def generate_fingerprints(file_name, k, t) :
    data = []
    f = open(file_name)
    data.append(f.read())
    
    preprocessed_data = preprocess(data)
    kgrams = generate_kgrams(preprocessed_data, k)
    # print(len(kgrams))
    document_fingerprints = winnowing(kgrams, k, t)
    return document_fingerprints

# def prep(doc):
#     prep_doc = []
#     for ele in doc:
#         ele_list = []
#         for item in ele:
#             item = item.lower()
#             ele_list.append(item)
#         prep_doc.append(ele_list)
#     return prep_doc

# def convert(doc):
#     conv_doc = []
#     for ele in doc:
#         temp = []
#         for item in ele[1]:
#             temp.append(ele[0])
#             temp.append(item)
#         conv_doc.append(temp)
#     return conv_doc

# def gen_fp(data, k, t):
#     conv_data = convert(data)
#     prep_data = prep(conv_data)
#     kgrams = generate_kgrams(prep_data, k)
#     doc_fp = winnowing(kgrams, k, t)
#     return doc_fp

# p1l1 = pickle.load(open("program1_lev1_pc.pickle", "rb"))
# p1l2 = pickle.load(open("program1_lev2_pc.pickle", "rb"))
# p2l1 = pickle.load(open("program2_lev1_pc.pickle", "rb"))
# p2l2 = pickle.load(open("program2_lev2_pc.pickle", "rb"))

# fp11 = gen_fp(p1l1, 13, 17)
# fp12 = gen_fp(p1l2, 13, 17)
# fp21 = gen_fp(p2l1, 13, 17)
# fp22 = gen_fp(p2l2, 13, 17)

# cs1 = cosine_similarity(fp11, fp21)
# cs2 = cosine_similarity(fp12, fp22)
# tot = (0.6 * cs1) + (0.4 * cs2)
# print("Total: " + str(tot))

program1 = 'program1'
program2 = 'program2'

def final_cos_simi(program1,program2):
    lev0s = []
    lev1s = []
    lev2s = []
    final_cosine_similarity_levs = []

    for i in range(10):
        fingerprints1_0 = generate_fingerprints((program1+"_lev0.txt"), 13, 17)
        fingerprints2_0 = generate_fingerprints((program2+"_lev0.txt"), 13, 17)
        cosine_similarity_lev0 = cosine_similarity(fingerprints1_0, fingerprints2_0)
        lev0s.append(cosine_similarity_lev0)

        fingerprints1_1 = generate_fingerprints((program1+"_lev1.txt"), 13, 17)
        fingerprints2_1 = generate_fingerprints((program2+"_lev1.txt"), 13, 17)
        cosine_similarity_lev1 = cosine_similarity(fingerprints1_1, fingerprints2_1)
        lev1s.append(cosine_similarity_lev1)

        fingerprints1_2 = generate_fingerprints((program1+"_lev2.txt"), 13, 17)
        fingerprints2_2 = generate_fingerprints((program2+"_lev2.txt"), 13, 17)
        cosine_similarity_lev2 = cosine_similarity(fingerprints1_2, fingerprints2_2)
        lev2s.append(cosine_similarity_lev2)
    # print(len(fingerprints1_0))
    # print(len(fingerprints2_0))

    # print(len(fingerprints1_1))
    # print(len(fingerprints2_1))

    # print(len(fingerprints1_2))
    # print(len(fingerprints2_2))

    final_cosine_similarity_lev0 = round(mean(lev0s), 2)
    final_cosine_similarity_lev1 = round(mean(lev1s), 2)
    final_cosine_similarity_lev2 = round(mean(lev2s), 2)

    final_cosine_similarity_levs.append(final_cosine_similarity_lev0)
    final_cosine_similarity_levs.append(final_cosine_similarity_lev1)
    final_cosine_similarity_levs.append(final_cosine_similarity_lev2)

    return final_cosine_similarity_levs




    # f10,f20 = buildVector(fingerprints1_0, fingerprints2_0)
    # f11,f21 = buildVector(fingerprints1_1, fingerprints2_1)
    # f12,f22 = buildVector(fingerprints1_2, fingerprints2_2)

    # print("Cosine similarity Level 0 : \n", cluster.util.cosine_distance(f10,f20))
    # print("Cosine similarity Level 1 : \n", cluster.util.cosine_distance(f11,f21))
    # print("Cosine similarity Level 2 : \n", cluster.util.cosine_distance(f12,f22))

    # print("Cosine similarity Level 0 : \n", final_cosine_similarity_lev0)
    # print("Cosine similarity Level 1 : \n", final_cosine_similarity_lev1)
    # print("Cosine similarity Level 2 : \n", final_cosine_similarity_lev2)

def result_winnowing():
    row = []
    final_cosine_similarity_levs = final_cos_simi(program1,program2)

    a_file = open(program1+"_count.txt")
    b_file = open(program2+"_count.txt")
    count_values=[]
    for c in range(3):
        a = int(a_file.readline())
        b = int(b_file.readline())
        count_values.append([a,b])

    normalization_score = 0
    t=0
    for c in range(3):
        x=count_values[c][0]
        y=count_values[c][1]
        if(x + y)!=0:
            t=t+1
            if x>y:
                s = 1-((x-y)/(x+y))
            else:
                s = 1-((y-x)/(x+y))    
            normalization_score+=(10*s)

    if t!=0:
        normalization_score=normalization_score/(t*10)
        total_similarity_score_win = ((0.5*final_cosine_similarity_levs[0]) + (0.3*final_cosine_similarity_levs[1]) + (0.2*final_cosine_similarity_levs[2]))
        normalization_score = normalization_score
        # print("Winnowing similarity score : \n", total_similarity_score_win)
        # print("Normalization score : \n", normalization_score)
        final_score = (total_similarity_score_win*60)+(normalization_score*40)
        print("Similarity score = : \n", final_score)
    else:
        total_similarity_score_win = ((0.5*final_cosine_similarity_levs[0]) + (0.3*final_cosine_similarity_levs[1]) + (0.2*final_cosine_similarity_levs[2]))
        # print("Winnowing similarity score : \n", total_similarity_score_win)
        # print("Invalid norm: \n", )
        final_score = (total_similarity_score_win*100)
        print("Similarity score = : \n", final_score)


    program1_name = open("program1.txt", "r").readline()
    program2_name = open("program2.txt", "r").readline()
    row.extend([program1_name, program2_name[8:], total_similarity_score_win, final_score])
    return row

# result_winnowing()


# import subprocess
# import csv

# def result(file_path):
#     row = result_winnowing()
#     try:
#         subprocess.run(["flake8", file_path], check=True, capture_output=True)
#         print(f"No linting issues found in {file_path}")
#         issues = None
#     except subprocess.CalledProcessError as e:
#         print(f"Linting issues found in {file_path}. Return code: {e.returncode}")
#         print(e.stdout.decode("utf-8"))
#         issues = e.stdout.decode("utf-8")

#         score = grade_flake8(issues)
#         row.append(score)
#         write_csv('output.csv', row)


# def grade_flake8(issues):
#     if issues is None:
#         return 100  # Return a score of 100 if no issues

#     num_errors = issues.count('\n')  # Count the number of lines as each line represents an issue
#     max_score = 100
#     score = max(0, max_score - num_errors)
#     return score

# def write_csv(file, row):
#     with open("experiments_python-loops.csv", "a") as file:
#         csvwriter = csv.writer(file)
#         csvwriter.writerow(row)

# result()
# Cosine similarity seems to be highest for k = 11 and t = 15, should try others.

# filename1 = "pycallgraph1"
# filename2 = "pycallgraph2"

# G1 = nx.MultiDiGraph(nx.drawing.nx_pydot.read_dot(filename1))
# G2 = nx.MultiDiGraph(nx.drawing.nx_pydot.read_dot(filename2))

# # networkx
# ged = nx.graph_edit_distance(G1,G2)
# print("Computing Graph Edit Distance ...")
# print("Graph Edit Distance from Networkx : ", ged)

# sub_ged = 0.2 * ged

# if(sub_ged >= 0.25):
#     sub_ged = 0.25

# if(sub_ged > 0):
#     print("Final Score: ", round((0.8*total_similarity_score) - (0.2*sub_ged), 2))
# else:
#     print("Final Score: ", round(total_similarity_score, 2))