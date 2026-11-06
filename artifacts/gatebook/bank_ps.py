from helpers import mcq, msq, nat, uniq


def items():
    o = []
    o.append(mcq(
        'P&S / counting',
        'A lab has 8 data scientists and 6 engineers. A review panel of 5 is formed with at least 2 engineers. The number of possible panels is',
        '1526',
        '2002',
        '560',
        '56',
        'A',
        'Count panels by number of engineers e=2,3,4,5: C(8,5-e)C(6,e). Sum equals 1526.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / counting',
        'Seven distinct faculty sit around a circular conference table. Two particular faculty refuse to sit next to each other. The number of distinct seating arrangements, treating rotations as identical, is',
        '480',
        '3600',
        '240',
        '720',
        'A',
        'Circular arrangements of 7 are 6!. Treat the pair as glued: 2*5!. Subtract to get 6!-2*5! = 480.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / counting',
        'From a standard 52-card deck, a 5-card hand is dealt. The number of hands that are flushes (all five cards of one suit, including straight flushes) is',
        '5148',
        '5108',
        '649740.0',
        '0',
        'A',
        'Choose suit in 4 ways then 5 ranks from 13: 4*C(13,5)=5148. (Straight-flush exclusion is not asked.)',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / counting',
        'A reading list is formed by choosing 3 books from 5 distinct ML texts, 4 distinct systems texts, and 3 distinct theory texts, with at least one ML text. The number of lists (order does not matter) is',
        '185',
        '10',
        '220',
        '105',
        'A',
        'Total C(12,3) minus lists with no ML book C(7,3) = 220-35=185.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / counting',
        'Let S be a 4-element set. The number of functions f: S -> S that are bijections AND satisfy f(f(x))=x for every x in S (involutions that are permutations) is',
        '10',
        '24',
        '4',
        '16',
        'A',
        '',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / counting',
        'There are 6 distinct courses. The number of ways to assign each course a slot in {morning, afternoon, evening} so that every slot is used at least once is',
        '540',
        '729',
        '20',
        '216',
        'A',
        'Onto functions from 6 courses to 3 slots: 3^6 - C(3,1)2^6 + C(3,2)= 729-192+3=540.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / counting',
        'A fair coin is tossed until the first head appears, but at most 4 tosses are made. The size of the sample space if an outcome is recorded as a finite string over {H,T} (stopping at H or at 4 tosses) is',
        '5',
        '16',
        '4',
        '8',
        'A',
        'Outcomes: H, TH, TTH, TTTH, TTTT. Five atoms.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / axioms',
        'A finite sample space Omega = {omega1, omega2, omega3} has P({omega1})=0.2 and P({omega2})=0.5. Which assignment is the only one compatible with Kolmogorov axioms?',
        'P({omega3})=0.3',
        'P({omega3})=0.7',
        'P({omega3})=-0.3',
        'P(Omega)=0.7',
        'A',
        'Non-negativity and P(Omega)=1 force P({omega3})=1-0.2-0.5=0.3.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / axioms',
        'For events A,B with P(A)=0.6, P(B)=0.7, the smallest possible value of P(A n B) is',
        '0.3',
        '0',
        '0.42',
        '0.6',
        'A',
        'Frechet bound: P(A n B) >= P(A)+P(B)-1 = 0.3.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / axioms',
        'For events A,B with P(A)=0.6, P(B)=0.7, the largest possible value of P(A n B) is',
        '0.6',
        '0.7',
        '1.3',
        '0.42',
        'A',
        'P(A n B) <= min(P(A),P(B))=0.6.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / axioms',
        'Consider statements about a probability measure P on a sample space Omega. (i) P(empty set)=0. (ii) If A subset B then P(A) <= P(B). Which option is correct?',
        'Both (i) and (ii) are true',
        '(i) true, (ii) false',
        '(i) false, (ii) true',
        'Both false',
        'A',
        'Both are standard consequences of Kolmogorov axioms (monotonicity and empty-set probability).',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / axioms',
        'Two events A and B satisfy P(A u B)=P(A)+P(B). This equality holds if and only if',
        'P(A n B)=0',
        'A and B are independent',
        'P(A)=P(B)',
        'A subset B',
        'A',
        'Additivity of P on a union requires the intersection to be null (almost surely disjoint).',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / axioms',
        'A die with faces {1,2,3,4,5,6} is loaded so that P(face k) is proportional to k. Then P(even face) equals',
        '12/21',
        '1/2',
        '9/21',
        '6/21',
        'A',
        'Weights 1+...+6=21; even faces 2+4+6=12, so 12/21.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / independence',
        'Events A,B satisfy P(A)=0.4, P(B)=0.5. They CANNOT be both mutually exclusive and independent because',
        'independence needs P(A n B)=0.2 while exclusivity needs P(A n B)=0',
        '0.4+0.5>1',
        'P(Omega) would fail',
        'they would have to be the same event',
        'A',
        'Independent nonempty-probability events have positive intersection probability P(A)P(B)>0, hence cannot be disjoint.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / independence',
        'Two fair coins are tossed independently. Let A = first coin is heads, B = second coin is heads, C = the two coins show different faces. Then',
        'A,B,C are pairwise independent but not mutually independent',
        'A,B,C are mutually independent',
        'A and C are disjoint',
        'P(A n B n C)=1/4',
        'A',
        'Pairwise: each pair has P=1/4 = (1/2)(1/2). But A n B n C is empty (two heads cannot differ), so P(A n B n C)=0 != 1/8.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / independence',
        'If A and B are mutually exclusive and P(A)>0, P(B)>0, then P(A|B) equals',
        '0',
        'P(A)',
        '1',
        'P(A)/P(B)',
        'A',
        'A n B is empty so the conditional probability is 0. They are dependent.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / independence',
        'Let A,B be independent. Which one is NOT necessarily true?',
        'P(A u B)=P(A)+P(B)',
        'A^c and B are independent',
        'A and B^c are independent',
        'A^c and B^c are independent',
        'A',
        'Independence is preserved by complements, but the union formula without subtracting the product is exclusivity, not independence.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / independence',
        'A fair six-sided die is rolled twice independently. Let D be the event that the sum is 7 and E the event that the first roll is 3. Then P(D n E) equals',
        '1/36',
        '1/6',
        '1/12',
        '0',
        'A',
        'D n E = {(3,4)} only, probability 1/36. Also P(D)=6/36, P(E)=1/6, product 1/36, so D and E are independent.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / independence',
        'Consider (i) mutually exclusive events with positive probability are dependent; (ii) Cov(X,Y)=0 always implies X,Y independent. Which is correct?',
        '(i) true, (ii) false',
        'both true',
        'both false',
        '(i) false, (ii) true',
        'A',
        '(i) holds because P(A n B)=0 != P(A)P(B). Uncorrelated does not imply independent (classic counterexamples).',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / joint',
        'The joint PMF of (X,Y) on {0,1}x{0,1} is p(0,0)=0.1, p(0,1)=0.2, p(1,0)=0.3, p(1,1)=0.4. Then P(X=1|Y=1) equals',
        '0.4/0.6',
        '0.4',
        '0.7',
        '0.4/0.7',
        'A',
        'P(Y=1)=0.2+0.4=0.6, so P(X=1|Y=1)=0.4/0.6=2/3.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / joint',
        'A joint table of (Job type J, Delay D) is: intern: on-time 20, delayed 10; full-time: on-time 40, delayed 30 (counts). Assuming uniform over the 100 jobs, P(delayed | intern) equals',
        '1/3',
        '10/100',
        '40/70',
        '1/2',
        'A',
        'Among 30 intern jobs, 10 delayed: 10/30=1/3.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / joint',
        'Random variables X,Y have joint PMF p(x,y)=c*(x+y) for x=1,2 and y=1,2,3. The normalising constant c equals',
        '1/21',
        '1/12',
        '1/18',
        '1/9',
        'A',
        'Sum of (x+y): (2+3+4)+(3+4+5)=21, so c=1/21.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / joint',
        'X and Y are independent. X is uniform on {1,2} and Y is uniform on {0,1}. Then P(X+Y=2) equals',
        '1/2',
        '3/8',
        '1/4',
        '1/8',
        'A',
        'Favourable independent pairs: (1,1) and (2,0), each with probability 1/4, total 1/2.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / joint',
        'For a joint density f_{X,Y}(x,y), the conditional density f_{X|Y}(x|y) equals (when f_Y(y)>0)',
        'f_{X,Y}(x,y)/f_Y(y)',
        'f_X(x)',
        'f_Y(y)',
        'F_X(x)',
        'A',
        'Definition of conditional density: joint over marginal.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / joint',
        'X,Y have joint density f(x,y)=1 on the unit square (0,1)^2. Then X and Y are',
        'independent Uniform(0,1)',
        'independent but not uniform',
        'uniform but dependent',
        'neither uniform nor independent',
        'A',
        'f factors as 1*1 and each marginal is Uniform(0,1).',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / joint',
        'A joint PMF is given by the table X\\Y | 0 1 2 and rows X=0: 0.05, 0.10, 0.15; X=1: 0.10, 0.20, 0.40. Which statement is TRUE?',
        'P(Y=2 | X=1) = 0.40/0.70',
        'X and Y are independent because no cell is zero',
        'P(X=0)=0.40',
        'The table already fails to be a PMF because the entries sum to more than 1',
        'A',
        'Row X=1 sums to 0.70, so the conditional is 0.40/0.70. Entries sum to 1.00 so it is a PMF; independence would need a product structure (fails: 0.05 vs 0.15*0.30? P(X=0)=0.30, P(Y=0)=0.15, product 0.045 != 0.05).',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / joint',
        'Let f_{X,Y}(x,y)=e^{-x-y} for x>0, y>0. Then X and Y are',
        'i.i.d. Exponential(1)',
        'jointly uniform',
        'dependent exponentials',
        'i.i.d. Normal',
        'A',
        'The joint factors as e^{-x} e^{-y} on the positive quadrant.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / Bayes',
        'Two factories ship phones. Factory F1 ships 2000 phones with 2% defective; F2 ships 3000 phones with 6% defective. A phone is drawn uniformly from the 5000 and is defective. P(it came from F1) is closest to',
        '0.18',
        '0.40',
        '0.02',
        '0.50',
        'A',
        'Defectives: 40 from F1, 180 from F2. P(F1|D)=40/220 ~ 0.182.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / cond-exp',
        'A two-stage experiment draws Y then X. The law of total expectation identifies E[X] with',
        'E[E[X|Y]]',
        'E[X|Y]',
        'Var(E[X|Y])',
        'E[X^2]',
        'A',
        'Tower property: E[E[X|Y]]=E[X].',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / cond-exp',
        'For a square-integrable response X and a discrete grouping variable Y, the law of total variance expands Var(X) as',
        'E[Var(X|Y)] + Var(E[X|Y])',
        'E[Var(X|Y)] only',
        'Var(E[X|Y]) only',
        'E[X^2] - E[X]',
        'A',
        'Var(X)=E[Var(X|Y)]+Var(E[X|Y]).',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / cond-exp',
        'X is Poisson(lambda). Then E[X(X-1)] equals',
        'lambda^2',
        'lambda',
        'lambda^2 + lambda',
        'lambda^2 - lambda',
        'A',
        'Falling factorial: E[X(X-1)]=lambda^2 for Poisson.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / cond-exp',
        'Let Z = a + bX + error with E[error]=0 and E[error(X-E[X])]=0. Given E[X]=1, Var(X)=4, Cov(Z,X)=-2 and E[Z]=3, the pair (a,b) is',
        'a=3.5, b=-0.5',
        'a=-2, b=1',
        'a=2, b=-1',
        'a=3, b=-2',
        'A',
        'b=Cov(Z,X)/Var(X)=-2/4=-1/2. Then E[Z]=a+b E[X] => 3=a-0.5 => a=3.5.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / cond-exp',
        'If E[X|Y]=c almost surely for a constant c, then',
        'E[X]=c and Cov(X,Y)=0',
        'X is independent of Y necessarily',
        'Var(X)=0',
        'X=c almost surely',
        'A',
        'Tower gives E[X]=c. Also E[XY]=E[E[X|Y] Y]=c E[Y] so Cov=0. Independence and degeneracy need not hold.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / cond-exp',
        'A biased coin with P(H)=1/3 is tossed independently until two consecutive heads appear. The expected number of tosses is',
        '12',
        '6',
        '9',
        '3',
        'A',
        'States 0,1,2=done. e0=1+(2/3)e0+(1/3)e1, e1=1+(2/3)e0+(1/3)*0. Solve: e1=1+(2/3)e0, e0=1+(2/3)e0+(1/3)+(2/9)e0 => (1/9)e0=4/3 => e0=12.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / descriptive',
        'The sample average of 40 observations is 25. After including a new observation 65, the updated sample average is',
        '26',
        '30',
        '25.5',
        '45',
        'A',
        '(40*25+65)/41=1065/41=26.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / descriptive',
        'Incomes have min 40, max 160, mean 88, sd 16 (all in thousands). The z-score of income 104 is',
        '1',
        '(104-40)/(160-40)',
        '(104-88)/160',
        '0.1',
        'A',
        'z=(104-88)/16=1. Min/max are distractors (min-max scaling).',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / descriptive',
        'For a unimodal right-skewed histogram of positive waiting times, which ordering is typical?',
        'mode < median < mean',
        'mean < median < mode',
        'mean = median = mode',
        'mode < mean < median always fails',
        'A',
        'Right skew pulls the mean toward the long right tail.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / descriptive',
        'Five integers from 0 to 20 (repetitions allowed) have mean 10, median 12, and a unique mode 14. Which statement is TRUE?',
        'After sorting x1<=x2<=x3<=x4<=x5 we must have x3=12, the unique mode 14 appears at least twice, and the mean constraint is  x1+...+x5=50',
        'The unique mode must be the median',
        'All five integers must equal 10',
        'Such a sample is impossible because mode 14 > median 12',
        'A',
        'Median is the middle of five. A unique mode 14 must occur more often than others and at least twice, which is compatible with median 12 if 14 occupies the upper end. Mean 10 is a sum constraint, not impossibility.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / covariance',
        'Which statement is TRUE for finite-variance random variables?',
        'Independent => Cov=0, but Cov=0 need not imply independent',
        'Cov=0 => independent',
        'Var(X+Y)=Var(X)+Var(Y) always',
        'Corr is defined even if Var(X)=0',
        'A',
        'Independence implies uncorrelatedness; the converse fails. Additivity of variance needs uncorrelatedness. Correlation needs positive variances.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / covariance',
        'Let X~Bernoulli(p) and Y=1-X. Then Corr(X,Y) equals',
        '-1',
        '1',
        '0',
        'p(1-p)',
        'A',
        'Y is an affine decreasing function of X with slope -1, so correlation is -1 (for 0<p<1).',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / covariance',
        'X~Uniform(-1,1) and Y=X^2. Then Corr(X,Y) equals',
        '0',
        '1',
        '-1',
        '1/2',
        'A',
        'X is symmetric about 0 and Y is even, so E[XY]=E[X^3]=0=E[X]E[Y]. Uncorrelated but dependent.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / covariance',
        'X~Uniform(-1,1). Given X=x, Y is Uniform(x^2-0.2, x^2+0.2). Then Corr(X,Y) equals',
        '0',
        '1',
        '-1',
        '0.2',
        'A',
        'E[Y|X]=X^2, so E[XY]=E[X^3]=0 and E[X]=0, hence Cov=0.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / covariance',
        'The correlation matrix of a non-degenerate random vector must be',
        'symmetric positive semidefinite with ones on the diagonal',
        'orthogonal',
        'diagonal with possibly negative entries',
        'skew-symmetric',
        'A',
        'Corr = D^{-1/2} Cov D^{-1/2} is a Gram matrix, hence SPD/PSD, with unit diagonal.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / covariance',
        'Let X,Y be independent, X~Bernoulli(0.4), Y~Normal(0, 25). Then Var((2X-1)Y) equals',
        '25',
        '10',
        '16',
        '9',
        'A',
        '(2X-1)= +/-1 with probabilities 0.4 and 0. (2X-1)^2=1, E[Y]=0 so second term 0, E[Y^2]=25. Twist on DA 2026 Q44 (which used p=0.3, var 100).',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / discrete',
        'A PMF on {1,2,3} is p(1)=c, p(2)=2c, p(3)=3c. Then c equals',
        '1/6',
        '1/3',
        '1',
        '1/2',
        'A',
        'c+2c+3c=1 => 6c=1.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / discrete',
        'Let F be the CDF of an integer-valued exam score. Which property must F satisfy?',
        'right-continuous and non-decreasing, with jumps at atoms of the law',
        'left-continuous',
        'a density',
        'strictly increasing',
        'A',
        'CDFs are always right-continuous and non-decreasing; discrete laws add jumps. They need not be left-continuous or strictly increasing.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / discrete',
        'A random variable X with PMF p(x)= (1-q) q^x for x=0,1,2,... (0<q<1) is',
        'Geometric starting at 0 with success probability 1-q',
        'Poisson(q)',
        'Binomial with n=inf',
        'Uniform',
        'A',
        'This is the Geometric(number of failures) law.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / discrete',
        'Which of the following is a valid PMF on {0,1,2}?',
        'p=(0.2, 0.3, 0.5)',
        'p=(0.2, 0.3, 0.6)',
        'p=(-0.1, 0.5, 0.6)',
        'p=(0.2, 0.2, 0.2)',
        'A',
        'Must be non-negative and sum to 1. Only (0.2,0.3,0.5) works.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / binomial',
        'X~Binomial(n=4, p=1/2). Then P(X=2)/P(X=1) equals',
        '3/2',
        '1',
        '2',
        'C(4,2)',
        'A',
        'C(4,2)/C(4,1)=6/4=3/2, and the p-powers match.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / Bernoulli',
        'A 3x3 random matrix has i.i.d. Bernoulli(1/2) entries. The probability that the first row sums to 3 (all ones) is',
        '1/8',
        '1/2',
        'C(9,3)/2^9',
        '1/27',
        'A',
        'Three independent fair bits: 2^{-3}=1/8.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / Poisson',
        'Consider (i) a Poisson random variable has equal mean and variance; (ii) a Geometric(p) random variable on {1,2,...} has equal mean and variance. Which is correct?',
        '(i) true, (ii) false',
        'both true',
        'both false',
        '(i) false, (ii) true',
        'A',
        'Poisson: mean=var=lambda. Geometric mean 1/p, variance (1-p)/p^2, equal only for special p (p= (sqrt(5)-1)/2 not generic). DA 2024 used Poisson+N(0,1); this pairs Poisson with Geometric instead.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / Poisson',
        'If X~Poisson(lambda) and Y~Poisson(mu) are independent, then the conditional law of X given X+Y=n is',
        'Binomial(n, lambda/(lambda+mu))',
        'Poisson(lambda/(lambda+mu))',
        'Binomial(n, 1/2) always',
        'Uniform{0,...,n}',
        'A',
        'Classic Poisson-binomial relationship.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / Poisson',
        'Rare independent events in 50 trials with success probability 0.02 are approximated by Poisson(lambda) with lambda equal to',
        '1',
        '50',
        '0.02',
        '2.5',
        'A',
        'np=1, the Poisson limit mean.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / continuous',
        'A waiting time X is modelled with a density f (no atoms). For any fixed a, P(X=a) equals',
        '0',
        'f(a)',
        'F(a)',
        '1',
        'A',
        'Atoms have probability 0 under a density.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / continuous',
        'Which listed property is required of every CDF F: R -> [0,1] of a real random variable?',
        'non-decreasing and right-continuous with limits 0 at -inf and 1 at +inf',
        'a density',
        'decreasing',
        'symmetric about 0',
        'A',
        'The characterisation of CDFs.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / continuous',
        'The CDF of X is 0 for x<0, x^2 for 0<=x<=1, and 1 for x>1. Then P(0.25 < X <= 0.75) equals',
        '0.5',
        '0.5625',
        '0.25',
        '0.75',
        'A',
        'F(0.75)-F(0.25)=0.5625-0.0625=0.5. Density 2x on (0,1).',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / continuous',
        'If F is the CDF of a continuous r.v. with density f, then almost everywhere',
        "F'(x)=f(x)",
        "f'(x)=F(x)",
        'F(x)=f(x)',
        'F(x)=1-f(x)',
        'A',
        'Fundamental theorem: the density is the derivative of the CDF.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / uniform',
        'X~Uniform(0,1), Y=1-X. Then (X,Y) is',
        'Uniform on the segment x+y=1, 0<x<1 (hence dependent)',
        'i.i.d. Uniform(0,1)',
        'independent with Y~Uniform(0,1) but a different copula',
        'jointly standard normal',
        'A',
        'Y is a deterministic function of X, supported on the line x+y=1.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / uniform',
        'The spacings of n i.i.d. Uniform(0,1) order statistics are distributed as',
        'normalised i.i.d. exponentials (Dirichlet(1,..,1) on the simplex)',
        'i.i.d. Uniform(0,1)',
        'i.i.d. Normal',
        'degenerate at 1/n',
        'A',
        'Classic fact: n+1 spacings including ends are like n+1 i.i.d. exp / sum.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / exponential',
        'A waiting-time model is called memoryless if P(X>s+t | X>s)=P(X>t). Which option lists memoryless laws?',
        'Exponential on (0,inf) and Geometric on {1,2,...}',
        'Binomial and Exponential',
        'Uniform(0,1) and Exponential',
        'Normal and Geometric',
        'A',
        'The memoryless laws on R+ and on N are Exponential and Geometric.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / exponential',
        'P(X>=3)=0.2 for an Exponential random variable X with mean 1/lambda. Then lambda equals',
        '(1/3) ln 5',
        'ln 5',
        'ln 0.2',
        '3 ln 5',
        'A',
        'e^{-3 lambda}=0.2 => 3 lambda = ln 5, lambda=(ln 5)/3.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / exponential',
        'X~Exponential with mean 1/ln 2. Let Y=floor(X). Then P(Y=ell) = (1-q) q^ell for ell=0,1,2,... The value of q is',
        '1/2',
        '1/4',
        'ln 2',
        '2',
        'A',
        'P(Y>=ell)=P(X>=ell)=e^{-ell ln 2}=2^{-ell}, a geometric ratio q=1/2.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / normal',
        'Z~N(0,1) and X=3Z+4. Then X is distributed as',
        'N(4, 9)',
        'N(4, 3)',
        'N(3, 4)',
        'N(4, 1)',
        'A',
        'Affine image of a Gaussian is Gaussian with mean 4 and variance 9.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / normal',
        'A z-test pivot is claimed to be standard normal. Which option correctly states the mean and variance of N(0,1)?',
        'mean 0 and variance 1',
        'mean 1 and variance 0',
        'mean 0 and variance 0',
        'mean 1 and variance 1',
        'A',
        'Definition of N(0,1).',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / normal',
        'X~N(mu, sigma^2), Z=(X-mu)/sigma. Then P(|X-mu|<sigma) equals',
        'P(|Z|<1) = 2Phi(1)-1',
        'Phi(1)',
        '1/2',
        '2Phi(sigma)-1',
        'A',
        'Standardise to a N(0,1) probability.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / normal',
        'Let Z1,Z2,Z3 be i.i.d. N(0,1) and W=Z1^2+Z2^2+Z3^2. Then Var(W) equals',
        '6',
        '3',
        '2',
        '9',
        'A',
        'W~chi^2_3, mean 3, variance 2*3=6.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / normal',
        'Independent X~N(1,4) and Y~N(2,9). Then X+Y is',
        'N(3, 13)',
        'N(3, 5)',
        'N(3, 36)',
        'not normal',
        'A',
        'Sum of independent Gaussians is Gaussian with added means and variances.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / normal',
        'The 68-95-99.7 rule says that about 95% of N(mu,sigma^2) mass lies in',
        '[mu-2sigma, mu+2sigma]',
        '[mu-sigma, mu+sigma]',
        '[0,1]',
        '[mu-3sigma, mu+sigma]',
        'A',
        'Two-sigma interval is the 95% heuristic (more precisely 1.96).',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / normal',
        'Z~N(0,1) with pdf g and CDF G; Y~t_1 with pdf h and CDF H. Let c>0 satisfy g(c)=h(c). Which statement is TRUE?',
        'G(0)=H(0)=1/2 because both densities are even',
        't_1 has lighter tails than N(0,1)',
        'G is the CDF of a Uniform(0,1)',
        'h is the N(0,1) density',
        'A',
        'Both laws are symmetric about 0 so both CDFs equal 1/2 at 0. t_1 (Cauchy) has heavier tails.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / chi-squared',
        'Noise samples Z1,...,Zk are i.i.d. N(0,1). The residual sum of squares Z1^2+...+Zk^2 follows',
        'chi^2 with k degrees of freedom',
        'N(0,k)',
        't_k',
        'Uniform(0,k)',
        'A',
        'Definition of chi^2_k.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / t-dist',
        'In the usual t construction, Z~N(0,1) is independent of V~chi^2_nu. The ratio Z/sqrt(V/nu) follows',
        't with nu degrees of freedom',
        'N(0,1)',
        'chi^2_nu',
        'F(nu,1)',
        'A',
        "Definition of Student's t.",
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / t-dist',
        'Compared with N(0,1), a t_nu density (nu finite) has',
        'heavier tails and a peak a little lower at 0',
        'lighter tails',
        'support (0,inf)',
        'mean equal to nu',
        'A',
        't is symmetric about 0 with polynomial tails; as nu->inf it approaches N(0,1).',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / t-dist',
        "Student's t with one degree of freedom is equal in law to which named distribution?",
        'standard Cauchy',
        'Exponential(1)',
        'Uniform(-1,1)',
        'chi^2_1',
        'A',
        'Student t with 1 df is Cauchy.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / chi-squared',
        'A one-sample variance CI for Normal data uses which pivotal quantity?',
        '(n-1) S^2 / sigma^2  ~ chi^2_{n-1}',
        'n S^2 / mu ~ t_{n-1}',
        'S^2 ~ N(0,1)',
        '(Xbar-mu)/S ~ chi^2',
        'A',
        'Gaussian sample variance pivot.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / t-dist',
        'A one-sample t-interval for mu (unknown sigma, Normal data) uses critical values from',
        't_{n-1}',
        'N(0,1) even for n=3',
        'chi^2_n',
        'F_{1,1}',
        'A',
        'The t pivot has n-1 degrees of freedom.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / cond-pdf',
        'X~Uniform(0,1). Given X=x, Y~Uniform(0,x). Then the joint density on 0<y<x<1 is',
        'f(x,y)=1/x',
        'f(x,y)=1',
        'f(x,y)=2',
        'f(x,y)=x',
        'A',
        'f_X(x)=1 on (0,1) and f_{Y|X}(y|x)=1/x on (0,x), product 1/x.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / cond-pdf',
        'If f_{X|Y}(x|y)=f_X(x) for (almost) all x,y in the support, then',
        'X and Y are independent',
        'X is constant',
        'Y is Normal',
        'the joint density cannot exist',
        'A',
        'Conditional equals marginal iff independence.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / cond-pdf',
        'Given Y=y, X is N(y, 1), and Y is N(0,1). Then the joint of (X,Y) is',
        'bivariate normal with Cov(X,Y)=1',
        'independent N(0,1)',
        'X~N(0,1) independent of Y',
        'degenerate on X=Y',
        'A',
        'E[X|Y]=Y so Cov(X,Y)=Var(Y)=1, Var(X)=E[Var(X|Y)]+Var(E[X|Y])=1+1=2. Bivariate Gaussian.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / CLT',
        'i.i.d. observations with mean mu and variance sigma^2 in (0,inf). For large n the sample mean Xbar is approximately',
        'N(mu, sigma^2/n)',
        'N(mu, sigma^2)',
        'chi^2_n',
        'exactly t_{n-1}',
        'A',
        'CLT scaling: variance of the mean is sigma^2/n.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / CLT',
        'Y~Binomial(200, 0.4). Using the CLT without continuity correction, P(70 <= Y <= 90) is approximately',
        'Phi(1.44)-Phi(-1.44)  because mean=80 and sd=sqrt(48)~6.93, (90-80)/6.93~1.44',
        'Phi(90)-Phi(70)',
        'Phi(1)-Phi(-1)',
        'exactly 0.5',
        'A',
        'np=80, npq=48, sd~6.928. z=(90-80)/6.928~1.44 and (70-80)/6.928~-1.44.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / CLT',
        'The Lindeberg-Lévy CLT requires which of the following as a sufficient set of hypotheses?',
        'i.i.d. with finite positive variance',
        'i.i.d. Cauchy',
        'only uncorrelated, no moment assumption',
        'finite sample size n=2',
        'A',
        'Classical CLT: i.i.d. and finite variance. Cauchy has no mean.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / CLT',
        'A de Moivre-Laplace application: n=16 independent Bernoulli(1/2). Approximate P(S=8) using a continuity correction as P(7.5<S*<8.5) where S*~N(8,4). This equals Phi((8.5-8)/2)-Phi((7.5-8)/2) = Phi(0.25)-Phi(-0.25). Using Phi(0.25)~0.5987 the approximation rounded to two decimals is',
        '0.20',
        '0.50',
        '0.40',
        '0.08',
        'A',
        '2*0.5987-1=0.1974 ~ 0.20.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / CLT',
        'Which quantity is asymptotically N(0,1) under i.i.d. finite-variance sampling, with mu, sigma known?',
        'sqrt(n) (Xbar - mu)/sigma',
        'n (Xbar - mu)',
        'Xbar - mu',
        'S^2 / sigma^2',
        'A',
        'The classical CLT statement.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / CI',
        'n i.i.d. observations with known sigma. The usual 95% z-confidence interval for the mean mu is',
        'Xbar +/- z_{0.025} * sigma/sqrt(n)',
        'Xbar +/- z_{0.025} * sigma',
        'mu +/- sigma',
        'Xbar +/- t_{n-1, 0.025} * sigma/sqrt(n)',
        'A',
        'SE is sigma/sqrt(n); z not t when sigma is known.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / CI',
        'A 99% interval with the same data is, compared with a 95% z-interval (known sigma),',
        'wider, because z_{0.005} > z_{0.025}',
        'narrower',
        'identical',
        'shifted but of equal length',
        'A',
        'Larger confidence needs a larger critical value.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / CI',
        'An approximate large-sample 95% CI for a proportion p-hat=0.4 based on n=100 uses se=sqrt(0.4*0.6/100)=0.049. Using 1.96 the interval is about',
        '(0.30, 0.50)',
        '(0.40, 0.50)',
        '(0,1)',
        '(0.35, 0.45)',
        'A',
        '0.4 +/- 1.96*0.049 ~ 0.4 +/- 0.096, i.e. about (0.30, 0.50).',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / CI',
        'Which statement about a 95% CI for mu is correct (repeated sampling interpretation)?',
        'About 95% of such random intervals contain the true mu',
        'P(mu in this already-computed interval)=0.95 as a posterior',
        'The interval always contains Xbar at an endpoint',
        'Width does not depend on n',
        'A',
        'Frequentist coverage is a property of the procedure, not of one realised interval as a posterior probability.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / CI',
        'If a 95% CI for mu is (2.1, 3.7), then a two-sided t-test of H0: mu=3 at level 5%',
        'does not reject H0',
        'rejects H0',
        'is inapplicable because 3 is an integer',
        'has p-value exactly 0.05',
        'A',
        '3 lies inside the interval, so H0 is not rejected at 5%.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / z-test',
        'A two-sided z-test of H0: mu=mu0 at level alpha (known sigma) rejects when',
        '|Z| > z_{alpha/2}',
        'Z > z_alpha only, ignoring the lower tail',
        'Z=0',
        'p-value > alpha',
        'A',
        'Two-sided rejection region is both tails.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / z-test',
        'For the z=1.5 two-sided test of H0: mu=50, using z_{0.025}=1.96, the decision at 5% is',
        'do not reject H0',
        'reject H0',
        'the test is undefined',
        'reject only the lower tail',
        'A',
        '|1.5|<1.96 so insufficient evidence against H0 at 5%.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / t-test',
        'A one-sample t-test (unknown sigma, Normal i.i.d. data) of H0: mu=mu0 uses the statistic',
        't = (Xbar-mu0)/(S/sqrt(n)) ~ t_{n-1} under H0',
        'z = (Xbar-mu0)/(sigma/sqrt(n)) with sigma replaced by 0',
        'chi^2 = n S^2',
        'F = Xbar / S',
        'A',
        'Definition of the one-sample t statistic.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / t-test',
        'For t=2 on 8 df, using the critical value t_{8, 0.025}~2.306, a two-sided 5% test',
        'does not reject H0',
        'rejects H0',
        'has p-value 0',
        'requires known sigma',
        'A',
        '|2|<2.306, so do not reject at 5%.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / t-test',
        'A two-sample unpaired t-test with equal-variance assumption uses a pooled variance estimator and df equal to',
        'n1+n2-2',
        'n1+n2',
        'n1-1 only',
        'min(n1,n2)',
        'A',
        'Two estimated means and one pooled variance: n1+n2-2.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / chi2-test',
        'A chi-squared goodness-of-fit test with k cells, probabilities fully specified (no parameter estimated), has under H0 the statistic sum (O-E)^2/E approximately',
        'chi^2_{k-1}',
        'chi^2_k',
        't_{k-1}',
        'N(0,1)',
        'A',
        'One linear constraint sum O=n, hence k-1 df.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / chi2-test',
        'A 2x2 contingency table independence test (no cell fusion) uses chi^2 with degrees of freedom',
        '1',
        '4',
        '3',
        '2',
        'A',
        '(2-1)(2-1)=1.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / chi2-test',
        'Pearson chi^2 for a 2x2 table can be written n(ad-bc)^2 / ((a+b)(c+d)(a+c)(b+d)). If a=b=c=d=10, the statistic equals',
        '0',
        'n',
        '1',
        '40',
        'A',
        'ad-bc=0, so the statistic is 0 (perfect independence in the table).',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / z-test',
        'A z-test of H0: p=0.5 vs H1: p>0.5 with n=100, p-hat=0.58 has z=(0.58-0.5)/sqrt(0.5*0.5/100)=1.6. Using z_{0.05}=1.645, at 5% one-sided we',
        'do not reject H0 (z=1.6 < 1.645)',
        'reject H0',
        'reject because p-hat>0.5',
        'cannot compute se',
        'A',
        'The statistic falls just short of the 5% critical value.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Consider (i) for X~Poisson(lambda), mean equals variance; (ii) for Z~N(0,4), mean is 0 and variance is 1. Which is correct?',
        '(i) true, (ii) false',
        'both true',
        'both false',
        '(i) false, (ii) true',
        'A',
        'Poisson mean=var. N(0,4) has variance 4, not 1..)',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Four fair coins are tossed independently. Let A be the event of at least three heads and B the event of at least three tails. Then P(A n B) equals',
        '0',
        '1/8',
        '1/2',
        '1/16',
        'A',
        'Cannot have >=3 heads and >=3 tails in 4 tosses.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'A fair six-sided die is rolled 4 times independently. P(at least one six) equals',
        '1-(5/6)^4',
        '(5/6)^4',
        '4/6',
        '1',
        'A',
        'Complement of no sixes.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Matching: Column P = memoryless continuous; Q = mean=variance; R = limits of t_n. Column 2: 1 Exponential, 2 Poisson, 3 N(0,1). The correct match is',
        'P-1, Q-2, R-3',
        'P-2, Q-1, R-3',
        'P-3, Q-2, R-1',
        'P-1, Q-3, R-2',
        'A',
        'Exponential is memoryless, Poisson has mean=var, t_n -> N(0,1).',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        "Let phi be convex and X integrable so that E[phi(X)] exists. Jensen's inequality states that",
        'phi(E[X]) <= E[phi(X)]',
        'phi(E[X]) >= E[phi(X)] always',
        'E[X^2] <= (E[X])^2',
        'Var(X)<=0',
        'A',
        'Convex: phi of mean <= mean of phi. Variance identity is the square case.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        "Assume the MGF M(t)=E[e^{tX}] exists in a neighbourhood of 0. Then M'(0) equals",
        'E[X]',
        'E[X^2]',
        'Var(X)',
        '1',
        'A',
        'The first derivative of the MGF at 0 is the mean.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Two independent Exp(1) r.v.s X,Y. Then X/(X+Y) is distributed as',
        'Uniform(0,1)',
        'Exp(1)',
        'Beta(2,1)',
        'N(0,1)',
        'A',
        'For i.i.d. Exp, the normalised first is Uniform (Dirichlet/Beta(1,1)).',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / mixed',
        'A Poisson process of rate 2 is observed for time 3. The count N(3) is distributed as',
        'Poisson(6)',
        'Poisson(2)',
        'Exp(2)',
        'Binomial(3,2)',
        'A',
        'Poisson process counts are Poisson(rate * time).',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Let I_A be the 0-1 indicator of an event A on a probability space. Then E[I_A] equals',
        'P(A)',
        'Var(A)',
        '1-P(A) only',
        'P(A)^2',
        'A',
        'Fundamental bridge: expectation of an indicator is the probability.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / multinomial',
        "A fair three-sided spinner (labels A,B,C) is spun 5 times independently. P(exactly 2 A's, 2 B's, 1 C) equals",
        '30 / 3^5',
        'C(5,2)/3^5',
        '1/3^5',
        '5/3',
        'A',
        'Multinomial: 5!/(2!2!1!) * (1/3)^5 = 30/243.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / tests',
        'In hypothesis testing, a Type I error is',
        'rejecting H0 when H0 is true',
        'rejecting H0 when H0 is false',
        'failing to reject H0 when H0 is false',
        'computing a CI instead of a test',
        'A',
        'Type I = false rejection; Type II = false non-rejection.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / tests',
        'Power of a level-alpha test against a particular alternative is',
        '1 - P(Type II error | that alternative)',
        'P(Type I error)',
        'the p-value',
        'always equal to alpha',
        'A',
        'Power = 1 - beta(alternative).',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / LLN',
        'i.i.d. Xi with finite mean mu. The weak law of large numbers states that Xbar_n converges to mu',
        'in probability',
        'almost surely only if the Xi are bounded, and never in probability otherwise',
        'in distribution to Uniform(0,1)',
        'only when the Xi are Normal',
        'A',
        'WLLN is convergence in probability. SLLN is a.s. (under slightly stronger hypotheses).',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / joint',
        'A survey of 80 students yields the counts (laptop, yes-coffee)=30, (laptop, no-coffee)=10, (no-laptop, yes-coffee)=20, (no-laptop, no-coffee)=20. P(coffee | laptop) equals',
        '30/40',
        '30/80',
        '50/80',
        '10/40',
        'A',
        'Among 40 laptop students, 30 drink coffee: 3/4.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Five i.i.d. N(0,1) r.v.s. Let S = X1^2+...+X5^2 and T = sqrt(5) Xbar. Which is TRUE?',
        'S ~ chi^2_5 and T^2 ~ chi^2_1, and S-T^2 ~ chi^2_4 independent of T',
        'S ~ N(0,5)',
        'T ~ chi^2_5',
        'S and T are equal',
        'A',
        'Cochran: sample ss splits into n(Xbar)^2 ~ chi^2_1 and residual chi^2_{n-1}, independent.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / mixed',
        'The matrix [[4, 3], [3, 1]] is claimed as a covariance matrix. This claim is',
        'false, because a 2x2 covariance must be PSD and 4*1-9=-5<0',
        'true, because it is symmetric',
        'true, because the diagonal is positive',
        'false only because 3>1',
        'A',
        'Symmetric is necessary but not sufficient: eigenvalues must be >=0, equivalently det>=0 here.',
        marks=2, diff='H',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Negative-binomial flavour: independent Bernoulli(p=1/2) trials. The number of trials T until (and including) the 3rd success has E[T] equal to',
        '6',
        '3',
        '1.5',
        '8',
        'A',
        'Sum of 3 geometric(1/2) waiting times: 3*(1/p)=6.',
        marks=1, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'A random variable X has MGF M(t)=exp(5t + 8 t^2). Then X is',
        'N(5, 16)',
        'N(5, 8)',
        'N(8, 5)',
        'Poisson(5)',
        'A',
        'Normal MGF exp(mu t + sigma^2 t^2 / 2) so sigma^2/2=8, sigma^2=16, mu=5.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Quantile: X~Exp(rate=ln 2) so median m satisfies P(X<=m)=1/2. Then m equals',
        '1',
        'ln 2',
        '2',
        '1/2',
        'A',
        'Survival e^{-(ln 2) m}=1/2 => (ln 2) m = ln 2 => m=1.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'Paired t-test vs two-sample t-test: 12 students measured before and after a workshop. The appropriate 1-sample analysis is a t-test on',
        'the 12 differences, with 11 degrees of freedom',
        '24 independent numbers, df=22',
        'the 12 before scores only',
        'a z-test with sigma=0',
        'A',
        'Pairing reduces to a one-sample t on differences; df=n-1=11.',
        marks=2, diff='M',
    ))
    o.append(mcq(
        'P&S / mixed',
        'A sample of size 5 has values 1,2,3,4,100. Compared with the mean, the median is',
        '3, and it is far less affected by the 100',
        '22, the same as the mean',
        '100',
        '1',
        'A',
        'Median is 3. Mean is 22. The outlier inflates the mean.',
        marks=1, diff='E',
    ))
    o.append(mcq(
        'P&S / mixed',
        'An ANOVA-free chi-squared: a spinner with 4 labelled faces is spun 40 times. Under fairness each expected count is 10. If all observed counts equal 10, the Pearson statistic is',
        '0, and one does not reject fairness',
        '40',
        '3',
        '10',
        'A',
        'O=E in every cell => chi^2=0.',
        marks=1, diff='E',
    ))
    o.append(msq(
        'P&S / axioms',
        'Let A,B be events in a probability space. Which of the following are ALWAYS true?',
        'P(A u B) = P(A)+P(B)-P(A n B)',
        'P(A^c) = 1-P(A)',
        'P(A n B) = P(A)P(B)',
        'P(A u B) <= P(A)+P(B)',
        'A;B;D',
        "Inclusion-exclusion and complement are axioms/theorems; Boole's inequality always holds. Product formula needs independence.",
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / independence',
        'A and B are independent with 0 < P(A),P(B) < 1. Which statements MUST be true?',
        'P(A n B)=P(A)P(B)',
        'P(A|B)=P(A)',
        'A and B are disjoint',
        'P(A u B)=P(A)+P(B)-P(A)P(B)',
        'A;B;D',
        'Independence is the product formula, which implies P(A|B)=P(A) and the inclusion-exclusion form. Disjointness would force a zero product, a contradiction.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / independence',
        'Which constructions yield independent events (assuming fair independent tosses of two coins)?',
        'A = first heads, B = second heads',
        'A = first heads, B = at least one head  (these are dependent)',
        'A = first heads, B = coins show equal faces',
        'A = empty event, B = any event',
        'A;C;D',
        "First and second heads are independent; first heads and equality: P both = 1/4 = (1/2)(1/2). Empty event is independent of everything. 'At least one head' is dependent on first heads.",
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / covariance',
        'Which claims are correct?',
        '|Corr(X,Y)| <= 1 whenever the correlation is defined',
        'Corr(aX+b, cY+d) = sign(ac) Corr(X,Y) for a,c != 0',
        'Var(X+Y) <= (sd X + sd Y)^2 always (finite variances)',
        'Cov(X,X)=0',
        'A;B;C',
        'Cauchy-Schwarz gives |rho|<=1 and the triangle inequality for sd. Affine transforms pick up the sign of the slopes. Cov(X,X)=Var(X), not 0.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / discrete',
        'Let X be integer-valued with CDF F. Which statements are correct?',
        'P(X=k)=F(k)-F(k-1) for integer k',
        'F is non-decreasing',
        'F is left-continuous',
        'F may have jump discontinuities',
        'A;B;D',
        'Standard discrete CDF facts. F is right-continuous, not left-continuous.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / continuous',
        'Let f be a PDF on R. Which properties MUST hold?',
        'f(x) >= 0 for (almost) all x',
        'int_{-inf}^{inf} f(x) dx = 1',
        'f(x) <= 1 for all x',
        'f is continuous',
        'A;B',
        'Non-negativity and unit integral. Densities may exceed 1 (e.g. Uniform(0,0.1)) and need not be continuous.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / exponential',
        'Let X~Exponential(rate=lambda). Which are true?',
        'P(X>s+t | X>s)=P(X>t) for s,t>0',
        'E[X^2]=2/lambda^2',
        'The MGF is lambda/(lambda-t) for t<lambda',
        'P(X=0)=lambda',
        'A;B;C',
        'Memoryless, second moment 2/l^2, MGF formula. A continuous law has P(X=0)=0.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / normal',
        'Let X~N(0,1). Which are true?',
        'The density is even: f(x)=f(-x)',
        'P(X>a)=P(X<-a) for all a',
        'E[X^3]=0',
        'P(X>0)=0',
        'A;B;C',
        'Standard normal is symmetric about 0, odd moments vanish, P(X>0)=1/2.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / chi-squared',
        'Let X1,...,Xn (n>=2) be i.i.d. N(0,1) and Xbar the sample mean. Which statements are correct?',
        'sum_{i=1}^n X_i^2 ~ chi^2_n',
        'sum_{i=1}^n (X_i - Xbar)^2 ~ chi^2_{n-1}',
        'X1^2 + X2^2 ~ Exponential with mean 2',
        '(sqrt(n) Xbar)^2 ~ chi^2_2',
        'A;B;C',
        'The last claim would require 2 degrees of freedom but sqrt(n) Xbar is N(0,1), so its square is chi^2_1. chi^2_2 is Exp with mean 2.',
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / t-dist',
        "Which are true for Student's t_nu as nu -> infinity?",
        't_nu converges in distribution to N(0,1)',
        'the variance of t_nu (for nu>2) tends to 1',
        't_nu becomes Uniform(-1,1)',
        'P(|t_nu|>2) tends to P(|Z|>2) for Z~N(0,1)',
        'A;B;D',
        'Standard limit of t. Variance is nu/(nu-2) -> 1.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / tests',
        'Which statements are correct about GATE-style hypothesis tests?',
        'A small p-value is evidence against H0 (under the modelling assumptions)',
        'Failing to reject H0 does not prove H0 is true',
        'z-tests require a known sigma (or a large-sample plug-in)',
        'A chi^2 GoF statistic is always exactly chi^2 even for n=5 sparse cells',
        'A;B;C',
        'p-values are not proof of H0. Chi^2 is an approximation requiring adequate expected counts.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / axioms',
        'Let A,B be events with 0<P(A)<1 and 0<P(B)<1. Which statements MUST be true?',
        'P(A u B) >= max(P(A), P(B))',
        'P(A n B) <= min(P(A), P(B))',
        'P(A|B) + P(A^c|B) = 1',
        'P(A|B) = P(B|A)',
        'A;B;C',
        'Monotonicity gives the two inequalities. Conditioning on B, A and A^c partition the space. Bayes does not force P(A|B)=P(B|A).',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / independence',
        'A fair coin is tossed twice independently. Let H1 = first toss heads, Eq = both tosses equal, Xor = tosses differ. Which of the following pairs are independent?',
        'H1 and Eq',
        'H1 and Xor',
        'Eq and Xor',
        'H1 and (H1 n Eq)',
        'A;B',
        'P(H1 n Eq)=P(HH)=1/4=P(H1)P(Eq). Same for Xor. But Eq and Xor are complementary, hence disjoint with positive probability, so dependent.',
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / Bayes',
        'A binary classifier for a rare class with prevalence 0.01 has sensitivity 0.99 and specificity 0.99. Which claims are correct?',
        'P(class=1 | predicted 1) is far below 0.99 because of the low prevalence',
        'P(predicted 1 | class=0) = 0.01',
        'Sensitivity equals P(predicted 1 | class=1)',
        'Specificity equals P(predicted 1 | class=0)',
        'A;B;C',
        'PPV is pulled down by the 99:1 prior odds. FPR=1-specificity=0.01. Specificity is P(predicted 0 | class=0), not the FPR.',
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / binomial',
        'X~Binomial(n=6, p=1/3). Which identities hold?',
        'E[X]=2',
        'Var(X)=6*(1/3)*(2/3)=4/3',
        'P(X=0)=(2/3)^6',
        'X is approximately N(2, 4/3) with no error even for n=6 (exact, not approximate)',
        'A;B;C',
        'Mean, variance and empty-success probability are exact. CLT is an approximation, not an identity for n=6.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / Poisson',
        'Let N~Poisson(lambda) with lambda>0. Which are true?',
        'P(N=0)=e^{-lambda}',
        'E[N(N-1)]=lambda^2',
        'The MGF is exp(lambda(e^t - 1))',
        'N takes values in (0, inf) with a density',
        'A;B;C',
        'Poisson is a discrete law on {0,1,2,...}; it has no density on the line. The factorial-moment and MGF formulae hold.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / normal',
        'X~N(2, 16) and Z=(X-2)/4. Which are true?',
        'Z ~ N(0,1)',
        'P(X>2)=1/2',
        'P(|X-2|<4)=P(|Z|<1)',
        'Var(X+Z)=16+1 because X and Z are independent',
        'A;B;C',
        'Z is an affine function of X, hence perfectly dependent with X; Var(X+Z)=Var(1.25 X - 0.5) is not 17.',
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / exponential',
        'Waiting times W1, W2 are i.i.d. Exponential(rate=1). Which are true?',
        'min(W1,W2) ~ Exponential(rate=2)',
        'W1+W2 ~ Gamma(shape=2, rate=1) (Erlang-2)',
        'P(W1<W2)=1/2',
        'max(W1,W2) ~ Exponential(rate=1)',
        'A;B;C',
        'Min of independent exponentials adds rates. Sum is Erlang. Symmetry gives P(W1<W2)=1/2.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / CLT',
        'Let X1,...,Xn be i.i.d. with mean mu and finite variance sigma^2>0. Which are true for large n?',
        'Xbar is approximately N(mu, sigma^2/n)',
        'sqrt(n)(Xbar-mu)/sigma is approximately N(0,1)',
        'Xbar converges in probability to mu (WLLN)',
        'Xbar is exactly t_{n-1} for every n, even if the Xi are Uniform',
        'A;B;C',
        'CLT and WLLN apply. The exact t law needs Gaussian data and an independent sample sd in the denominator, not the raw mean.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / CI',
        'n i.i.d. N(mu, sigma^2) with sigma known. A 95% z-interval I_n = Xbar +/- 1.96 sigma/sqrt(n). Which are true?',
        'P_mu(I_n contains mu)=0.95 for every n>=1',
        'The length of I_n tends to 0 as n tends to inf',
        'Replacing 1.96 by 2.58 produces a 99% interval of the same centre',
        'The interval is a posterior 95% credible set under every prior',
        'A;B;C',
        'Exact Gaussian z-interval has exact coverage. Length shrinks. Larger z widens a still-centred interval.',
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / tests',
        'In a level-alpha two-sided z-test of H0: mu=mu0 (sigma known), which are true?',
        'Type I error probability is alpha when H0 is true (under the Normal/CLT model)',
        'Power is a function of the true mu, n, sigma and alpha',
        'p-value < alpha is the same decision as rejecting at level alpha',
        'Failing to reject H0 proves mu=mu0',
        'A;B;C',
        'Standard Neyman-Pearson facts. Non-rejection is not a proof of H0.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / t-dist',
        'A one-sample t-test is applied to n=9 allegedly i.i.d. Normal observations. Which are true?',
        'Under H0 the t statistic has 8 degrees of freedom',
        'If sigma were known one would use a z-test instead',
        'Heavy-tailed true data (not Normal, small n) make the nominal 5% level untrustworthy',
        'The t critical value is smaller than the z critical value for the same tail probability',
        'A;B;C',
        't_{n-1} is heavier-tailed than N(0,1), so |t|_{crit} > z_crit. Normality matters for small n.',
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / chi2-test',
        'A Pearson chi-squared test of independence is run on an r x c table with large n. Which are true?',
        'Degrees of freedom equal (r-1)(c-1)',
        'Expected cell counts use the product of fitted marginals',
        'A large statistic (with small p) is evidence against independence',
        'The test requires the two classification variables to be Normal',
        'A;B;C',
        'It is a categorical test; Normality of the labels is not assumed. Expected counts are n * p_row * p_col under independence.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / covariance',
        'X,Y have finite positive variances. Which are true?',
        'Corr(X,Y)=Cov(X,Y)/(sdX sdY)',
        '|Corr(X,Y)|<=1',
        'Corr(X,Y)=1 iff Y=a+bX a.s. for some b>0',
        'Corr(X,Y)=0 iff X and Y are independent',
        'A;B;C',
        'Cauchy-Schwarz: |rho|=1 iff linear relation a.s. with the sign of b. Zero correlation is weaker than independence.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / cond-exp',
        'X,Y square-integrable. Which identities always hold?',
        'E[E[X|Y]]=E[X]',
        'Var(X)=E[Var(X|Y)]+Var(E[X|Y])',
        'E[X g(Y)]=E[E[X|Y] g(Y)] for bounded g',
        'E[X|Y]=E[X] almost surely even when X and Y are dependent',
        'A;B;C',
        'Tower property, law of total variance, and the defining projection property. E[X|Y]=E[X] is independence-like (mean independence), not automatic.',
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / counting',
        'Let S be a finite n-set. Which counting formulae are correct?',
        'The number of k-subsets is C(n,k)',
        'The number of injections from a k-set to S is P(n,k)=n!/(n-k)! for k<=n',
        'The number of permutations of S is n!',
        'The number of 2-element sequences with repetition from S is C(n,2)',
        'A;B;C',
        'Sequences with repetition: n^2, not C(n,2). C(n,2) counts unordered pairs.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / uniform',
        'X~Uniform(0,2). Which are true?',
        'f_X(x)=1/2 for x in (0,2)',
        'E[X]=1',
        'Var(X)=(2-0)^2/12=1/3',
        'P(X=1)=1/2',
        'A;B;C',
        'Continuous uniform has P(X=1)=0. Mean is the midpoint, variance the interval-length formula.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / joint',
        'A 2x2 joint PMF on {0,1}x{0,1} has all four cells equal to 1/4. Which are true?',
        'X and Y are independent Bernoulli(1/2)',
        'P(X=Y)=1/2',
        'Corr(X,Y)=0',
        'P(X=1,Y=1)=1/2',
        'A;B;C',
        'Product structure 1/4=(1/2)(1/2). P(X=Y)=P(00)+P(11)=1/2. P(11)=1/4 not 1/2.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / discrete',
        'X takes values in {0,1,2} with p=(0.2,0.5,0.3). Which are true?',
        'E[X]=1.1',
        'F(1.7)=P(X<=1.7)=0.7',
        'The mode is 1',
        'P(X=1.7)=0.7',
        'A;B;C',
        'E[X]=0.5+0.6=1.1. CDF at 1.7 includes 0 and 1. A discrete law has P(X=1.7)=0.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / z-test',
        'n=100, sigma=10, Xbar=103, H0: mu=100 vs H1: mu != 100, alpha=0.05, z_crit=1.96. Which are true?',
        'z = (103-100)/(10/10) = 3',
        'The two-sided test rejects H0',
        'An approximate p-value is 2(1-Phi(3)) ~ 0.0027',
        'The 95% z-interval for mu is centred at 100',
        'A;B;C',
        'SE=1, z=3>1.96 so reject. The CI is centred at Xbar=103, not at the H0 value.',
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / mixed',
        'Let X~Binomial(n,p) and Y~Poisson(np) with the same mean. Which comparisons are correct for 0<p<1, n>=2?',
        'E[X]=E[Y]',
        'Var(X)=np(1-p) < np = Var(Y)',
        'P(X=0)=(1-p)^n which is not equal to e^{-np} in general',
        'X and Y are equal almost surely',
        'A;B;C',
        'Poisson has the larger variance np vs np(1-p). They are different laws; Poisson is a limit, not an a.s. identity.',
        marks=2, diff='H',
    ))
    o.append(msq(
        'P&S / mixed',
        'A data set of 7 distinct numbers is summarised. Which are true?',
        'The sample median is the 4th order statistic',
        'Changing the largest value does not change the median',
        'The sample mean is sensitive to that largest value',
        'The unique mode of 7 distinct numbers is the largest',
        'A;B;C',
        "For odd n the median is the middle order statistic, robust to extremes. With all values distinct there are 7 modes (or none unique), not 'the largest'.",
        marks=2, diff='M',
    ))
    o.append(msq(
        'P&S / mixed',
        'Let F be the CDF of Uniform(0,1). Which are true?',
        'F(x)=0 for x<0, F(x)=x for x in [0,1], F(x)=1 for x>1',
        'F is continuous',
        'F is differentiable at 0.3 with derivative 1',
        'F has a jump at 0',
        'A;B;C',
        'Continuous uniform CDF is continuous (no jumps) and has density 1 on (0,1).',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'The number of onto (surjective) functions from a 4-element feature-index set to a 3-element label set {red, green, blue} is _____.',
        '36',
        'Inclusion-exclusion: 3^4 - C(3,1)2^4 + C(3,2)1^4 = 81-48+3 = 36. Equivalently 3! S(4,3) = 6*6 = 36.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'Five boys and four girls sit in a row so that no two girls are adjacent. The number of seating arrangements of these 9 distinct people is _____.',
        '43200',
        'Seat boys first: 5! ways, creating 6 gaps; choose 4 gaps for girls: C(6,4)*4!. Product is 43200.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'The number of onto functions from a 5-element domain to a 3-element codomain is _____.',
        '150',
        '3^5 - C(3,1)2^5 + C(3,2)1^5 = 243-96+3 = 150. Also 3! S(5,3)=6*25=150.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'How many 5-digit integers (no leading zero) can be formed using digits 0-9 if repetition is not allowed?',
        '27216',
        'First digit: 9 choices (1-9). Then 9 remaining (including 0) for the second, then 8,7,6. Product 27216.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'Four married couples sit around a circular table so that spouses sit together (each couple occupies two adjacent seats). Treating rotations as the same, the number of seating arrangements is _____.',
        '96',
        'Treat each couple as a block: 3! circular block arrangements, and each block can be ordered 2 ways: 6*16=96.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / counting',
        'Using inclusion-exclusion, the number of integers from 1 to 100 that are divisible by 2 or 3 or 5 is _____.',
        '74',
        '|A u B u C| = 50+33+20 -16 -10 -6 +3 = 74.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'The number of integer solutions of w+x+y+z=8 with each variable >=0 and w>=2 is _____.',
        '84',
        "Set w'=w-2>=0 so w'+x+y+z=6: C(9,3)=84.",
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / joint',
        'Joint PMF p(x,y)=(x+y)/21 for x=1,2 and y=1,2,3. Then P(X=2) equals _____ (rounded to two decimals).',
        '0.57',
        'P(X=2)=((2+1)+(2+2)+(2+3))/21=12/21=0.571..., report 0.57.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / joint',
        'Joint PMF: P(X=0,Y=0)=0.15, P(X=0,Y=1)=0.25, P(X=1,Y=0)=0.20, P(X=1,Y=1)=0.40. Then Cov(X,Y) equals _____ (two decimals).',
        '0.01',
        'E[XY]=P(1,1)=0.40, E[X]=0.60, E[Y]=0.65, so 0.40-0.39=0.01.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / joint',
        'Joint density f(x,y)=8xy on the triangle 0<y<x<1. Then P(Y < 1/2) equals _____ (four decimals).',
        '0.4375',
        'Integrate 8xy over y<1/2 inside the triangle: x in (0,1/2] with y<x plus x in (1/2,1] with y<1/2, giving 1/16+3/8=0.4375.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / joint',
        'On the unit square with uniform joint density, P(Y > X+0.5) equals _____ (three decimals).',
        '0.125',
        'The region is a right triangle of legs 0.5, area 0.125.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / joint',
        'If f(x,y)=e^{-x-y} for x>0,y>0, then P(X+Y <= 1) equals 1-2/e. Numerically this is _____ (rounded to two decimals).',
        '0.26',
        'Integrate e^{-x-y} over x+y<=1, x,y>0: 1-2e^{-1} ~ 0.264.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / Bayes',
        'A rare plant disease affects 2% of a greenhouse. A leaf test detects the disease with probability 0.95 if present and falsely flags 5% of healthy plants. Given a positive test, P(diseased) equals _____ (rounded to two decimals).',
        '0.28',
        'Bayes: 0.019/(0.019+0.049)=0.019/0.068 ~ 0.28.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'In a mailbox, 30% of messages are spam. A filter tags spam with probability 0.90 and tags ham as spam with probability 0.05. Given a tagged message, P(spam) equals _____ (two decimals).',
        '0.89',
        '0.27/(0.27+0.035)=0.27/0.305 ~ 0.89.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'Plant A makes 70% of chips (defect rate 1%); plant B makes the rest (defect rate 4%). A randomly chosen chip is defective. P(it came from plant B) equals _____ (two decimals).',
        '0.63',
        'P(B|D)=0.012/(0.007+0.012)=0.012/0.019 ~ 0.63.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        "Tomorrow rains with probability 0.2. A forecast says 'rain' with probability 0.8 if it will rain and with probability 0.1 if it will not. Given a 'rain' forecast, P(rain) equals _____ (two decimals).",
        '0.67',
        '0.16/(0.16+0.08)=0.16/0.24=2/3 ~ 0.67.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'Three drawers: D1 has 3 gold 1 silver coins; D2 has 1 gold 3 silver; D3 has 2 gold 2 silver. A drawer is chosen uniformly. A gold coin is drawn. P(drawer was D1 | gold) equals _____ (two decimals).',
        '0.5',
        'P(G)=(1/3)(3/4+1/4+1/2)= (1/3)(1.5)=0.5. P(D1|G)=(0.25)/0.5=0.50.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'A box contains two coins: one fair and one two-headed. A coin is picked at random and flipped; it shows heads. P(the coin is two-headed | heads) equals _____ (two decimals).',
        '0.67',
        'P(H)=0.25+0.5=0.75, P(two-headed|H)=0.5/0.75=2/3 ~ 0.67.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'A server crash is due to hardware with prior 0.3, otherwise software. A diagnostic flags hardware with probability 0.9 if hardware and 0.2 if software. Given a hardware flag, P(true hardware fault) equals _____ (two decimals).',
        '0.66',
        '0.27/(0.27+0.14)=0.27/0.41 ~ 0.66.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'An oil well is wet with prior 0.4. A seismic test is positive with probability 0.85 if wet and 0.25 if dry. Given a positive test, P(wet) equals _____ (two decimals).',
        '0.69',
        '0.34/(0.34+0.15)=0.34/0.49 ~ 0.69.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'City buses are 80% blue and 20% green. A witness identifies a bus as green; the witness is correct 75% of the time (and otherwise names the other colour). P(bus is green | identified green) equals _____ (two decimals).',
        '0.43',
        '0.15/(0.15+0.20)=0.15/0.35 ~ 0.43.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'A malware scanner flags 98% of infected files and 4% of clean files. Prevalence of infection is 1%. Given a flag, P(infected) equals _____ (two decimals).',
        '0.2',
        '0.0098/(0.0098+0.0396)=0.0098/0.0494 ~ 0.20.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'Among donors, 40% are type A, 10% type B, 50% type O. A mistyped record lists a donor as type A with probability 0.9 if truly A, 0.05 if B, 0.05 if O. Given a listed-A record, P(true type A) equals _____ (two decimals).',
        '0.92',
        '0.36/(0.36+0.005+0.025)=0.36/0.39 ~ 0.92.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'Radar: an object is an aircraft with prior 0.05, else a bird. The radar alarm sounds with probability 0.99 on aircraft and 0.10 on birds. Given an alarm, P(aircraft) equals _____ (two decimals).',
        '0.34',
        '0.0495/(0.0495+0.095)=0.0495/0.1445 ~ 0.34.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'A student knows the answer with probability 0.7, otherwise guesses uniformly among 4 options. Given a correct response, P(the student knew it) equals _____ (two decimals).',
        '0.9',
        '0.70/(0.70+0.075)=0.70/0.775 ~ 0.90.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        "Packets drop due to congestion (prior 0.6) or due to a link fault. A monitor reports 'congestion-like' with probability 0.8 under congestion and 0.3 under fault. Given that report, P(congestion) equals _____ (two decimals).",
        '0.8',
        '0.48/(0.48+0.12)=0.48/0.60=0.80.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'At customs, 5% of travellers carry undeclared goods. A scanner alarms with probability 0.92 if undeclared goods are present and 0.08 otherwise. Given an alarm, P(undeclared goods) equals _____ (two decimals).',
        '0.38',
        '0.046/(0.046+0.076)=0.046/0.122 ~ 0.38.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'A tumour is present with prior 0.01. An MRI is positive with probability 0.95 if a tumour is present and 0.02 otherwise. Given a positive MRI, P(tumour) equals _____ (two decimals).',
        '0.32',
        '0.0095/(0.0095+0.0198)=0.0095/0.0293 ~ 0.32.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'Lots: 90% of lots are good (defect rate 1%) and 10% are bad (defect rate 20%). One item drawn from a random lot is defective. P(the lot is bad) equals _____ (two decimals).',
        '0.69',
        '0.020/(0.009+0.020)=0.020/0.029 ~ 0.69.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bayes',
        'A login failure is a brute-force attack with prior 0.15, else a user typo. An anomaly score is high with probability 0.88 on attacks and 0.12 on typos. Given a high score, P(attack) equals _____ (two decimals).',
        '0.56',
        '0.132/(0.132+0.102)=0.132/0.234 ~ 0.56.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / cond-exp',
        'Y is Uniform on {1,2,3}. Given Y=y, X is Uniform on {1,...,y} (discrete). Then E[X] equals _____ (rounded to two decimals).',
        '1.5',
        'E[X|Y=1]=1, E[X|Y=2]=1.5, E[X|Y=3]=2, average 1.5.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / cond-exp',
        'A fair die is rolled. If the face is even, a fair coin is tossed once and X=number of heads; if odd, the coin is tossed twice and X=number of heads. E[X] equals _____ (two decimals).',
        '0.75',
        'P(even)=1/2, E[X|even]=1/2; E[X|odd]=1. Total 0.75.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / cond-exp',
        'N~Poisson(3) and given N=n, X is Binomial(n, 0.5) (X=0 if n=0). Then E[X] equals _____ (one decimal).',
        '1.5',
        'E[X]=E[E[X|N]]=E[0.5 N]=1.5.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / cond-exp',
        'N~Poisson(4) and given N=n, S is the sum of n i.i.d. Uniform{1,2} (S=0 if n=0). E[S] equals _____ (integer).',
        '6',
        'E[S|N]=N*1.5 so E[S]=6.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / cond-exp',
        'A gambler starts with 0. Each step a fair coin adds +1 or -1. Let T be the first time the fortune is +2 or -2. E[T] equals _____ (integer).',
        '4',
        'Simple symmetric random walk hitting time of +/-a from 0 has mean a^2=4.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / descriptive',
        'A data set of n=5 values has sum 20 and sum of squares 100. The population variance (divide by n) is _____.',
        '4',
        'E[X^2]-(E[X])^2=20-16=4.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / covariance',
        'Var(X)=4, Var(Y)=9, Corr(X,Y)=0.5. Then Var(2X-Y) equals _____.',
        '13',
        '4VarX+VarY-4 Cov=16+9-12=13.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / covariance',
        'X is Uniform on {1,2,3} and Y=X^2. Then Cov(X,Y)=E[X^3]-E[X]E[X^2]. This covariance equals _____ (rounded to two decimals).',
        '2.67',
        'E[X]=2, E[X^2]=14/3, E[X^3]=12, Cov=12-2*(14/3)=12-28/3=8/3~2.67.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / discrete',
        'X has PMF P(X=-1)=0.2, P(X=0)=0.3, P(X=2)=0.5. Then Var(X) equals _____ (two decimals).',
        '1.56',
        '2.2-0.64=1.56.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / discrete',
        'X ~ Geometric(p=1/3) on {1,2,...}. Then P(X>4 | X>2) equals P(X>2) by memorylessness, and P(X>2)=(2/3)^2. The conditional probability equals _____ (rounded to two decimals).',
        '0.44',
        'Memoryless: P(X>2+2 | X>2)=P(X>2)=4/9 ~ 0.44.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'A packet of 8 seeds germinates independently with probability 0.5. P(exactly 3 germinate) equals C(8,3)/256. The probability as a simplified fraction C(8,3)/256 equals, in decimal, _____ (rounded to three decimals).',
        '0.219',
        'C(8,3)=56, 56/256=0.219.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'A basketball player hits a free throw with probability 0.6 independently. In 5 attempts, P(exactly 4 hits) equals _____ (rounded to three decimals).',
        '0.259',
        'C(5,4)(0.6)^4(0.4)=5*0.1296*0.4=0.259.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'A 10-question MCQ is guessed independently with 4 options each. P(at least one correct) = 1-(3/4)^10. This value rounded to two decimals is _____.',
        '0.94',
        '1-0.75^10 ~ 1-0.0563=0.94.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'Four independent servers fail with probability 0.1 each. P(exactly two fail) equals _____ (rounded to four decimals).',
        '0.0486',
        'C(4,2)*0.01*0.81=0.0486.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'A fair die is rolled 5 times. P(exactly two sixes) equals _____ (rounded to three decimals).',
        '0.161',
        'C(5,2)*(1/6)^2*(5/6)^3=10*(1/36)*(125/216)=1250/7776 ~ 0.161.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'Eight emails, each independently spam with probability 1/4. P(exactly 2 spam) equals _____ (rounded to four decimals).',
        '0.3115',
        'C(8,2)*(1/16)*(0.75)^6=28*0.0625*0.177978515625 ~ 0.3115.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'A batter gets a hit with probability 0.3 independently in 8 at-bats. P(at least one hit)=1-(0.7)^8. Rounded to two decimals this is _____.',
        '0.94',
        '0.7^8 ~ 0.0576, so 0.94.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'A login succeeds with probability 0.4 independently. In 5 attempts, P(first success occurs on the 5th attempt) equals _____ (rounded to four decimals). (This is a geometric probability, not a binomial count.)',
        '0.0518',
        'Four failures then one success: (0.6)^4 * 0.4 = 0.0518.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / Bernoulli',
        'A 4x4 matrix of i.i.d. Bernoulli(1/2) entries. P(the first row sums to 2 AND the first column sums to 2). The overlapping (1,1) entry is shared. This probability, rounded to three decimals, is _____.',
        '0.141',
        'Condition on a11. Each case multiplies two independent Binomial(3,1/2) probabilities: 0.5*(3/8)^2 + 0.5*(3/8)^2 = (3/8)^2 = 0.140625 ~ 0.141.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / continuous',
        'f(x)=3x^2 on (0,1). Then Var(X) equals _____ (four decimals).',
        '0.0375',
        'E[X^2]=int 3x^4=3/5=0.6, Var=0.6-0.5625=0.0375.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / exponential',
        'X is Exponential with mean 5. If P(X>5)=e^{-1}, then P(X>10 | X>5) equals _____ (rounded to two decimals).',
        '0.37',
        'Memoryless: P(X>5)=e^{-1}~0.37.)',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / cond-pdf',
        'Joint density f(x,y)=e^{-x-y} for x>0,y>0. Then f_{X|Y}(x|y) for x>0 equals e^{-x} (does not depend on y). The value of f_{X|Y}(1|5) rounded to two decimals is _____.',
        '0.37',
        'Independence: conditional density is e^{-x}, so e^{-1}~0.37.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / cond-pdf',
        'Joint density f(x,y)=8xy on 0<y<x<1. The conditional f_{Y|X}(y|x) for 0<y<x is 2y/x^2. Hence f_{Y|X}(0.2|0.5) equals _____.',
        '1.6',
        '2*0.2/0.25=1.6.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / cond-pdf',
        'X~Uniform(0,1), Y|X=x ~ Uniform(0,x). Then E[Y] equals _____ (two decimals).',
        '0.25',
        'E[Y|X]=X/2 so E[Y]=1/4.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / cond-pdf',
        'Bivariate density f(x,y)= (x+y)/8 on 0<x<2, 0<y<2. The marginal f_X(1) equals int_0^2 (1+y)/8 dy = _____ (three decimals).',
        '0.5',
        'int_0^2 (1+y)/8 dy = (y + y^2/2)/8 |_0^2 = (2+2)/8=0.5.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / CLT',
        'n=25 i.i.d. Uniform(0,12), which have variance 12. Then sd of Xbar is _____ (two decimals).',
        '0.69',
        'Var Uniform(0,12)=144/12=12, sd of mean = sqrt(12)/5 ~ 0.693. Report 0.69.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / CI',
        'n=16, sigma=8, Xbar=50, z_{0.025}=1.96. Half-width of the 95% z-interval is 1.96*8/4 = _____ (two decimals).',
        '3.92',
        'SE=2, half-width 3.92.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / CI',
        'To have a 95% z-interval half-width at most 0.5 when sigma=2 and z=1.96, the smallest integer n satisfying n >= (1.96*2/0.5)^2 is _____.',
        '62',
        '(3.92/0.5)^2=7.84^2=61.4656, so n=62.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / CI',
        'n=9 Normal observations, s=3, t_{8, 0.025}=2.306. Half-width of the 95% t-interval is 2.306*s/sqrt(n) = _____ (two decimals).',
        '2.31',
        'SE=1, half-width 2.31.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / chi2-test',
        'A die is rolled 60 times. Under fairness E_i=10 for each face. Observed counts 8,12,9,11,7,13. The Pearson chi^2 statistic sum (O-E)^2/E equals _____ (one decimal).',
        '2.8',
        '(4+4+1+1+9+9)/10=2.8.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / mixed',
        'Three fair coins. Let T = at least two heads and W = at least one tail. P(T n W) equals _____ (three decimals).',
        '0.375',
        'T n W is exactly two heads (three heads has no tail). Probability 3/8=0.375.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / mixed',
        'Order statistics: 3 i.i.d. Uniform(0,1). E[max] equals 3/4 = _____ (two decimals).',
        '0.75',
        'F_max(t)=t^3, density 3t^2, mean 3/4.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / mixed',
        '3 i.i.d. Uniform(0,1). E[min] equals 1/4 = _____ (two decimals).',
        '0.25',
        'Density of min is 3(1-t)^2, mean 1/4.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / mixed',
        'A hypergeometric flavour without the name: an urn has 5 red and 7 blue tokens. Three tokens are drawn without replacement. P(all red) = C(5,3)/C(12,3) equals _____ (rounded to three decimals).',
        '0.045',
        '10/220=1/22~0.045.',
        marks=2, diff='M',
    ))
    o.append(nat(
        'P&S / mixed',
        'A coupon-collector with 4 coupon types, uniform independent draws. Expected draws to complete the set is 4(1+1/2+1/3+1/4) = _____ (one decimal).',
        '8.3',
        '4*(1+0.5+0.333+0.25)=8.3.',
        marks=2, diff='H',
    ))
    o.append(nat(
        'P&S / counting',
        'A 4-person working group is chosen from 9 researchers and then one of the 4 is designated chair. The number of possible (group, chair) outcomes is _____.',
        '504',
        'C(9,4)*4 = 126*4 = 504. Equivalently P(9,1)*C(8,3)=9*56=504.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / axioms',
        'Three events A,B,C are pairwise disjoint with P(A)=0.1, P(B)=0.25, P(C)=0.15. Then P(A u B u C) equals _____ (two decimals).',
        '0.5',
        'Disjoint union: 0.1+0.25+0.15=0.50.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / independence',
        'Three independent alarms each fail with probability 0.2. The probability that at least one works is _____ (three decimals).',
        '0.992',
        'Complement of all fail: 1-0.008=0.992.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / joint',
        'Joint density f(x,y)=8xy on 0<y<x<1. The marginal f_X(x) for x in (0,1) is 4x^3. Hence f_X(1/2) equals _____ (one decimal).',
        '0.5',
        '4*(1/2)^3=0.5.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / cond-exp',
        'A mixed distribution: with probability 0.4, X~Bernoulli(0.5); with probability 0.6, X is identically 1. Then E[X] equals _____ (two decimals).',
        '0.8',
        'E[E[X|regime]]=0.4*0.5+0.6*1=0.80.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / descriptive',
        'The interquartile range of the ordered sample 2,4,6,8,10,12,14 is Q3-Q1. With Q1=4 and Q3=12 (seven-point convention using medians of halves excluding the overall median), IQR equals _____.',
        '8',
        'Q1=4, Q3=12, IQR=8.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / covariance',
        'A 2D sample of 4 points: (1,2), (2,4), (3,6), (4,8). The (Pearson) sample correlation is _____.',
        '1',
        'Y=2X exactly on the sample, so r=1.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / discrete',
        'X takes values 1,2,3,4 each with probability 1/4. Then P(X <= 2.5) equals _____ (two decimals).',
        '0.5',
        'X=1 or 2, probability 1/2.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / Bernoulli',
        'A bit-flip channel writes a bit correctly with probability 0.9 (Bernoulli success). The variance of a single written bit-error indicator (1 if error) is _____ (two decimals).',
        '0.09',
        'Error ~ Bernoulli(0.1), variance 0.09.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / binomial',
        'A shopper buys a warranty on a visit with probability 0.3, independently across 7 visits. The variance of the number of warranties sold is _____ (two decimals).',
        '1.47',
        'np(1-p)=7*0.21=1.47.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / Poisson',
        'Calls arrive as Poisson with mean 3 per minute. P(no call in a given minute) equals e^{-3}. Rounded to three decimals this is _____.',
        '0.05',
        'e^{-3}~0.050.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / continuous',
        'Density f(x)=2x on (0,1). The median m satisfies F(m)=1/2, so m equals _____ (rounded to two decimals).',
        '0.71',
        'm^2=1/2, m=sqrt(1/2)~0.71.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / uniform',
        'Two independent Uniform(0,1) r.v.s U,V. P(U+V<=1) equals _____ (one decimal).',
        '0.5',
        'Lower triangle of the unit square, area 1/2.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / exponential',
        'Two independent Exponential(rate=1) clocks. The expected time until the first rings is _____ (one decimal).',
        '0.5',
        'Minimum of two i.i.d. Exp(1) is Exp(2), mean 1/2.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / normal',
        'If X~N(0, sigma^2), the MGF E[e^{tX}] equals exp(sigma^2 t^2 / 2). For sigma=2 and t=1 the MGF equals e^k with k=_____.',
        '2',
        '4*1/2=2.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / chi-squared',
        'If Z~N(0,1) then P(Z^2 <= 3.84) with 3.84 ~ chi^2_{1, 0.95} quantile is approximately _____ (two decimals).',
        '0.95',
        'chi^2_1 quantile 0.95 is 1.96^2~3.84.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / t-dist',
        'Var of t_nu for nu=4 equals nu/(nu-2) = _____.',
        '2',
        '4/(4-2)=2.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / cond-pdf',
        'Let Y ~ N(0,1) and, given Y=y, let X ~ N(y, 1). Then Var(X) equals _____.',
        '2',
        '1 + Var(Y)=2.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / CLT',
        'Sum S_n of n i.i.d. with mean 0 variance 1. Approximate P(S_n / sqrt(n) <= 0) for large n is _____ (one decimal).',
        '0.5',
        'The standardised sum is approx N(0,1).',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / CI',
        'A 95% z-interval is built from n=16, sigma=8, Xbar=50 and z_{0.025}=1.96. Its lower endpoint is _____ (two decimals).',
        '46.08',
        '50-3.92=46.08.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / z-test',
        'A one-sided z-test has z=1.64. Using Phi(1.64)~0.9495, the p-value P(Z>1.64) rounded to two decimals is _____.',
        '0.05',
        '1-0.9495=0.0505 ~ 0.05.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / t-test',
        'n=9, Xbar=4, s=3, H0: mu=2. The t statistic equals _____ (integer).',
        '2',
        'SE=3/3=1, t=(4-2)/1=2.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / chi2-test',
        'A 2x3 contingency table (independence, no estimated extra parameters beyond margins) has chi^2 degrees of freedom equal to _____.',
        '2',
        '(2-1)(3-1)=2.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / mixed',
        'Skewness of N(mu, sigma^2) is 0. For Exp(rate=1) the skewness E[(X-1)^3]/1^3 equals 2. The difference (Exp skewness minus Normal skewness) is _____.',
        '2',
        'Exponential(1) has skewness 2, Gaussian has 0.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / multinomial',
        'Dice: a fair six-sided die is rolled 4 times. The number of outcome tuples with each of four distinct faces (a permutation of four different numbers) is P(6,4)= _____.',
        '360',
        'P(6,4)=360.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'A byte is 8 independent bits, each equal to 1 with probability 0.5. P(the byte has even parity), i.e. even number of 1s, equals _____ (two decimals).',
        '0.5',
        'For a fair independent bits, even and odd parity are equally likely: 0.50.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'From 10 distinct papers, 3 are chosen for an oral exam and then ordered (first, second, third). The number of possible ordered triples is _____.',
        '720',
        'P(10,3)=720.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / counting',
        "The multinomial coefficient 6!/(2!2!2!) counts the number of words of length 6 with two A's, two B's and two C's. Its value is _____.",
        '90',
        '720/8=90.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / counting',
        'A robot on a grid may move only right or up. The number of shortest paths from (0,0) to (4,3) is _____.',
        '35',
        'Need 4 right and 3 up, in some order: C(7,3)=35.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / Poisson',
        'A Poisson process has rate 5 per hour. The expected waiting time (in hours) until the first event is _____ (one decimal).',
        '0.2',
        'Waiting time is Exponential(5), mean 1/5=0.2.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'A password is a length-4 string over {A,B,C,D,E} with no two consecutive characters equal. The number of such passwords is _____.',
        '320',
        'First char 5 choices; each later char has 4 choices (not equal to previous): 5*4^3=320.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / binomial',
        'Among 6 independent TCP packets, each is lost with probability 0.2. The expected number of lost packets is _____ (one decimal).',
        '1.2',
        'Binomial mean np=6*0.2=1.2.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / binomial',
        'Each day of a 7-day week is rainy independently with probability 0.3. P(no rainy day) equals _____ (rounded to three decimals).',
        '0.082',
        '0.7^7 ~ 0.082.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'A 9-match season is split into 4 wins, 3 draws, 2 losses. The number of result sequences is 9!/(4!3!2!) = _____.',
        '1260',
        '362880/(24*6*2)=1260.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'The number of derangements of 4 distinct recommendation letters into 4 envelopes (no letter in the matching envelope) is _____.',
        '9',
        '!4 = 4!(1-1+1/2-1/6+1/24) = 9.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / counting',
        'The number of ways to distribute 7 identical USB sticks to 3 distinct interns (each may get zero) is _____.',
        '36',
        'Stars and bars C(9,2)=36.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / cond-exp',
        'X given Y=y is Exponential with mean y, and Y is Exponential with mean 2. Then E[X] equals _____ (integer).',
        '2',
        'E[X]=E[E[X|Y]]=E[Y]=2.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / descriptive',
        'Five exam scores have mean 12. After a sixth score 18 is included, the new mean is _____ (one decimal).',
        '13',
        'Total 60+18=78, mean 13.0.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / binomial',
        'Each of 12 students passes a qualifier independently with probability 0.8. The expected number who pass is _____ (one decimal).',
        '9.6',
        '12*0.8=9.6.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / counting',
        'A 6-character OTP is formed from digits 0-9 with all characters distinct. The number of possible OTPs is _____.',
        '151200',
        'P(10,6) = 10!/4! = 151200.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / axioms',
        'A sample space has 8 equally likely outcomes. Event A contains 3 of them. P(A^c) equals _____ (three decimals).',
        '0.625',
        'P(A)=3/8 so P(A^c)=5/8=0.625.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / joint',
        'Using the same joint table P(X=1,Y=1)=0.10, P(X=1,Y=2)=0.20, P(X=2,Y=1)=0.30, P(X=2,Y=2)=0.40, the value of P(Y=1|X=1) is _____ (rounded to two decimals).',
        '0.33',
        'P(X=1)=0.30 so 0.10/0.30=1/3 ~ 0.33.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / descriptive',
        'For {4, 8, 10, 12, 16}, the population standard deviation (divide by n, not n-1) equals _____ (two decimals).',
        '4',
        'Variance (36+4+0+4+36)/5=16, sd=4.00? 80/5=16, sd=4. Let me use 4.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / mixed',
        'A 2x2 covariance matrix [[4, 1], [1, 9]] has Corr(X,Y) equal to 1/(2*3) = _____ (rounded to two decimals).',
        '0.17',
        'rho=1/(sd 2 * sd 3)=1/6~0.17.',
        marks=1, diff='M',
    ))
    o.append(nat(
        'P&S / counting',
        'In a workshop of 12 people, every pair shakes hands exactly once. The number of handshakes is _____.',
        '66',
        'C(12,2)=66.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / independence',
        'Three independent alarms each fail with probability 0.1. The probability that all three fail is _____ (three decimals).',
        '0.001',
        '0.1^3=0.001.',
        marks=1, diff='E',
    ))
    o.append(nat(
        'P&S / descriptive',
        'z-score of a value 82 when the attribute has mean 70 and sd 8 equals _____ (one decimal).',
        '1.5',
        '(82-70)/8=1.5.',
        marks=1, diff='E',
    ))
    return uniq(o)

