"""GATE DA Artificial Intelligence item bank (search, logic, uncertainty only)."""
from helpers import mcq, msq, nat, uniq


def items():
    o = []
    o.append(mcq(
        'UninformedSearch',
        'Which of the following is an uninformed search strategy (no goal heuristic h(n))?',
        'A* with a consistent heuristic',
        'Greedy best-first using straight-line distance',
        'Breadth-first search',
        'Hill climbing on an evaluation function',
        'C',
        'BFS uses only the graph structure; it does not consult h(n).',
        marks=1, diff='E'))
    o.append(msq(
        'UninformedSearch',
        'Which of these search algorithms are uninformed?',
        'Breadth-first search',
        'Depth-first search',
        'Uniform-cost search',
        'A* search',
        'A;B;C',
        'A* is informed. UCS uses path cost g(n) but not a goal heuristic.',
        marks=2, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'On a tree with unit step costs, BFS is optimal because',
        'it expands by depth, so the first goal found is a shallowest and hence cheapest goal',
        'it expands the highest-h node first',
        'it is identical to DFS',
        'it requires an admissible heuristic',
        'A',
        'Unit costs make shallowest equivalent to cheapest.',
        marks=1, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'DFS as graph-search with a closed set on a finite graph is',
        'complete on that finite graph but not cost-optimal in general',
        'optimal for any positive costs',
        'incomplete even with a closed set on a finite graph',
        'identical to uniform-cost search',
        'A',
        'Closed-set DFS cannot loop forever on a finite graph; it need not find a cheapest path.',
        marks=2, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'Uniform-cost search expands nodes in order of increasing',
        'heuristic h(n)',
        'path cost g(n)',
        'depth only, ignoring action costs',
        'f=g+h with a nonzero h',
        'B',
        'UCS is Dijkstra on the implicit state graph.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'Iterative-deepening search (IDS) is designed to combine',
        'the memory of DFS with the completeness of BFS on trees',
        'A* optimality with greedy memory',
        'minimax with UCS',
        'alpha-beta with variable elimination',
        'A',
        'IDS reruns DFS with a rising depth bound.',
        marks=1, diff='M'))
    o.append(nat(
        'UninformedSearch',
        'A full binary tree, root at depth 0, a unique goal at depth 3. Number of nodes at depths 0 through 3 is ____.',
        '15',
        '1+2+4+8=15.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'Road map: S-A cost 1, S-B cost 4, A-G cost 5, B-G cost 1. Uniform-cost search from S to G returns a path of cost',
        '6 via A',
        '5 via B',
        '1',
        '9',
        'B',
        'S-B-G costs 5, S-A-G costs 6. UCS returns the cheaper path S-B-G.',
        marks=2, diff='M'))
    o.append(nat(
        'UninformedSearch',
        'Same map S-A=1, S-B=4, A-G=5, B-G=1. The cheapest S-to-G cost is ____.',
        '5',
        'S-B-G = 5.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'BFS versus DFS on a complete binary tree of depth 12 looking for a shallow goal at depth 2: BFS will typically',
        'find it after exploring only a small prefix of the tree, while DFS may dive to depth 12 first',
        'use less memory than DFS on that tree',
        'be identical to IDS at every step',
        'require an admissible heuristic',
        'A',
        'BFS explores level by level; DFS can go deep down the leftmost branch.',
        marks=2, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'Depth-limited search with limit L is incomplete if',
        'every goal lies at depth greater than L',
        'the branching factor is 2',
        'step costs are 1',
        'the graph is a tree',
        'A',
        'Goals beyond L are invisible to DLS.',
        marks=1, diff='E'))
    o.append(nat(
        'UninformedSearch',
        'IDS with successive limits 0,1,2,3 on a binary tree. Number of distinct depth-limit runs is ____.',
        '4',
        'Limits 0 through 3: four runs.',
        marks=1, diff='E'))
    o.append(msq(
        'UninformedSearch',
        'Which statements about uniform-cost search are TRUE?',
        'With nonnegative costs, the first time a node is expanded it has an optimal g-value (graph-search)',
        'UCS with all costs equal to 1 behaves like BFS (up to tie-breaking)',
        'UCS is informed because it uses g(n)',
        'Negative action costs can break UCS optimality',
        'A;B;D',
        'g(n) is not a heuristic; UCS is uninformed. Negative costs invalidate Dijkstra-style proofs.',
        marks=2, diff='H'))
    o.append(mcq(
        'UninformedSearch',
        'A search node is a data structure storing at least',
        'a state, a parent pointer (or path), and a path cost g',
        'only a heuristic, never a state',
        'only the goal test',
        'a full Bayesian network',
        'A',
        'Standard node: state, parent, action, g.',
        marks=1, diff='E'))
    o.append(nat(
        'UninformedSearch',
        'Graph: S-A 2, S-C 1, A-G 1, C-G 4. Cheapest S-G cost is ____.',
        '3',
        'S-A-G = 3 beats S-C-G = 5.',
        marks=1, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'On an infinite tree with no goal, DFS is',
        'complete',
        'incomplete (it can follow an infinite branch)',
        'optimal',
        'equivalent to A*',
        'B',
        'An infinite branch traps DFS.',
        marks=1, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'BFS graph-search memory, branching factor b, goal depth d, is on the order of',
        'O(bd) like DFS',
        'O(b^d) nodes in the frontier',
        'O(1)',
        'O(d) only',
        'B',
        'The frontier at level d has Theta(b^d) nodes.',
        marks=1, diff='M'))
    o.append(nat(
        'UninformedSearch',
        'Unit-cost tree, goal at depth 2, branching 3. Number of nodes at the goal depth is ____.',
        '9',
        '3^2=9.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'Bidirectional uninformed search (when a predecessor function exists) meets in the middle to cut',
        'the exponent in b^{d/2} + b^{d/2} versus b^d',
        'the need for a goal test',
        'all path costs to 0',
        'the closed set',
        'A',
        'Two frontiers of depth d/2.',
        marks=2, diff='H'))
    o.append(mcq(
        'UninformedSearch',
        'A Grok campus map is an unweighted graph. To find a fewest-hops walk from Lab to Canteen one should run',
        'BFS',
        'DFS (which is hop-optimal)',
        'greedy best-first with a random h',
        'alpha-beta',
        'A',
        'Fewest hops = BFS on an unweighted graph.',
        marks=1, diff='E'))
    o.append(nat(
        'UninformedSearch',
        'UCS on S-A=10, S-G=100, A-G=1. Cost of the path UCS returns is ____.',
        '11',
        'S-A-G=11 beats the direct 100.',
        marks=2, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'Closed-set graph-search is used to',
        'avoid re-expanding a repeated state',
        'compute d-separation',
        'convert a formula to CNF',
        'sample a Bayesian network',
        'A',
        'The explored set blocks duplicates.',
        marks=1, diff='E'))
    o.append(msq(
        'UninformedSearch',
        'Which uninformed methods are complete on finite graphs with nonnegative costs (graph-search)?',
        'BFS',
        'UCS',
        'DFS with a closed set',
        'DLS with a limit smaller than the goal depth',
        'A;B;C',
        'DLS with too small a limit misses the goal.',
        marks=2, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'The frontier (open list) of BFS is a',
        'FIFO queue',
        'LIFO stack',
        'priority queue on h(n)',
        'minimax game tree',
        'A',
        'BFS = queue.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'The frontier of DFS is a',
        'FIFO queue',
        'LIFO stack',
        'priority queue on g(n)',
        'CNF clause set',
        'B',
        'DFS = stack.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'The frontier of UCS is a',
        'FIFO queue',
        'LIFO stack',
        'priority queue ordered by g(n)',
        'random set',
        'C',
        'UCS pops least g.',
        marks=1, diff='E'))
    o.append(nat(
        'UninformedSearch',
        'A path S-A-B-G with costs 2,2,2. Path cost g(G) is ____.',
        '6',
        '2+2+2=6.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'If every action cost is strictly positive, UCS cannot have',
        'an infinite cheap-loop problem of zero-cost cycles',
        'a finite graph',
        'a priority queue',
        'a start state',
        'A',
        'Positive costs make cycles strictly more expensive.',
        marks=1, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        'IDS time complexity on a tree (goal depth d, branching b) is still O(b^d) because',
        'the last iteration dominates the geometric series of earlier iterations',
        'each iteration is O(1)',
        'IDS is exponential in the memory',
        'IDS uses A* internally',
        'A',
        'b^0+...+b^d = Theta(b^d).',
        marks=2, diff='M'))
    o.append(nat(
        'UninformedSearch',
        'Depth-limited search with L=0 on a nonempty state space expands (goal-test on the root only) how many nodes?',
        '1',
        'Only the root, then the limit cuts every child.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'A robot on a grid can move N,S,E,W at cost 1. Fewest moves from (0,0) to (2,2) is',
        '2',
        '4',
        '8',
        '0',
        'B',
        'Manhattan distance 4; BFS finds it.',
        marks=1, diff='E'))
    o.append(nat(
        'UninformedSearch',
        'Grid (0,0) to (3,0) with 4-moves of cost 1. UCS/BFS optimal cost is ____.',
        '3',
        'Three east moves.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        'Tree-search DFS (no closed set) on a graph with cycles is',
        'complete',
        'in danger of infinite loops along a cycle',
        'optimal for unit costs',
        'the same as UCS',
        'B',
        'Without a closed set, a cycle can be re-entered forever.',
        marks=1, diff='M'))
    o.append(mcq(
        'UninformedSearch',
        "Matching: 'expand shallowest first' names",
        'BFS',
        'DFS',
        'greedy best-first',
        'minimax',
        'A',
        'Definition of BFS.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        "Matching: 'expand deepest first' names",
        'BFS',
        'DFS',
        'UCS',
        'A*',
        'B',
        'Definition of DFS.',
        marks=1, diff='E'))
    o.append(mcq(
        'UninformedSearch',
        "Matching: 'expand cheapest-path-so-far first' names",
        'DFS',
        'UCS',
        'greedy best-first',
        'random walk',
        'B',
        'UCS orders by g(n).',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'A* search ranks the frontier by',
        'f(n)=g(n)+h(n)',
        'h(n) only',
        'g(n) only',
        'depth only',
        'A',
        'Standard A* evaluation.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'Greedy best-first search ranks the frontier by',
        'f=g+h',
        'h(n) only',
        'g(n) only',
        'alpha',
        'B',
        'Greedy looks only at the heuristic.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'A heuristic h is admissible if for every node n',
        'h(n) >= h*(n) (never underestimates)',
        'h(n) <= h*(n) (never overestimates true remaining cost)',
        'h(n)=0 for every n',
        'h is inconsistent',
        'B',
        'Admissible = optimistic: h <= true cost-to-go.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        "A heuristic is consistent (monotone) if for every edge n->n' of cost c",
        "h(n) <= c + h(n')  (triangle inequality)",
        "h(n) >= c + h(n')",
        'h(n)=g(n)',
        'h is zero only at the start',
        'A',
        'Consistency implies admissibility.',
        marks=1, diff='M'))
    o.append(msq(
        'InformedSearch',
        'h1 and h2 are both admissible. Which combinations remain admissible?',
        'h(n)=max(h1(n),h2(n))',
        'h(n)=min(h1(n),h2(n))',
        'h(n)=h1(n)+h2(n) in general (no further assumption)',
        'h(n)=0',
        'A;B;D',
        'Max of admissible is admissible and dominating. Sum can double-count and overestimate. Zero is admissible. Min is admissible but weaker.',
        marks=2, diff='H'))
    o.append(mcq(
        'InformedSearch',
        'If h1 and h2 are admissible, the dominating choice among them is',
        'min(h1,h2)',
        'max(h1,h2)',
        'h1+h2',
        'h1-h2',
        'B',
        'Larger still-admissible h prunes more.',
        marks=1, diff='M'))
    o.append(nat(
        'InformedSearch',
        'True remaining cost h*=6. Heuristics 4 and 5, both admissible. max(h1,h2) at this node equals ____.',
        '5',
        'max(4,5)=5 still <=6.',
        marks=1, diff='E'))
    o.append(nat(
        'InformedSearch',
        'True remaining cost h*=6. Heuristics 4 and 5. The sum 4+5 equals 9, which is (1 if admissible at this node, else 0): report 0 because 9>6. That indicator is ____.',
        '0',
        'Sum 9 overestimates, so not admissible here.',
        marks=1, diff='M'))
    o.append(mcq(
        'InformedSearch',
        'Straight-line distance to Bucharest is admissible for road-map path cost (km) because',
        'a straight line is a lower bound on any road distance',
        'a straight line always overestimates road distance',
        'it equals g(n)',
        'it is inconsistent on every map',
        'A',
        'Euclidean distance <= any path length.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'Graph: S-A cost 1, S-B cost 2, A-G cost 3, B-G cost 1. Heuristic h(S)=2, h(A)=2, h(B)=1, h(G)=0. Is h admissible on these four nodes?',
        'Yes, because h <= true remaining: h*(S)=min(4,3)=3>=2, h*(A)=3>=2, h*(B)=1>=1, h*(G)=0',
        'No, h(A)=2 underestimates nothing wait it is admissible as listed',
        'No, because h(B)=1 equals h*(B) which is forbidden',
        'No, because h(G) must be 1',
        'A',
        'Admissible allows equality with h*. Cheapest S-G is S-B-G=3.',
        marks=2, diff='H'))
    o.append(nat(
        'InformedSearch',
        'In that graph S-A=1, S-B=2, A-G=3, B-G=1, cheapest S-G cost is ____.',
        '3',
        'S-B-G=3 < S-A-G=4.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'A* with a consistent h on graph-search expands nodes in nondecreasing f-order and is',
        'optimal (returns a cheapest path)',
        'suboptimal always',
        'identical to DFS',
        'uninformed',
        'A',
        'Consistency => optimality of graph-search A*.',
        marks=1, diff='M'))
    o.append(mcq(
        'InformedSearch',
        'A* with an admissible but inconsistent h, if one uses tree-search (reopen paths), is still',
        'optimal',
        'incomplete on finite graphs',
        'the same as greedy',
        'forbidden in GATE',
        'A',
        'Tree-search A* + admissible h is optimal; graph-search needs consistency (or reopening).',
        marks=2, diff='H'))
    o.append(nat(
        'InformedSearch',
        'Node with g=4, h=3. A* f-value is ____.',
        '7',
        'f=g+h=7.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'If h=0 everywhere, A* reduces to',
        'DFS',
        'UCS',
        'greedy best-first',
        'alpha-beta',
        'B',
        'f=g, which is UCS.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'If one ignores g and ranks by h only, the algorithm is',
        'UCS',
        'greedy best-first',
        'BFS',
        'IDS',
        'B',
        'Greedy best-first.',
        marks=1, diff='E'))
    o.append(msq(
        'InformedSearch',
        'Which heuristics for 8-puzzle Manhattan / misplaced-tiles are admissible?',
        'Number of misplaced tiles',
        'Sum of Manhattan distances of tiles to goals',
        'Twice the Manhattan sum (generally)',
        'h=0',
        'A;B;D',
        'Each move fixes at most one Manhattan unit and at most one misplaced tile. Doubling Manhattan can overestimate.',
        marks=2, diff='H'))
    o.append(nat(
        'InformedSearch',
        '8-puzzle: two tiles each 1 step from home, others home. Misplaced-tile h equals ____.',
        '2',
        'Two tiles are misplaced.',
        marks=1, diff='E'))
    o.append(nat(
        'InformedSearch',
        'Same two tiles each Manhattan 1, others 0. Manhattan h equals ____.',
        '2',
        '1+1=2.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'Greedy best-first can be badly suboptimal because',
        'it ignores g(n), so a cheap-looking fringe node may sit on an expensive path',
        'it is the same as UCS',
        'h is always 0',
        'it expands every node',
        'A',
        'Classic greedy failure mode.',
        marks=1, diff='M'))
    o.append(mcq(
        'InformedSearch',
        'Weighted A* with f=g+W h, W>1, typically',
        'trades optimality for speed (may return a suboptimal path)',
        'is always optimal for any W',
        'becomes DFS',
        'zeros the heuristic',
        'A',
        'Inflation of h can overestimate, losing admissibility.',
        marks=2, diff='M'))
    o.append(nat(
        'InformedSearch',
        'Start f=g+h with g=0, h(S)=5. The first f(S) is ____.',
        '5',
        '0+5=5.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'A* graph-search with a consistent heuristic never needs to reopen a closed node because',
        'the first time a node is expanded, g is already optimal',
        'h is always 0',
        'the frontier is a stack',
        'cycles have zero cost',
        'A',
        'Monotonicity of f along paths.',
        marks=2, diff='H'))
    o.append(mcq(
        'InformedSearch',
        'An overestimating heuristic (not admissible) can make A*',
        'miss a truly cheaper path, hence suboptimal',
        'always faster and still optimal',
        'identical to BFS always',
        'refuse to run',
        'A',
        'Overestimates can rank the optimal path behind a worse one that looks cheap.',
        marks=1, diff='M'))
    o.append(nat(
        'InformedSearch',
        'h1=3, h2=5, both admissible at n, h*=8. The dominating admissible combo max= ____.',
        '5',
        'max(3,5)=5 <=8.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'Manhattan distance on a 4-connected grid with only unit orthogonal moves is',
        'admissible and consistent',
        'inadmissible because it overestimates',
        'equal to Euclidean always',
        'a minimax value',
        'A',
        'Each move cuts Manhattan by at most 1.',
        marks=1, diff='M'))
    o.append(mcq(
        'InformedSearch',
        'Euclidean distance on that same 4-connected unit grid is',
        'still admissible (a lower bound) but looser than Manhattan',
        'inadmissible',
        'always larger than Manhattan',
        'equal to g(n)',
        'A',
        'Euclidean <= Manhattan <= true 4-move cost.',
        marks=2, diff='M'))
    o.append(nat(
        'InformedSearch',
        'Grid from (0,0) to (3,4). Manhattan h at the start is ____.',
        '7',
        '3+4=7.',
        marks=1, diff='E'))
    o.append(nat(
        'InformedSearch',
        'Grid from (0,0) to (3,4). Euclidean h at the start is ____.',
        '5',
        '3-4-5 triangle.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'IDA* is iterative-deepening A*, i.e.',
        'depth-first searches with a rising f-bound',
        'BFS with h=0',
        'minimax of heuristics',
        'Gibbs sampling of paths',
        'A',
        'IDA* = DFS-style f-limited iterations.',
        marks=1, diff='M'))
    o.append(msq(
        'InformedSearch',
        'h=0 everywhere. Which algorithms then coincide (up to tie-breaking) with UCS?',
        'A*',
        'greedy best-first',
        'IDA* with f=g',
        'DFS',
        'A;C',
        'Greedy with h=0 ranks all nodes equal (not UCS). DFS is not cost-ordered.',
        marks=2, diff='H'))
    o.append(mcq(
        'InformedSearch',
        'A* is called informed because it uses',
        'a problem-specific estimate h(n) of remaining cost',
        'only the branching factor',
        'only a stack',
        'a CNF encoding of the map',
        'A',
        'That is the definition of informed search.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'If two admissible heuristics satisfy h1(n) >= h2(n) for all n, then A* with h1 generally',
        'expands a subset of the nodes that h2 would expand (never more, ignoring ties)',
        'always expands more nodes',
        'becomes inadmissible',
        'ignores g',
        'A',
        'Dominating admissible heuristics prune at least as much.',
        marks=2, diff='H'))
    o.append(nat(
        'InformedSearch',
        'Path S-A-G with costs 2, 5 and h(A)=4, h(G)=0, h(S)=6. f(A) after reaching A via S is ____.',
        '6',
        'g(A)=2, f=2+4=6.',
        marks=1, diff='M'))
    o.append(mcq(
        'InformedSearch',
        'A heuristic with h(G)!=0 at the goal is',
        'not admissible unless the true remaining cost is at least that value; typically we require h(G)=0',
        'always consistent',
        'required by UCS',
        'the definition of greedy',
        'A',
        'h*(G)=0 so admissibility forces h(G)=0.',
        marks=1, diff='M'))
    o.append(nat(
        'InformedSearch',
        'Three heuristics 2, 6, 4 all admissible at a node (h*=10). max of the three is ____.',
        '6',
        'max=6.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'Best-first search is a family; A* is the instance whose evaluation is',
        'f=g+h',
        'f=h',
        'f=-g',
        'f=depth',
        'A',
        'A* is best-first with f=g+h.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'In a two-player zero-sum game of perfect information, minimax at a MAX root returns',
        'the max over legal moves of the min-value of the resulting position',
        'the average of leaf values',
        'a random legal move',
        'A* f-values',
        'A',
        'Definition of minimax.',
        marks=1, diff='E'))
    o.append(nat(
        'Adversarial',
        'MAX root with two moves: Left to a MIN node with leaves 3 and 5; Right to a MIN node with leaves 2 and 9. The minimax value of the root is ____.',
        '3',
        'Left min=3, Right min=2, max=3.',
        marks=2, diff='M'))
    o.append(mcq(
        'Adversarial',
        "In that same tree (Left leaves 3,5; Right leaves 2,9), MAX's best first move is",
        'Left',
        'Right',
        'either, values equal',
        'pass',
        'A',
        "Left yields 3 > Right's 2.",
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'MAX root, three MIN children with leaf-pairs (4,1), (6,6), (2,8). Minimax root value is ____.',
        '6',
        'mins 1,6,2; max=6.',
        marks=2, diff='M'))
    o.append(mcq(
        'Adversarial',
        'MAX root, MIN children (4,1), (6,6), (2,8). The unique best first move is toward the child whose min is',
        '1',
        '6',
        '2',
        '8',
        'B',
        'Only the (6,6) branch yields 6.',
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'A MAX leaf that is also a terminal with payoff 7 contributes minimax value ____.',
        '7',
        'Terminals equal their utility.',
        marks=1, diff='E'))
    o.append(msq(
        'Adversarial',
        'Which claims about minimax (deterministic, zero-sum, perfect information) are TRUE?',
        'It assumes the opponent plays optimally against you',
        'It can be computed bottom-up on a finite game tree',
        'It maximises the worst-case payoff',
        'It requires a heuristic h like A* even at terminals with known utility',
        'A;B;C',
        'Terminal utilities are given; a heuristic is used only when the tree is truncated.',
        marks=2, diff='M'))
    o.append(mcq(
        'Adversarial',
        'Alpha-beta pruning, with optimal move ordering, can reduce time to about',
        'O(b^{d/2}) instead of O(b^d)',
        'O(1)',
        'O(d)',
        'O(b^d) still, never better',
        'A',
        'Best-case branching ~ sqrt of minimax.',
        marks=1, diff='M'))
    o.append(mcq(
        'Adversarial',
        'Alpha in alpha-beta is',
        'the best (highest) value MAX can currently guarantee',
        'the best (lowest) value MIN can currently guarantee',
        'always 0',
        'the A* heuristic',
        'A',
        "Alpha = MAX's current lower bound.",
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'Beta in alpha-beta is',
        "MAX's lower bound",
        'the best (lowest) value MIN can currently guarantee',
        'always +inf',
        'path cost g',
        'B',
        "Beta = MIN's current upper bound.",
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'A MIN node can prune a remaining child when',
        'its current value is already <= alpha (MAX would never choose this node)',
        'beta is +inf',
        'the child is a MAX node only',
        'h is admissible',
        'A',
        'Beta cutoff: MIN has already a value <= alpha.',
        marks=2, diff='M'))
    o.append(mcq(
        'Adversarial',
        'A MAX node can prune a remaining child when',
        'its current value is already >= beta (MIN would never choose this node)',
        'alpha is -inf always',
        'the branching factor is 1',
        'UCS is running',
        'A',
        'Alpha cutoff.',
        marks=2, diff='M'))
    o.append(nat(
        'Adversarial',
        'MAX root; left MIN leaves 3 then 5; right MIN first leaf 2, then a second leaf x. Alpha-beta (left-to-right) prunes the leaf x no matter what x is. The root value is ____.',
        '3',
        'Left min=3; right min<=2 already, so MAX keeps 3. x is never needed.',
        marks=2, diff='H'))
    o.append(mcq(
        'Adversarial',
        'In that left-to-right alpha-beta tree (left leaves 3,5; right first leaf 2 then x), the pruned leaf is',
        'the 3',
        'the 5',
        'the 2',
        'the second right leaf x',
        'D',
        "After seeing 2, MIN's node is <=2<=alpha=3, cutoff.",
        marks=2, diff='H'))
    o.append(nat(
        'Adversarial',
        'Worst-case alpha-beta (adversarial ordering) on a tree of 8 leaves still evaluates how many leaves?',
        '8',
        'No pruning in the worst order; all leaves are seen.',
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'A complete binary game tree of depth 2 (four leaves). Minimax examines all 4 leaves. Report that count: ____.',
        '4',
        'No pruning claimed; 4 terminals.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'Evaluation function at a truncated depth is used because',
        'the full tree may be too large; a heuristic estimates the utility of a nonterminal',
        'minimax is undefined on terminals',
        'alpha is always a heuristic',
        'BFS needs h',
        'A',
        'Standard depth-limited minimax / heuristic play.',
        marks=1, diff='E'))
    o.append(nat(
        'Adversarial',
        'MAX root with one move to a terminal 4. Minimax value is ____.',
        '4',
        'Forced payoff 4.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'Negamax is a reformulation of minimax that',
        'uses a single recursive function with a sign flip, equivalent on zero-sum games',
        'solves Bayesian networks',
        'is uninformed search',
        'requires CNF',
        'A',
        'negamax(n) = max_c -negamax(c).',
        marks=1, diff='M'))
    o.append(msq(
        'Adversarial',
        'Which are TRUE of alpha-beta versus plain minimax on the same tree and same left-to-right order?',
        'The returned root value is the same',
        'Some leaves may not be evaluated',
        'Alpha-beta can change the identity of an optimal root move only if there are ties, not the value',
        'Alpha-beta can return a different numeric value than minimax on the same finite tree',
        'A;B;C',
        'Pruning is correctness-preserving for the value.',
        marks=2, diff='H'))
    o.append(nat(
        'Adversarial',
        'Leaves of a MAX-over-MIN tree in left-to-right order: 1,8 | 6,4. Minimax root is max(min(1,8),min(6,4))=max(1,4)= ____.',
        '4',
        'max(1,4)=4.',
        marks=2, diff='M'))
    o.append(mcq(
        'Adversarial',
        'Leaves 1,8 | 6,4 as above, left-to-right alpha-beta. After left MIN=1, alpha=1. Right MIN sees 6, then 4. Is 4 pruned?',
        'No, because 6>alpha so MIN must look further; 4 is evaluated and min becomes 4',
        'Yes, 6 already prunes',
        'The 1 is pruned',
        'The 8 is pruned',
        'A',
        '6>alpha=1, no cutoff yet; 4 is seen. (8 is seen too: left MIN looks at both 1 and 8.)',
        marks=2, diff='H'))
    o.append(nat(
        'Adversarial',
        'MAX-MIN tree leaves 7,3 | 2,9. Root minimax value is ____.',
        '3',
        'mins 3 and 2; max=3.',
        marks=2, diff='M'))
    o.append(mcq(
        'Adversarial',
        'MAX-MIN leaves 7,3 | 2,9. Best first move is the left child because',
        'min(7,3)=3 > min(2,9)=2',
        'min(2,9) is larger',
        '9 is the root value',
        '7 is already the answer',
        'A',
        'Left guarantees 3.',
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'A MIN root (MIN to move) with MAX children having leaves (2,5) and (4,1). Minimax value at the MIN root is ____.',
        '4',
        'MAX children: max(2,5)=5 and max(4,1)=4; MIN chooses min(5,4)=4.',
        marks=2, diff='H'))
    o.append(nat(
        'Adversarial',
        'Tic-style toy: MAX can move to terminals 1, 0, -1. Minimax chooses the move of value ____.',
        '1',
        'MAX picks the largest terminal 1.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'A chance node in expectiminimax (dice) is evaluated by',
        'the probability-weighted average of children, not min or max',
        'always min',
        'always max',
        'A* f-value',
        'A',
        'Chance nodes average.',
        marks=1, diff='M'))
    o.append(mcq(
        'Adversarial',
        'Horizon effect in depth-limited minimax is',
        'a bad tactic pushed just beyond the cutoff looking fine at the leaf evaluator',
        'alpha always equalling beta',
        'UCS failing on unit costs',
        'CNF explosion',
        'A',
        'Search-horizon pathology.',
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'Branching factor 3, depth-2 full game tree. Number of leaves is ____.',
        '9',
        '3^2=9.',
        marks=1, diff='E'))
    o.append(nat(
        'Adversarial',
        'Branching 2, depth 3. Number of leaves is ____.',
        '8',
        '2^3=8.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'Move ordering that tries the eventual best move first in alpha-beta',
        'maximises pruning',
        'prevents all pruning',
        'changes the minimax value',
        'turns the game into UCS',
        'A',
        'Best-first ordering is ideal for alpha-beta.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'If alpha >= beta at a node, alpha-beta',
        'prunes remaining unexamined children of that node',
        'restarts minimax from the root',
        'sets all leaves to 0',
        'switches to uninformed DFS',
        'A',
        'Cutoff condition.',
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'Leaves under a MIN node: 4, 9, 1. The MIN value is ____.',
        '1',
        'min=1.',
        marks=1, diff='E'))
    o.append(nat(
        'Adversarial',
        'Leaves under a MAX node: 4, 9, 1. The MAX value is ____.',
        '9',
        'max=9.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'A two-ply (MAX then MIN) search with an evaluator at depth 2 is',
        'minimax to depth 2 using the evaluator as stand-in utilities',
        'BFS on the game graph',
        'resolution on CNF',
        'Gibbs sampling',
        'A',
        'Bounded-depth game search.',
        marks=1, diff='E'))
    o.append(msq(
        'Adversarial',
        'Which algorithms belong to adversarial search as in GATE DA?',
        'minimax',
        'alpha-beta pruning',
        'expectiminimax (chance nodes)',
        'k-means clustering of board positions as the primary solver',
        'A;B;C',
        'k-means is unsupervised ML, not adversarial search.',
        marks=2, diff='M'))
    o.append(mcq(
        'Adversarial',
        'If two root moves both attain the minimax value, then',
        'either is minimax-optimal',
        'neither is legal',
        'alpha-beta is invalid',
        'the smaller index is required',
        'A',
        'Ties among optimal actions are all optimal.',
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'Root MAX, four terminal children 0, 2, 2, -5. Minimax value is ____.',
        '2',
        'max=2.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'Quiescence search extends the horizon in tactical lines to reduce',
        'horizon-effect blunders on captures just beyond the depth limit',
        'd-separation work',
        'CNF conversion cost',
        'likelihood-weighting variance',
        'A',
        'Continue while the position is noisy.',
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'MAX-MIN leaves 5,0 | 1,1. Root value max(min(5,0),min(1,1))= ____.',
        '1',
        'max(0,1)=1.',
        marks=2, diff='M'))
    o.append(mcq(
        'Adversarial',
        'MAX-MIN leaves 5,0 | 1,1. Best first move is',
        'Right, because it guarantees 1 > 0',
        'Left, because 5 is large',
        'pass',
        'the leaf 0',
        'A',
        "Right's min is 1.",
        marks=1, diff='M'))
    o.append(nat(
        'Adversarial',
        'Alpha starts at -inf, beta at +inf. After MAX sees a child value 4, alpha becomes ____.',
        '4',
        'alpha := max(alpha,4)=4.',
        marks=1, diff='M'))
    o.append(mcq(
        'PropLogic',
        'A propositional formula is a tautology iff it is',
        'true under every truth assignment',
        'true under some assignment',
        'false under every assignment',
        'built only from implication',
        'A',
        'Tautology = valid = true in all models.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'A propositional formula is satisfiable iff',
        'some assignment makes it true',
        'every assignment makes it true',
        'no assignment makes it true',
        'it is necessarily a tautology',
        'A',
        'SAT = at least one model.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'A formula is unsatisfiable (a contradiction) iff it is',
        'true in every model',
        'false under every truth assignment',
        'a tautology',
        'Horn',
        'B',
        'No model exists.',
        marks=1, diff='E'))
    o.append(msq(
        'PropLogic',
        'Which of the following propositional formulae are tautologies?',
        'P v ~P',
        'P -> P',
        '~(P & ~P)',
        'P & ~P',
        'A;B;C',
        'P & ~P is a contradiction.',
        marks=2, diff='M'))
    o.append(mcq(
        'PropLogic',
        'De Morgan: ~(P & Q) is equivalent to',
        '~P & ~Q',
        '~P v ~Q',
        'P v Q',
        'P -> Q',
        'B',
        '~(P&Q) ? ~P v ~Q.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'Implication P -> Q is equivalent to',
        '~P v Q',
        'P v Q',
        '~P & Q',
        'P & Q',
        'A',
        'Standard rewrite used en route to CNF.',
        marks=1, diff='E'))
    o.append(nat(
        'PropLogic',
        'Number of distinct truth assignments to 3 atoms P,Q,R is ____.',
        '8',
        '2^3=8.',
        marks=1, diff='E'))
    o.append(nat(
        'PropLogic',
        'Number of models of P v Q on atoms {P,Q} is ____.',
        '3',
        'Only FF fails.',
        marks=1, diff='M'))
    o.append(nat(
        'PropLogic',
        'Number of models of P & Q on atoms {P,Q} is ____.',
        '1',
        'Only TT.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'CNF of (P -> Q) & (Q -> R) is',
        '(~P v Q) & (~Q v R)',
        '(P v Q) & (Q v R)',
        '~P & ~Q & R',
        'P & Q & R',
        'A',
        'Rewrite each implication as a clause.',
        marks=2, diff='M'))
    o.append(mcq(
        'PropLogic',
        'CNF of ~(P -> Q): first ~( ~P v Q ) ? P & ~Q. The CNF clauses are',
        'the unit clauses {P} and {~Q}',
        'the single clause {P,~Q}',
        '{~P,Q}',
        'the empty set of clauses',
        'A',
        'A conjunction of two unit clauses.',
        marks=2, diff='M'))
    o.append(mcq(
        'PropLogic',
        'CNF of P <-> Q uses (P->Q)&(Q->P), i.e.',
        '(~P v Q) & (~Q v P)',
        'P v Q',
        '~P v ~Q',
        'P & Q only',
        'A',
        'Biconditional as two clauses.',
        marks=1, diff='M'))
    o.append(msq(
        'PropLogic',
        'Which formulae are equivalent to P -> (Q -> P)?',
        'a tautology (true under all four assignments of P,Q)',
        '~P v (~Q v P)',
        '(P & Q) -> P',
        'P & ~P',
        'A;B;C',
        'P -> (Q -> P) is a tautology; D is a contradiction.',
        marks=2, diff='H'))
    o.append(mcq(
        'PropLogic',
        'Modus ponens: from P and (P -> Q) one infers',
        'Q',
        '~Q',
        'P & ~Q',
        '~P',
        'A',
        'Inference rule MP.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'Resolution on clauses {P,Q} and {~P,R} yields',
        '{Q,R}',
        '{P,~P}',
        'the empty clause always',
        '{Q} only',
        'A',
        'Resolve on P.',
        marks=1, diff='M'))
    o.append(nat(
        'PropLogic',
        'Resolution of the unit clauses {P} and {~P} produces a clause with how many literals?',
        '0',
        'The empty clause.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'The empty clause in resolution proofs means',
        'a contradiction has been derived (the clause set is unsatisfiable)',
        'a tautology was derived',
        'the set is satisfiable',
        'a Horn query that is true',
        'A',
        'Empty clause = False.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'A Horn clause has at most one positive literal. Which of these is Horn?',
        '~P v ~Q v R',
        'P v Q',
        'P v Q v R',
        '~P v Q v R',
        'A',
        '~P v ~Q v R is (P & Q) -> R, definite Horn. D has two positives Q and R.',
        marks=1, diff='M'))
    o.append(mcq(
        'PropLogic',
        'Forward chaining on Horn clauses is complete for',
        'atomic entailments from a Horn KB',
        'all tautologies of arbitrary CNF',
        'first-order validity in general',
        'minimax values',
        'A',
        'Horn-SAT / definite-clause FC.',
        marks=1, diff='M'))
    o.append(nat(
        'PropLogic',
        'Truth table of P -> Q: number of T rows among 4 is ____.',
        '3',
        'Only P=T,Q=F is false.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'KB entails sentence S (written KB |= S) iff',
        'every model of KB is a model of S',
        'some model of KB is a model of S',
        'KB is unsatisfiable always',
        'S is a Horn query only',
        'A',
        'Semantic entailment.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'If KB is unsatisfiable, then for every S',
        'KB |= S (explosion / ex falso)',
        'KB entails nothing',
        'S must be a tautology independently',
        'resolution cannot run',
        'A',
        'From False everything follows.',
        marks=2, diff='H'))
    o.append(msq(
        'PropLogic',
        'Which statements are TRUE?',
        'If S is a tautology then KB |= S for every KB',
        'P |= P v Q',
        'P & ~P |= Q',
        'P v Q |= P always',
        'A;B;C',
        'P v Q does not entail P (countermodel P false, Q true).',
        marks=2, diff='H'))
    o.append(mcq(
        'PropLogic',
        'Distributivity needed in CNF: P v (Q & R) becomes',
        '(P v Q) & (P v R)',
        '(P & Q) v R',
        'P v Q v R',
        '~P',
        'A',
        'Or-over-and.',
        marks=1, diff='M'))
    o.append(nat(
        'PropLogic',
        'CNF of P v (Q & R) has how many clauses?',
        '2',
        '(P v Q) and (P v R).',
        marks=1, diff='M'))
    o.append(mcq(
        'PropLogic',
        'A literal is',
        'an atom or a negated atom',
        'a conjunction of clauses',
        'a tautology only',
        'an A* node',
        'A',
        'P or ~P.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        'Unit propagation: a unit clause {L} forces',
        'L true, so ~L is deleted from other clauses and clauses containing L are satisfied',
        'the empty clause immediately in every KB',
        'all atoms true',
        'greedy search',
        'A',
        'DPLL unit prop.',
        marks=1, diff='M'))
    o.append(nat(
        'PropLogic',
        'Atoms P,Q. Number of inequivalent propositional formulae (up to logical equivalence) is ____.',
        '16',
        '2^(2^2)=16 Boolean functions of 2 vars.',
        marks=2, diff='H'))
    o.append(mcq(
        'PropLogic',
        'P |= Q is FALSE in particular when',
        'P is true and Q is false in some assignment (a countermodel)',
        'P is a contradiction',
        'Q is a tautology',
        'P is P & P',
        'A',
        'Entailment fails iff a model of P is not a model of Q.',
        marks=1, diff='M'))
    o.append(mcq(
        'PropLogic',
        'Conversion of (P -> Q) -> R to CNF: first rewrite as ~(~P v Q) v R ? (P & ~Q) v R ? (P v R) & (~Q v R). The CNF has clauses',
        '{P,R} and {~Q,R}',
        '{P,Q,R}',
        '{~P,~Q,~R}',
        '{R} only',
        'A',
        'Two binary clauses.',
        marks=2, diff='H'))
    o.append(nat(
        'PropLogic',
        'How many clauses in that CNF of (P -> Q) -> R?',
        '2',
        'Two clauses.',
        marks=1, diff='M'))
    o.append(msq(
        'PropLogic',
        'Which are valid equivalences?',
        'P -> Q  ?  ~Q -> ~P  (contrapositive)',
        '~~P ? P',
        'P v P ? P',
        'P & ~P ? P v ~P',
        'A;B;C',
        'Contradiction is not equivalent to a tautology.',
        marks=2, diff='M'))
    o.append(mcq(
        'PropLogic',
        'SAT is NP-complete. 2-SAT (clauses of size <=2) is',
        'solvable in polynomial time (e.g. implication graph / SCCs)',
        'undecidable',
        'the same as FOL validity',
        'minimax',
        'A',
        '2-SAT is in P.',
        marks=2, diff='H'))
    o.append(mcq(
        'PropLogic',
        'A knowledge base {P -> Q, Q -> R, P} entails R by',
        'two applications of modus ponens',
        'alpha-beta',
        'k-means',
        'PCA',
        'A',
        'P, P->Q => Q; Q, Q->R => R.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'The FOL sentence forall x (Cat(x) -> Mammal(x)) together with Cat(Nori) entails',
        'Mammal(Nori)',
        '~Mammal(Nori)',
        'forall x Cat(x)',
        'exists x ~Mammal(x)',
        'A',
        'Universal instantiation + MP.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'exists x P(x) does NOT entail',
        'exists y P(y)  (alpha-equivalent)',
        'P(A) for a previously unused constant A without existential instantiation care',
        '~~ exists x P(x)',
        'exists x (P(x) v Q(x))',
        'B',
        'You may not replace exists x P(x) by P(A) for an arbitrary old constant A; EI needs a fresh Skolem.',
        marks=2, diff='H'))
    o.append(msq(
        'FOL',
        'Which FOL statements are TRUE?',
        'forall x P(x) entails P(A) for any ground term A in the language',
        'P(A) entails exists x P(x)',
        'exists x forall y Likes(x,y) entails forall y exists x Likes(x,y)',
        'forall y exists x Likes(x,y) entails exists x forall y Likes(x,y)',
        'A;B;C',
        'Quantifier order: a single liker-of-all implies everyone is liked by someone, not conversely.',
        marks=2, diff='H'))
    o.append(mcq(
        'FOL',
        'Negating forall x P(x) yields',
        'exists x ~P(x)',
        'forall x ~P(x)',
        'exists x P(x)',
        '~P(x) with free x as a sentence',
        'A',
        'Standard quantifier negation.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'Negating exists x P(x) yields',
        'forall x ~P(x)',
        'exists x ~P(x)',
        'forall x P(x)',
        'P(x)',
        'A',
        '~exists = forall not.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'Unification of P(x,A) and P(B,y) succeeds with mgu',
        '{x/B, y/A}',
        '{x/A, y/B}',
        'fail',
        '{x/y}',
        'A',
        'Substitute x by B and y by A.',
        marks=1, diff='M'))
    o.append(mcq(
        'FOL',
        'Unification of P(x,x) and P(A,B) for distinct constants A,B',
        'succeeds with {x/A}',
        'fails occurs/constant clash',
        'succeeds with {A/B}',
        'succeeds with empty theta',
        'B',
        'x cannot be both A and B.',
        marks=1, diff='M'))
    o.append(mcq(
        'FOL',
        'Occurs check: unify x and f(x)',
        'fails, because x occurs in f(x)',
        'succeeds with {x/f(x)} as a finite unifier',
        'succeeds with empty theta',
        'is the same as resolution',
        'A',
        'No finite unifier; occurs check rejects it.',
        marks=2, diff='M'))
    o.append(mcq(
        'FOL',
        'Prenex form pulls quantifiers front. A prenex equivalent of forall x P(x) -> Q (Q sentence, x not free in Q) is',
        'exists x (P(x) -> Q)',
        'forall x (P(x) -> Q)',
        'Q -> forall x P(x)',
        'P(x) -> Q with free x',
        'A',
        'Implication (forall x P) -> Q ? exists x (P(x)->Q) when x not free in Q.',
        marks=2, diff='H'))
    o.append(mcq(
        'FOL',
        'Skolemisation of exists y forall x P(x,y) introduces',
        'a Skolem constant c with forall x P(x,c)',
        'a Skolem function f(x) with P(x,f(x))',
        'nothing',
        'a propositional atom only',
        'A',
        'Existential first (not in the scope of a universal) => constant.',
        marks=2, diff='M'))
    o.append(mcq(
        'FOL',
        'Skolemisation of forall x exists y P(x,y) introduces',
        'a Skolem function f with forall x P(x,f(x))',
        'a single constant c and P(x,c) for all x, which is stronger',
        'nothing',
        'CNF of Q',
        'A',
        'Existential in the scope of x becomes f(x).',
        marks=1, diff='M'))
    o.append(msq(
        'FOL',
        'Regarding entailment, which hold?',
        'forall x (P(x) -> Q(x)), P(A)  |=  Q(A)',
        'exists x (P(x) & Q(x))  |=  (exists x P(x)) & (exists x Q(x))',
        '(exists x P(x)) & (exists x Q(x))  |=  exists x (P(x) & Q(x))',
        'forall x (P(x) & Q(x))  |=  (forall x P(x)) & (forall x Q(x))',
        'A;B;D',
        'Two possibly different witnesses do not give a common witness. C fails.',
        marks=2, diff='H'))
    o.append(mcq(
        'FOL',
        'The FOL implication forall x (Student(x) -> Smart(x)) is NOT equivalent to',
        'forall x (~Student(x) v Smart(x))',
        'exists x (Student(x) & ~Smart(x))',
        '~ exists x (Student(x) & ~Smart(x))',
        'the same sentence with a renamed bound variable y',
        'B',
        'B is the negation, not the original.',
        marks=2, diff='M'))
    o.append(mcq(
        'FOL',
        'Ground atomic sentence P(A) in a Herbrand interpretation is true iff',
        "the interpretation's set of true ground atoms contains P(A)",
        'A is a variable',
        'P is a function symbol',
        'the sentence is CNF of Q',
        'A',
        'Herbrand models are sets of ground atoms.',
        marks=1, diff='M'))
    o.append(nat(
        'FOL',
        'Language with one constant A and one unary function f. Number of ground terms of syntactic depth at most 1 (A and f(A)) is ____.',
        '2',
        'A, f(A). (Depth-0 and applying f once.)',
        marks=1, diff='M'))
    o.append(mcq(
        'FOL',
        'Universal instantiation: from forall x P(x) infer',
        'P(t) for a ground term t',
        'exists x ~P(x)',
        'P(x) with x still bound incorrectly as a sentence',
        'minimax(P)',
        'A',
        'UI.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'Existential generalisation: from P(A) infer',
        'exists x P(x)',
        'forall x P(x)',
        '~P(A)',
        'A=A only',
        'A',
        'EG.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'Conversion of FOL to clausal form includes: implications out, negations in, standardise variables, prenex, Skolemise, drop universals, distribute. Dropping universals is valid after Skolemisation because',
        'remaining variables are implicitly universally quantified in clauses',
        'there are never variables left',
        'Skolem functions remove all variables',
        'CNF cannot have variables',
        'A',
        'Clause variables are universal.',
        marks=2, diff='M'))
    o.append(mcq(
        'FOL',
        'Which pair is a unifier of Knows(John,x) and Knows(John,Jane)?',
        '{x/Jane}',
        '{x/John}',
        'fail',
        '{Jane/x, John/Jane}',
        'A',
        'x binds to Jane.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'Most general unifier of P(x,f(y)) and P(g(z),f(A)) is',
        '{x/g(z), y/A}  (or {x/g(z), y/A} up to renaming z)',
        '{x/A, y/g(z)}',
        'fail because f occurs',
        '{z/x}',
        'A',
        'x=g(z), f(y)=f(A) so y=A.',
        marks=2, diff='H'))
    o.append(msq(
        'FOL',
        'X is forall x (P(x)->Q(x)). Which sentences does X entail?',
        'P(A) -> Q(A)',
        'forall y (P(y)->Q(y))',
        '~Q(A) -> ~P(A)',
        'exists x P(x)  (without further premises)',
        'A;B;C',
        'A universal implication does not by itself assert existence of a P-object.',
        marks=2, diff='H'))
    o.append(mcq(
        'FOL',
        'The sentence exists x (P(x) -> Q(x)) is true in a structure if',
        'some element satisfies ~P or Q (quite weak)',
        'every element is P and Q',
        'P is empty necessarily',
        'Q is empty necessarily',
        'A',
        'exists x (~P(x) v Q(x)) is easy to satisfy.',
        marks=2, diff='H'))
    o.append(mcq(
        'FOL',
        'FOL validity is',
        'undecidable in general (Church/Turing) though semi-decidable by proof procedures',
        'decidable by a 2-SAT algorithm',
        'the same as 2-SAT',
        'solved by k-means',
        'A',
        'Validity is r.e. but not recursive.',
        marks=2, diff='H'))
    o.append(nat(
        'FOL',
        'Arity of a binary predicate Likes(x,y) is ____.',
        '2',
        'Two arguments.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'A term is built from',
        'variables, constants, and function symbols; it is not a formula by itself',
        'quantifiers only',
        'implication only',
        'clauses of CNF only',
        'A',
        'Terms vs formulae.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'Substitution {x/A} applied to forall x P(x) (bound x)',
        'does not capture the bound x; the sentence is unchanged',
        'becomes forall A P(A) which is ill-formed and intended',
        'entails P(A) by substitution into the binder',
        'fails occurs check',
        'A',
        'Bound variables are not free for substitution.',
        marks=2, diff='M'))
    o.append(mcq(
        'FOL',
        'From ~ exists x P(x) one may infer',
        'forall x ~P(x)',
        'exists x P(x)',
        'P(A)',
        'forall x P(x)',
        'A',
        'Quantifier negation.',
        marks=1, diff='E'))
    o.append(nat(
        'FOL',
        'Unification of f(x) with f(A) uses how many bindings in the mgu {x/A}?',
        '1',
        'One binding.',
        marks=1, diff='E'))
    o.append(mcq(
        'FOL',
        'Resolution in FOL uses unification to',
        'align complementary literals before resolving, via an mgu',
        'compute A* f-values',
        'd-separate a BN',
        'sample Gibbs',
        'A',
        'Binary resolution + unification.',
        marks=1, diff='M'))
    o.append(msq(
        'FOL',
        'Which are closed sentences (no free variables)?',
        'forall x P(x)',
        'exists y Q(y)',
        'P(x) with free x',
        'forall x exists y R(x,y)',
        'A;B;D',
        'P(x) is open.',
        marks=2, diff='M'))
    o.append(mcq(
        'FOL',
        'The formula forall x exists y (y = x+1) over integers uses equality. It is true in (Z, +1) because',
        'every integer has a successor',
        'some integer has no successor',
        'addition is not a function',
        'it is unsatisfiable',
        'A',
        'Successor always exists in Z.',
        marks=1, diff='M'))
    o.append(mcq(
        'BayesNet',
        'A Bayesian network on variables V encodes a joint by',
        "the product of each node's CPT given its parents",
        'a single full table of size 2^{|V|} always stored explicitly as the only option',
        'k-means centroids',
        'CNF of the DAG',
        'A',
        'P(v) = product_i P(v_i | pa_i).',
        marks=1, diff='E'))
    o.append(mcq(
        'BayesNet',
        'Alarm BN: B->A<-E, A->J, A->M. The joint factorises as',
        'P(B)P(E)P(A|B,E)P(J|A)P(M|A)',
        'P(B)P(E)P(A)P(J)P(M)',
        'P(J)P(M)P(A|J,M)P(B,E)',
        'P(B,E,A,J,M) as 32 unconstrained numbers',
        'A',
        'Parents of A are B,E; parents of J,M are A; B,E are roots.',
        marks=2, diff='M'))
    o.append(msq(
        'BayesNet',
        'In the Alarm network B->A<-E, A->J, A->M, which conditional independences hold by d-separation?',
        'J ? M | A',
        'B ? E  (unconditionally)',
        'B ? E | A  (explaining-away collider)',
        'J ? B | A',
        'A;B;D',
        'Conditioning on the collider A opens B-E. J ? M | A and J ? B | A hold.',
        marks=2, diff='H'))
    o.append(mcq(
        'BayesNet',
        'A collider chain A -> C <- B is blocked when',
        'C is not observed and no descendant of C is observed',
        'C is observed',
        'A is observed',
        'always never blocked',
        'A',
        'Colliders block unless they (or a descendant) are in the evidence.',
        marks=2, diff='M'))
    o.append(mcq(
        'BayesNet',
        'A chain A -> C -> B is blocked when',
        'C is observed',
        'C is unobserved',
        'A is a leaf',
        'the DAG has no edges',
        'A',
        'Serial chain blocked by observing the middle.',
        marks=1, diff='M'))
    o.append(mcq(
        'BayesNet',
        'A fork A <- C -> B is blocked when',
        'C is observed',
        'C is unobserved',
        'B is a parent of A',
        'always open',
        'A',
        'Common-cause fork blocked by observing C.',
        marks=1, diff='M'))
    o.append(mcq(
        'BayesNet',
        'Explaining away: observing Alarm, then also observing Burglary, typically',
        'lowers P(Earthquake | Alarm, Burglary) relative to P(Earthquake | Alarm)',
        'raises P(Earthquake | Alarm) necessarily to 1',
        'd-connects J and M given A',
        'makes B independent of E given A still',
        'A',
        'Collider opening + competing explanations.',
        marks=2, diff='H'))
    o.append(nat(
        'BayesNet',
        'Binary Alarm net B,E,A,J,M as above. Naive full joint table size is 2^5 = ____.',
        '32',
        'Five binary vars.',
        marks=1, diff='E'))
    o.append(nat(
        'BayesNet',
        'Same Alarm net: CPT parameters (unconstrained, not using last-prob=1-p) : 1+1+4+2+2 = ____.',
        '10',
        'P(B),P(E) one each; P(A|B,E) four; P(J|A) two; P(M|A) two. (If using 1-p: 1+1+4+2+2 wait same if we count both rows... GATE often counts free params 1+1+4+2+2=10 unconstrained or 1+1+4+1+1=8 with 1-p. We count listed CPT entries as 10.)',
        marks=2, diff='M'))
    o.append(mcq(
        'BayesNet',
        'Student network: Difficulty -> Grade <- Intelligence, Intelligence -> SAT, Grade -> Letter. Then SAT ? Letter | Intelligence, Grade is',
        'true by d-separation? Path SAT-I-Grade-Letter: observing I blocks the fork at I, but Grade is also observed so the chain Grade->Letter is not needed... Path SAT-I-Grade-Letter: I observed blocks SAT-I-Grade. No other path. So SAT ? Letter | I,G. The question says | Intelligence, Grade. TRUE.',
        'false because a chain remains',
        'undefined',
        'equivalent to k-means',
        'A',
        'The only path SAT-I-Grade-Letter is blocked at I (fork).',
        marks=2, diff='H'))
    o.append(mcq(
        'BayesNet',
        'WetGrass: Cloudy -> Sprinkler, Cloudy -> Rain, Sprinkler -> Wet, Rain -> Wet. Unconditionally Sprinkler ? Rain is',
        'false: they share the fork Cloudy, which is unobserved, so they are dependent',
        'true by a collider at Wet',
        'true because they are roots',
        'true iff Wet is observed',
        'A',
        'Common cause Cloudy, unobserved => dependent. Observing Cloudy would block.',
        marks=2, diff='H'))
    o.append(msq(
        'BayesNet',
        'WetGrass network C->S, C->R, S->W, R->W. Which hold?',
        'S ? R | C',
        'S not? R  (marginally, generally)',
        'S not? R | W  (collider W opens explaining away)',
        'W ? C | S,R  is false in general? actually W is a child of S,R so given S,R, W is independent of C (no path around). W ? C | S,R holds.',
        'A;B;C',
        "Option D is actually TRUE (W ? C | S,R) so if the stem lists D as a true CI, the answer would include D. The option text says 'is false in general' making D a false claim. So A;B;C.",
        marks=2, diff='H'))
    o.append(mcq(
        'BayesNet',
        'Local Markov condition in a BN: a node is independent of its non-descendants given',
        'its parents',
        'its children',
        'the empty set always',
        'all variables',
        'A',
        'P(node | parents, non-descendants) = P(node | parents).',
        marks=1, diff='M'))
    o.append(mcq(
        'BayesNet',
        'd-separation is a graphical test for',
        'conditional independences implied by the DAG (Markov condition)',
        'minimax values',
        'CNF tautology',
        'A* consistency',
        'A',
        'Sound (and complete for faithful distributions).',
        marks=1, diff='E'))
    o.append(nat(
        'BayesNet',
        'A chain of 4 binary nodes A->B->C->D, each CPT with 2 free params except A with 1. Free parameter count using 1-p normalisation: 1+2+2+2= ____.',
        '7',
        'Root 1, three 2-row CPTs with 2 free each? Wait each child given 1 parent has 2 params (P(child=1|parent=0) and P(child=1|parent=1)), root 1, total 7.',
        marks=2, diff='M'))
    o.append(mcq(
        'BayesNet',
        "If a BN's DAG is fully connected (topological complete DAG), the number of free parameters is",
        'the same order as an unconstrained joint (no CI savings)',
        'always 1',
        'always |V|',
        'zero',
        'A',
        'No missing edges => no CI.',
        marks=1, diff='M'))
    o.append(mcq(
        'BayesNet',
        'Moralisation of a DAG (for conversion to an undirected Markov network) adds edges between',
        'co-parents (nodes sharing a child) then drops directions',
        'all non-adjacent pairs',
        'leaves only',
        'roots only',
        'A',
        'Marry the parents, then undirect.',
        marks=2, diff='H'))
    o.append(nat(
        'BayesNet',
        'Binary node with 3 binary parents. CPT rows: 2^3 = ____.',
        '8',
        'One row per parent configuration.',
        marks=1, diff='E'))
    o.append(nat(
        'BayesNet',
        'That CPT with 1-p normalisation has how many free parameters?',
        '8',
        'One free prob per row, 8 rows.',
        marks=1, diff='M'))
    o.append(mcq(
        'BayesNet',
        'A v-structure (collider) A->C<-B with A not adjacent to B is the pattern that',
        'distinguishes essential graph orientation in many structure-learning arguments',
        'is illegal in BNs',
        'forces A ? B | C',
        'equals a chain',
        'A',
        'Unshielded collider.',
        marks=2, diff='H'))
    o.append(msq(
        'BayesNet',
        'Named factorisation P(X)P(Y)P(Z|X,Y). Which independences are implied?',
        'X ? Y  (no edge, no common child observed)',
        'X ? Z | Y  is not implied (X is a parent of Z)',
        'X not? Z',
        'Z ? Y | X  is not implied (Y is a parent of Z)',
        'A;C',
        'X and Y are marginally independent; each is dependent with Z. B and D are false claims of CI.',
        marks=2, diff='H'))
    o.append(mcq(
        'BayesNet',
        'Flu -> Fever, Flu -> Cough. Observing Flu, Fever ? Cough if there is no other path. This is a',
        'fork blocked by observing the common cause',
        'collider opening',
        'chain through Fever to Cough',
        'uninformed search',
        'A',
        'Common-cause independence given the cause.',
        marks=1, diff='M'))
    o.append(mcq(
        'VarElim',
        'Variable elimination computes a marginal by',
        'summing out hidden variables one at a time, multiplying and summing factors',
        'drawing Gibbs samples only',
        'running A* on the DAG',
        'converting the BN to CNF and SAT-solving always',
        'A',
        'Exact inference by factor algebra.',
        marks=1, diff='E'))
    o.append(mcq(
        'VarElim',
        'VE is an exact inference algorithm, whereas Gibbs sampling is',
        'approximate (MCMC)',
        'also exact after one sample',
        'uninformed search',
        'resolution',
        'A',
        'Contrast asked in GATE-style.',
        marks=1, diff='E'))
    o.append(mcq(
        'VarElim',
        'The complexity of VE is governed mainly by',
        'the size of the largest intermediate factor (induced width / treewidth related)',
        'only the number of edges, never clique size',
        'the minimax depth',
        'the CNF length',
        'A',
        'Large factors blow up.',
        marks=1, diff='M'))
    o.append(nat(
        'VarElim',
        'Factors f(A,B) and g(B,C) on binary vars. Their product h(A,B,C) has how many entries?',
        '8',
        '2^3=8.',
        marks=1, diff='M'))
    o.append(nat(
        'VarElim',
        'Summing h(A,B,C) over C (binary) yields a factor on A,B with how many entries?',
        '4',
        '2^2=4.',
        marks=1, diff='E'))
    o.append(mcq(
        'VarElim',
        'Elimination order can change',
        'intermediate factor sizes (efficiency) but not the exact answer (in exact arithmetic)',
        'the exact numerical marginal always',
        'd-separation',
        'the DAG edges',
        'A',
        'Associativity of sum/product; cost depends on order.',
        marks=2, diff='M'))
    o.append(mcq(
        'VarElim',
        'To compute P(Q | e) by VE one typically',
        'reduces factors by evidence, eliminates hidden vars, then normalises the remaining factor on Q',
        'ignores evidence',
        'runs DFS on the moral graph only',
        'uses hinge loss',
        'A',
        'Standard VE query.',
        marks=1, diff='M'))
    o.append(nat(
        'VarElim',
        'A factor on 5 binary variables has size ____.',
        '32',
        '2^5=32.',
        marks=1, diff='E'))
    o.append(msq(
        'VarElim',
        'Which claims about VE versus sampling are TRUE?',
        'VE is exact (modulo numeric precision)',
        'Gibbs is approximate MCMC',
        'VE can be infeasible when treewidth is large even if n is moderate',
        'Gibbs always returns the exact marginal after 2 samples',
        'A;B;C',
        'A few Gibbs samples do not give exactness.',
        marks=2, diff='M'))
    o.append(mcq(
        'VarElim',
        'Pointwise product of factors f(X,Y) and g(Y,Z) is defined on',
        'the union of scopes {X,Y,Z}',
        'the intersection {Y} only',
        'the empty scope',
        'CNF clauses',
        'A',
        'Scope union.',
        marks=1, diff='E'))
    o.append(mcq(
        'VarElim',
        'Summing out Y from f(X,Y) produces a factor on',
        'X',
        'Y',
        'X,Y still',
        'nothing always empty',
        'A',
        'Marginalisation drops Y.',
        marks=1, diff='E'))
    o.append(nat(
        'VarElim',
        'Chain A-B-C all binary. Eliminating B from f(A,B)*g(B,C) produces a factor of size ____.',
        '4',
        'Scope {A,C}, size 4.',
        marks=2, diff='M'))
    o.append(mcq(
        'VarElim',
        'A bad elimination order on a grid-like BN can create',
        'factors whose scope is a long cutset, exponential in the cut width',
        'only size-2 factors always',
        'CNF tautologies',
        'A* nodes',
        'A',
        'Induced width depends on order.',
        marks=2, diff='H'))
    o.append(mcq(
        'VarElim',
        'Evidence V=v is incorporated in VE by',
        'restricting factors whose scope includes V to the slice V=v',
        'adding a random CPT',
        'dropping the DAG',
        'running minimax',
        'A',
        'Factor reduction / observation.',
        marks=1, diff='M'))
    o.append(nat(
        'VarElim',
        'Binary Q with unnormalised VE result [2, 6]. P(Q=1) after normalising is ____.',
        '0.75',
        '6/(2+6)=0.75.',
        marks=2, diff='M'))
    o.append(nat(
        'VarElim',
        'Unnormalised [1,1,2] on a 3-value var. P(first value) is ____.',
        '0.25',
        '1/4=0.25.',
        marks=1, diff='M'))
    o.append(mcq(
        'VarElim',
        'If all hidden variables are summed out and Q is binary, the remaining factor has',
        '2 entries (then normalised to a Bernoulli)',
        '2^n entries always',
        '0 entries',
        'n leaves of a game tree',
        'A',
        'Scope {Q}.',
        marks=1, diff='E'))
    o.append(msq(
        'VarElim',
        'Exact inference algorithms in the GATE DA uncertainty syllabus include',
        'variable elimination',
        'enumeration of the joint (brute force)',
        'Gibbs sampling as an exact closed form',
        'likelihood weighting as an exact closed form',
        'A;B',
        'Sampling methods are approximate. Enumeration is exact but exponential.',
        marks=2, diff='M'))
    o.append(mcq(
        'VarElim',
        'VE on a polytree (singly connected BN) with a good order is',
        'polynomial in the CPT sizes (belief propagation style)',
        'always exponential in n regardless of structure',
        'undecidable',
        'the same as alpha-beta',
        'A',
        'Treewidth 1 / polytree.',
        marks=2, diff='H'))
    o.append(nat(
        'VarElim',
        'Product of two factors each of size 4, scopes {A,B} and {A,B} (same scope, binary). Result size is ____.',
        '4',
        'Same scope, still 4 entries.',
        marks=1, diff='M'))
    o.append(mcq(
        'Sampling',
        'Prior (ancestral) sampling from a BN draws each node',
        'in topological order from P(node | already sampled parents)',
        'in reverse topological order always',
        'uniformly ignoring CPTs',
        'by minimax',
        'A',
        'Forward sampling.',
        marks=1, diff='E'))
    o.append(mcq(
        'Sampling',
        'Rejection sampling for P(Q|e) draws ancestral samples and',
        'throws away any sample inconsistent with evidence e, then histograms Q on the rest',
        'weights every sample by 1 regardless of evidence',
        'never uses the CPTs',
        'solves VE factors',
        'A',
        'Classic rejection.',
        marks=1, diff='E'))
    o.append(mcq(
        'Sampling',
        'Likelihood weighting, compared with rejection on a tiny BN with rare evidence,',
        'never rejects: it clamps evidence nodes and multiplies a weight P(e_i | parents)',
        'rejects more often than plain rejection',
        'is exact after one sample always',
        'requires a closed-form VE factor',
        'A',
        'LW is designed for rare evidence.',
        marks=1, diff='M'))
    o.append(msq(
        'Sampling',
        'On the tiny Rain->Wet BN, evidence Wet=true (a child). Which are TRUE?',
        'Rejection sampling discards worlds with Wet=false',
        'Likelihood weighting sets Wet=true and weights by P(Wet=true | Rain)',
        'Both methods (with infinite samples) can estimate P(Rain | Wet=true)',
        'VE is approximate here while LW is exact in finite samples',
        'A;B;C',
        'VE is the exact one; LW is approximate in finite samples.',
        marks=2, diff='H'))
    o.append(mcq(
        'Sampling',
        'Gibbs sampling in a BN is a Markov chain that, at each step, resamples one variable from',
        'its full conditional given the current values of all other variables (or the Markov blanket)',
        'the prior P(node) ignoring the rest',
        'a uniform coin always',
        'A* f-values',
        'A',
        'MCMC Gibbs update.',
        marks=1, diff='M'))
    o.append(mcq(
        'Sampling',
        'The Markov blanket of a node in a BN is',
        'parents, children, and co-parents (other parents of the children)',
        'only the parents',
        'all non-descendants',
        'the empty set always',
        'A',
        'd-separated from the rest given the blanket.',
        marks=1, diff='M'))
    o.append(nat(
        'Sampling',
        'Rejection sampling: 100 ancestral draws, 40 match evidence, of those 10 have Q=true. Estimate of P(Q=true|e) is ____.',
        '0.25',
        '10/40=0.25.',
        marks=2, diff='M'))
    o.append(nat(
        'Sampling',
        'Likelihood weighting: two samples with weights 0.2 and 0.6, Q values true and true. Weighted estimate of P(Q=true) is ____.',
        '1',
        'Both samples have Q=true, so 1.',
        marks=1, diff='E'))
    o.append(nat(
        'Sampling',
        'LW: weights 0.2 (Q=1) and 0.6 (Q=0). Estimate of P(Q=1) is ____.',
        '0.25',
        '0.2/(0.2+0.6)=0.25.',
        marks=2, diff='M'))
    o.append(mcq(
        'Sampling',
        'If evidence is a root node, ancestral rejection versus clamping that root',
        'wastes draws that do not match the root; clamping the root is just sampling from the posterior slice and is exact in distribution for descendants',
        'is identical to minimax',
        'cannot be done',
        'requires CNF',
        'A',
        'Evidence at roots is easy: just fix them.',
        marks=2, diff='H'))
    o.append(msq(
        'Sampling',
        'Which are approximate inference methods in the GATE DA syllabus?',
        'rejection sampling',
        'likelihood weighting',
        'Gibbs sampling',
        'variable elimination',
        'A;B;C',
        'VE is exact.',
        marks=2, diff='M'))
    o.append(mcq(
        'Sampling',
        'Gibbs sampling needs a burn-in because',
        'the chain starts from an arbitrary state and only approaches the target posterior after mixing',
        'VE factors must warm up',
        'alpha-beta cutoffs burn nodes',
        'CNF conversion is random',
        'A',
        'MCMC mixing.',
        marks=1, diff='M'))
    o.append(nat(
        'Sampling',
        'Three Gibbs samples of a binary Q after burn-in: 1,0,1. Estimate of P(Q=1) is ____.',
        '2/3',
        'Two 1s out of 3.',
        marks=1, diff='E'))
    o.append(mcq(
        'Sampling',
        'A problem with rejection sampling when P(e) is 10^{-6} is',
        'almost every sample is thrown away, so the estimator is high-variance / starved',
        'the method becomes exact too quickly',
        'VE is then approximate',
        'd-separation fails',
        'A',
        'Rare evidence kills rejection.',
        marks=1, diff='M'))
    o.append(mcq(
        'Sampling',
        'Likelihood weighting still has high variance when',
        'evidence nodes are deep descendants with unlikely values given randomly sampled parents',
        'there is no evidence',
        'the BN has one node',
        'all weights equal 1 and evidence is a root that was clamped consistently',
        'A',
        'Parents sampled from the prior, not the posterior, can make weights tiny.',
        marks=2, diff='H'))
    o.append(nat(
        'Sampling',
        'Ancestral sample on A->B with P(A=1)=0.5, P(B=1|A=1)=1, P(B=1|A=0)=0. Draw A=1 then B is ____.',
        '1',
        'Deterministically 1.',
        marks=1, diff='E'))
    o.append(mcq(
        'Sampling',
        'Importance-sampling view: LW is importance sampling whose proposal',
        'samples non-evidence nodes from the prior CPTs with evidence clamped',
        'samples from the exact posterior always',
        'samples uniformly in {0,1}^n ignoring CPTs',
        "is Gibbs' full conditional",
        'A',
        'Proposal = prior with evidence fixed.',
        marks=2, diff='H'))
    o.append(mcq(
        'Sampling',
        'To estimate P(Wet=true) with no evidence on WetGrass, the most direct sampler is',
        'ancestral (prior) sampling, no rejection needed',
        'rejection with empty evidence still throwing 50%',
        'alpha-beta',
        'resolution',
        'A',
        'Forward sampling estimates any prior marginal.',
        marks=1, diff='M'))
    o.append(nat(
        'Sampling',
        'Prior sampling 20 draws of Rain, 4 are true. Estimate of P(Rain=true) is ____.',
        '0.2',
        '4/20=0.2.',
        marks=1, diff='E'))
    o.append(msq(
        'Sampling',
        'Comparing VE, LW, and Gibbs on a 5-node binary Alarm net for P(B | J=true, M=true):',
        'VE can compute the exact rational (or floating) value from the CPTs',
        'LW gives a weighted Monte Carlo estimate',
        'Gibbs gives an MCMC estimate using Markov-blanket updates',
        'all three are guaranteed to match to 10 decimals after 2 samples',
        'A;B;C',
        'Two samples do not certify 10-decimal agreement.',
        marks=2, diff='M'))
    o.append(mcq(
        'Sampling',
        'A valid Gibbs update for node X given the rest uses only',
        "X's Markov blanket values (parents, children, co-parents)",
        'the leaves of a game tree',
        'CNF clauses of X',
        'the A* open list',
        'A',
        'Full conditional factorises on the blanket.',
        marks=1, diff='M'))
    o.append(nat(
        'Sampling',
        'LW weight for evidence child E=true with P(E=true|parents)=0.3 is a factor ____.',
        '0.3',
        'Multiply by that CPT entry.',
        marks=1, diff='E'))
    o.append(mcq(
        'Sampling',
        'If every LW sample has weight 0, the usual cause is',
        'the clamped evidence is impossible given the sampled parents (CPT zeros)',
        'VE failed',
        'the DAG has no edges and evidence is a root with P=1',
        'minimax pruned the BN',
        'A',
        'Hard zeros in CPTs.',
        marks=1, diff='M'))
    o.append(mcq(
        'Sampling',
        'Mixing of Gibbs is slow when variables are',
        'strongly dependent (tight CPTs / near-deterministic relations)',
        'all independent (then Gibbs is unnecessary but mixes immediately)',
        'absent',
        'CNF atoms',
        'A',
        'Strong coupling => slow MCMC.',
        marks=1, diff='M'))
    o.append(nat(
        'Sampling',
        'Rejection: 50 samples, 0 consistent with evidence. The number of usable samples for the histogram is ____.',
        '0',
        'All rejected.',
        marks=1, diff='E'))
    o.append(mcq(
        'Sampling',
        "An unbiasedness remark: rejection sampling's histogram on accepted samples is unbiased for P(Q|e) (given at least one accept). LW's weighted average is",
        'also unbiased for P(Q|e) (self-normalised LW is consistent, slightly biased in finite samples)',
        'exact for n=1 always',
        'a minimax value',
        'a tautology',
        'A',
        'Self-normalised importance sampling is consistent.',
        marks=2, diff='H'))
    o.append(mcq(
        'UninformedSearch',
        'A librarian wants a cheapest rupee-cost walk on a metro map with unequal fares. The uninformed algorithm that returns an optimal path is',
        'uniform-cost search',
        'DFS',
        'greedy best-first with h=straight-line',
        'depth-limited search with L=1',
        'A',
        'Unequal nonnegative costs: UCS.',
        marks=1, diff='M'))
    o.append(mcq(
        'InformedSearch',
        'Two admissible heuristics for a campus map: h_walk = walking minutes lower bound, h_crow = crow-flies minutes. A* should use',
        'max(h_walk, h_crow), still admissible and dominating',
        'h_walk + h_crow always',
        'min of them only, never max',
        'their product',
        'A',
        'Max of admissible remains admissible.',
        marks=2, diff='M'))
    o.append(nat(
        'Adversarial',
        'MAX root children are terminals 8, -2, 5. Best move value is ____.',
        '8',
        'MAX picks 8.',
        marks=1, diff='E'))
    o.append(mcq(
        'PropLogic',
        "Which search problem is uninformed among: (i) BFS on a formula's implication graph, (ii) A* with a SAT heuristic. The uninformed one is",
        '(i) BFS',
        '(ii) A*',
        'both informed',
        'neither a search',
        'A',
        'BFS remains uninformed even if the graph encodes logic.',
        marks=1, diff='M'))
    o.append(mcq(
        'FOL',
        'Sentence X: forall x (Bird(x) -> Flies(x)). Sentence Y: Bird(Tweety) -> Flies(Tweety). Then',
        'X entails Y',
        'Y entails X',
        'neither entails the other',
        'X is unsatisfiable',
        'A',
        'UI on Tweety.',
        marks=1, diff='E'))
    o.append(mcq(
        'BayesNet',
        "Named factorisation P(Cloudy)P(Rain|Cloudy)P(Sprinkler|Cloudy)P(Wet|Rain,Sprinkler). Wet's parents are",
        'Rain and Sprinkler',
        'only Cloudy',
        'the empty set',
        'every variable',
        'A',
        'Read off the conditioning.',
        marks=1, diff='E'))
    o.append(nat(
        'VarElim',
        'After eliminating all hidden vars, unnormalised [5, 15] for binary Q. P(Q=1) is ____.',
        '0.75',
        '15/20=0.75.',
        marks=1, diff='M'))
    o.append(mcq(
        'Sampling',
        'On a two-node BN A->E with evidence E=true, likelihood weighting draws A from P(A) then',
        'sets E=true and weights by P(E=true|A)',
        'rejects if A=false always',
        'runs minimax on A',
        'unifies A with E',
        'A',
        'Canonical one-edge LW.',
        marks=2, diff='M'))
    o.append(mcq(
        'Sampling',
        'Metropolis-Hastings is a general MCMC; Gibbs is the special case where the proposal is',
        'the full conditional, so the acceptance probability is 1',
        'uniform over the whole joint always without conditionals',
        'A* with h=0',
        'unit-clause propagation',
        'A',
        'Gibbs acceptance = 1.',
        marks=2, diff='H'))
    o.append(mcq(
        'UninformedSearch',
        'Romania-style: Arad-Sibiu 140, Arad-Timisoara 118, Arad-Zerind 75. UCS from Arad expands first the neighbour of cost',
        '75 (Zerind)',
        '140 (Sibiu)',
        '118 (Timisoara)',
        '0 (Arad twice)',
        'A',
        'Least-cost fringe node Zerind.',
        marks=1, diff='M'))
    o.append(nat(
        'UninformedSearch',
        'Costs 75, 118, 140 from Arad. The g-value of the first expanded neighbour in UCS is ____.',
        '75',
        'Zerind.',
        marks=1, diff='E'))
    o.append(mcq(
        'InformedSearch',
        'Arad to Bucharest, h(Arad)=366, a step Arad-Sibiu cost 140, h(Sibiu)=253. A* f(Sibiu) via Arad is',
        '140+253=393',
        '366',
        '253',
        '140',
        'A',
        'f=g+h=393.',
        marks=2, diff='M'))
    o.append(nat(
        'InformedSearch',
        'g=140, h=253. f equals ____.',
        '393',
        '140+253=393.',
        marks=1, diff='E'))
    o.append(mcq(
        'Adversarial',
        'In alpha-beta, the pair (alpha,beta) at the root starts at',
        '(-inf, +inf)',
        '(0,0)',
        '(1,0)',
        '(h,g)',
        'A',
        'No bounds yet.',
        marks=1, diff='E'))
    o.append(nat(
        'Adversarial',
        'Depth-1 MAX with three terminals 2, 7, -4. After examining 2 then 7, alpha is ____.',
        '7',
        'max(2,7)=7.',
        marks=1, diff='M'))
    o.append(mcq(
        'PropLogic',
        'Formula (P v Q) & (~P v Q) & (P v ~Q). One satisfying assignment is',
        'P=T, Q=T  (check: T,T,T all hold? (T v T)&(~T v T)&(T v ~T)=T&T&T)',
        'P=F, Q=F  ((F v F) already false)',
        'none, it is unsat',
        'only Q=F, P=T: (T v F)&(~T v F)&(T v T)= T & F & T = F',
        'A',
        'P=T,Q=T works. P=F,Q=T: (F v T)&(T v T)&(F v F)= T&T&F=F. So unique model TT? P=T,Q=F fails as above. Unique TT.',
        marks=2, diff='H'))
    o.append(nat(
        'PropLogic',
        'That formula (P v Q)&(~P v Q)&(P v ~Q) has how many models on {P,Q}?',
        '1',
        'Only TT, as FF, FT, TF fail.',
        marks=2, diff='H'))
    o.append(mcq(
        'FOL',
        'From forall x ~Likes(x,x) one may infer',
        '~Likes(John,John)',
        'Likes(John,John)',
        'exists x Likes(x,x)',
        'forall x Likes(x,x)',
        'A',
        'UI + the negated atom.',
        marks=1, diff='E'))
    o.append(mcq(
        'BayesNet',
        'In Alarm, JohnCalls is a descendant of Alarm. J ? E | A holds because the path J-A-E is a',
        'chain/fork through A, blocked by observing A',
        'collider at A that opens',
        'direct edge J-E',
        'cycle',
        'A',
        'J <- A <- E is a chain blocked at A; also J <- A -> ... no E. Path J-A-E is A as middle of a chain from E to J? E->A->J is a chain, blocked by A.',
        marks=2, diff='M'))
    o.append(nat(
        'VarElim',
        'Eliminating a binary var from a factor of scope 3 binaries (size 8) yields size ____.',
        '4',
        '2^{2}=4.',
        marks=1, diff='E'))
    o.append(mcq(
        'Sampling',
        'Gibbs versus VE on Alarm P(B|J,M): after 10^7 well-mixed Gibbs samples the histogram',
        'approximates the same number VE would compute exactly from the CPTs',
        'is always 0.5 regardless of CPTs',
        'solves SAT',
        'returns a tautology',
        'A',
        'MCMC consistency vs exact VE.',
        marks=2, diff='M'))
    return uniq(o)
