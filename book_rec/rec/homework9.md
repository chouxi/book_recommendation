<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
##HW10A
###Section II
Yanhao Wang 175002614

Zheng Qi 174003950

Mohan Xiao 174005865

### 9.1

Assume that there are no more than n clauses and 2SAT can get a solution in T(n). If there is a 2SAT problem which has n + 1 clauses, the previous clause plus a clause which is $(a \bigcup b)$.

Then we start from a as false, this clause is true when b is true. So this clause is solved, remaining 2SAT problem has n cluases same as the assumption.

The remaing 2SAT with n clauses can be solved in T(n), and then combine with the previous a=false,b=true part. If the reaming clauses is not satisfied, the problem is not satisfied.

We expand the remaing 2SAT with n clauses like the first one, no matter it satisfied or not, it will stop or return in linear time. If it's not satisfied, we return to first and change a to true.

And repeated the process.

So the time is a = true plus expand all with  a = false plus expand all, which is O(n).

Obviously we can get a recursion function.

T(n) = O(n) + T(n-1) Which is in polynomial time.

### 9.2

(a).
A subproblem is a new instance of the Rudrata Path on a subgraph the origin graph,the starting point is one of the vertex v belongs V. This subproblem can help use to solve problem from each verteices. 

(b). 
Choose can be implement by picking the subproblem defined on the smaller graph. This is reasonable as smaller graphs will be evaluated faster. Moreover, this will reduce space complexity of the algorithm
as a single active path must be kept in the tree of possible Rudrata paths.

(c).
To expend a subproblem , we just difined as Rudrate Path starting at a subgraph of origiin graph and the divide it into subproblem $ P_1 $to $ P_n $, and the $ i_th $ iteration is the subgraph of origin graph

### 9.4 
First, choose an vertex $v\in |V|$, and add $v$ into set S. Then for all $e_{u,v}$, delete $u$. Repeate this process until $|V|$ is empty. Since each iteration, ($1+d$) vertices are deleted, thus $|S|\geq \frac{|V|} {(1+d)} \geq \frac{|Max Independent Set|} {(1+d)}$.

### 9.5
(a).
First, for any  $e_{u,v} \in T'$, if  $e_{u,v}$ is also in $T$, then no edge-swaps needed.
If $e_{u,v}\notin T $, then there must exist a path $p_{u,v} $from $u$ to $v$. Also, there must exist an edge e'. such that it is not in $T'$, because if there doesn't exist, $T$ will become a cycle. Thus we can swap e' with $e_{u,v}$. Taking the above approach, at most $|V|-1$ swaps, $T$ will become $T'$

(b). 
When swapping, choose edge-swap ($e,e'$) such that $w_e<w_{e'}$. Repeate this swapping, when there are no edge-swapping which  $w_e<w_{e'}$, then $T$ is the minimum spanning tree. If there exists such swap, we can perform another swap to make the total weight smaller, and then $T$ is not the minimum spanning tree. 

(c)
The idea is similar with previous question. Suppose the Minimum Spanning tree is $T'$. And if $T$ is not the minimum spanning tree, then there must exist an edge-swap ($e,e'$) such that $w_e<w_{e'}$. If not, then $T's $ total weight must be less or equal to $T'$ which is the minimum spanning tree. 
This process takes at most $|V|-1$ iterations. 