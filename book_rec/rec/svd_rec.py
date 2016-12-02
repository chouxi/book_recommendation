from numpy import *
from numpy import linalg as la
from heapq import nlargest
import orig_matrix

seterr(invalid='ignore')
REC_NUM = int(10)

def eclud_sim(inA,inB):
    return 1.0/(1.0 + la.norm(inA - inB))

def pears_sim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5+0.5*corrcoef(inA, inB, rowvar = 0)[0][1]

def cos_sim(inA,inB):
    num = float(inA.T*inB)
    denom = la.norm(inA)*la.norm(inB)
    if denom == 0: return 0
    return 0.5+0.5*(num/denom)
    
def svd_est(data, user, sim_func, item, decomp_mat):
    n = shape(data)[1]
    sim_total = 0.0; rate_total = 0.0
    for j in range(n):
        rating = data[user,j]
        if rating == 0 or j==item: continue
        similarity = sim_func(decomp_mat[item,:].T,\
                             decomp_mat[j,:].T)
        sim_total += similarity
        rate_total += similarity *rating 
    if sim_total == 0.0: return 0
    else: return rate_total/sim_total

def recommend(data, user, sim_func=pears_sim, est_func=svd_est):
    unrated_items = nonzero(data[user,:]==0)[0]
    U,Sigma,VT = la.svd(data)
    sig_compress = mat(eye(418)*Sigma[:418]) # power value more than 0.9
    decomp_mat = (data.T.dot(U[:,:418])).dot(sig_compress.I)
    #calculate the energy of the matrix
    #Sig2 = Sigma ** 2
    #sum_sig = sum(Sig2) * 0.9
    #print sum_sig
    #print sum(Sig2[:417])
    if len(unrated_items) == 0: return None
    item_scores = []
    for item in unrated_items:
        estimated_score = est_func(data, user, sim_func, item, decomp_mat)
        item_scores.append((item, estimated_score))
    return nlargest(REC_NUM, item_scores, key=lambda ele:ele[1])
