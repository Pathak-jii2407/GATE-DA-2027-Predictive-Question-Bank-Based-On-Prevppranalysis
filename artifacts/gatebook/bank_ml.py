"""GATE DA Machine Learning item bank (supervised + unsupervised syllabus only)."""
from helpers import mcq, msq, nat, uniq


def items():
    o = []
    o.append(nat(
        'SLR',
        'Chai stall on FC Road records cups x versus revenue in 10 Rs y as (1,2), (2,3), (3,5), (4,6). Fit simple OLS with intercept. The fitted slope equals ____.',
        '1.4',
        'b1 = Sxy/Sxx = 1.4.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'Using the OLS line fitted on Chai stall on FC Road pairs (1,2), (2,3), (3,5), (4,6) (cups vs revenue in 10 Rs), the prediction at x=5 is ____.',
        '7.5',
        'yhat = 0.5 + 1.4*5 = 7.5.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'Wheat plots in Nanded records kg urea x versus quintals y as (0,2), (1,3), (2,5), (3,6). Fit simple OLS with intercept. The fitted slope equals ____.',
        '1.4',
        'b1 = Sxy/Sxx = 1.4.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'For Wheat plots in Nanded data (0,2), (1,3), (2,5), (3,6) of kg urea against quintals, the OLS intercept is ____.',
        '1.9',
        'b0 = ybar - b1 xbar = 1.9.',
        marks=1, diff='M'))
    o.append(nat(
        'SLR',
        'Pune-Mumbai express buses records speed in 10 km/h x versus stopping metres y as (4,8), (5,11), (6,13), (7,16). Fit simple OLS with intercept. The fitted slope equals ____.',
        '2.6',
        'b1 = Sxy/Sxx = 2.6.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'On Pune-Mumbai express buses the OLS residual sum of squares for (4,8), (5,11), (6,13), (7,16) (speed in 10 km/h, stopping metres) equals ____.',
        '0.2',
        'SSE = sum (y-yhat)^2 = 0.2.',
        marks=2, diff='H'))
    o.append(nat(
        'SLR',
        'DiyaMart click log records thousand impressions x versus clicks y as (1,2), (3,4), (5,7), (7,9). Fit simple OLS with intercept. The fitted slope equals ____.',
        '1.2',
        'b1 = Sxy/Sxx = 1.2.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'Using the OLS line fitted on DiyaMart click log pairs (1,2), (3,4), (5,7), (7,9) (thousand impressions vs clicks), the prediction at x=8 is ____.',
        '10.3',
        'yhat = 0.7 + 1.2*8 = 10.3.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'Clinic BP desk records BMI units over 20 x versus systolic excess y as (1,4), (2,6), (3,7), (4,9). Fit simple OLS with intercept. The fitted slope equals ____.',
        '1.6',
        'b1 = Sxy/Sxx = 1.6.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'For Clinic BP desk data (1,4), (2,6), (3,7), (4,9) of BMI units over 20 against systolic excess, the OLS intercept is ____.',
        '2.5',
        'b0 = ybar - b1 xbar = 2.5.',
        marks=1, diff='M'))
    o.append(nat(
        'SLR',
        'Ice factory ledger records C above 0 x versus tonnes sold y as (2,1), (4,2), (6,2), (8,3). Fit simple OLS with intercept. The fitted slope equals ____.',
        '0.3',
        'b1 = Sxy/Sxx = 0.3.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'On Ice factory ledger the OLS residual sum of squares for (2,1), (4,2), (6,2), (8,3) (C above 0, tonnes sold) equals ____.',
        '0.2',
        'SSE = sum (y-yhat)^2 = 0.2.',
        marks=2, diff='H'))
    o.append(nat(
        'SLR',
        'Tutoring centre mocks records weeks enrolled x versus mock score y as (1,40), (2,48), (3,52), (5,64). Fit simple OLS with intercept. The fitted slope equals ____.',
        '5.8286',
        'b1 = Sxy/Sxx = 5.8286.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'Using the OLS line fitted on Tutoring centre mocks pairs (1,40), (2,48), (3,52), (5,64) (weeks enrolled vs mock score), the prediction at x=6 is ____.',
        '69.9429',
        'yhat = 34.9714 + 5.8286*6 = 69.9429.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'Printer toner test records hundred pages x versus density drop y as (2,1), (3,2), (4,2), (5,3). Fit simple OLS with intercept. The fitted slope equals ____.',
        '0.6',
        'b1 = Sxy/Sxx = 0.6.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'For Printer toner test data (2,1), (3,2), (4,2), (5,3) of hundred pages against density drop, the OLS intercept is ____.',
        '-0.1',
        'b0 = ybar - b1 xbar = -0.1.',
        marks=1, diff='M'))
    o.append(nat(
        'SLR',
        'Solar tilt trial records degrees over 10 x versus kWh y as (0,5), (2,8), (4,10), (6,13). Fit simple OLS with intercept. The fitted slope equals ____.',
        '1.3',
        'b1 = Sxy/Sxx = 1.3.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'On Solar tilt trial the OLS residual sum of squares for (0,5), (2,8), (4,10), (6,13) (degrees over 10, kWh) equals ____.',
        '0.2',
        'SSE = sum (y-yhat)^2 = 0.2.',
        marks=2, diff='H'))
    o.append(nat(
        'SLR',
        'Bakery oven log records minutes extra x versus loaf height mm y as (1,10), (2,14), (3,16), (4,20). Fit simple OLS with intercept. The fitted slope equals ____.',
        '3.2',
        'b1 = Sxy/Sxx = 3.2.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'Using the OLS line fitted on Bakery oven log pairs (1,10), (2,14), (3,16), (4,20) (minutes extra vs loaf height mm), the prediction at x=5 is ____.',
        '23',
        'yhat = 7 + 3.2*5 = 23.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'Cricket nets session records overs faced x versus runs y as (2,6), (4,10), (6,16), (8,20). Fit simple OLS with intercept. The fitted slope equals ____.',
        '2.4',
        'b1 = Sxy/Sxx = 2.4.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'For Cricket nets session data (2,6), (4,10), (6,16), (8,20) of overs faced against runs, the OLS intercept is ____.',
        '1',
        'b0 = ybar - b1 xbar = 1.',
        marks=1, diff='M'))
    o.append(nat(
        'SLR',
        'Library extra hours records hours open extra x versus entries in tens y as (1,3), (2,5), (3,6), (4,8). Fit simple OLS with intercept. The fitted slope equals ____.',
        '1.6',
        'b1 = Sxy/Sxx = 1.6.',
        marks=2, diff='M'))
    o.append(nat(
        'SLR',
        'On Library extra hours the OLS residual sum of squares for (1,3), (2,5), (3,6), (4,8) (hours open extra, entries in tens) equals ____.',
        '0.2',
        'SSE = sum (y-yhat)^2 = 0.2.',
        marks=2, diff='H'))
    o.append(mcq(
        'SLR',
        'Four GATE mock pairs (hours, score) are (1,10), (2,20), (3,30), (4,40). After fitting OLS, the residual at hours=3 is',
        '0',
        '10',
        '-10',
        '5',
        'A',
        'The points lie on y=10x, so every residual is 0.',
        marks=1, diff='E'))
    o.append(mcq(
        'SLR',
        'OLS of y on x is y=4+2x. The same sample is used to regress x on y. Which identity ALWAYS holds?',
        'The reverse slope must be 1/2',
        'The reverse slope equals 2',
        'The product of the two OLS slopes equals r^2',
        'The reverse intercept is 4',
        'C',
        'b_yx * b_xy = r^2 always.',
        marks=2, diff='H'))
    o.append(msq(
        'SLR',
        'Let e_i be OLS residuals from simple linear regression with intercept. Which identities ALWAYS hold?',
        'sum e_i = 0',
        'sum e_i x_i = 0',
        'sum e_i y_i = 0',
        'sum e_i yhat_i = 0',
        'A;B;D',
        'Normal equations give 1^T e = 0 and x^T e = 0. yhat lives in col(X), so yhat^T e = 0.',
        marks=2, diff='M'))
    o.append(mcq(
        'SLR',
        'For a sample, corr(x,y)=0.6, s_x=2, s_y=5. The OLS slope of y on x equals',
        '0.60',
        '1.50',
        '2.40',
        '0.24',
        'B',
        'b1 = r * s_y / s_x = 0.6*5/2 = 1.5.',
        marks=1, diff='E'))
    o.append(nat(
        'SLR',
        'A lab reports SST=80 and SSE=20 for an OLS fit of absorbance on concentration (with intercept). R^2 is ____.',
        '0.75',
        'R^2 = 1-SSE/SST = 1-20/80 = 0.75.',
        marks=1, diff='E'))
    o.append(mcq(
        'SLR',
        'Simple OLS is fitted through the origin to (x,y) in {(1,1),(2,2),(3,1)}. The slope minimising SSE is',
        '1',
        '6/7',
        '4/7',
        '5/7',
        'C',
        'b = (sum xy)/(sum x^2) = 8/14 = 4/7.',
        marks=2, diff='M'))
    o.append(mcq(
        'SLR',
        'In OLS y=b0+b1 x+e, adding 5 to every x-value and leaving y unchanged will',
        'increase b1 by 5',
        'leave b1 unchanged and decrease b0 by 5 b1',
        'leave both b0 and b1 unchanged',
        'multiply b1 by 5',
        'B',
        'Slope is shift-invariant in x; intercept adjusts by -b1*5.',
        marks=1, diff='M'))
    o.append(nat(
        'SLR',
        'Pairs (2,3), (4,7), (6,11) lie on a straight line. OLS slope of y on x is ____.',
        '2',
        'Slope (7-3)/(4-2)=2.',
        marks=1, diff='E'))
    o.append(mcq(
        'SLR',
        'A residual plot of OLS of marks on hours fans out as hours grow. This most directly suggests',
        'the intercept is biased toward 0',
        'heteroscedasticity, so equal-variance Gauss-Markov fails',
        'the slope must be negative',
        'R^2 is necessarily 0',
        'B',
        'A fan shape is non-constant variance.',
        marks=1, diff='M'))
    o.append(nat(
        'SLR',
        'For n=5 observations, OLS with intercept uses how many degrees of freedom for SSE?',
        '3',
        'Two parameters, so df=5-2=3.',
        marks=1, diff='E'))
    o.append(mcq(
        'SLR',
        'If all x-values are identical, simple OLS with intercept',
        'has a unique slope',
        'cannot estimate the slope because Sxx=0',
        'forces R^2=1',
        'makes every residual equal to x',
        'B',
        'No x-variation means the slope is unidentified.',
        marks=1, diff='M'))
    o.append(nat(
        'SLR',
        'xbar=3, ybar=10, b1=2. The OLS intercept is ____.',
        '4',
        'b0=10-2*3=4.',
        marks=1, diff='E'))
    o.append(mcq(
        'SLR',
        'R^2=0 for an OLS line with intercept means',
        'every residual is 0',
        'the fitted slope is 0 (horizontal line at ybar)',
        'SST=0',
        'the intercept is 0',
        'B',
        'SSR=0 iff the slope is 0 when an intercept is present.',
        marks=1, diff='M'))
    o.append(mcq(
        'MLR',
        'Design matrix X is n x (p+1) including a column of ones. Unique OLS exists iff',
        'n > p+1 only',
        'X has full column rank p+1',
        'y is orthogonal to col(X)',
        'features are standard-normal',
        'B',
        'Need X^T X invertible, i.e. rank(X)=p+1.',
        marks=1, diff='E'))
    o.append(msq(
        'MLR',
        'In MLR y=X beta+e with full-column-rank OLS, which are ALWAYS true?',
        'The residual vector is orthogonal to every column of X',
        'H=X(X^T X)^{-1}X^T is the orthogonal projector onto col(X)',
        'Unadjusted R^2 cannot decrease when a linearly independent column is added',
        'Every coefficient stays unbiased even if a relevant variable is omitted',
        'A;B;C',
        'Omitted-variable bias can wreck unbiasedness. A-C are geometry/algebra of OLS.',
        marks=2, diff='M'))
    o.append(nat(
        'MLR',
        'A house-price model uses intercept, area, and a binary near-metro flag. n=40. Columns of X: ____.',
        '3',
        'Intercept + area + dummy = 3.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLR',
        'Features satisfy x2=2 x1 on every training row. OLS of y on (1,x1,x2)',
        'has singular X^T X so the usual unique solution does not exist',
        'forces the x2 slope to 2',
        'has VIF of x1 equal to 0',
        'makes predictions undefined for every y',
        'A',
        'Perfect collinearity: rank(X)<3.',
        marks=2, diff='M'))
    o.append(nat(
        'MLR',
        'Fitted MLR yhat=3+2 x1 - x2. At (x1,x2)=(4,5) the prediction is ____.',
        '6',
        '3+8-5=6.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLR',
        'Two centered features are sample-orthogonal. Then each MLR slope',
        'equals the SLR slope of y on that feature (with intercept)',
        'must be 0',
        'equals the inverse SLR slope',
        'cannot be estimated',
        'A',
        'X^T X diagonal => coefficients decouple to simple-regression formulae.',
        marks=2, diff='M'))
    o.append(nat(
        'MLR',
        'Dummy-coded MLR uses 4 city levels plus intercept and no other features. Dummy columns excluding intercept: ____.',
        '3',
        'k levels need k-1 dummies with intercept.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLR',
        'Adjusted R^2 differs from R^2 because it',
        'uses a kernel smoother',
        'penalises extra parameters via residual df, so it can fall when a useless feature is added',
        'is always larger than R^2',
        'equals 1-SSE/SST with no n,p',
        'B',
        'R_adj^2 = 1-(SSE/(n-p-1))/(SST/(n-1)).',
        marks=1, diff='M'))
    o.append(msq(
        'MLR',
        'Which models stay inside multiple linear regression (linear in parameters)?',
        'y=b0+b1 x+b2 x^2+e',
        'y=b0+b1 log x+e with x>0',
        'y=b0+b1 x1+b2 x2+b3 x1 x2+e',
        'y=sigmoid(b0+b1 x) with Bernoulli likelihood',
        'A;B;C',
        'A-C are linear in beta. D is logistic regression.',
        marks=2, diff='M'))
    o.append(nat(
        'MLR',
        'n=12, p=3 predictors plus intercept. Residual df for OLS SSE is ____.',
        '8',
        '12-4=8.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLR',
        'True map y=1+2 x1+0 x2+noise; we still include x2 in OLS. As n grows, the x2 coefficient',
        'converges to 0 in probability (correctly specified zero)',
        'forces R^2 to 0',
        'makes X^T X singular',
        'makes the intercept unestimable',
        'A',
        'No omitted-variable bias; OLS is consistent and that entry -> 0.',
        marks=2, diff='M'))
    o.append(mcq(
        'MLR',
        'yhat=10+3 x1-2 x2. Holding x1 fixed, a unit increase in x2 changes mean response by',
        '3',
        '-2',
        '1',
        '10',
        'B',
        'Partial slope of x2 is -2.',
        marks=1, diff='E'))
    o.append(nat(
        'MLR',
        'Centered orthogonal features: sum x1^2=10, sum x2^2=5, sum x1 y=20, sum x2 y=-10. OLS slope of x1 is ____.',
        '2',
        'b1=(x1^T y)/(x1^T x1)=20/10=2.',
        marks=2, diff='M'))
    o.append(mcq(
        'MLR',
        'Including an interaction x1 x2 in MLR means',
        'the partial effect of x1 is allowed to depend on the value of x2',
        'x1 and x2 must be independent in the population',
        'OLS becomes nonlinear in beta',
        'the intercept must be dropped',
        'A',
        'dyhat/dx1 = b1 + b3 x2.',
        marks=1, diff='M'))
    o.append(nat(
        'MLR',
        'yhat=5+0*x1+4*x2. At (10, 0.5) predicted y is ____.',
        '7',
        '5+2=7.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLR',
        'Multicollinearity among predictors primarily inflates',
        'the residual degrees of freedom',
        'the sampling variance of the involved coefficients',
        'the number of columns of y',
        'R^2 toward -1',
        'B',
        'Near-singular X^T X => large diagonal of (X^T X)^{-1}.',
        marks=1, diff='M'))
    o.append(mcq(
        'Ridge',
        'Ridge (intercept unpenalised, features centered) solves',
        'min ||y-Xb||_2^2 + lambda ||b||_2^2 for lambda>0',
        'min ||y-Xb||_1 + lambda ||b||_2',
        'min ||y-Xb||_2^2 + lambda ||b||_1',
        'min ||b||_2 s.t. ||y-Xb||=0',
        'A',
        'Squared loss plus L2 penalty on slopes.',
        marks=1, diff='E'))
    o.append(msq(
        'Ridge',
        'Relative to OLS, increasing ridge lambda typically',
        'raises bias of the coefficient vector',
        'lowers variance of the coefficient vector',
        'drives coefficients toward 0',
        'makes X^T X + lambda I more ill-conditioned',
        'A;B;C',
        'Adding lambda I improves conditioning; it does not worsen it.',
        marks=2, diff='M'))
    o.append(nat(
        'Ridge',
        '1-D no intercept: X^T X=4, X^T y=8, lambda=4. Ridge coefficient is ____.',
        '1',
        '8/(4+4)=1.',
        marks=2, diff='M'))
    o.append(nat(
        'Ridge',
        'Same 1-D Gram 4 and X^T y=8 but lambda=0. The coefficient is ____.',
        '2',
        '8/4=2, recovering OLS.',
        marks=1, diff='E'))
    o.append(mcq(
        'Ridge',
        'As lambda -> infinity with fixed centered design, ridge slopes',
        'diverge',
        'approach the OLS vector',
        'approach the zero vector',
        'approach PCA loadings',
        'C',
        'Penalty dominates: b -> 0.',
        marks=1, diff='E'))
    o.append(mcq(
        'Ridge',
        'Why add lambda I to X^T X in ridge?',
        'To enforce integer coefficients',
        'To guarantee a unique finite solution even when X is rank-deficient, and to shrink',
        'To turn the loss into hinge loss',
        'To make residuals heteroscedastic on purpose',
        'B',
        'X^T X + lambda I is SPD for lambda>0.',
        marks=2, diff='M'))
    o.append(nat(
        'Ridge',
        'Orthogonal centered columns with norms squared 9 and 4; X^T y=(18,8); lambda=3. First ridge coeff is ____.',
        '1.5',
        '18/(9+3)=1.5.',
        marks=2, diff='M'))
    o.append(mcq(
        'Ridge',
        'Wide matrix p>n with dependent columns:',
        'OLS has a unique minimiser, ridge does not',
        'ridge has a unique minimiser, OLS does not',
        'both fail to have any minimiser',
        'both yield identical coefficients',
        'B',
        'Ridge is strictly convex; OLS loss is flat along the null space.',
        marks=2, diff='M'))
    o.append(mcq(
        'Ridge',
        'Standardising features before ridge is recommended because',
        'lambda then penalises coefficients on a comparable scale',
        'OLS already requires standardising to exist',
        'standardising removes the need for a penalty',
        'it converts ridge into LDA',
        'A',
        'L2 penalty is not scale-invariant.',
        marks=1, diff='E'))
    o.append(msq(
        'Ridge',
        'Which statements about ridge are TRUE?',
        'Effective degrees of freedom fall as lambda grows',
        'Ridge paths are piecewise linear in lambda like lasso',
        'For a fixed design, b_ridge=(X^T X + lambda I)^{-1} X^T y',
        'Ridge zeros coefficients exactly for large finite lambda',
        'A;C',
        'Ridge shrinks but does not zero; paths are smooth.',
        marks=2, diff='H'))
    o.append(nat(
        'Ridge',
        'Scalar ridge on x=1,1,1 and y=3,5,7 (no intercept). X^T X=3, X^T y=15, lambda=2. Coefficient is ____.',
        '3',
        '15/(3+2)=3.',
        marks=1, diff='M'))
    o.append(mcq(
        'Ridge',
        'A report claims raising lambda increased training R^2 versus OLS on the same design. This is',
        'expected because ridge always fits better',
        'impossible: OLS minimises training SSE among linear predictors, and ridge is a shrinkage of it',
        'required by Gauss-Markov',
        'proof that lambda was negative',
        'B',
        'Ridge cannot beat OLS on train SSE unless lambda=0.',
        marks=2, diff='H'))
    o.append(nat(
        'Ridge',
        'X^T X=diag(2,2), X^T y=[4,2], lambda=2. Ridge b2 equals ____.',
        '0.5',
        '2/(2+2)=0.5.',
        marks=2, diff='M'))
    o.append(mcq(
        'Ridge',
        'Bias-variance reading of moderate ridge vs OLS in an ill-posed problem:',
        'cuts variance more than it adds bias, often lowering expected prediction error',
        'cuts bias and raises variance',
        'is identical to dropping the intercept',
        'is the same as k-means',
        'A',
        'Classic shrinkage trade-off under multicollinearity.',
        marks=1, diff='M'))
    o.append(nat(
        'Ridge',
        'OLS 1-D slope (no intercept) is 5. Ridge uses lambda so that (X^T X+lambda)=2(X^T X). Ridge slope is ____.',
        '2.5',
        'Half of OLS: 2.5.',
        marks=2, diff='M'))
    o.append(mcq(
        'Ridge',
        'Ridge closed form replaces the OLS normal equation X^T X b = X^T y by',
        '(X^T X + lambda I) b = X^T y',
        'X^T X b + lambda = y',
        'X b = lambda y',
        'b = lambda X^T y',
        'A',
        'The defining linear system of ridge.',
        marks=1, diff='E'))
    o.append(mcq(
        'Logistic',
        'Logistic regression models P(Y=1|x) as',
        'w^T x (unbounded)',
        'sigmoid(w^T x+b)=1/(1+exp(-(w^T x+b)))',
        'the N(w^T x,1) density',
        'a hard 0-1 threshold of w^T x',
        'B',
        'Logistic sigmoid maps a linear score to (0,1).',
        marks=1, diff='E'))
    o.append(nat(
        'Logistic',
        'Fitted sigmoid outputs f(x)=0.8. The derivative f(x)(1-f(x)) equals ____.',
        '0.16',
        '0.8*0.2=0.16.',
        marks=1, diff='E'))
    o.append(nat(
        'Logistic',
        'Sigmoid output 0.2. Then f(1-f) equals ____.',
        '0.16',
        '0.2*0.8=0.16 by symmetry.',
        marks=1, diff='E'))
    o.append(nat(
        'Logistic',
        'Logistic score z=2x-2. At x=1 the predicted probability is ____.',
        '0.5',
        'z=0, sigmoid(0)=1/2.',
        marks=1, diff='E'))
    o.append(mcq(
        'Logistic',
        'log P/(1-P)=3-6x. The P=0.5 boundary occurs at x equal to',
        '0',
        '0.5',
        '2',
        '3',
        'B',
        '3-6x=0 => x=1/2.',
        marks=1, diff='M'))
    o.append(msq(
        'Logistic',
        'Which are TRUE of binary logistic regression trained by MLE?',
        'Negative log-likelihood is convex in (w,b)',
        'With linearly separable data and no regularisation, ||w|| may diverge',
        'Predicted probabilities are guaranteed to be exactly 0 or 1 on train points',
        'A feature-scale change can be absorbed into w',
        'A;B;D',
        'NLL is convex; separability sends unregularised MLE to infinity; p stays in (0,1).',
        marks=2, diff='H'))
    o.append(nat(
        'Logistic',
        'One pair x=2, y=1. Model p=sigmoid(w x), current w=0. Grad of log-loss is (p-y)x. One SGD step eta=0.5 updates w to ____.',
        '0.5',
        'p=0.5, grad=(0.5-1)*2=-1, w := 0-0.5*(-1)=0.5.',
        marks=2, diff='H'))
    o.append(nat(
        'Logistic',
        'Current w=1, x=0 so p=0.5, y=0, eta=1, grad=(p-y)x=0. After one SGD step w equals ____.',
        '1',
        'Gradient 0 because x=0.',
        marks=1, diff='M'))
    o.append(mcq(
        'Logistic',
        'Binary cross-entropy on a single point with y=1 and p=0.5 equals (natural log)',
        '0',
        'log 2',
        '1',
        '0.5',
        'B',
        '-log(0.5)=log 2.',
        marks=1, diff='M'))
    o.append(mcq(
        'Logistic',
        'Unlike LDA, logistic regression',
        'requires class-conditional Gaussians',
        'models P(Y|x) directly and does not need a Gaussian class-conditional assumption',
        'cannot use a linear decision boundary',
        'cannot output probabilities',
        'B',
        'Logistic is a discriminative model for the log-odds.',
        marks=1, diff='M'))
    o.append(nat(
        'Logistic',
        'Odds P/(1-P)=3. Then P equals ____.',
        '0.75',
        'P=3(1-P) => P=0.75.',
        marks=1, diff='E'))
    o.append(mcq(
        'Logistic',
        'A 1-D logistic classifier predicts class 1 iff 4x-2>=0. The threshold on x is',
        '0',
        '0.5',
        '2',
        '4',
        'B',
        'x>=1/2.',
        marks=1, diff='E'))
    o.append(nat(
        'Logistic',
        'Sigmoid derivative at f(x)=0.5 equals ____.',
        '0.25',
        '0.5*0.5=0.25.',
        marks=1, diff='E'))
    o.append(mcq(
        'Logistic',
        'L2-regularised logistic adds (lambda/2)||w||^2. As lambda grows, predictions',
        'must become quadratic',
        'approach an intercept-only (prior) classifier as w shrinks to 0',
        'interpolate every label',
        'become k-means',
        'B',
        'Shrinkage drives w to 0.',
        marks=2, diff='M'))
    o.append(mcq(
        'Logistic',
        'A logistic weight on hours_studied is +1.2. Holding others fixed, one extra hour',
        'adds 1.2 to the probability',
        'adds 1.2 to the log-odds',
        'multiplies the probability by 1.2',
        'is illegal in logistic models',
        'B',
        'Coefficients are log-odds slopes.',
        marks=1, diff='M'))
    o.append(nat(
        'Logistic',
        'Score z=0. Predicted class-1 probability is ____.',
        '0.5',
        'sigmoid(0)=0.5.',
        marks=1, diff='E'))
    o.append(mcq(
        'Logistic',
        'For a linear logistic model in 2-D with w nonzero, {x: P(Y=1|x)=0.5} is',
        'a line (a hyperplane in 2-D)',
        'always a circle',
        'a union of k-means cells',
        'empty',
        'A',
        'P=0.5 iff w^T x+b=0.',
        marks=1, diff='M'))
    o.append(nat(
        'Logistic',
        'p=0.9. Then p(1-p) equals ____.',
        '0.09',
        '0.9*0.1=0.09.',
        marks=1, diff='E'))
    o.append(mcq(
        'kNN',
        'Train: A(0,0) class0, B(0,2) class0, C(2,0) class1, D(2,2) class1. Query q=(0,1). Euclidean 1-NN predicts',
        'class 0, because A and B are both at distance 1 while C,D are farther',
        'class 1',
        'class 0 only if Manhattan is used',
        'a four-way tie',
        'A',
        'd(q,A)=d(q,B)=1, d(q,C)=d(q,D)=sqrt5.',
        marks=2, diff='M'))
    o.append(nat(
        'kNN',
        'Points P(0,0) y=1, Q(4,0) y=2, R(0,3) y=2. Query (1,1). Euclidean 1-NN label is ____.',
        '1',
        'd(P)~1.41, d(R)~2.24, d(Q)~3.16 so P wins.',
        marks=2, diff='M'))
    o.append(mcq(
        'kNN',
        'On P(0,0):1, Q(4,0):2, R(0,3):2, query (1,1), 3-NN majority label is',
        '1 because P wins',
        '2 because Q and R out-vote P',
        'undefined because k exceeds n',
        'always equal to 1-NN',
        'B',
        'Labels 1,2,2 majority 2.',
        marks=1, diff='E'))
    o.append(msq(
        'kNN',
        'Which statements about k-NN classification are TRUE?',
        'Training error of 1-NN is 0 if no two equal-x points have different labels',
        'As k->n the prediction approaches the global majority class',
        '1-NN typically has lower bias and higher variance than a large k',
        'k-NN needs an explicit parametric density for each class',
        'A;B;C',
        'k-NN is a nonparametric local vote; no class-density model is fitted.',
        marks=2, diff='M'))
    o.append(nat(
        'kNN',
        '1-D train x=0,1,2,3 labels 0,0,1,1. Query x=1.6, k=1 Euclidean. Predicted label is ____.',
        '1',
        'Nearest is x=2 (dist 0.4) label 1.',
        marks=1, diff='E'))
    o.append(nat(
        'kNN',
        'Same 1-D train x=0,1,2,3 labels 0,0,1,1. Query 1.6 with k=3. Majority label is ____.',
        '1',
        'Neighbours x=2,1,3 labels 1,0,1 majority 1.',
        marks=2, diff='H'))
    o.append(mcq(
        'kNN',
        'Manhattan 1-NN on A(0,0):0, B(3,0):1, query (1,1). Predicted class is',
        '0, since |1|+|1|=2 < |2|+|1|=3',
        '1',
        'tie',
        '2',
        'A',
        'd1(A)=2, d1(B)=3.',
        marks=1, diff='M'))
    o.append(mcq(
        'kNN',
        'A large k in k-NN, relative to k=1, typically',
        'fits more wiggly decision boundaries',
        'smooths the decision boundary and raises bias',
        'is undefined for classification',
        'always overfits more than 1-NN',
        'B',
        'Larger neighbourhoods average more.',
        marks=1, diff='E'))
    o.append(nat(
        'kNN',
        'Five neighbour labels 1,1,1,0,0. 5-NN majority class is ____.',
        '1',
        'Votes 3-2.',
        marks=1, diff='E'))
    o.append(mcq(
        'kNN',
        'k-NN regression k=2 on (0,0),(2,4),(10,0). Query x=1. Prediction is',
        '0',
        '2',
        '4',
        '1',
        'B',
        'Nearest (0,0) and (2,4); mean response 2.',
        marks=2, diff='M'))
    o.append(mcq(
        'kNN',
        'Feature A in millimetres, B in kilometres. Euclidean k-NN without scaling will',
        'treat both axes as equally important automatically',
        'be dominated by the large-magnitude axis unless features are scaled',
        'become logistic regression',
        'ignore the training labels',
        'B',
        'Distance k-NN is not scale-invariant.',
        marks=1, diff='E'))
    o.append(nat(
        'kNN',
        'Train on the line -2,-1,0,8 labels 1,1,1,0. 3-NN at query 7. Predicted label is ____.',
        '1',
        'Neighbours 8,0,-1 labels 0,1,1 majority 1.',
        marks=2, diff='M'))
    o.append(nat(
        'kNN',
        '3-NN, 2-class, neighbours labelled 1,1,0. Predicted class is ____.',
        '1',
        'Majority 1.',
        marks=1, diff='E'))
    o.append(mcq(
        'kNN',
        'k-NN is a lazy learner meaning',
        'it updates a global w by SGD at train time',
        'it stores the training set and defers computation to query time',
        'it discards the training set after building a tree of depth k',
        'it requires linearly separable data',
        'B',
        'No parametric model is fitted at train time.',
        marks=1, diff='E'))
    o.append(nat(
        'kNN',
        'Points (0,0),(0,2),(6,0). Query (1,0). Euclidean 1-NN distance to the winner is ____.',
        '1',
        'Winner (0,0), distance 1.',
        marks=1, diff='E'))
    o.append(mcq(
        'kNN',
        'If k equals n, unweighted majority-vote k-NN ignores the query location and returns',
        'the 1-NN label',
        'the training majority class',
        'a uniformly random class always',
        'the mean of the features',
        'B',
        'Every training point is a neighbour.',
        marks=1, diff='E'))
    o.append(mcq(
        'kNN',
        'Distance-weighted 1-NN (weight 1/d) on two neighbours at distances 1 and 3 with labels 0 and 1. The query is labelled',
        '0, because the nearer neighbour gets all the 1-NN vote; with k=1 only the nearest is used',
        '1',
        'the mean 0.5 as a class',
        'undefined',
        'A',
        '1-NN uses only the single nearest point.',
        marks=1, diff='M'))
    o.append(mcq(
        'NaiveBayes',
        'Bernoulli NB on K classes and one binary feature, counting K priors and K Bernoulli weights, has parameter count',
        'K',
        '2K',
        '2K+1',
        'K^2',
        'B',
        'K priors + K success probabilities = 2K.',
        marks=1, diff='M'))
    o.append(nat(
        'NaiveBayes',
        'Gaussian NB, K classes, one scalar feature, class-specific means, ONE shared variance, and K priors. Parameter count is ____.',
        '2K+1',
        'K priors + K means + 1 variance = 2K+1.',
        marks=1, diff='M'))
    o.append(nat(
        'NaiveBayes',
        'Gaussian NB with 3 classes and 4 features, class-specific means and variances plus 3 priors. Parameter count is ____.',
        '27',
        '3 + 12 means + 12 vars = 27.',
        marks=2, diff='M'))
    o.append(mcq(
        'NaiveBayes',
        "Spam: 3/5 docs contain 'buy'; ham: 1/5 contain 'buy'; P(spam)=1/2. A mail with 'buy' has P(spam|buy) equal to",
        '1/2',
        '3/4',
        '3/5',
        '1/4',
        'B',
        '0.6*0.5=0.3 and 0.2*0.5=0.1, posterior 0.3/0.4=0.75.',
        marks=2, diff='M'))
    o.append(nat(
        'NaiveBayes',
        'P(C)=0.4, P(X=1|C)=0.5, P(X=1|D)=0.1, P(D)=0.6. Then P(C|X=1) rounded to 2 decimals is ____.',
        '0.77',
        '0.2 / (0.2+0.06) = 0.2/0.26 ~ 0.77.',
        marks=2, diff='M'))
    o.append(msq(
        'NaiveBayes',
        'Which modelling assumptions/facts does naive Bayes involve?',
        'Features are conditionally independent given the class',
        'The class prior may be estimated by class frequencies',
        'Features must be jointly Gaussian with a full covariance',
        'A zero training count for a (feature,class) pair can zero a Bernoulli likelihood unless smoothed',
        'A;B;D',
        'Full joint Gaussian is LDA/QDA, not NB.',
        marks=2, diff='M'))
    o.append(nat(
        'NaiveBayes',
        'Laplace add-1 for a binary word given spam: 0 occurrences in 8 spam mails. Smoothed P(word=1|spam) is ____.',
        '0.1',
        '(0+1)/(8+2)=0.1.',
        marks=1, diff='M'))
    o.append(mcq(
        'NaiveBayes',
        'Gaussian NB with diagonal class-covariances differs from LDA because LDA',
        'does not use class priors',
        'shares one covariance across classes and does not force feature independence unless that covariance is diagonal',
        'cannot produce a linear boundary',
        'is identical to 1-NN',
        'B',
        'LDA: shared Sigma, possibly correlated features.',
        marks=2, diff='M'))
    o.append(nat(
        'NaiveBayes',
        '2-class Bernoulli NB on 5 binary features uses 2 priors and 5 coin-weights per class. Parameter count is ____.',
        '12',
        '2+10=12.',
        marks=1, diff='E'))
    o.append(mcq(
        'NaiveBayes',
        "Four spam bags contribute 8 tokens with 'win' appearing twice. Multinomial NB MLE P(win|spam) without smoothing is",
        '1/2',
        '2/4',
        '2/8',
        '1/8',
        'C',
        '2/8=1/4.',
        marks=2, diff='M'))
    o.append(nat(
        'NaiveBayes',
        'Priors 0.7 and 0.3, likelihoods 0.2 and 0.9. MAP class index (1 or 2) is ____.',
        '2',
        '0.14 vs 0.27, class 2.',
        marks=1, diff='E'))
    o.append(mcq(
        'NaiveBayes',
        'Why sum log class-conditionals in NB?',
        'Logs cancel the independence assumption',
        'To avoid underflow of a long product of probabilities',
        'Because MLE is undefined in log space',
        'So that features become dependent',
        'B',
        'Numerical underflow of a long product.',
        marks=1, diff='E'))
    o.append(nat(
        'NaiveBayes',
        'Add-1 Laplace, word seen 3 times in 14 class-A docs (binary presence). P(word=1|A) is ____.',
        '0.25',
        '(3+1)/(14+2)=4/16=0.25.',
        marks=1, diff='M'))
    o.append(mcq(
        'NaiveBayes',
        'If two features are identical copies, naive Bayes',
        'automatically drops one copy',
        'double-counts that evidence, over-confidently pushing posteriors',
        'becomes SVM',
        'is still well-specified because copies are independent',
        'B',
        'Independence is badly false; likelihood is squared.',
        marks=2, diff='M'))
    o.append(nat(
        'NaiveBayes',
        'Three classes, uniform priors, likelihoods 0.1, 0.2, 0.7. Posterior of class 3 is ____.',
        '0.7',
        'Uniform priors: posterior equals normalised likelihoods already summing to 1.',
        marks=1, diff='E'))
    o.append(msq(
        'NaiveBayes',
        'Which statements are TRUE of naive Bayes?',
        'NB can still classify well even when independence is mildly false',
        'A missing category count can zero a whole posterior path without smoothing',
        'Gaussian NB boundaries are linear if covariances are shared and diagonal (a special LDA)',
        'NB requires linearly separable classes',
        'A;B;C',
        'Separability is not required. Zero counts are fatal without smoothing.',
        marks=2, diff='H'))
    o.append(nat(
        'NaiveBayes',
        'Binary feature d=1, classes K=4, Bernoulli NB with K priors. Parameter count is ____.',
        '8',
        '4+4=8.',
        marks=1, diff='E'))
    o.append(mcq(
        'NaiveBayes',
        'P(Y=1)=0.2, P(X=red|Y=1)=0.9, P(X=red|Y=0)=0.3. Then P(Y=1|X=red) is closest to',
        '0.20',
        '0.43',
        '0.90',
        '0.06',
        'B',
        '0.18/(0.18+0.24)=0.18/0.42=3/7~0.43.',
        marks=2, diff='M'))
    o.append(mcq(
        'LDA',
        "Fisher's two-class LDA seeks a direction w maximising",
        'w^T S_W w / w^T S_B w',
        'w^T S_B w / w^T S_W w',
        '||w||_1',
        'the Gini of the projected labels',
        'B',
        'Between-class scatter over within-class scatter.',
        marks=1, diff='E'))
    o.append(mcq(
        'LDA',
        'Two-class means m1,m2 and invertible pooled S_W. An optimal Fisher direction is',
        'S_W (m1+m2)',
        'S_W^{-1} (m1-m2)',
        'S_B^{-1} (m1+m2)',
        'PC1 of the pooled unlabelled data',
        'B',
        'w ? S_W^{-1}(m1-m2).',
        marks=2, diff='M'))
    o.append(msq(
        'LDA',
        'Assumptions of classical Gaussian LDA (two classes) include',
        'class-conditional Gaussians',
        'a shared covariance matrix',
        'equal class priors (mandatory)',
        'a linear log-posterior-odds boundary',
        'A;B;D',
        'Priors need not be equal; they only shift the threshold.',
        marks=2, diff='M'))
    o.append(nat(
        'LDA',
        'Class means 0 and 4 (1-D), shared variance 1, equal priors. LDA threshold is ____.',
        '2',
        'Midpoint 2.',
        marks=1, diff='E'))
    o.append(nat(
        'LDA',
        '1-D two-class means 0 and 2, equal priors and equal variance. LDA threshold is ____.',
        '1',
        'Midpoint 1.',
        marks=1, diff='E'))
    o.append(mcq(
        'LDA',
        'S_W is singular when, in generic position,',
        'n is huge and features independent',
        'the feature dimension p exceeds within-class rank (about n-K)',
        'classes are well separated',
        'priors are equal',
        'B',
        'Within scatter lives in an (n-K)-dimensional space.',
        marks=2, diff='H'))
    o.append(nat(
        'LDA',
        'Class A samples 1,2,3 and class B samples 5,6,7. Pooled sample variance (divisor n1+n2-2) is ____.',
        '1',
        'Each class has sample var 1; pooled=1.',
        marks=2, diff='M'))
    o.append(mcq(
        'LDA',
        'Multi-class LDA with K classes projects onto at most how many useful Fisher directions?',
        'K',
        'K-1',
        'n',
        '1 always',
        'B',
        'Rank(S_B)<=K-1.',
        marks=1, diff='M'))
    o.append(mcq(
        'LDA',
        'LDA vs logistic on well-separated Gaussian classes with shared Sigma:',
        'LDA is the generative counterpart and is statistically efficient when its model is true',
        'logistic always has strictly lower error',
        'LDA cannot output a posterior',
        'they fit identical parameters for any finite sample',
        'A',
        'LDA uses p(x,y); logistic uses only p(y|x).',
        marks=2, diff='H'))
    o.append(nat(
        'LDA',
        'Means m1=(0,0), m2=(2,0), S_W=I. Fisher vector S_W^{-1}(m1-m2) has second coordinate ____.',
        '0',
        'I^{-1}(-2,0)=(-2,0).',
        marks=1, diff='E'))
    o.append(msq(
        'LDA',
        'Which are TRUE of S_B and S_W in two-class Fisher LDA?',
        'S_B is rank-1, proportional to (m1-m2)(m1-m2)^T',
        'S_W is a pooled within-class scatter',
        'The Rayleigh quotient leads to the generalised eigenproblem S_B w = lambda S_W w',
        'S_W^{-1} S_B is always symmetric even if S_W is not a multiple of I',
        'A;B;C',
        'S_W^{-1} S_B need not be symmetric; one solves a generalised eigenproblem.',
        marks=2, diff='H'))
    o.append(mcq(
        'LDA',
        'If class covariances are equal but features are correlated, Gaussian NB (diagonal) is misspecified while LDA',
        'can still model that correlation through the shared Sigma',
        'also forces diagonal Sigma',
        'becomes k-means',
        'cannot use priors',
        'A',
        "LDA's shared Sigma may have off-diagonals.",
        marks=1, diff='M'))
    o.append(nat(
        'LDA',
        'Projected LDA scores have class means -3 and +3 (balanced). Midpoint threshold is ____.',
        '0',
        '(-3+3)/2=0.',
        marks=1, diff='E'))
    o.append(mcq(
        'LDA',
        'QDA drops which LDA assumption?',
        'Gaussian class-conditionals',
        'shared covariance across classes',
        'existence of class priors',
        'use of Bayes rule',
        'B',
        'Class-specific Sigma yields quadratic boundaries.',
        marks=1, diff='M'))
    o.append(nat(
        'LDA',
        'n1=n2=2, class1: 0,2 and class2: 8,10. Difference of means m2-m1 is ____.',
        '8',
        'Means 1 and 9.',
        marks=1, diff='E'))
    o.append(mcq(
        'LDA',
        'Using PC1 of pooled unlabelled data as the LDA direction is',
        'always identical to Fisher LDA',
        'generally different, because PCA maximises total variance not the between/within ratio',
        'impossible in 2-D',
        'required when S_W is invertible',
        'B',
        'PCA is not LDA.',
        marks=1, diff='M'))
    o.append(mcq(
        'SVM',
        'Hard-margin linear SVM on linearly separable data minimises',
        '(1/2)||w||^2 s.t. y_i(w?x_i+b)>=1',
        'hinge+L1 with C=0',
        '||w||_1 s.t. y_i(w?x_i+b)>=0',
        'the Gini of slack',
        'A',
        'Canonical hard-margin primal.',
        marks=1, diff='E'))
    o.append(nat(
        'SVM',
        'Hyperplane w=(3,4), b=0. The Euclidean ||w|| is ____.',
        '5',
        '3-4-5 triangle.',
        marks=1, diff='E'))
    o.append(nat(
        'SVM',
        'Canonical hard-margin SVM with ||w||=4. Margin width 2/||w|| equals ____.',
        '0.5',
        '2/4=0.5.',
        marks=1, diff='E'))
    o.append(mcq(
        'SVM',
        'Points (1,1)+,(1,-1)+,(-1,1)-,(-1,-1)-. A hard-margin SVM using the separator x=0 has how many support vectors?',
        '1',
        '2',
        '4',
        '0',
        'C',
        'All four lie on the margin planes after scaling.',
        marks=2, diff='M'))
    o.append(msq(
        'SVM',
        'Which points can be support vectors in a soft-margin linear SVM?',
        'Points on the margin planes',
        'Misclassified points',
        'Points inside the margin strip but correctly signed',
        'A far, correctly classified point with dual alpha exactly 0',
        'A;B;C',
        'SVs have alpha>0. Well-inside correct points have alpha=0.',
        marks=2, diff='M'))
    o.append(mcq(
        'SVM',
        'The dual of a kernel SVM depends on data only through',
        'inner products (or kernel evaluations) K(x_i,x_j)',
        'explicit high-dimensional phi(x) coordinates',
        'decision-tree Gini',
        'k-means centroids',
        'A',
        'Kernel trick.',
        marks=1, diff='E'))
    o.append(nat(
        'SVM',
        'Hinge loss of a point with y f(x)=3 is ____.',
        '0',
        'max(0,1-3)=0.',
        marks=1, diff='E'))
    o.append(nat(
        'SVM',
        'Hinge loss of a point with y f(x)=-1 is ____.',
        '2',
        'max(0,1-(-1))=2.',
        marks=1, diff='E'))
    o.append(nat(
        'SVM',
        'Hinge loss at y f(x)=0.2 is ____.',
        '0.8',
        'max(0,1-0.2)=0.8.',
        marks=1, diff='E'))
    o.append(mcq(
        'SVM',
        'Increasing C in min 1/2||w||^2 + C sum xi typically',
        'allows more margin violations',
        'penalises slack more, tending toward a harder margin',
        'changes the kernel degree',
        'has no primal effect',
        'B',
        'Large C ~ hard-margin.',
        marks=1, diff='M'))
    o.append(mcq(
        'SVM',
        'A linear SVM weight w is a linear combination of training points with nonzero coefficients only for',
        'all points equally',
        'support vectors',
        'the class means as in LDA',
        'the first PC',
        'B',
        'w = sum alpha_i y_i x_i, alpha_i=0 for non-SVs.',
        marks=1, diff='E'))
    o.append(nat(
        'SVM',
        'Two 1-D SVs at x=-2 (label -1) and x=4 (label +1). The midpoint threshold is at x= ____.',
        '1',
        '(-2+4)/2=1.',
        marks=1, diff='M'))
    o.append(msq(
        'SVM',
        'Which are valid PSD kernels commonly used with SVMs?',
        'Linear K=x^T z',
        'Gaussian RBF K=exp(-||x-z||^2/(2 sigma^2))',
        'Polynomial K=(x^T z+c)^d for c>=0 and d a positive integer',
        'K(x,z)=||x-z||^2 (raw squared Euclidean)',
        'A;B;C',
        'Raw squared Euclidean is not a kernel by itself.',
        marks=2, diff='H'))
    o.append(mcq(
        'SVM',
        'XOR in the plane is not linearly separable. A degree-2 polynomial kernel',
        'cannot help',
        'can make the classes linearly separable in the implicit feature space',
        'reduces XOR to k-means',
        'forces the margin to 0',
        'B',
        'phi includes the product x1 x2.',
        marks=1, diff='M'))
    o.append(nat(
        'SVM',
        'Canonical w=(0,2), b=-2. Point x=(0,2), y=+1 has y(w?x+b) equal to ____.',
        '2',
        '4-2=2.',
        marks=1, diff='M'))
    o.append(mcq(
        'SVM',
        'If training data are linearly separable, a hard-margin SVM',
        'has a unique maximum-margin w (in general position)',
        'does not exist',
        'always coincides with the OLS hyperplane',
        'has margin 0',
        'A',
        'Max-margin separator is unique in w for generic separable data.',
        marks=2, diff='H'))
    o.append(mcq(
        'SVM',
        'A dual variable pinned at alpha_i=C (box 0<=alpha<=C) typically corresponds to',
        'a non-support vector',
        'a margin violator (slack or misclassified)',
        'the unique class mean',
        'hinge 0 necessarily',
        'B',
        'KKT: alpha=C usually means slack.',
        marks=2, diff='H'))
    o.append(nat(
        'SVM',
        '1-D labels: -3,-1 are -1 and +2,+5 are +1. Hard-margin SV gap (margin width) is ____.',
        '3',
        'Closest opposite pair -1 and +2, gap 3.',
        marks=2, diff='M'))
    o.append(mcq(
        'SVM',
        'Soft-margin slack xi_i is 0 whenever',
        'y_i f(x_i) >= 1',
        'the point is a support vector',
        'C=0',
        'the kernel is RBF',
        'A',
        'No slack once the point is on the correct side of the margin.',
        marks=1, diff='M'))
    o.append(nat(
        'DecisionTree',
        'A binary node has 2 positives and 2 negatives. Gini 1-sum p_c^2 equals ____.',
        '0.5',
        '1-2*0.25=0.5.',
        marks=1, diff='E'))
    o.append(nat(
        'DecisionTree',
        'A pure node with 5 positives and 0 negatives has Gini ____.',
        '0',
        '1-1^2=0.',
        marks=1, diff='E'))
    o.append(nat(
        'DecisionTree',
        'Node with 3 yes and 1 no. Gini equals ____.',
        '0.375',
        '1-9/16-1/16=0.375.',
        marks=1, diff='M'))
    o.append(mcq(
        'DecisionTree',
        'Rows (colour,label): (red,+),(red,+),(blue,+),(blue,-). Split on colour. Weighted child Gini is',
        '0',
        '0.25',
        '0.50',
        '1',
        'B',
        '0.5*0 + 0.5*0.5=0.25.',
        marks=2, diff='M'))
    o.append(nat(
        'DecisionTree',
        'Parent Gini 0.5, weighted children Gini 0.25. Gini gain is ____.',
        '0.25',
        '0.5-0.25=0.25.',
        marks=1, diff='E'))
    o.append(mcq(
        'DecisionTree',
        'Entropy of a 50-50 binary node (log base 2) is',
        '0',
        '0.5',
        '1 bit',
        '2 bits',
        'C',
        'H=1 bit.',
        marks=1, diff='E'))
    o.append(msq(
        'DecisionTree',
        'Which splits are useless for a greedy impurity tree?',
        'Reusing a feature on a child that is already pure (gain 0)',
        'A threshold that sends every row to one child',
        'A split that improves gain on an impure node',
        'A multiway split on a 3-level categorical at the root',
        'A;B',
        'Zero-gain / degenerate splits are useless.',
        marks=2, diff='M'))
    o.append(nat(
        'DecisionTree',
        'Right child has counts 1+ and 4-. Its Gini is 0.32. Report 100 times that Gini, i.e. ____.',
        '32',
        '1-(1/5)^2-(4/5)^2=0.32.',
        marks=2, diff='H'))
    o.append(mcq(
        'DecisionTree',
        'Unpruned trees that split to purity tend to',
        'underfit with high bias',
        'overfit: low training error, high variance',
        'match ridge with large lambda',
        'be identical to LDA',
        'B',
        'Deep trees interpolate labels.',
        marks=1, diff='E'))
    o.append(mcq(
        'DecisionTree',
        'Axis-aligned binary trees in 2-D produce regions that are',
        'always balls',
        'rectangles (products of intervals), possibly unbounded',
        'linear halfspaces only',
        'circles centred at means',
        'B',
        'Each split is x_j ? t.',
        marks=1, diff='E'))
    o.append(nat(
        'DecisionTree',
        'A full binary classification tree has 5 leaves. Internal split nodes: ____.',
        '4',
        'internals=leaves-1.',
        marks=1, diff='E'))
    o.append(mcq(
        'DecisionTree',
        'To predict a numeric house price with piecewise-constant axis splits one uses a',
        'classification tree with Gini',
        'regression tree, typically with squared-error split criterion',
        'hard-margin SVM',
        'k-medoid',
        'B',
        'Regression trees minimise child SSE.',
        marks=1, diff='E'))
    o.append(nat(
        'DecisionTree',
        'Node [+, -]=[6,2]. Majority-class misclassification rate is ____.',
        '0.25',
        '2/8=0.25.',
        marks=1, diff='E'))
    o.append(msq(
        'DecisionTree',
        'Compared with a linear SVM, a deep axis-aligned tree',
        'can represent XOR without a kernel',
        'has a piecewise-constant decision surface',
        'always maximises the geometric margin',
        'is more prone to high variance when unpruned',
        'A;B;D',
        'XOR is two splits; no margin objective.',
        marks=2, diff='M'))
    o.append(nat(
        'DecisionTree',
        'Parent entropy 1 bit, children weights 1/2 with entropies 0 and 1. Information gain (bits) is ____.',
        '0.5',
        '1-0.5=0.5.',
        marks=1, diff='M'))
    o.append(mcq(
        'DecisionTree',
        'A categorical ID with as many levels as rows, if allowed to split fully, will',
        'have zero training error and almost surely terrible generalisation',
        'be ignored by Gini because gain is 0',
        'become a support vector',
        'estimate a ridge penalty',
        'A',
        'ID splits isolate each row.',
        marks=2, diff='M'))
    o.append(nat(
        'DecisionTree',
        'A node of 10 rows splits into pure children of sizes 7 and 3. Parent majority-class error was ____.',
        '0.3',
        '7 vs 3 opposite labels, error 0.3.',
        marks=2, diff='M'))
    o.append(mcq(
        'DecisionTree',
        'Matching task to algorithm: piecewise-constant 2-way classification on a tiny labelled table of colour vs label is done by a',
        'decision tree using Gini or entropy',
        'ridge with lambda=10^6',
        'PCA projection',
        'k-means with k=10',
        'A',
        "That's the running example of a classification tree.",
        marks=1, diff='E'))
    o.append(mcq(
        'BiasVariance',
        'For k-NN classification, decreasing k from 51 to 1 typically',
        'raises bias and lowers variance',
        'lowers bias and raises variance',
        'does not affect the decomposition',
        'makes the classifier linear',
        'B',
        '1-NN is wiggly (high variance, low bias).',
        marks=1, diff='E'))
    o.append(mcq(
        'BiasVariance',
        'Raising the ridge penalty lambda typically',
        'lowers bias, raises variance',
        'raises bias, lowers variance',
        'raises both',
        'has no bias effect',
        'B',
        'Shrinkage trades bias for variance.',
        marks=1, diff='E'))
    o.append(msq(
        'BiasVariance',
        'Which moves sit on the high-variance side?',
        'Degree-9 polynomial through 10 noisy points',
        '1-NN instead of 25-NN',
        'Unpruned deep trees',
        'Intercept-only mean predictor on a clearly linear trend',
        'A;B;C',
        'The mean predictor is high bias, low variance.',
        marks=2, diff='M'))
    o.append(mcq(
        'BiasVariance',
        'Expected test MSE of a regression estimator decomposes (squared loss) as',
        'noise + bias^2 + variance',
        'only variance',
        'only bias',
        'hinge + Gini',
        'A',
        'Standard decomposition.',
        marks=1, diff='E'))
    o.append(mcq(
        'BiasVariance',
        'A linear fit to a sinusoid is a prototype of',
        'high bias',
        'zero approximation error',
        'infinite variance always',
        'perfect test R^2',
        'A',
        'Systematic misspecification.',
        marks=1, diff='E'))
    o.append(nat(
        'BiasVariance',
        'Noise=1, bias^2=4, variance=3. Expected MSE is ____.',
        '8',
        '1+4+3=8.',
        marks=1, diff='E'))
    o.append(mcq(
        'BiasVariance',
        'Training error of 1-NN (no label noise, unique x) is 0, yet test error can be large. This gap signals',
        'high variance / overfit',
        'high bias / underfit',
        'a biased intercept in ridge',
        'd-separation',
        'A',
        'Zero train error with poor test is overfit.',
        marks=1, diff='E'))
    o.append(msq(
        'BiasVariance',
        'Which statements are TRUE?',
        'Bayes error is a lower bound no model can beat',
        'Variance of an estimator usually falls with n',
        'A more flexible model always has lower test error',
        'Regularisation is one way to move along the bias-variance curve',
        'A;B;D',
        'Flexibility can overfit; test error is U-shaped.',
        marks=2, diff='M'))
    o.append(mcq(
        'BiasVariance',
        'k-fold CV is used in this story mainly to',
        'estimate prediction error and help pick a complexity knob',
        'remove the noise term',
        'force bias to 0',
        'compute S_W^{-1} S_B',
        'A',
        'CV estimates extra-sample error.',
        marks=1, diff='E'))
    o.append(nat(
        'BiasVariance',
        'Two uncorrelated unbiased estimators have variances 4 and 9. Variance of their average is ____.',
        '3.25',
        '(4+9)/4=3.25.',
        marks=2, diff='M'))
    o.append(mcq(
        'BiasVariance',
        'As polynomial degree grows to n-1 on n noiseless distinct x, train SSE',
        'stays constant',
        'tends to 0 (interpolation)',
        'must increase',
        'equals SST always',
        'B',
        'Degree n-1 interpolates n points.',
        marks=1, diff='M'))
    o.append(nat(
        'BiasVariance',
        'Bias of an estimator is 2, so bias^2 contribution is ____.',
        '4',
        '2^2=4.',
        marks=1, diff='E'))
    o.append(mcq(
        'BiasVariance',
        '1-NN vs large-k NN: the 1-NN classifier is the one with',
        'higher variance and more jagged boundaries',
        'higher bias and a near-linear boundary always',
        'zero Bayes error always',
        'a unique support vector',
        'A',
        'Small k => flexible, noisy boundary.',
        marks=1, diff='E'))
    o.append(mcq(
        'LOOCV',
        'LOOCV on n distinct training points fits how many models?',
        '1',
        'k',
        'n',
        'n-1',
        'C',
        'One fit per left-out point.',
        marks=1, diff='E'))
    o.append(nat(
        'LOOCV',
        '1-NN LOOCV on (0,class0),(1,class0),(10,class1),(11,class1). Number of misclassified left-out points is ____.',
        '0',
        "Each point's NN among the other three is its same-class twin.",
        marks=2, diff='M'))
    o.append(nat(
        'LOOCV',
        '1-NN LOOCV on 1-D pairs (0,0),(1,0),(2,1), ties broken toward smaller x. Number of LOO errors is ____.',
        '1',
        'Only the point at 2 is classified as 0 when left out.',
        marks=2, diff='H'))
    o.append(mcq(
        'LOOCV',
        'OLS PRESS formula e_i/(1-H_ii) shows that LOOCV residuals',
        'can be computed from a single OLS fit and the leverages',
        'cannot be computed without n separate factorisations even in theory',
        'equal training SSE',
        'are undefined if an intercept is present',
        'A',
        'Classic hat-matrix shortcut.',
        marks=2, diff='H'))
    o.append(nat(
        'LOOCV',
        'n=5 points, 1-NN. Each LOO prediction uses how many neighbours?',
        '1',
        '1-NN uses one of the remaining n-1.',
        marks=1, diff='E'))
    o.append(mcq(
        'LOOCV',
        'LOOCV of the intercept-only mean predictor trains each fold on how many responses when the sample has n points?',
        'n-1',
        'n+1',
        '2n',
        'k',
        'A',
        'Each left-out is predicted by the mean of the other n-1.',
        marks=1, diff='E'))
    o.append(nat(
        'LOOCV',
        'y=1,3,5. Intercept-only model. LOO prediction of the first point is ____.',
        '4',
        'Mean of 3 and 5.',
        marks=1, diff='E'))
    o.append(nat(
        'LOOCV',
        'y=1,3,5 intercept-only. Squared LOO error on the first point is ____.',
        '9',
        '(1-4)^2=9.',
        marks=1, diff='E'))
    o.append(nat(
        'LOOCV',
        'y=1,3,5 intercept-only LOOCV MSE (average of three squared errors) is ____.',
        '6',
        'Errors 3,0,3 squared 9,0,9 average 6.',
        marks=2, diff='M'))
    o.append(mcq(
        'LOOCV',
        'Compared with 5-fold CV, LOOCV on the same data typically',
        'has higher variance of the estimated extra-sample error and is nearly unbiased for training size n-1',
        'always has lower variance',
        'cannot be used for k-NN',
        'requires a validation set besides the n points',
        'A',
        'n highly correlated leave-one-out errors.',
        marks=2, diff='H'))
    o.append(nat(
        'LOOCV',
        '1-NN LOOCV on two points with different labels. Number of errors is ____.',
        '2',
        'Each is classified as the other label.',
        marks=1, diff='M'))
    o.append(nat(
        'KFold',
        'n=200, 10-fold CV. Each training fold has how many points (equal folds)?',
        '180',
        'Test 20, train 180.',
        marks=1, diff='E'))
    o.append(nat(
        'KFold',
        'n=30, 5-fold. Number of models fitted is ____.',
        '5',
        'One per held-out fold.',
        marks=1, diff='E'))
    o.append(mcq(
        'KFold',
        '2-fold CV, y=(0,0,4,8), folds {0,0} vs {4,8}, intercept-only. The four predictions are',
        '6,6,0,0',
        '0,0,4,8',
        '3,3,3,3',
        '2,2,2,2',
        'A',
        'Mean 6 predicts the two zeros; mean 0 predicts 4 and 8.',
        marks=2, diff='M'))
    o.append(msq(
        'KFold',
        'Which are TRUE of k-fold CV?',
        'k=n recovers LOOCV',
        'k=2 has more bias (smaller trains) than k=10 typically',
        'The k test folds partition the n points in standard CV',
        'k-fold requires a separate extra test set of size k',
        'A;B;C',
        'Standard k-fold partitions the training sample.',
        marks=2, diff='M'))
    o.append(nat(
        'KFold',
        '5-fold CV MSE on folds 2,4,3,5,6. Mean CV estimate is ____.',
        '4',
        'Average 4.',
        marks=1, diff='E'))
    o.append(mcq(
        'KFold',
        'Choosing k=n vs k=5 trades',
        'bias and variance of the estimated risk, plus compute',
        'only the kernel width',
        'whether PCA axes are orthogonal',
        'the SVM margin formula',
        'A',
        'Standard CV design trade-off.',
        marks=1, diff='E'))
    o.append(nat(
        'KFold',
        'n=100, 4-fold. Each test fold size is ____.',
        '25',
        '100/4=25.',
        marks=1, diff='E'))
    o.append(mcq(
        'KFold',
        'Nested CV is needed when hyperparameters are tuned because otherwise',
        'the risk estimate is optimistically biased by selection on the same loops',
        'the design matrix is square',
        'one uses only LDA',
        'n=2 always',
        'A',
        'Tuning+evaluating on the same CV leaks.',
        marks=2, diff='H'))
    o.append(nat(
        'KFold',
        'n=45, 9-fold. Train size per fold is ____.',
        '40',
        'Test 5, train 40.',
        marks=1, diff='E'))
    o.append(mcq(
        'KFold',
        'A student reports LOOCV accuracy by training on all n points then evaluating n times. This is',
        'correct LOOCV',
        'not LOOCV: each evaluation must train without the held-out point',
        'k-fold with k=1',
        'ridge with lambda=n',
        'B',
        'Training on all n leaks the test point.',
        marks=2, diff='M'))
    o.append(mcq(
        'MLP',
        'A fully connected net input-4, hidden-5, output-3, biases on hidden and output, no extra layers. Parameter count is',
        '4*5+5*3',
        '4*5+5 + 5*3+3',
        '5*3',
        '4+5+3',
        'B',
        'Weights 20+15, biases 5+3, total 43. Option B is 20+5+15+3=43.',
        marks=2, diff='M'))
    o.append(nat(
        'MLP',
        'Input-2, hidden-2, output-1, with biases on hidden and output. Number of scalar parameters is ____.',
        '9',
        '2*2+2 + 2*1+1 = 4+2+2+1=9.',
        marks=2, diff='M'))
    o.append(nat(
        'MLP',
        "Sigmoid unit outputs 0.8. Local derivative sigma'(z)=sigma(1-sigma) equals ____.",
        '0.16',
        '0.8*0.2=0.16.',
        marks=1, diff='E'))
    o.append(nat(
        'MLP',
        'ReLU(x)=max(0,x). ReLU(-3) equals ____.',
        '0',
        'Negative part is zeroed.',
        marks=1, diff='E'))
    o.append(nat(
        'MLP',
        'ReLU(2.5) equals ____.',
        '2.5',
        'Positive part unchanged.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLP',
        'XOR of two bits cannot be realised by a linear (no hidden layer) classifier, but a one-hidden-layer MLP can, because',
        'the hidden units can create a nonlinear feature map',
        'XOR is linearly separable',
        'MLPs always output 0',
        'weights must be integers',
        'A',
        'Hidden layer provides the nonlinear lifting.',
        marks=1, diff='M'))
    o.append(msq(
        'MLP',
        'Which are TRUE of a feed-forward MLP trained by backprop?',
        'Forward pass computes activations layer by layer',
        'Backprop applies the chain rule to obtain dLoss/dW',
        'A sigmoid hidden layer is a linear function of its input',
        'SGD may use a minibatch gradient instead of the full-batch gradient',
        'A;B;D',
        'Sigmoid is nonlinear. SGD/minibatch is standard.',
        marks=2, diff='M'))
    o.append(nat(
        'MLP',
        'Linear unit y=w x with w=0.5, x=4, target t=3, loss (1/2)(y-t)^2. dLoss/dw equals (y-t)*x = ____.',
        '-4',
        'y=2, (2-3)*4=-4.',
        marks=2, diff='M'))
    o.append(nat(
        'MLP',
        'One SGD step on that unit: w=0.5, grad=-4, eta=0.1. Updated w is ____.',
        '0.9',
        'w := 0.5 - 0.1*(-4)=0.9.',
        marks=2, diff='M'))
    o.append(mcq(
        'MLP',
        'Vanishing gradients in a deep sigmoid MLP occur because',
        'sigmoid derivative <= 0.25, so a long product of derivatives shrinks',
        'ReLU derivative is always 0',
        'SGD cannot use minibatches',
        'the output must be one-hot',
        'A',
        'Chain of factors each at most 1/4.',
        marks=2, diff='M'))
    o.append(nat(
        'MLP',
        'Softmax on logits (0,0,0) for 3 classes. Probability of class 1 is ____.',
        '1/3',
        'Equal logits => uniform 1/3.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLP',
        'A 2-2-1 MLP with linear hidden and linear output (no nonlinearities) is',
        'still universal',
        'equivalent to a single linear layer, hence cannot represent XOR',
        'a decision tree',
        'k-means',
        'B',
        'Composition of linear maps is linear.',
        marks=2, diff='M'))
    o.append(nat(
        'MLP',
        'Hidden layer of 3 sigmoids, input dim 4, including hidden biases, no output yet. Hidden-layer parameter count is ____.',
        '15',
        '4*3 weights + 3 biases = 15.',
        marks=1, diff='M'))
    o.append(mcq(
        'MLP',
        'Cross-entropy + softmax at the output of an MLP is preferred over SSE for classification because',
        'it matches the multinomial likelihood and avoids saturation issues of SSE+sigmoid',
        'it forces linear hidden units',
        'it maximises Gini',
        'it is the k-means objective',
        'A',
        'Standard classification loss.',
        marks=1, diff='M'))
    o.append(nat(
        'MLP',
        'Forward: z=w x+b with w=2, b=-1, x=1, activation tanh. Argument z equals ____.',
        '1',
        '2*1-1=1.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLP',
        'Weight decay in MLP training is essentially',
        'an L2 penalty on weights, akin to ridge',
        'k-medoid swapping',
        'PCA whitening of labels',
        'dropout of the loss',
        'A',
        'L2 regularisation on W.',
        marks=1, diff='E'))
    o.append(nat(
        'MLP',
        'A minibatch of 8, dataset of 80, one epoch. Number of SGD steps per epoch is ____.',
        '10',
        '80/8=10.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLP',
        'If every hidden unit uses identity activation, stacking layers without residual tricks',
        'does not increase representational power beyond one linear layer',
        'always solves XOR',
        'computes a decision tree',
        'forces Gini splits',
        'A',
        'Linear o linear = linear.',
        marks=1, diff='M'))
    o.append(nat(
        'MLP',
        'Output sigmoid 0.5, binary target 1, log-loss -log p. Using log base e, -log 0.5 = log 2 ~ 0.693. Rounded to 2 decimals: ____.',
        '0.69',
        'ln 2 ~ 0.693 ~ 0.69.',
        marks=1, diff='M'))
    o.append(mcq(
        'MLP',
        'Backprop through a ReLU unit with pre-activation z<0 sends',
        'zero gradient to its inputs',
        'gradient 1 always',
        'gradient -1',
        'undefined NaN always',
        'A',
        "ReLU'(z)=0 for z<0.",
        marks=1, diff='E'))
    o.append(mcq(
        'KMeans',
        'k-means with Euclidean distance updates each centroid to',
        'the coordinate-wise mean of its assigned points',
        'a randomly chosen training label',
        'the median of all features globally',
        'the first principal component',
        'A',
        'The mean minimises within-cluster SSE.',
        marks=1, diff='E'))
    o.append(nat(
        'KMeans',
        'Points 1,2,3,10 on a line, k=2, initial centroids 1 and 10. After the first assignment, the left cluster size is ____.',
        '3',
        '1,2,3 nearer to 1 than to 10.',
        marks=1, diff='M'))
    o.append(nat(
        'KMeans',
        'After that assignment {1,2,3} and {10}, the new left centroid is ____.',
        '2',
        'Mean of 1,2,3 is 2.',
        marks=1, diff='E'))
    o.append(mcq(
        'KMeans',
        'Four shops A(0,0), B(0,6), C(8,0), D(8,6). If A and D are forced into the SAME Euclidean 2-means cluster at a fixed point of k-means, then',
        'B and C may freely sit in the other cluster, because k-means cells need not be convex',
        "the cluster is a Voronoi cell of its centroid, hence convex, so the rectangle's interior is constrained; in particular B or C cannot form a separated pair skipping the diagonal without splitting A-D",
        'k-means ignores coordinates',
        'the objective becomes Gini',
        'B',
        'Euclidean k-means cells are Voronoi, hence convex.',
        marks=2, diff='H'))
    o.append(mcq(
        'KMeans',
        'Points on a line P=1, Q=2, R=3, S=10. If P and S lie in the same k-means cluster (k=2) after convergence, which MUST be true?',
        'Q and R lie in that same cluster, because clusters are intervals (convex) on the line',
        'Q must be a singleton',
        'R must be a medoid',
        'k-means is undefined on a line',
        'A',
        'Convex Voronoi cells on a line are intervals, so everything between P and S joins them.',
        marks=2, diff='H'))
    o.append(nat(
        'KMeans',
        "Seeds for k-means on W(1,1), X(1,2), Y(5,1), Z(5,2) are W and Z. After the first assignment, number of points assigned to Z's cluster is ____.",
        '2',
        'Y and Z nearer to Z; W,X nearer to W.',
        marks=2, diff='M'))
    o.append(msq(
        'KMeans',
        'Which are TRUE of k-means?',
        'The SSE objective is nonincreasing at each assign/update step',
        'The algorithm can converge to a local minimum depending on initialisation',
        'Empty clusters can occur for bad seeds',
        'The global SSE minimum is always found in one iteration',
        'A;B;C',
        'k-means is locally convergent, not globally optimal.',
        marks=2, diff='M'))
    o.append(nat(
        'KMeans',
        'Cluster { (0,0),(0,2),(2,0),(2,2) }. Euclidean centroid is (a,a) with a= ____.',
        '1',
        'Mean x=1, mean y=1.',
        marks=1, diff='E'))
    o.append(mcq(
        'KMeans',
        'k-means vs k-medoid: a centroid in k-means',
        'must be an actual data point',
        'need not be a data point (it is a mean)',
        'is always a support vector',
        'minimises Gini',
        'B',
        'Means generally lie off the data cloud.',
        marks=1, diff='E'))
    o.append(nat(
        'KMeans',
        '1-D points 0,0,0,10, k=1. The k-means centroid (the mean) is ____.',
        '2.5',
        '(0+0+0+10)/4=2.5.',
        marks=1, diff='E'))
    o.append(mcq(
        'KMeans',
        'After assignment, a point x is in cluster j at a Euclidean k-means fixed point only if',
        '||x-mu_j|| <= ||x-mu_i|| for every i (Voronoi / nearest centroid)',
        'x is a medoid',
        'x has label j in a supervised file',
        '||x|| is maximal',
        'A',
        'Assignment step is nearest-centroid.',
        marks=1, diff='M'))
    o.append(nat(
        'KMeans',
        'Two clusters with SSE 4 and 5. Total k-means objective is ____.',
        '9',
        'Sum of SSEs.',
        marks=1, diff='E'))
    o.append(mcq(
        'KMeans',
        'Increasing k from 1 to n (one cluster per point) makes the k-means objective',
        'increase',
        'drop to 0',
        'become the Gini of y',
        'undefined',
        'B',
        'Singletons have SSE 0.',
        marks=1, diff='E'))
    o.append(mcq(
        'KMeans',
        'k-means is sensitive to feature scaling because',
        'SSE uses Euclidean geometry',
        'it maximises Gini',
        'it is a kernel SVM',
        'labels must be scaled',
        'A',
        'Distances change under rescaling.',
        marks=1, diff='E'))
    o.append(mcq(
        'KMedoid',
        'A medoid of a cluster is',
        'any mean vector, possibly off the data',
        'an actual data point that minimises total distance to other members',
        'the first principal component',
        'a support vector of an SVM',
        'B',
        'Medoid is a prototype from the dataset.',
        marks=1, diff='E'))
    o.append(mcq(
        'KMedoid',
        'k-medoid (PAM) is often preferred to k-means when',
        'one needs robustness to outliers and a prototype that is a real observation',
        'one needs a differentiable mean for SGD',
        'labels are continuous',
        'PCA must be avoided',
        'A',
        'Medoids are robust and interpretable as actual points.',
        marks=1, diff='M'))
    o.append(nat(
        'KMedoid',
        '1-D points 0,1,100. The 1-medoid (min total L1 distance) is the median point, i.e. ____.',
        '1',
        'Median of 0,1,100 is 1; L1 total 1+0+99=100, better than 0 (101) or 100 (199).',
        marks=2, diff='M'))
    o.append(msq(
        'KMedoid',
        'Which are TRUE?',
        'k-medoid cluster centres are members of the dataset',
        'k-means centres need not be members of the dataset',
        'A single swap step in PAM evaluates replacing a medoid by a non-medoid',
        'k-medoid requires class labels',
        'A;B;C',
        'Both are unsupervised; PAM uses swap.',
        marks=2, diff='M'))
    o.append(nat(
        'KMedoid',
        'Points A,B,C with pairwise distances AB=2, AC=3, BC=4. The 1-medoid (min total distance to the others) is the point with smallest sum, namely A with sum ____.',
        '5',
        'A: 2+3=5; B: 2+4=6; C: 3+4=7.',
        marks=2, diff='M'))
    o.append(mcq(
        'KMedoid',
        'Manhattan k-medoid on four named cities uses pairwise L1 distances. Unlike k-means,',
        'updates are restricted to swapping among the observed city locations',
        'centroids can sit at the L1 mean off the cities always as medoids',
        'labels are required',
        'PCA axes must be orthogonal first',
        'A',
        'Medoids remain data points (cities).',
        marks=1, diff='M'))
    o.append(mcq(
        'HAC',
        'Agglomerative (bottom-up) clustering starts with',
        'one cluster containing every point',
        'each point in its own cluster, then merges',
        'a random SVM',
        'PCA scores of labels',
        'B',
        'Bottom-up: n singletons, n-1 merges.',
        marks=1, diff='E'))
    o.append(mcq(
        'HAC',
        'Divisive (top-down) clustering starts with',
        'n singletons',
        'one cluster of all points, then recursively splits',
        'k random medoids only',
        'a logistic boundary',
        'B',
        'Top-down is divisive.',
        marks=1, diff='E'))
    o.append(mcq(
        'HAC',
        'Single linkage uses, as the distance between clusters A and B,',
        'the maximum pairwise distance between a point of A and a point of B',
        'the minimum pairwise distance between a point of A and a point of B',
        'the distance between centroids only, never points',
        'Gini impurity',
        'B',
        'Single = min, complete = max.',
        marks=1, diff='E'))
    o.append(mcq(
        'HAC',
        'Complete linkage uses',
        'min pairwise distance',
        'max pairwise distance',
        'mean of labels',
        'hinge loss',
        'B',
        'Complete = max.',
        marks=1, diff='E'))
    o.append(nat(
        'HAC',
        'HAC on Oak(0,0), Pine(1,0), Elm(0,2), Teak(4,0) with Manhattan distance. The first single-linkage merge height is ____.',
        '1',
        'Closest pair Oak-Pine at L1=1.',
        marks=2, diff='M'))
    o.append(mcq(
        'HAC',
        'After merging Oak+Pine in that Manhattan single-linkage run, the next merge (into the dendrogram) joins',
        'the Oak-Pine cluster with Elm, at height min(2,3)=2',
        'Teak with Elm at 6',
        'all four at once',
        'Teak with Oak-Pine at 1',
        'A',
        'd(OP,Elm)=min(Oak-Elm,Pine-Elm)=min(2,3)=2 < d(OP,Teak)=min(4,3)=3.',
        marks=2, diff='H'))
    o.append(nat(
        'HAC',
        'Same four trees, complete linkage Manhattan. After Oak-Pine merge at 1, the complete-linkage distance of {Oak,Pine} to Elm is max(2,3)= ____.',
        '3',
        'Complete uses max pairwise.',
        marks=2, diff='M'))
    o.append(nat(
        'HAC',
        'Cities Pune(0,0), Nashik(0,4), Kolhapur(6,0), Solapur(6,5). Manhattan single-linkage first merge height is ____.',
        '4',
        'Pune-Nashik L1=4 is the unique minimum (Kolhapur-Solapur is 5).',
        marks=2, diff='M'))
    o.append(mcq(
        'HAC',
        'On those four cities, Manhattan complete linkage first merge is still Pune-Nashik at 4. Next complete-linkage distance of {Pune,Nashik} to Solapur is max(11,7)= ____ wait as MCQ: the pair merged second under single linkage is',
        'Kolhapur with Solapur at 5',
        'Pune with Solapur at 11',
        'all remaining at 0',
        'Nashik with Kolhapur at 4',
        'A',
        'After PN, single-linkage next smallest unused is Kolhapur-Solapur=5.',
        marks=2, diff='H'))
    o.append(nat(
        'HAC',
        'Points Anu(0,0), Bala(2,0), Chetan(0,1), Diya(5,0), Manhattan. Single-linkage first merge height (Anu-Chetan) is ____.',
        '1',
        'Anu-Chetan L1=1 is smallest.',
        marks=1, diff='M'))
    o.append(mcq(
        'HAC',
        'Anu, Bala, Chetan, Diya as above. After merging Anu-Chetan, single-linkage next joins',
        'that cluster with Bala at min(AB,CB)=min(2,3)=2',
        'Diya with Bala at 3 as the first merge',
        'all four at height 1',
        'Chetan with Diya at 1',
        'A',
        'Next min is Anu-Bala=2.',
        marks=2, diff='H'))
    o.append(nat(
        'HAC',
        'Same four people, complete linkage. After Anu-Chetan at 1, complete distance of {Anu,Chetan} to Bala is max(2,3)= ____.',
        '3',
        'Complete = max.',
        marks=1, diff='M'))
    o.append(msq(
        'HAC',
        'Which are TRUE of hierarchical agglomerative clustering?',
        'Single linkage can produce chaining (elongated clusters)',
        'Complete linkage prefers compact clusters',
        'The dendrogram of n points has n-1 merge levels',
        'HAC requires a pre-specified k at the start, unlike k-means',
        'A;B;C',
        'k is chosen by cutting the dendrogram later; it is not needed to start agglomerative HAC.',
        marks=2, diff='M'))
    o.append(mcq(
        'HAC',
        'Cutting a dendrogram at a height that yields 3 clusters is a way to',
        'choose k=3 after seeing the hierarchy',
        'train an SVM',
        'compute R^2',
        'estimate S_W',
        'A',
        'Post-hoc cut of HAC.',
        marks=1, diff='E'))
    o.append(nat(
        'HAC',
        'n=6 points, agglomerative clustering. Number of merge operations until one cluster is ____.',
        '5',
        'n-1 merges.',
        marks=1, diff='E'))
    o.append(mcq(
        'HAC',
        'Average linkage defines cluster distance as',
        'the average of all cross-pair distances',
        'the min cross-pair distance',
        'the max cross-pair distance',
        'Gini of labels',
        'A',
        'UPGMA-style average.',
        marks=1, diff='M'))
    o.append(mcq(
        'HAC',
        'Single-linkage HAC on a chain of points equally spaced on a line will',
        'merge neighbours sequentially, producing a chain',
        'always produce balanced complete blobs',
        'equal k-means with k=2 after one merge',
        'require labels',
        'A',
        'Classic chaining behaviour.',
        marks=1, diff='M'))
    o.append(mcq(
        'PCA',
        'Principal components of a centered data matrix are',
        'orthogonal directions of successive maximal variance (eigenvectors of the covariance)',
        'the class-mean differences of LDA',
        'support vectors',
        'Gini-maximising splits',
        'A',
        'PCA = eigendecomposition of covariance (or SVD of the centered data).',
        marks=1, diff='E'))
    o.append(msq(
        'PCA',
        'Which are TRUE of PCA?',
        'The principal axes are pairwise orthogonal',
        'The first PC maximises projected variance among unit vectors',
        'PCA uses class labels',
        'The scores on distinct PCs are uncorrelated (for the empirical covariance)',
        'A;B;D',
        'PCA is unsupervised; it ignores labels.',
        marks=2, diff='M'))
    o.append(nat(
        'PCA',
        'A 2-D centered cloud has covariance diag(4,1). Variance explained by PC1 is ____.',
        '4',
        'Largest eigenvalue 4.',
        marks=1, diff='E'))
    o.append(nat(
        'PCA',
        'Same covariance diag(4,1). Fraction of variance on PC1 is ____.',
        '0.8',
        '4/(4+1)=0.8.',
        marks=1, diff='E'))
    o.append(mcq(
        'PCA',
        'Failing to center the data before PCA',
        'can make the leading component point toward the mean rather than a direction of spread',
        'is required for orthogonality',
        'turns PCA into SVM',
        'zeros all eigenvalues',
        'A',
        'Uncentered Gram is dominated by the mean vector.',
        marks=2, diff='M'))
    o.append(nat(
        'PCA',
        'Centered points (-1,0),(1,0),(0,0). Empirical (1/n) covariance has (1,1) entry ____.',
        '2/3',
        '((-1)^2+1+0)/3=2/3.',
        marks=2, diff='M'))
    o.append(mcq(
        'PCA',
        'If two features are exactly linearly dependent, the covariance has',
        'a zero eigenvalue (rank-deficient)',
        'all eigenvalues equal',
        'negative variance',
        'no eigenvectors',
        'A',
        'Rank at most 1 in that plane.',
        marks=1, diff='M'))
    o.append(nat(
        'PCA',
        'Eigenvalues 5, 3, 2, 0. Number of PCs needed to capture ALL variance is ____.',
        '3',
        'The zero eigenvalue carries no variance; three PCs suffice.',
        marks=1, diff='M'))
    o.append(mcq(
        'PCA',
        'Projecting onto the first k PCs gives the best rank-k linear reconstruction in',
        'Frobenius / total squared error for centered data',
        'hinge loss',
        'Gini',
        '0-1 loss',
        'A',
        'Eckart-Young / PCA optimality.',
        marks=2, diff='M'))
    o.append(nat(
        'PCA',
        '2-D points (1,1),(1,1),(1,1) already equal. After centering, all PCA eigenvalues are ____.',
        '0',
        'No variance left.',
        marks=1, diff='E'))
    o.append(mcq(
        'PCA',
        'LDA vs PCA: LDA maximises the between/within ratio using labels; PCA maximises',
        'total variance without labels',
        'Gini',
        'the SVM margin',
        'k-means SSE',
        'A',
        'Unsupervised vs supervised linear projection.',
        marks=1, diff='E'))
    o.append(nat(
        'PCA',
        'Covariance [[2,0],[0,2]]. Any unit vector is a PC direction of eigenvalue ____.',
        '2',
        'Isotropic: every direction variance 2.',
        marks=1, diff='M'))
    o.append(mcq(
        'PCA',
        'Whitening / sphering using PCA rescales along PCs so that',
        'the empirical covariance becomes I (on the span of nonzero eigenvalues)',
        'labels become balanced',
        'k-means SSE is maximised',
        'the intercept of OLS vanishes',
        'A',
        'Divide by sqrt(eigenvalue).',
        marks=1, diff='M'))
    o.append(nat(
        'PCA',
        'Scores on PC1 of three centered points sum to ____.',
        '0',
        'PC scores of centered data have mean 0.',
        marks=1, diff='E'))
    o.append(msq(
        'PCA',
        'Which preprocessing steps are the usual prelude to PCA on heterogeneous features?',
        'Center each feature',
        'Optionally scale to unit variance (standardise) so scale does not dominate',
        'Replace features by their labels',
        'Drop orthogonality of PCs on purpose',
        'A;B',
        'Center always; standardise when units differ.',
        marks=2, diff='M'))
    o.append(mcq(
        'PCA',
        'The loading vector of PC2 is orthogonal to PC1 because',
        'covariance (or Gram) eigenvectors for distinct eigenvalues can be chosen orthonormal, and PCA enforces that',
        'labels force orthogonality',
        'k-means does',
        'Gini is orthogonal',
        'A',
        'Symmetric eigenproblem.',
        marks=1, diff='E'))
    o.append(nat(
        'PCA',
        'Variance on PC1 is 9, on PC2 is 1. Cumulative fraction after 1 PC is ____.',
        '0.9',
        '9/10=0.9.',
        marks=1, diff='E'))
    o.append(mcq(
        'PCA',
        'A student runs PCA on 100 features with n=20 without regularisation. The covariance estimate is',
        'at most rank 19 (centered), so at least 81 eigenvalues are 0',
        'full rank 100 always',
        'equal to S_W of LDA',
        'a kernel of SVM',
        'A',
        'Centered n=20 => rank <=19.',
        marks=2, diff='H'))
    o.append(mcq(
        'MLMatch',
        'Task: separate two linearly separable classes with a maximum-margin hyperplane. Algorithm:',
        'hard-margin SVM',
        'k-means with k=2',
        'PCA to 1-D then threshold at random',
        'single-linkage HAC',
        'A',
        "That's the SVM primal.",
        marks=1, diff='E'))
    o.append(mcq(
        'MLMatch',
        'Task: compress unlabeled 50-D sensor readings to 3 orthogonal directions of maximal variance.',
        'PCA',
        'logistic regression',
        'LDA with 3 classes only',
        'decision tree Gini',
        'A',
        'PCA is the unlabeled variance maximiser.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLMatch',
        'Task: classify email using word presence under a class-conditional independence model.',
        'naive Bayes',
        'ridge OLS',
        'k-medoid',
        'PCA',
        'A',
        'Bernoulli/multinomial NB.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLMatch',
        'Task: shrink OLS coefficients to handle multicollinearity without forcing zeros.',
        'ridge',
        '1-NN',
        'single-linkage',
        'hard-margin SVM',
        'A',
        'L2 shrinkage.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLMatch',
        'Task: produce a binary tree of axis-aligned splits on a tiny colour/label table.',
        'decision tree',
        'MLP with linear hidden units only',
        'k-means',
        'PCA',
        'A',
        'CART-style tree.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLMatch',
        'Task: assign shop locations to k groups by iteratively averaging coordinates.',
        'k-means',
        'logistic regression',
        'A* search',
        'resolution theorem proving',
        'A',
        'k-means centroids.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLMatch',
        'Task: two-class labelled Gaussians with a shared full covariance. Natural linear classifier:',
        'LDA (Fisher)',
        'k-NN with k=n',
        'HAC single linkage',
        'unregularised interpolating tree',
        'A',
        'LDA is the model.',
        marks=1, diff='E'))
    o.append(mcq(
        'MLMatch',
        'Task: probability of default from a linear score squeezed to (0,1).',
        'logistic regression',
        'PCA',
        'k-medoid',
        'complete-linkage HAC',
        'A',
        'Sigmoid score.',
        marks=1, diff='E'))
    return uniq(o)
