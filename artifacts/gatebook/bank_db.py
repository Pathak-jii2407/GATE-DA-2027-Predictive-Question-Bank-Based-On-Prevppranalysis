"""GATE DA bank: Database Management and Warehousing."""
from __future__ import annotations

from itertools import combinations
from helpers import mcq, msq, nat, uniq
import math
import sqlite3
import statistics


def _sql(setup, query):
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    for s in setup:
        cur.execute(s)
    cur.execute(query)
    rows = cur.fetchall()
    con.close()
    return rows


def _sql_ok(setup, stmt):
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("PRAGMA foreign_keys = ON")
    try:
        for s in setup:
            cur.execute(s)
        cur.execute(stmt)
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        con.close()
        return False


def _closure(attrs, fds):
    c = set(attrs)
    changed = True
    while changed:
        changed = False
        for L, R in fds:
            if set(L) <= c and not set(R) <= c:
                c |= set(R)
                changed = True
    return c


def _cands(universe, fds):
    u = list(universe)
    keys = []
    for k in range(1, len(u) + 1):
        for comb in combinations(u, k):
            if _closure(comb, fds) >= set(u):
                s = set(comb)
                if not any(prev < s for prev in keys):
                    keys.append(s)
    keys = [k for k in keys if not any(other < k for other in keys if other is not k)]
    return keys


def _is_super(x, keys):
    xs = set(x)
    return any(k <= xs for k in keys)


def _prime_attrs(keys):
    p = set()
    for k in keys:
        p |= k
    return p


def _highest_nf(universe, fds):
    keys = _cands(universe, fds)
    primes = _prime_attrs(keys)
    bcnf = True
    nf3 = True
    nf2 = True
    # split fds to single attrs
    atom = []
    for L, R in fds:
        for a in R:
            atom.append((set(L), a))
    for L, a in atom:
        if a in L:
            continue
        if not _is_super(L, keys):
            bcnf = False
            if a not in primes:
                nf3 = False
        # 2NF: no partial dependency of nonprime on a proper subset of a cand key
        if a not in primes:
            for k in keys:
                if L < k:
                    nf2 = False
    if bcnf:
        return "BCNF"
    if nf3:
        return "3NF"
    if nf2:
        return "2NF"
    return "1NF"


def _er():
    o = []
    T = "ER model"

    o.append(
        mcq(
            T,
            "An ER diagram for Clinic has entity Patient (key pid) and entity Doctor (key did) linked by Treats with attributes date and fee. Treats is M:N. The minimum number of tables needed in a standard relational mapping (no extra attributes on entities besides keys/names) is",
            "3",
            "2",
            "1",
            "4",
            "A",
            "M:N relationship becomes its own table with the two keys plus relationship attributes.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "In an ER model of Library, Copy is a weak entity identified by (isbn, copyno) relative to Book. The identifying relationship HasCopy is",
            "1:N from Book to Copy, with total participation of Copy",
            "M:N between Book and Copy",
            "1:1 with partial participation of Copy",
            "an ordinary strong relationship that can drop copyno",
            "A",
            "A weak entity is identified by a 1:N identifying relationship and depends totally on the owner.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "Which statements about ER constructs are correct?",
            "A weak entity has no complete key of its own",
            "Total participation of A in R means every entity of A appears in R",
            "An M:N relationship can always be mapped without creating a new relation",
            "A composite attribute is typically flattened into component columns",
            "A;B;D",
            "M:N mapping needs a relationship table.",
            marks=2,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "University ER: Student (sid) ---(enrolls)--- Course (cid), enrolls is M:N with grade. Department (dno) has 1:N WorksIn into Instructor. Mapping to relations yields how many relations if every entity becomes a table and every M:N becomes a table (1:N is absorbed as a FK)?",
            "4",
            "3",
            "5",
            "2",
            "A",
            "Student, Course, Enrolls, Instructor (with dno FK). Department is a fifth entity - wait: Student, Course, Department, Instructor, Enrolls = 5. Stem listed Department and Instructor. 5 tables. Fix.",
            marks=1,
            diff="M",
        )
    )
    o[-1] = mcq(
        T,
        "University ER: entity sets Student, Course, Department, Instructor. Relationships: Enrolls(Student,Course) M:N with grade; WorksIn(Instructor,Department) N:1. Standard mapping (entity table each; M:N table; 1:N as FK) produces how many relations?",
        "4",
        "5",
        "6",
        "3",
        "B",
        "Four entity tables plus Enrolls. WorksIn is absorbed as a department FK on Instructor.",
        marks=1,
        diff="M",
    )
    o.append(
        mcq(
            T,
            "In the ER diagram of Harbour, Berth participates totally in Occupies with Ship, cardinality 1:1. After mapping, the key of Ship may be placed as a FK in Berth. This FK is",
            "NOT NULL and UNIQUE",
            "NULL-able and non-unique",
            "a set-valued attribute",
            "unnecessary because 1:1 needs no FK",
            "A",
            "Total 1:1 participation of Berth forces a unique non-null FK to Ship.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        nat(
            T,
            "A ternary relationship Supplies(Supplier, Part, Project) is M:N:P. In the standard mapping, the relationship table has how many foreign keys (one per entity key, assuming simple keys)?",
            3,
            "Each participating entity contributes its key as an FK, and the three together form the relationship key.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "ISA hierarchy: Employee is the superclass; Engineer and Manager are disjoint subclasses, total specialisation. A mapping that uses one table per subclass plus one for Employee (with shared ssn) is the",
            "8A / superclass-and-subclass method",
            "single-table-with-nulls method only",
            "relationship-table method for M:N",
            "unnormalised blob method",
            "A",
            "The standard options are one-table, two-table (subclasses only), or superclass plus subclass tables.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "An ER diagram for Festival has entity Performer and entity Stage linked by PlaysOn (M:N) and a recursive relationship Mentors on Performer (1:N). Which mappings are required?",
            "a table Performer",
            "a table Stage",
            "a table PlaysOn with two FKs",
            "Mentors absorbed as a nullable mentor_id FK on Performer",
            "A;B;C;D",
            "Recursive 1:N becomes a self-FK; M:N becomes a table.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Attribute age derived from dob on entity Citizen should, in a normalised relational schema, usually be",
            "not stored, or stored only as a view/computed column",
            "part of the primary key",
            "a foreign key to Date",
            "a multivalued attribute table",
            "A",
            "Derived attributes are computed, not independently stored, to avoid update anomalies.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Entity Product has a multivalued attribute color (a product may have 3 colours) and a composite attribute size(length,width). Standard mapping: Product table plus a table ProductColor. How many relations result from this fragment?",
            2,
            "Composite size flattens into columns of Product; colors need a separate table.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Partial participation of Employee in Manages (1:1 with Department on the other side, Department total) means",
            "some employees are not managers; every department has a manager",
            "every employee manages a department",
            "some departments have no manager",
            "Manages is M:N",
            "A",
            "Partial on Employee, total on Department: manager_id is a unique NOT NULL FK on Department.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "A identifying relationship for weak entity InvoiceLine of Invoice is drawn with a double diamond / double rectangle in many texts. The primary key of InvoiceLine is",
            "invoice_id plus a discriminator line_no",
            "line_no alone",
            "invoice_id alone",
            "a surrogate that ignores Invoice",
            "A",
            "Weak-entity keys are owner key plus partial key.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            T,
            "Which ER features require an extra relation in the standard mapping (beyond one table per strong entity)?",
            "M:N relationship",
            "multivalued attribute",
            "1:N relationship (FK can be placed on the N side)",
            "composite attribute (components become columns)",
            "A;B",
            "1:N and composite attributes do not by themselves add a table.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "Garage ER: Car, Owner, Mechanic, Job. Relationships Owns(Owner,Car) 1:N, WorksOn(Mechanic,Job) M:N, ForCar(Job,Car) N:1. Number of relations after standard mapping (entity tables + M:N table, 1:N as FKs) is",
            5,
            "Four entity tables plus WorksOn. Owns and ForCar become FKs.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Aggregation in ER (a relationship treated as an entity so it can participate in another relationship) is used when, for example,",
            "a WorksOn(Employee,Project) relationship is itself related to a Supplier via Sponsors",
            "two entities have a 1:1 relationship",
            "an attribute is derived",
            "a key is composite",
            "A",
            "Aggregation is the ER device for relationships on relationships.",
            marks=1,
            diff="M",
        )
    )
    return o


def _rel_fd():
    o = []
    T = "Relational model and FDs"

    schemas = [
        (
            "Voyage",
            "ABCDE",
            [(["A"], ["B", "C"]), (["C", "D"], ["E"]), (["E"], ["A"])],
            "schema Voyage(A,B,C,D,E) with FDs A->BC, CD->E, E->A",
        ),
        (
            "Roster",
            "ABCD",
            [(["A", "B"], ["C"]), (["C"], ["D"]), (["D"], ["A"])],
            "schema Roster(A,B,C,D) with FDs AB->C, C->D, D->A",
        ),
        (
            "ClinicVisit",
            "ABCDE",
            [(["A"], ["B"]), (["B"], ["C"]), (["C", "D"], ["E"]), (["E"], ["A"])],
            "schema ClinicVisit(A,B,C,D,E) with FDs A->B, B->C, CD->E, E->A",
        ),
        (
            "Invoice",
            "ABCD",
            [(["A"], ["B", "C"]), (["C"], ["D"])],
            "schema Invoice(A,B,C,D) with FDs A->BC, C->D",
        ),
        (
            "FlightLeg",
            "ABCDE",
            [(["A", "B"], ["C"]), (["C"], ["D"]), (["D"], ["E"]), (["E"], ["A"])],
            "schema FlightLeg(A,B,C,D,E) with FDs AB->C, C->D, D->E, E->A",
        ),
        (
            "LabSample",
            "ABCD",
            [(["A"], ["B"]), (["B"], ["C"]), (["C"], ["A"]), (["A", "D"], ["C"])],
            "schema LabSample(A,B,C,D) with FDs A->B, B->C, C->A, AD->C",
        ),
        (
            "HarbourBerth",
            "ABCDE",
            [(["A"], ["B", "C", "D", "E"])],
            "schema HarbourBerth(A,B,C,D,E) with FD A->BCDE",
        ),
        (
            "MatchCard",
            "ABCD",
            [(["A", "B"], ["C", "D"]), (["C"], ["A"])],
            "schema MatchCard(A,B,C,D) with FDs AB->CD, C->A",
        ),
        (
            "Payroll",
            "ABCDE",
            [(["A", "B"], ["C"]), (["C"], ["D", "E"]), (["E"], ["A"])],
            "schema Payroll(A,B,C,D,E) with FDs AB->C, C->DE, E->A",
        ),
        (
            "StoreSku",
            "ABCD",
            [(["A", "B"], ["C"]), (["A", "B"], ["D"]), (["C"], ["D"])],
            "schema StoreSku(A,B,C,D) with FDs AB->C, AB->D, C->D",
        ),
        (
            "Enroll",
            "ABC",
            [(["A", "B"], ["C"]), (["C"], ["A"])],
            "schema Enroll(A,B,C) with FDs AB->C, C->A",
        ),
        (
            "Sensor",
            "ABCDE",
            [(["A"], ["B"]), (["B", "C"], ["D"]), (["D"], ["E"]), (["E"], ["C"])],
            "schema Sensor(A,B,C,D,E) with FDs A->B, BC->D, D->E, E->C",
        ),
    ]

    for name, univ, fds, phrase in schemas:
        keys = _cands(univ, fds)
        key_str = ", ".join("".join(sorted(k)) for k in sorted(keys, key=lambda s: (len(s), "".join(sorted(s)))))
        nkeys = len(keys)
        o.append(
            nat(
                T,
                "Let " + phrase + ". The number of candidate keys is",
                nkeys,
                "Candidate keys are " + key_str + ".",
                marks=2,
                diff="H",
            )
        )
        nf = _highest_nf(univ, fds)
        others = [x for x in ["1NF", "2NF", "3NF", "BCNF"] if x != nf]
        # pad
        while len(others) < 3:
            others.append("4NF")
        o.append(
            mcq(
                T,
                "Let " + phrase + ". Assuming the schema is already in 1NF, the highest normal form it is guaranteed to be in is",
                nf,
                others[0],
                others[1],
                others[2],
                "A",
                "Candidate keys " + key_str + ". Highest NF is " + nf + ".",
                marks=2,
                diff="H",
            )
        )

    o.append(
        mcq(
            T,
            "Relation R(A,B,C) with FDs A->B and B->C. Which is a candidate key?",
            "A",
            "B",
            "C",
            "BC",
            "A",
            "A+ = ABC, so A is a key. B+ = BC misses A; C+ = C.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            T,
            "Relation Shop(A,B,C,D) with FDs A->B, B->C, C->D. Which statements are true?",
            "A is the unique candidate key",
            "the schema is in BCNF",
            "B->C is a 3NF violation (B is not a superkey and C is nonprime)",
            "a lossless BCNF decomposition can produce (A,B), (B,C), (C,D)",
            "A;C;D",
            "Nontrivial FDs B->C and C->D have left sides that are not superkeys, so not BCNF/3NF. The chain decomposition is lossless.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        nat(
            T,
            "Number of superkeys of R(A,B,C) with only FD A->BC (so A is the unique candidate key) is",
            4,
            "Superkeys are all supersets of {A}: A, AB, AC, ABC. Four of them.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Armstrong axioms. From X->Y and Y->Z we may infer X->Z. This is",
            "transitivity",
            "augmentation",
            "reflexivity",
            "union",
            "A",
            "Transitivity is the third Armstrong axiom.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "A decomposition of R into R1 and R2 is lossless-join iff",
            "R1 ∩ R2 -> R1 or R1 ∩ R2 -> R2 (the intersection is a key of one piece)",
            "R1 ∩ R2 is empty",
            "R1 ∪ R2 has more attributes than R",
            "both R1 and R2 are in BCNF",
            "A",
            "The standard test: common attributes form a superkey of at least one of the two schemas.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "Relation R(A,B,C) with FDs A->B and C->B. A decomposition into R1(A,B) and R2(C,B). Which hold?",
            "the join is lossless because? wait: intersection is {B} and B determines neither R1 nor R2, so lossy",
            "the decomposition is lossy",
            "dependency A->B is preserved in R1",
            "dependency C->B is preserved in R2",
            "B;C;D",
            "B is not a key of either side, so the join can invent spurious tuples. Each local FD lives in its piece.",
            marks=2,
            diff="H",
        )
    )
    o[-1] = msq(
        T,
        "Relation R(A,B,C) with FDs A->B and C->B is decomposed into R1(A,B) and R2(C,B). Which statements hold?",
        "the decomposition is lossy (R1 ∩ R2 = {B} is not a key of either)",
        "A->B is preserved in R1",
        "C->B is preserved in R2",
        "the decomposition is in BCNF and lossless",
        "A;B;C",
        "{B} determines neither AB nor CB. Each FD is local, but the join is lossy.",
        marks=2,
        diff="H",
    )
    o.append(
        nat(
            T,
            "How many FDs of the form X->Y with X,Y nonempty subsets of {A,B} hold in a relation whose only candidate key is AB (no nontrivial FD)? Count all X->Y that are implied by Armstrong reflexivity / trivial FDs only, with X,Y subsets of {A,B}, Y nonempty, X nonempty, Ysubseteq X. That number is",
            5,
            "Nonempty Ysubseteq X: (A->A), (B->B), (AB->A), (AB->B), (AB->AB). Five trivial FDs.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        mcq(
            T,
            "Relation Coach(A,B,C) with FDs AB->C and C->A. Candidate keys are",
            "AB and BC",
            "AB and C",
            "A and BC",
            "C only",
            "A",
            "AB+ = ABC. C+ = CA, needs B so BC+ = BCA. AB and BC are keys. C is not.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "The schema Coach(A,B,C) with AB->C and C->A is",
            "in 3NF but not in BCNF",
            "in BCNF",
            "not in 3NF",
            "not even in 1NF",
            "A",
            "C->A has left side not a superkey (C is not a key) but A is prime, so 3NF not BCNF.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        nat(
            T,
            "Attribute closure of CD under FDs A->B, CD->E, E->A on ABCDE. | (CD)+ | (number of attributes in the closure) is",
            5,
            "CD -> E -> A -> B, so CDEAB, all five.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "Which are candidate keys of R(A,B,C,D,E) with F={A->BC, CD->E, E->A}?",
            "AD",
            "ED",
            "CD",
            "BD",
            "A;B;C",
            "AD+ = AD+BC+E = ABCDE; ED+ similarly; CD+ = CDE+A+BC. BD+ = BD only.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        mcq(
            T,
            "A relation is in 2NF if it is in 1NF and",
            "no nonprime attribute is partially dependent on a candidate key",
            "every determinant is a candidate key",
            "it has no transitive dependency of a nonprime on a key",
            "it has a single-attribute key",
            "A",
            "2NF bans partial dependence of nonprimes. BCNF is 'every determinant is a superkey'. Transitive is 3NF.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "A relation is in BCNF if",
            "for every nontrivial FD X->Y, X is a superkey",
            "for every FD X->A, X is a superkey or A is prime",
            "it is in 3NF and has no overlapping candidate keys",
            "it is in 1NF and has no partial dependency",
            "A",
            "BCNF is the superkey-determinant condition. 3NF allows prime-right-hand sides.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "R(A,B,C,D) with FDs A->B, B->C, C->D. Size of A+ is",
            4,
            "A determines the whole chain ABCD.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Dependency preservation: a decomposition is dependency-preserving if",
            "the union of local FDs (projected) implies the original cover",
            "the join is lossless",
            "each piece is in BCNF",
            "there are no FDs",
            "A",
            "Lossless and dependency-preserving are independent goals; BCNF cannot always do both.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "If a decomposition is not dependency-preserving, which operator is needed more often to enforce FDs that span pieces?",
            "join",
            "selection",
            "projection",
            "union",
            "A",
            "Checking a cross-piece FD requires joining the pieces.",
            marks=1,
            diff="M",
        )
    )
    return o


def _ra_trc():
    o = []
    T = "Relational algebra and tuple calculus"

    o.append(
        mcq(
            T,
            "Relations Team(name) and Player(name, team). RA expression that returns team names that have at least one player is",
            "pi_name(Team) ∩ pi_team(Player)   [with rename so attributes match]",
            "Team - Player",
            "Player ÷ Team",
            "Team × Player",
            "A",
            "Intersect the team names with the projected Player.team column.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Relations Defender(name) and Forward(name) and Team(name). Which RA expression is empty exactly when every Team.name appears in Defender or Forward?",
            "pi_name(Team) - (pi_name(Defender) ∪ pi_name(Forward))",
            "Defender ∩ Forward ∩ Team",
            "Team × Defender",
            "(Defender ∪ Forward) - Team",
            "A",
            "The difference is the set of team names missing from both positions; it is empty iff coverage is complete.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        nat(
            T,
            "R has 5 tuples, S has 4 tuples, R and S are union-compatible and share 2 tuples. |R ∪ S| is",
            7,
            "5+4-2=7.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
        "R has 5 tuples, S has 4, they share 2. |R ∩ S| is",
            2,
            "Intersection size is the overlap.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "R has 5 tuples, S has 4, overlap 2. |R - S| is",
            3,
            "5-2=3.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "R(A,B) has 6 tuples, S(B,C) has 5 tuples. A foreign-key-like join: each R.B matches exactly one S.B and every S.B occurs at least once. |R ⋈ S| equals",
            6,
            "Many-to-one from R to S; join cardinality equals |R|.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Division: Completed(student, course) and Required(course) with Required = {DB,ML}. student who completed at least those courses is expressed by",
            "Completed ÷ Required",
            "Completed - Required",
            "Completed × Required",
            "pi_student(Completed)",
            "A",
            "Division is the RA operator for 'for all' / 'every required course'.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Tuple relational calculus: {t | t in Player ∧ t.team = 'Goa'}. This is equivalent to",
            "sigma_{team='Goa'}(Player)",
            "pi_team(Player)",
            "Player ÷ {Goa}",
            "Player × Team",
            "A",
            "The calculus formula is a selection.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            T,
            "Which RA expressions are equivalent to sigma_{A=1}(R ⋈ S) when A is an attribute of R only?",
            "(sigma_{A=1}(R)) ⋈ S",
            "R ⋈ (sigma_{A=1}(S))",
            "sigma_{A=1}(R) × S  (if the join is a natural join on other attributes, not in general)",
            "the selection can be pushed to the R side",
            "A;D",
            "Selection on an R-only attribute pushes to R. It cannot be applied to S.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "A tuple-calculus query {t | ∃p ∈ Player (t.name = p.name ∧ p.team = 'Pune')} is",
            "a projection of a selection of Player",
            "unsafe, because t is not bound to a relation",
            "the Cartesian product Player × Player",
            "a division",
            "A",
            "t is determined by p.name; it is the names of Pune players. (If t is a Player tuple it is a selection.)",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Unsafe TRC query example: {t | t.A = t.A} ranges over",
            "the infinite universe of all tuples, hence unsafe",
            "one empty tuple",
            "the active domain automatically",
            "a single attribute A of a stored relation",
            "A",
            "Safety requires every value of a result tuple to come from the active domain of the query.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "R has attributes (A,B), 4 tuples; S has (B,C), 3 tuples; natural join on B is a full Cartesian because all R.B equal all S.B (single shared B-value). |R ⋈ S| is",
            12,
            "4*3=12 when the join key is constant.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "pi_{A}(R) ∪ pi_{A}(S) versus pi_{A}(R ∪ S) when R and S are union-compatible. They are",
            "equal",
            "unequal in general",
            "equal only if A is a key",
            "equal only if R=S",
            "A",
            "Projection and union commute: both yield the set of A-values appearing in either.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "pi_{A}(R ∩ S) versus pi_{A}(R) ∩ pi_{A}(S). In general they are",
            "the left is a subset of the right; they may differ",
            "always equal",
            "the right is a subset of the left",
            "incomparable",
            "A",
            "An A-value may occur in R and in S with different B's, so it survives the projected intersection but not the intersection of the original tuples.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        msq(
            T,
            "Natural join R ⋈ S. Which are always true?",
            "if R and S have no common attributes, ⋈ is Cartesian product",
            "|R ⋈ S| <= |R| * |S|",
            "|R ⋈ S| >= |R| + |S| always",
            "natural join is commutative up to column order",
            "A;B;D",
            "Join size can be 0, which is not at least |R|+|S|.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "The RA rename operator ρ_{S(A,B)}(R) is needed so that",
            "union/intersection/difference can be applied after aligning attribute names",
            "selection can test constants",
            "projection can drop columns",
            "division can be rewritten as join",
            "A",
            "Set operators require identical schemas, hence rename.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Relation Match(home, away, goals) has 8 rows. pi_home(Match) has 5 distinct homes. The number of rows returned by pi_home(Match) is",
            5,
            "Projection is a set of distinct homes.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "TRC query of 'students who take every course in Dept=CS': {s | s ∈ Student ∧ ∀c (c ∈ Course ∧ c.dept='CS' => ∃e ∈ Enroll (e.sid=s.sid ∧ e.cid=c.cid))}. This is the calculus form of",
            "division of Enroll by the CS courses (after suitable projection)",
            "a simple selection on Student",
            "Student - Course",
            "an unsafe query with no active domain",
            "A",
            "Universal quantification over CS courses is division.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        mcq(
            T,
            "Left outer join R ⟕ S, |R|=4, |S|=3, inner join has 2 matching R-tuples (each matches one S). How many rows in the left outer join?",
            "4",
            "2",
            "7",
            "3",
            "A",
            "All 4 R-tuples appear: 2 matched plus 2 padded with nulls.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "Full outer join of those R and S (inner matches 2 pairs; 2 unmatched R; 1 unmatched S) has how many rows?",
            5,
            "2 matched + 2 left-only + 1 right-only = 5.",
            marks=1,
            diff="M",
        )
    )
    return o


def _sql_items():
    o = []
    T = "SQL"

    # --- Kabaddi-like sports table ---
    setup = [
        "CREATE TABLE Raider(id INT PRIMARY KEY, name TEXT, team TEXT, points INT)",
        "INSERT INTO Raider VALUES (1,'Ajay','Patna',12)",
        "INSERT INTO Raider VALUES (2,'Naveen','Patna',18)",
        "INSERT INTO Raider VALUES (3,'Pawan','Jaipur',12)",
        "INSERT INTO Raider VALUES (4,'Pardeep','Jaipur',20)",
        "INSERT INTO Raider VALUES (5,'Maninder','Delhi',18)",
        "INSERT INTO Raider VALUES (6,'Nitin','Delhi',9)",
    ]
    q = "SELECT team FROM Raider WHERE points > (SELECT AVG(points) FROM Raider)"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Relation Raider\n"
            "id name    team   points\n"
            "1  Ajay    Patna  12\n"
            "2  Naveen  Patna  18\n"
            "3  Pawan   Jaipur 12\n"
            "4  Pardeep Jaipur 20\n"
            "5  Maninder Delhi 18\n"
            "6  Nitin   Delhi  9\n"
            "Query: SELECT team FROM Raider WHERE points > (SELECT AVG(points) FROM Raider);\n"
            "The number of rows returned is",
            len(rows),
            "AVG is (12+18+12+20+18+9)/6=14.833..., so 18,20,18: three rows.",
            marks=2,
            diff="M",
        )
    )
    q = "SELECT team, COUNT(*) FROM Raider GROUP BY team HAVING COUNT(*)>=2"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On the same Raider table, SELECT team, COUNT(*) FROM Raider GROUP BY team HAVING COUNT(*)>=2 returns how many groups?",
            len(rows),
            "Each of Patna, Jaipur, Delhi has 2 raiders; three groups.",
            marks=1,
            diff="E",
        )
    )
    q = "SELECT DISTINCT points FROM Raider"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On Raider, SELECT DISTINCT points FROM Raider returns how many rows?",
            len(rows),
            "Distinct points: 12,18,20,9 -> 4.",
            marks=1,
            diff="E",
        )
    )

    # Loan-like
    setup = [
        "CREATE TABLE Loan(lno TEXT PRIMARY KEY, branch TEXT, amount INT)",
        "INSERT INTO Loan VALUES ('L11','Banjara',90000)",
        "INSERT INTO Loan VALUES ('L14','Kondapur',50000)",
        "INSERT INTO Loan VALUES ('L15','SRNagar',40000)",
        "INSERT INTO Loan VALUES ('L22','SRNagar',25000)",
        "INSERT INTO Loan VALUES ('L23','Balanagar',80000)",
        "INSERT INTO Loan VALUES ('L25','Kondapur',70000)",
        "INSERT INTO Loan VALUES ('L19','SRNagar',65000)",
    ]
    q = (
        "SELECT L1.lno FROM Loan L1 WHERE L1.amount > "
        "(SELECT MAX(L2.amount) FROM Loan L2 WHERE L2.branch='SRNagar')"
    )
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Relation Loan\n"
            "lno branch   amount\n"
            "L11 Banjara  90000\n"
            "L14 Kondapur 50000\n"
            "L15 SRNagar  40000\n"
            "L22 SRNagar  25000\n"
            "L23 Balanagar 80000\n"
            "L25 Kondapur 70000\n"
            "L19 SRNagar  65000\n"
            "SELECT L1.lno FROM Loan L1 WHERE L1.amount > (SELECT MAX(L2.amount) FROM Loan L2 WHERE L2.branch='SRNagar');\n"
            "Number of rows returned is",
            len(rows),
            "MAX of SRNagar is 65000; amounts > 65000 are 90000,80000,70000: three rows.",
            marks=2,
            diff="M",
        )
    )

    # Car
    setup = [
        "CREATE TABLE Car(serial INT PRIMARY KEY, model TEXT, year INT, color TEXT)",
        "CREATE TABLE Make(maker TEXT, model TEXT, PRIMARY KEY(maker,model))",
        "CREATE TABLE Own(owner TEXT, serial INT, PRIMARY KEY(owner,serial))",
        "INSERT INTO Car VALUES (10,'Swift',2019,'red')",
        "INSERT INTO Car VALUES (11,'Swift',2020,'blue')",
        "INSERT INTO Car VALUES (12,'City',2018,'red')",
        "INSERT INTO Car VALUES (13,'Nexon',2021,'red')",
        "INSERT INTO Make VALUES ('Maruti','Swift')",
        "INSERT INTO Make VALUES ('Honda','City')",
        "INSERT INTO Make VALUES ('Tata','Nexon')",
        "INSERT INTO Own VALUES ('Ravi',10)",
        "INSERT INTO Own VALUES ('Ravi',12)",
        "INSERT INTO Own VALUES ('Asha',11)",
        "INSERT INTO Own VALUES ('Asha',13)",
        "INSERT INTO Own VALUES ('Isha',13)",
    ]
    q = (
        "SELECT DISTINCT owner FROM Own JOIN Car ON Own.serial=Car.serial "
        "JOIN Make ON Car.model=Make.model WHERE color='red' AND maker='Tata'"
    )
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Car(serial,model,year,color): (10,Swift,2019,red), (11,Swift,2020,blue), (12,City,2018,red), (13,Nexon,2021,red).\n"
            "Make(maker,model): (Maruti,Swift), (Honda,City), (Tata,Nexon).\n"
            "Own(owner,serial): (Ravi,10), (Ravi,12), (Asha,11), (Asha,13), (Isha,13).\n"
            "SELECT DISTINCT owner FROM Own JOIN Car JOIN Make WHERE color='red' AND maker='Tata'.\n"
            "Number of rows is",
            len(rows),
            "Only serial 13 is a red Tata; owners Asha and Isha: 2 rows.",
            marks=2,
            diff="H",
        )
    )

    # NULL 3VL
    setup = [
        "CREATE TABLE Emp(id INT, dept TEXT, bonus INT)",
        "INSERT INTO Emp VALUES (1,'HR',100)",
        "INSERT INTO Emp VALUES (2,'HR',NULL)",
        "INSERT INTO Emp VALUES (3,'IT',200)",
        "INSERT INTO Emp VALUES (4,'IT',NULL)",
        "INSERT INTO Emp VALUES (5,NULL,50)",
    ]
    q = "SELECT id FROM Emp WHERE bonus > 100"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Emp(id,dept,bonus): (1,HR,100), (2,HR,NULL), (3,IT,200), (4,IT,NULL), (5,NULL,50).\n"
            "SELECT id FROM Emp WHERE bonus > 100 returns how many rows?",
            len(rows),
            "NULL > 100 is UNKNOWN, not TRUE. Only id 3 qualifies.",
            marks=1,
            diff="M",
        )
    )
    q = "SELECT id FROM Emp WHERE bonus > 100 OR bonus IS NULL"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On the same Emp table, SELECT id FROM Emp WHERE bonus > 100 OR bonus IS NULL returns how many rows?",
            len(rows),
            "id 3 (200) plus ids 2 and 4 (NULL): 3 rows.",
            marks=1,
            diff="M",
        )
    )
    q = "SELECT COUNT(*) FROM Emp"
    cstar = _sql(setup, q)[0][0]
    q = "SELECT COUNT(bonus) FROM Emp"
    cbon = _sql(setup, q)[0][0]
    q = "SELECT COUNT(dept) FROM Emp"
    cdep = _sql(setup, q)[0][0]
    o.append(
        mcq(
            T,
            "On Emp as above, (COUNT(*), COUNT(bonus), COUNT(dept)) is",
            f"{cstar}, {cbon}, {cdep}",
            "5, 5, 5",
            "5, 3, 5",
            "4, 3, 4",
            "A",
            "COUNT(*) counts rows (5). COUNT(col) skips NULLs: bonus has 2 NULLs so 3; dept has 1 NULL so 4.",
            marks=2,
            diff="M",
        )
    )
    q = "SELECT dept FROM Emp WHERE dept = NULL"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On Emp, SELECT dept FROM Emp WHERE dept = NULL returns how many rows?",
            len(rows),
            "In SQL, = NULL is UNKNOWN for every row; use IS NULL. Zero rows.",
            marks=1,
            diff="E",
        )
    )
    q = "SELECT id FROM Emp WHERE NOT (bonus > 100)"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On Emp, SELECT id FROM Emp WHERE NOT (bonus > 100) returns how many rows?",
            len(rows),
            "NOT UNKNOWN is UNKNOWN, so NULL bonuses drop. bonus>100 is true only for 3, false for 1 and 5. NOT false keeps 1 and 5: 2 rows.",
            marks=2,
            diff="H",
        )
    )

    # OUTER JOIN
    setup = [
        "CREATE TABLE Team(tid INT PRIMARY KEY, tname TEXT)",
        "CREATE TABLE Player(pid INT PRIMARY KEY, pname TEXT, tid INT)",
        "INSERT INTO Team VALUES (1,'Goa')",
        "INSERT INTO Team VALUES (2,'Pune')",
        "INSERT INTO Team VALUES (3,'Kochi')",
        "INSERT INTO Player VALUES (10,'Amit',1)",
        "INSERT INTO Player VALUES (11,'Bala',1)",
        "INSERT INTO Player VALUES (12,'Chet',2)",
    ]
    q = "SELECT tname FROM Team LEFT JOIN Player ON Team.tid=Player.tid WHERE Player.pid IS NULL"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Team: (1,Goa), (2,Pune), (3,Kochi). Player: (10,Amit,1), (11,Bala,1), (12,Chet,2).\n"
            "SELECT tname FROM Team LEFT JOIN Player ON Team.tid=Player.tid WHERE Player.pid IS NULL;\n"
            "Number of rows is",
            len(rows),
            "Kochi has no player: one row. This is the anti-join.",
            marks=2,
            diff="M",
        )
    )
    q = "SELECT Team.tid FROM Team LEFT JOIN Player ON Team.tid=Player.tid"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On the same Team/Player, SELECT Team.tid FROM Team LEFT JOIN Player ON Team.tid=Player.tid returns how many rows?",
            len(rows),
            "Goa matches 2 players, Pune 1, Kochi 1 padded: 4 rows.",
            marks=1,
            diff="M",
        )
    )

    # EXISTS
    setup = [
        "CREATE TABLE Course(cid INT, cname TEXT, dept TEXT)",
        "CREATE TABLE Enroll(sid INT, cid INT)",
        "INSERT INTO Course VALUES (1,'DB','CS')",
        "INSERT INTO Course VALUES (2,'ML','CS')",
        "INSERT INTO Course VALUES (3,'Opt','MA')",
        "INSERT INTO Enroll VALUES (8,1)",
        "INSERT INTO Enroll VALUES (8,2)",
        "INSERT INTO Enroll VALUES (9,1)",
        "INSERT INTO Enroll VALUES (9,3)",
        "INSERT INTO Enroll VALUES (7,3)",
    ]
    q = (
        "SELECT sid FROM Enroll E WHERE NOT EXISTS "
        "(SELECT * FROM Course C WHERE C.dept='CS' AND NOT EXISTS "
        "(SELECT * FROM Enroll E2 WHERE E2.sid=E.sid AND E2.cid=C.cid))"
    )
    # this returns sids that take every CS course, but possibly with duplicates from Enroll
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Course: (1,DB,CS), (2,ML,CS), (3,Opt,MA). Enroll(sid,cid): (8,1),(8,2),(9,1),(9,3),(7,3).\n"
            "SQL: sids from Enroll for which NOT EXISTS a CS course they did not take.\n"
            "Number of rows returned (Enroll-level, not DISTINCT) is",
            len(rows),
            "Only sid 8 takes both CS courses; sid 8 appears twice in Enroll, so 2 rows without DISTINCT.",
            marks=2,
            diff="H",
        )
    )

    # GROUP BY NULL
    setup = [
        "CREATE TABLE T(x INT, y INT)",
        "INSERT INTO T VALUES (1,10)",
        "INSERT INTO T VALUES (1,20)",
        "INSERT INTO T VALUES (NULL,30)",
        "INSERT INTO T VALUES (NULL,40)",
        "INSERT INTO T VALUES (2,50)",
    ]
    q = "SELECT x, COUNT(*) FROM T GROUP BY x"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "T(x,y): (1,10),(1,20),(NULL,30),(NULL,40),(2,50). SELECT x, COUNT(*) FROM T GROUP BY x returns how many groups?",
            len(rows),
            "NULLs form a single group. Groups: 1, NULL, 2 -> 3.",
            marks=1,
            diff="M",
        )
    )

    # more sports
    setup = [
        "CREATE TABLE Match(mid INT, home TEXT, away TEXT, goals INT)",
        "INSERT INTO Match VALUES (1,'Goa','Pune',3)",
        "INSERT INTO Match VALUES (2,'Goa','Kochi',1)",
        "INSERT INTO Match VALUES (3,'Pune','Kochi',2)",
        "INSERT INTO Match VALUES (4,'Pune','Goa',0)",
        "INSERT INTO Match VALUES (5,'Kochi','Goa',4)",
    ]
    q = "SELECT home FROM Match GROUP BY home HAVING SUM(goals) > 3"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Match(mid,home,away,goals): (1,Goa,Pune,3),(2,Goa,Kochi,1),(3,Pune,Kochi,2),(4,Pune,Goa,0),(5,Kochi,Goa,4).\n"
            "SELECT home FROM Match GROUP BY home HAVING SUM(goals)>3 returns how many rows?",
            len(rows),
            "Goa 3+1=4, Pune 2+0=2, Kochi 4. Two homes (Goa, Kochi).",
            marks=2,
            diff="M",
        )
    )
    q = "SELECT COUNT(*) FROM Match M WHERE goals = (SELECT MAX(goals) FROM Match)"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On Match, SELECT COUNT(*) FROM Match M WHERE goals >= ALL (SELECT goals FROM Match) returns",
            rows[0][0],
            ">= ALL is the maximum; only 4 (Kochi vs Goa). Equivalent: goals = MAX(goals).",
            marks=1,
            diff="M",
        )
    )

    # self join
    setup = [
        "CREATE TABLE Emp2(id INT, name TEXT, mgr INT)",
        "INSERT INTO Emp2 VALUES (1,'Amy',NULL)",
        "INSERT INTO Emp2 VALUES (2,'Ben',1)",
        "INSERT INTO Emp2 VALUES (3,'Cal',1)",
        "INSERT INTO Emp2 VALUES (4,'Dee',2)",
        "INSERT INTO Emp2 VALUES (5,'Eve',2)",
    ]
    q = "SELECT E.name FROM Emp2 E JOIN Emp2 M ON E.mgr=M.id WHERE M.name='Ben'"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Emp2(id,name,mgr): (1,Amy,NULL),(2,Ben,1),(3,Cal,1),(4,Dee,2),(5,Eve,2).\n"
            "SELECT E.name FROM Emp2 E JOIN Emp2 M ON E.mgr=M.id WHERE M.name='Ben' returns how many rows?",
            len(rows),
            "Ben's reports are Dee and Eve: 2.",
            marks=1,
            diff="M",
        )
    )

    # UNION vs UNION ALL
    setup = [
        "CREATE TABLE A(x INT)",
        "CREATE TABLE B(x INT)",
        "INSERT INTO A VALUES (1),(2),(2),(3)",
        "INSERT INTO B VALUES (2),(3),(4)",
    ]
    u = _sql(setup, "SELECT x FROM A UNION SELECT x FROM B")
    ua = _sql(setup, "SELECT x FROM A UNION ALL SELECT x FROM B")
    o.append(
        mcq(
            T,
            "A.x = {1,2,2,3}, B.x={2,3,4}. (|UNION|, |UNION ALL|) is",
            f"{len(u)}, {len(ua)}",
            "4, 4",
            "3, 7",
            "4, 6",
            "A",
            "UNION distinct: 1,2,3,4 (4). UNION ALL concatenates 4+3=7.",
            marks=1,
            diff="M",
        )
    )

    o.append(
        msq(
            T,
            "SQL three-valued logic. Which evaluations are UNKNOWN (not TRUE)?",
            "NULL = 5",
            "NULL IS NULL",
            "NOT (NULL > 0)",
            "5 = 5",
            "A;C",
            "IS NULL is TRUE for NULL. Comparisons with NULL are UNKNOWN; NOT UNKNOWN is UNKNOWN.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "Concerning COUNT and NULLs in SQL:",
            "COUNT(*) counts rows including those with NULLs",
            "COUNT(A) ignores rows where A is NULL",
            "SUM(A) ignores NULLs",
            "AVG(A) treats NULL as 0",
            "A;B;C",
            "AVG ignores NULLs too; it does not treat them as 0.",
            marks=2,
            diff="E",
        )
    )

    # more unique tables
    setup = [
        "CREATE TABLE Voyage(vid INT, ship TEXT, day INT, cargo INT)",
        "INSERT INTO Voyage VALUES (1,'Nila',1,40)",
        "INSERT INTO Voyage VALUES (2,'Nila',2,10)",
        "INSERT INTO Voyage VALUES (3,'Orca',1,25)",
        "INSERT INTO Voyage VALUES (4,'Orca',3,25)",
        "INSERT INTO Voyage VALUES (5,'Pinta',2,60)",
    ]
    q = "SELECT ship FROM Voyage GROUP BY ship HAVING MIN(cargo) >= 25"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Voyage(vid,ship,day,cargo): (1,Nila,1,40),(2,Nila,2,10),(3,Orca,1,25),(4,Orca,3,25),(5,Pinta,2,60).\n"
            "SELECT ship FROM Voyage GROUP BY ship HAVING MIN(cargo)>=25 returns how many rows?",
            len(rows),
            "Nila min 10 fails; Orca 25 and Pinta 60 pass: 2.",
            marks=1,
            diff="M",
        )
    )

    setup = [
        "CREATE TABLE Clinic(pid INT, ward TEXT, bill INT)",
        "INSERT INTO Clinic VALUES (1,'ICU',900)",
        "INSERT INTO Clinic VALUES (2,'ICU',400)",
        "INSERT INTO Clinic VALUES (3,'GEN',400)",
        "INSERT INTO Clinic VALUES (4,'GEN',100)",
        "INSERT INTO Clinic VALUES (5,'DAY',50)",
    ]
    q = (
        "SELECT pid FROM Clinic C WHERE bill > (SELECT AVG(bill) FROM Clinic C2 WHERE C2.ward=C.ward)"
    )
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Clinic(pid,ward,bill): (1,ICU,900),(2,ICU,400),(3,GEN,400),(4,GEN,100),(5,DAY,50).\n"
            "Correlated: pid whose bill > average bill of their own ward. Number of rows is",
            len(rows),
            "ICU avg 650 so pid 1; GEN avg 250 so pid 3; DAY avg 50 none. 2 rows.",
            marks=2,
            diff="H",
        )
    )

    setup = [
        "CREATE TABLE Book(isbn INT, title TEXT, copies INT)",
        "INSERT INTO Book VALUES (1,'Ada',3)",
        "INSERT INTO Book VALUES (2,'C',0)",
        "INSERT INTO Book VALUES (3,'ML',5)",
        "INSERT INTO Book VALUES (4,'DB',1)",
    ]
    q = "SELECT title FROM Book WHERE copies BETWEEN 1 AND 4"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Book(isbn,title,copies): (1,Ada,3),(2,C,0),(3,ML,5),(4,DB,1). SELECT title FROM Book WHERE copies BETWEEN 1 AND 4 returns how many rows?",
            len(rows),
            "Ada (3) and DB (1); C=0 and ML=5 out: 2.",
            marks=1,
            diff="E",
        )
    )

    setup = [
        "CREATE TABLE Marks(sid INT, course TEXT, m INT)",
        "INSERT INTO Marks VALUES (1,'DB',80)",
        "INSERT INTO Marks VALUES (1,'ML',70)",
        "INSERT INTO Marks VALUES (2,'DB',90)",
        "INSERT INTO Marks VALUES (2,'ML',60)",
        "INSERT INTO Marks VALUES (3,'DB',90)",
    ]
    q = "SELECT course, AVG(m) FROM Marks GROUP BY course"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Marks(sid,course,m): (1,DB,80),(1,ML,70),(2,DB,90),(2,ML,60),(3,DB,90). SELECT course, AVG(m) FROM Marks GROUP BY course returns how many rows?",
            len(rows),
            "Two courses DB and ML.",
            marks=1,
            diff="E",
        )
    )

    q = "SELECT sid FROM Marks GROUP BY sid HAVING COUNT(*) = (SELECT COUNT(DISTINCT course) FROM Marks)"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On Marks, students who have a row for every distinct course: SELECT sid FROM Marks GROUP BY sid HAVING COUNT(*) = (SELECT COUNT(DISTINCT course) FROM Marks). Number of rows is",
            len(rows),
            "Two distinct courses; sids 1 and 2 have 2 rows, sid 3 has 1. Answer 2.",
            marks=2,
            diff="H",
        )
    )

    o.append(
        mcq(
            T,
            "SQL query SELECT * FROM R WHERE A IN (SELECT A FROM S). If S.A contains NULL and 5, and R.A=5, the row with 5",
            "is returned (5 IN (5,NULL) is TRUE)",
            "is rejected because of the NULL",
            "causes a runtime error",
            "is returned only if R has no NULLs",
            "A",
            "IN is TRUE if any equality is TRUE; UNKNOWN others do not cancel a TRUE match.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        mcq(
            T,
            "SELECT * FROM R WHERE A NOT IN (SELECT A FROM S) when S.A is {5, NULL} and R.A=7",
            "the row is filtered out because NOT IN with a NULL in the set is UNKNOWN",
            "the row is returned because 7 != 5",
            "the query errors",
            "NULL is ignored in NOT IN always",
            "A",
            "NOT IN is NOT(OR of equalities). A NULL equality is UNKNOWN, so the OR is UNKNOWN if no TRUE, and NOT UNKNOWN is UNKNOWN.",
            marks=2,
            diff="H",
        )
    )

    # INSERT FK questions handled later; more counts
    setup = [
        "CREATE TABLE Sensor(id INT, loc TEXT, t INT, val REAL)",
        "INSERT INTO Sensor VALUES (1,'Dock',1,3.2)",
        "INSERT INTO Sensor VALUES (2,'Dock',2,3.2)",
        "INSERT INTO Sensor VALUES (3,'Yard',1,4.0)",
        "INSERT INTO Sensor VALUES (4,'Yard',2,1.0)",
        "INSERT INTO Sensor VALUES (5,'Gate',1,4.0)",
    ]
    q = "SELECT loc FROM Sensor GROUP BY loc HAVING COUNT(DISTINCT val)=1"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Sensor(id,loc,t,val): (1,Dock,1,3.2),(2,Dock,2,3.2),(3,Yard,1,4.0),(4,Yard,2,1.0),(5,Gate,1,4.0).\n"
            "SELECT loc FROM Sensor GROUP BY loc HAVING COUNT(DISTINCT val)=1 returns how many rows?",
            len(rows),
            "Dock all 3.2; Yard two values; Gate one value. Two locs.",
            marks=2,
            diff="M",
        )
    )

    setup = [
        "CREATE TABLE Exam(sid INT, subj TEXT, score INT)",
        "INSERT INTO Exam VALUES (1,'DA',80)",
        "INSERT INTO Exam VALUES (2,'DA',80)",
        "INSERT INTO Exam VALUES (3,'DA',60)",
        "INSERT INTO Exam VALUES (1,'GA',70)",
        "INSERT INTO Exam VALUES (2,'GA',90)",
    ]
    q = "SELECT sid FROM Exam WHERE subj='DA' AND score >= 80"
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "Exam(sid,subj,score): (1,DA,80),(2,DA,80),(3,DA,60),(1,GA,70),(2,GA,90). SELECT sid FROM Exam WHERE subj='DA' AND score>=80 returns how many rows?",
            len(rows),
            "Sids 1 and 2: two rows.",
            marks=1,
            diff="E",
        )
    )

    q = (
        "SELECT E1.sid FROM Exam E1 WHERE E1.subj='DA' AND EXISTS "
        "(SELECT 1 FROM Exam E2 WHERE E2.sid=E1.sid AND E2.subj='GA' AND E2.score>E1.score)"
    )
    rows = _sql(setup, q)
    o.append(
        nat(
            T,
            "On Exam, sids whose DA score is strictly less than their own GA score. Number of rows is",
            len(rows),
            "sid1: DA 80 vs GA 70 no; sid2: 80 vs 90 yes; sid3 has no GA. 1 row.",
            marks=2,
            diff="H",
        )
    )
    return o


def _integrity():
    o = []
    T = "Integrity constraints"

    o.append(
        msq(
            T,
            "Relations r(A,B) and s(B,C) with FK r.B -> s.B (every r.B must appear in s). Which operations NEVER violate this FK, regardless of the current tuples (assuming they currently satisfy the FK)?",
            "inserting a tuple into s",
            "deleting a tuple from r",
            "inserting a tuple into r",
            "deleting a tuple from s",
            "A;B",
            "Inserting into the referenced table s, or deleting from the referencing table r, cannot create a dangling FK. Inserts into r and deletes from s can.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "ON DELETE CASCADE on FK Child.pid -> Parent.pid means that deleting a Parent row",
            "deletes matching Child rows",
            "is rejected if any Child references it",
            "sets Child.pid to NULL",
            "moves Child rows to an archive table automatically",
            "A",
            "CASCADE propagates the delete. RESTRICT/NO ACTION reject; SET NULL is the third option.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "ON DELETE SET NULL requires that the FK column is",
            "nullable",
            "part of the child's primary key",
            "a candidate key of the parent",
            "composite",
            "A",
            "You cannot set NULL on a NOT NULL FK (or on a PK component that is not nullable).",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            T,
            "A table Emp(ssn PK, name, dno FK->Dept.dno, CHECK (salary > 0)). Which inserts are rejected on an empty Emp with Dept already containing dno=5 only?",
            "(1,'A',5) with salary 10 if salary is a fourth column >0 — wait use concrete",
            "a row with duplicate ssn",
            "a row with dno=9 (not in Dept)",
            "a row with salary = -3",
            "B;C;D",
            "Placeholder.",
            marks=2,
            diff="M",
        )
    )
    o[-1] = msq(
        T,
        "Emp(ssn PRIMARY KEY, dno REFERENCES Dept(dno), salary INT CHECK (salary > 0)). Dept currently contains only dno=5. Which new Emp rows are rejected?",
        "ssn that already exists in Emp",
        "dno=9 (absent from Dept)",
        "salary=0 (fails CHECK)",
        "dno=5, salary=10, fresh ssn",
        "A;B;C",
        "The last row satisfies PK, FK and CHECK.",
        marks=2,
        diff="M",
    )
    o.append(
        mcq(
            T,
            "A UNIQUE constraint on column email of User allows how many NULLs in SQL (standard, UNIQUE is satisfied by NULL != NULL)?",
            "any number of NULLs (in most SQL systems UNIQUE allows multiple NULLs)",
            "exactly one NULL",
            "zero NULLs always",
            "NULL is equal to NULL under UNIQUE so at most one",
            "A",
            "UNIQUE treats two NULLs as not equal, so multiple NULLs are allowed in the usual interpretation. PRIMARY KEY still forbids NULL.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "PRIMARY KEY versus UNIQUE NOT NULL. In SQL they are similar, but a table may have",
            "at most one PRIMARY KEY and any number of UNIQUE constraints",
            "any number of PRIMARY KEYs",
            "no UNIQUE if it has a PRIMARY KEY",
            "a PRIMARY KEY that contains NULLs",
            "A",
            "One PK; PK columns are NOT NULL; several UNIQUE are fine.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Relation Takes(sid, cid, grade) with PRIMARY KEY (sid,cid) and FK sid->Student, cid->Course. Inserting (1,10,'A') succeeds once. A second insert of (1,10,'B') is rejected. The number of tuples in Takes after both attempts is",
            1,
            "The PK rejects the duplicate (sid,cid).",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Referential integrity from R.a to S.b is violated by which one of these, if S currently has b-values {1,2} and R has a-values {1}?",
            "DELETE FROM S WHERE b=1",
            "INSERT INTO S VALUES (3)",
            "DELETE FROM R WHERE a=1",
            "UPDATE S SET b=2 WHERE b=2",
            "A",
            "Deleting the referenced 1 leaves R.a=1 dangling.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            T,
            "Deferred constraint checking (end of transaction) is useful because",
            "a cycle of FKs can be inserted in one transaction",
            "a tuple can temporarily violate a CHECK that a later statement of the same transaction repairs",
            "it makes PRIMARY KEY optional",
            "it disables FOREIGN KEY forever",
            "A;B",
            "DEFERRABLE constraints are checked at COMMIT, not after each statement.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "A domain constraint / CHECK (status IN ('open','closed')) rejects",
            "status='pending'",
            "status='open'",
            "a NULL status if CHECK treats NULL as pass (UNKNOWN is not FALSE)",
            "both pending and NULL in all engines uniformly",
            "A",
            "CHECK fails only when the condition is FALSE. UNKNOWN (NULL) typically passes. 'pending' is FALSE.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        nat(
            T,
            "Parent P(id PK) has rows 1,2. Child C(id PK, pid FK->P) has rows (10,1),(11,1). ON DELETE CASCADE. DELETE FROM P WHERE id=1. How many rows remain in C?",
            0,
            "Both child rows referenced pid=1 and are deleted. Wait, only those two exist so 0 remain. Yes.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Same P/C but ON DELETE RESTRICT. DELETE FROM P WHERE id=1 is attempted. Number of rows remaining in P is",
            2,
            "The delete is rejected; both parent rows stay.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "An assertion 'every team name in Team appears in Defender or Forward' is the SQL counterpart of which RA test being empty?",
            "Team_names - (Defender_names ∪ Forward_names)",
            "Team × Defender",
            "Defender ∩ Forward",
            "pi_name(Team)",
            "A",
            "The assertion is that the difference is empty.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "Which are integrity constraints in the relational model?",
            "entity integrity (no NULL in primary key)",
            "referential integrity of foreign keys",
            "user-defined CHECK / assertions",
            "the physical block size of a file",
            "A;B;C",
            "Block size is physical design, not an integrity constraint.",
            marks=2,
            diff="E",
        )
    )
    return o


def _files_index():
    o = []
    T = "Files and indexing"

    fanouts = [
        ("Voyage", 4096, 10, 11, 12),
        ("Invoice", 2048, 8, 12, 8),
        ("Roster", 8192, 16, 20, 16),
        ("Clinic", 4096, 6, 10, 8),
        ("Harbour", 512, 4, 8, 4),
        ("SensorLog", 4096, 12, 16, 12),
        ("MatchCard", 1024, 6, 10, 8),
        ("Payroll", 4096, 8, 14, 8),
        ("LibraryCopy", 2048, 10, 14, 10),
        ("FlightLeg", 8192, 10, 18, 12),
    ]
    for rel, block, nodeptr, key, recptr in fanouts:
        # non-leaf: n * nodeptr + (n-1)*key <= block  => n*(nodeptr+key) <= block+key
        n = (block + key) // (nodeptr + key)
        o.append(
            nat(
                T,
                "A B+ tree is built on relation "
                + rel
                + ". Node size = "
                + str(block)
                + " bytes, node-pointer size = "
                + str(nodeptr)
                + " bytes, search-key size = "
                + str(key)
                + " bytes, data-record pointer = "
                + str(recptr)
                + " bytes. A non-leaf stores n node pointers and n-1 keys, packed with no extra header. The maximum n (fanout) is",
                n,
                "n*nodeptr + (n-1)*key <= block => n <= floor((block+key)/(nodeptr+key)) = "
                + str(n)
                + ".",
                marks=2,
                diff="H",
            )
        )
        # leaf: n keys + n data ptrs + 1 sibling ptr
        leaf_n = (block - nodeptr) // (key + recptr)
        o.append(
            nat(
                T,
                "For the same B+ tree on "
                + rel
                + " (block "
                + str(block)
                + ", key "
                + str(key)
                + ", record-ptr "
                + str(recptr)
                + ", sibling/node-ptr "
                + str(nodeptr)
                + "), a leaf holds n keys and n record pointers plus one sibling pointer. Maximum n is",
                leaf_n,
                "n*(key+recptr) + nodeptr <= block => n = floor((block-nodeptr)/(key+recptr)) = "
                + str(leaf_n)
                + ".",
                marks=2,
                diff="H",
            )
        )

    o.append(
        mcq(
            T,
            "A dense index has one index entry per",
            "record",
            "block of the data file",
            "distinct search-key value in a sparse clustered file only — wait dense: per record",
            "overflow page",
            "A",
            "Dense: every record (or every key occurrence). Sparse: one per data block, typically on a clustered file.",
            marks=1,
            diff="E",
        )
    )
    o[-1] = mcq(
        T,
        "A dense secondary index on attribute A of HeapFile Staff has one entry per",
        "record of Staff",
        "block of Staff",
        "distinct A-value only, even if A is not unique, with no posting list",
        "cylinder of the disk",
        "A",
        "Dense means every record is referenced. A sparse index points at blocks.",
        marks=1,
        diff="E",
    )
    o.append(
        msq(
            T,
            "Which index types support range predicates (A BETWEEN 10 AND 20) efficiently?",
            "B+ tree on A",
            "sorted dense index on A",
            "hash index on A (extendible / static hash)",
            "clustered B+ tree on A",
            "A;B;D",
            "Hash indexes are for equality, not ranges.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "A clustered (primary) index on A usually requires the data file to be",
            "ordered on A",
            "a heap in arbitrary order",
            "hashed on a different key",
            "a bitmap",
            "A",
            "Clustered means data records are stored in the search-key order.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "A heap file of 10000 records, blocking factor 10 records/block. Number of blocks is",
            1000,
            "10000/10=1000.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Unsorted heap, 1000 blocks, linear search for a missing equality key (unindexed). Worst-case block reads are",
            1000,
            "The whole file is scanned.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Sorted file, 1000 blocks, binary search on the sort key, one record per matching key. Worst-case block reads (approx ceil(log2 1000)) are",
            math.ceil(math.log2(1000)),
            "ceil(log2 1000)=10.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Blocking factor of a file of 200-byte records in 4096-byte blocks with unspanned records is",
            "20",
            "21",
            "19",
            "4096",
            "A",
            "floor(4096/200)=20. Unspanned wastes the leftover 96 bytes.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Extendible hashing doubles the directory when a bucket overflows. The directory is an array of",
            "bucket pointers of size 2^{global depth}",
            "records",
            "B+ leaves",
            "cylinders",
            "A",
            "Global depth d => 2^d directory entries.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "B+ tree leaves are linked. Which follow?",
            "an equality search is O(height)",
            "a range scan after locating the start is sequential along leaves",
            "non-leaf nodes store record pointers for every key in the usual internal-node design",
            "all record pointers live in the leaves in a typical B+ tree",
            "A;B;D",
            "Internal nodes store only keys and child pointers; data pointers are at the leaves.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "A B+ tree of order (max keys per node) 4 and height 2 (root height 0, leaves at level 2) can store at most how many keys if every node is full? Internal fanout 5 children, 4 keys/node. Leaves also 4 keys. Max keys = 5^2 * 4 =",
            100,
            "5^2=25 leaves * 4 keys = 100.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        mcq(
            T,
            "Static hashing with n buckets. Expected time for equality search under uniform hashing and no overflow is",
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n log n)",
            "A",
            "One hash computation plus one bucket access.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "A bitmap index on a low-cardinality attribute Gender of N rows uses (ignoring compression) about",
            "2 bit-vectors of N bits",
            "N B+ tree leaves",
            "one float per row",
            "a hash table of size N",
            "A",
            "One bitmap per distinct value.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "Data file 8000 records, sparse clustered index with one index entry per data block, 40 records/block. Number of index entries is",
            200,
            "8000/40=200 data blocks, one entry each.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "ISAM is a static multilevel index. Inserts that overflow a leaf go to",
            "overflow chains",
            "a freshly split leaf that updates the root always",
            "a hash bucket",
            "the WAL only",
            "A",
            "Classic ISAM does not rebalance; overflow chains degrade it.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "File organisations. Which pairs are matched correctly?",
            "heap file: insert is O(1) (append), equality search is linear",
            "sorted file: range search is efficient, insert is expensive",
            "hashed file: equality search expected O(1), range search poor",
            "sorted file: insert is O(1) append at end regardless of key",
            "A;B;C",
            "Inserting into a sorted file while keeping order is not an append (unless the key is maximal).",
            marks=2,
            diff="M",
        )
    )
    return o


def _transform():
    o = []
    T = "Data types and transformation"

    series = [
        ("AgeYears", [10, 20, 30, 40, 50]),
        ("RainMm", [0, 2, 4, 6, 18]),
        ("SalaryLakh", [4, 5, 6, 7, 18]),
        ("TempC", [0, 10, 10, 20, 40]),
        ("DelayMin", [1, 1, 2, 3, 13]),
        ("ScoreRaw", [35, 45, 50, 55, 65]),
        ("LoadKw", [2, 4, 4, 6, 14]),
        ("DepthM", [3, 6, 9, 12, 15]),
    ]
    for name, xs in series:
        mn, mx = min(xs), max(xs)
        # min-max of last value to [0,1]
        mm = (xs[-1] - mn) / (mx - mn)
        mu = statistics.mean(xs)
        sd = statistics.pstdev(xs)  # population
        zlast = (xs[-1] - mu) / sd if sd else 0.0
        o.append(
            nat(
                T,
                "Attribute "
                + name
                + " has values "
                + str(xs)
                + ". Min-max normalisation into [0,1] maps the last value to (round to two decimals if needed; if it is a terminating decimal, give that). Report the exact value as a simplified decimal or integer.",
                round(mm, 4) if mm != int(mm) else int(mm),
                "(x-min)/(max-min) = ("
                + str(xs[-1])
                + "-"
                + str(mn)
                + ")/("
                + str(mx)
                + "-"
                + str(mn)
                + ") = "
                + str(mm)
                + ".",
                marks=2,
                diff="M",
            )
        )
        o.append(
            nat(
                T,
                "On the same "
                + name
                + " sample "
                + str(xs)
                + ", using population standard deviation, the z-score of the last value rounded to two decimals is",
                round(zlast, 2),
                "z=(x-mean)/sigma. mean="
                + str(mu)
                + ", sigma="
                + str(sd)
                + ", z="
                + str(zlast)
                + ".",
                marks=2,
                diff="H",
            )
        )

    o.append(
        mcq(
            T,
            "Equal-width discretisation of AgeYears on [10,50] into 4 bins uses bin width",
            "10",
            "4",
            "40",
            "5",
            "A",
            "(50-10)/4=10.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Equal-frequency (quantile) discretisation of a sample of 12 distinct values into 4 bins puts how many values in each bin?",
            "3",
            "4",
            "12",
            "2",
            "A",
            "12/4=3 observations per bin.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            T,
            "Which are lossless compression schemes (in the information-lossless sense)?",
            "Huffman coding of a discrete alphabet",
            "run-length encoding of a bit-vector",
            "JPEG at quality 30 on a photo",
            "dictionary (LZ) compression of a text file",
            "A;B;D",
            "JPEG is lossy. Huffman, RLE and LZ are lossless.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Sampling 20 rows out of 200 without replacement. The probability a given row is included is",
            "0.1",
            "0.2",
            "1/20",
            "20",
            "A",
            "Simple random sample: 20/200=0.1.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Sampling with replacement of 20 draws from 200. Expected number of times a given row appears is",
            "0.1",
            "1",
            "20",
            "0",
            "A",
            "Each draw includes it with p=1/200; 20 draws => 20/200=0.1.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Min-max normalisation to [0,1] is sensitive to",
            "outliers that stretch min or max",
            "the mean only",
            "the mode only",
            "the order of columns in the table",
            "A",
            "A single extreme value changes min or max and rescales everyone.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "z-score normalisation uses",
            "(x-mean)/std",
            "(x-min)/(max-min)",
            "log(1+x)",
            "rank(x)/n",
            "A",
            "Standard score. Min-max is the other common linear rescaling.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            T,
            "Data-type roles in warehousing / mining. Which assignments are reasonable?",
            "Gender: categorical (nominal)",
            "Temperature in C: numeric (interval/ratio depending on scale use)",
            "T-shirt size S<M<L: ordinal",
            "Employee-id as a 6-digit code: numeric quantity on which means are meaningful",
            "A;B;C",
            "IDs are nominal identifiers, not magnitudes.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "Decimal 13 in 4-bit two's complement does not fit. The largest non-negative integer representable in 4-bit two's complement is",
            7,
            "Range is -8..7.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "A CHAR(10) column versus VARCHAR(10) for strings of typical length 3. VARCHAR is preferred because",
            "it stores only the actual length plus a length prefix, saving space",
            "it is always faster to index",
            "it forbids trailing spaces by standard",
            "it is a numeric type",
            "A",
            "CHAR pads to the declared width; VARCHAR is variable-length.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Discretising a numeric attribute before naive Bayes is done so that",
            "a multinomial / categorical model can be used on bins",
            "the mean of the attribute becomes 0",
            "compression becomes lossy",
            "the attribute becomes a key",
            "A",
            "Binning turns a continuous feature into a categorical one.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "Stratified sampling: a table is 30% class A and 70% class B. A stratified sample of 100 rows (proportional) contains how many class-A rows?",
            30,
            "0.3*100=30.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Run-length encoding of the bit-vector 0000011111000 (13 bits) can store it as counts",
            "5 zeros, 5 ones, 3 zeros",
            "13 ones",
            "8 zeros",
            "2 runs only",
            "A",
            "Three runs: 5,5,3.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Normalising a numeric column to zero mean and unit variance is",
            "z-score standardisation",
            "min-max to [0,1]",
            "equal-width binning",
            "lossy JPEG",
            "A",
            "That is the definition of z-score / standard-score scaling.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Attribute DelayMin = [1,1,2,3,13]. After min-max to [0,1], the first value maps to",
            0,
            "min is 1, so (1-1)/(13-1)=0.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Sampling a data cube's facts at 10% (random) mainly affects",
            "approximate aggregates, with variance depending on the sample size",
            "the schema of dimensions",
            "the BCNF status of the fact table",
            "foreign-key directions",
            "A",
            "Sampling is an approximation technique for warehouse queries.",
            marks=1,
            diff="M",
        )
    )
    return o


def _warehouse():
    o = []
    T = "Warehousing and OLAP"

    o.append(
        mcq(
            T,
            "A star schema for RetailSales has a fact table SalesFact(date_id, store_id, sku_id, qty, amount) and dimension tables DateDim, StoreDim, SkuDim. This is a star rather than a snowflake because",
            "dimensions are denormalised single tables, not split into sub-dimensions",
            "there is no fact table",
            "every dimension is in BCNF with many hops",
            "measures are stored in every dimension",
            "A",
            "Star: one denormalised table per dimension. Snowflake: dimensions normalised into subtables.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Snowflake schema for the same warehouse splits StoreDim into Store, City, State. Compared with star,",
            "snowflake reduces dimension redundancy and adds more joins at query time",
            "snowflake always speeds every query",
            "star cannot represent hierarchies",
            "fact tables disappear",
            "A",
            "Normalised dimensions trade join cost for less redundancy.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Cube SalesQty is visualised by ProductType × Month × Country. To see ProductType × Month × State (State is a finer geographic level under Country) the OLAP operation is",
            "drill-down",
            "roll-up",
            "slice",
            "dice",
            "A",
            "Drill-down walks down a concept hierarchy (Country to State).",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "From the same SalesQty cube, aggregating Month up to Quarter is",
            "roll-up",
            "drill-down",
            "slice",
            "pivot",
            "A",
            "Roll-up climbs a hierarchy or drops a dimension by aggregation.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Fixing Country = 'India' and viewing ProductType × Month is",
            "a slice",
            "a drill-down",
            "a snowflake",
            "a bitmap join",
            "A",
            "Slice selects a single value of one dimension, reducing dimensionality by one.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "Selecting Country in {India, Nepal} and Month in {Jan, Feb} on the cube is",
            "dice",
            "slice",
            "roll-up",
            "star join",
            "A",
            "Dice selects ranges/sets on multiple dimensions.",
            marks=1,
            diff="E",
        )
    )
    cubes = [
        ("ClinicVisits", "Hospital, Ward, Day", "Ward to Bed"),
        ("HarbourTonnage", "Port, ShipType, Month", "Port to Berth"),
        ("GridLoad", "Region, Fuel, Hour", "Hour to Minute"),
        ("CourseEnrol", "Dept, Programme, Sem", "Dept to Faculty"),
        ("MatchGoals", "Team, Venue, Week", "Week to MatchDay"),
        ("SensorAvg", "Station, Metric, Day", "Station to SensorId"),
        ("PayrollCost", "Org, Grade, Month", "Org to Team"),
        ("LibraryLoans", "Branch, Genre, Month", "Genre to Shelf"),
    ]
    for cname, dims, finer in cubes:
        o.append(
            mcq(
                T,
                "Cube "
                + cname
                + " is shown at dimensions "
                + dims
                + ". Moving the last geographic/organisational/time level to the finer grain ("
                + finer
                + ") is",
                "drill-down",
                "roll-up",
                "slice",
                "dice",
                "A",
                "Finer grain along a hierarchy is drill-down on cube " + cname + ".",
                marks=1,
                diff="E",
            )
        )
        o.append(
            mcq(
                T,
                "On cube "
                + cname
                + " ("
                + dims
                + "), aggregating away the middle dimension entirely (summing the measure over it) is",
                "roll-up / projection of a dimension",
                "drill-down",
                "a foreign-key insert",
                "2NF decomposition",
                "A",
                "Dropping a dimension by aggregation is a roll-up.",
                marks=1,
                diff="M",
            )
        )

    o.append(
        msq(
            T,
            "Measures of a warehouse fact. Which classifications are correct?",
            "quantity sold is additive across all dimensions",
            "account balance is semi-additive (cannot sum over time)",
            "ratio of defective items (a percentage) is typically non-additive",
            "date_id in the fact table is an additive measure",
            "A;B;C",
            "date_id is a dimension foreign key, not a measure.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Grain of SalesFact is 'one row per sku per store per day'. A query that needs 'per week' should",
            "roll-up the Date dimension along day < week",
            "insert extra fact rows",
            "change the FK direction",
            "dice on sku only",
            "A",
            "Time hierarchy day < week < month < year supports roll-up.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "A concept hierarchy for Location is Store < City < State < Country. The coarsest level is",
            "Country",
            "Store",
            "City",
            "the fact table",
            "A",
            "The top of the hierarchy is the coarsest aggregation.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            T,
            "Star schema facts. Which statements hold?",
            "the fact table is typically in (near) BCNF with FKs to dimensions plus measures",
            "dimension tables are often denormalised and not in BCNF",
            "a snowflake normalises dimension hierarchies into separate tables",
            "a star schema cannot have more than two dimensions",
            "A;B;C",
            "Stars routinely have many dimensions (date, store, product, promo, ...).",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Pivot (rotate) on a cube Product × Month showing Sales is",
            "swapping the axes so Month × Product is displayed",
            "deleting the Product dimension",
            "a B+ tree split",
            "an FK cascade",
            "A",
            "Pivot/rotate changes which dimensions are on which axis.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "A warehouse ETL pipeline's 'T' (transform) step typically includes",
            "cleaning, conforming dimensions, and computing measures",
            "dropping all FKs",
            "replacing SQL by Python loops only",
            "forcing every table into 6NF",
            "A",
            "Transform is the cleansing / conforming / surrogate-key stage.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "A conformed dimension DateDim shared by SalesFact and InventoryFact means",
            "both facts join to the same Date dimension table / meaning of dates",
            "the facts are the same table",
            "dates are stored as TEXT without a dimension",
            "the warehouse has no time hierarchy",
            "A",
            "Conformed dimensions are reusable across facts (Kimball).",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "A 3-dimensional cube Product(10) × Store(5) × Day(30) stored densely has how many cells?",
            1500,
            "10*5*30=1500.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Slicing that cube on Store='Pune' (one of 5 stores) leaves how many cells in the remaining Product × Day plane (dense)?",
            300,
            "10*30=300.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "MOLAP versus ROLAP: MOLAP stores the cube in",
            "a specialised multidimensional array structure",
            "only normalised 3NF tables with no aggregates",
            "a B+ tree of XML",
            "main-memory Python lists exclusively",
            "A",
            "MOLAP: multidimensional arrays; ROLAP: relational star/snowflake plus SQL.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "Which are OLAP operations on cube HarbourTonnage(Port, ShipType, Month)?",
            "roll-up Month to Year",
            "drill-down Port to Berth",
            "slice Month='Jan'",
            "BCNF decomposition of the cube",
            "A;B;C",
            "Normal-form decomposition is a relational design step, not an OLAP navigation operator.",
            marks=2,
            diff="E",
        )
    )
    o.append(
        mcq(
            T,
            "A degenerate dimension in a fact table is",
            "a dimension key with no attributes (e.g. a bill_no stored in the fact)",
            "a dimension in 6NF",
            "a measure that is additive",
            "an ETL error",
            "A",
            "Degenerate dimensions are identifiers without a dimension table.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Slowly changing dimension Type 2 on CustomerDim handles a city change by",
            "inserting a new dimension row with new surrogate key and version dates",
            "overwriting the city in place with no history (Type 1)",
            "dropping the customer",
            "storing the city in the fact table only",
            "A",
            "Type 2 versions rows. Type 1 overwrites.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            T,
            "Factless fact table Attendance(date_id, student_id, course_id) records events with no numeric measure. A COUNT(*) grouped by course_id computes",
            "the number of attendance events per course",
            "a salary",
            "a z-score",
            "fanout",
            1,
            "The only measure is the event count itself.",
            marks=1,
            diff="M",
        )
    )
    # The above nat has a wrong argument order - I passed 1 as sol start. Let me fix.
    o[-1] = nat(
        T,
        "Factless fact table Attendance(date_id, student_id, course_id) stores event rows with no numeric measure. For a course that appears in 17 fact rows, COUNT(*) for that course is",
        17,
        "Each fact row is one attendance event.",
        marks=1,
        diff="E",
    )
    o.append(
        mcq(
            T,
            "Additive measure amount can be summed along Store and along Date. Semi-additive inventory_qty can be summed along Store but not along Date. The right way to get a monthly inventory picture is",
            "take an average or end-of-month snapshot along Date, sum along Store",
            "sum inventory_qty over all days and all stores",
            "ignore Date",
            "use COUNT(DISTINCT) on qty",
            "A",
            "Semi-additive measures need a time snapshot policy.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            T,
            "Concept hierarchy Time: Day < Week < Month < Quarter < Year. Which OLAP moves are correctly named for cube Sales(Product, Day)?",
            "Day to Month: roll-up",
            "Month to Day: drill-down",
            "Day to Year: roll-up",
            "Year to Month: roll-up",
            "A;B;C",
            "Year to Month is finer, hence drill-down not roll-up.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "Bitmap indexes are attractive in warehouses because",
            "dimension attributes often have low cardinality and queries are range/aggregate heavy",
            "every fact table is updated thousands of times per second in OLTP style",
            "they replace the need for a Date dimension",
            "they implement BCNF",
            "A",
            "Low-cardinality bits + AND/OR of bitmaps fit OLAP predicates. They are costly to maintain under heavy OLTP updates.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "A data mart versus an enterprise warehouse: a mart is",
            "a subject-area subset (e.g. sales only), often a star",
            "always a normalised 3NF EDW of the whole company",
            "a B+ tree",
            "an OLTP orders table",
            "A",
            "Marts are departmental; the EDW is enterprise-wide.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            T,
            "Cube GridLoad(Region 8 × Fuel 4 × Hour 24). Drill-down Hour to 4 fifteen-minute slots (4× finer) multiplies the dense cell count by",
            4,
            "One dimension becomes 4 times longer; 8*4*96 / (8*4*24) = 4.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            T,
            "HOLAP (hybrid OLAP) typically",
            "keeps detailed facts in relational tables and some aggregates in MOLAP storage",
            "forbids SQL",
            "stores only bitmaps",
            "is identical to 1NF",
            "A",
            "Hybrid: relational detail + multidimensional aggregates.",
            marks=1,
            diff="M",
        )
    )
    return o


def _more_db():
    """Extra unique items to hit mix and 260+."""
    o = []
    o.append(
        msq(
            "ER model",
            "Mapping a 1:N relationship WorksIn(Instructor -> Department) . Which are correct?",
            "Department's key becomes a FK in Instructor",
            "a separate WorksIn table is mandatory",
            "Instructor's key as FK in Department would force each dept to have at most one instructor if UNIQUE",
            "total participation of Instructor makes the FK NOT NULL",
            "A;C;D",
            "1:N is absorbed as a FK on the N-side. A relationship table is optional, not mandatory.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            "SQL",
            "On Emp(bonus) with some NULLs, which queries count only non-NULL bonuses?",
            "SELECT COUNT(bonus) FROM Emp",
            "SELECT COUNT(*) FROM Emp WHERE bonus IS NOT NULL",
            "SELECT COUNT(*) FROM Emp",
            "SELECT SUM(1) FROM Emp WHERE bonus IS NOT NULL",
            "A;B;D",
            "COUNT(*) over the whole table includes NULL-bonus rows.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            "Relational model and FDs",
            "R(A,B,C,D) with FDs AB->C, C->D, D->A. Which are candidate keys?",
            "AB",
            "BC",
            "BD",
            "CD",
            "A;B;C",
            "AB+ = ABCD; BC+ : C->D->A so BCAD; BD+ : D->A so ABD then AB->C. CD+ = CDA misses B.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        msq(
            "Warehousing and OLAP",
            "Cube MatchGoals(Team, Venue, Week). Which operations are correctly named?",
            "Week to MatchDay: drill-down",
            "Venue='Pune' only, keep Team × Week: slice",
            "Team in {Goa,Pune} and Week in {1,2}: dice",
            "Week to MatchDay: roll-up",
            "A;B;C",
            "Finer time is drill-down, not roll-up.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            "Files and indexing",
            "A B+ tree index is chosen over a hash index when",
            "queries include range predicates on the key",
            "the key is used in ORDER BY",
            "only point lookups occur and ranges never do (hash would be competitive)",
            "the attribute has two values (bitmap may be even better) but ranges still matter",
            "A;B",
            "Hash wins pure equality; B+ wins ranges and ordered scans. The question asks when B+ is chosen over hash: A and B. C argues the opposite.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            "Integrity constraints",
            "Foreign key Child.pid REFERENCES Parent.pid. Currently satisfying. Which statements never introduce a violation by themselves?",
            "INSERT INTO Parent",
            "DELETE FROM Child",
            "UPDATE Child SET pid to a value that exists in Parent",
            "DELETE FROM Parent of a referenced pid without CASCADE/SET NULL (NO ACTION)",
            "A;B;C",
            "D is the classic violation. C is OK if the new pid exists.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            "Data types and transformation",
            "Given AgeYears = [10,20,30,40,50], which are true?",
            "min-max of 10 to [0,1] is 0",
            "min-max of 50 to [0,1] is 1",
            "the sample mean is 30",
            "equal-width 4 bins on [10,50] have width 20",
            "A;B;C",
            "Width is (50-10)/4=10, not 20.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            "Relational algebra and tuple calculus",
            "Let R and S be union-compatible. Which identities hold?",
            "R ∪ S = S ∪ R",
            "R ∩ S = R - (R - S)",
            "R × S = S × R (up to attribute order)",
            "R - S = S - R always",
            "A;B;C",
            "Difference is not commutative.",
            marks=2,
            diff="E",
        )
    )
    o.append(
        nat(
            "SQL",
            "SELECT 1 FROM dual WHERE 1=1 AND NULL=NULL returns how many rows in standard SQL 3VL?",
            0,
            "NULL=NULL is UNKNOWN; AND with TRUE is UNKNOWN; WHERE keeps only TRUE.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            "SQL",
            "SELECT 1 WHERE 1=1 OR NULL=NULL returns how many rows?",
            1,
            "TRUE OR UNKNOWN is TRUE.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "SQL",
            "SELECT AVG(x) FROM (VALUES (1),(2),(NULL)) t(x) in standard SQL is",
            "1.5",
            "1",
            "NULL",
            "0.75",
            "A",
            "AVG ignores NULL: (1+2)/2=1.5.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "ER model",
            "A recursive relationship MarriedTo on Person that is 1:1 and symmetric is mapped by",
            "a nullable unique FK spouse_id on Person (or a two-column table with a symmetric constraint)",
            "two Person tables",
            "an M:N table with no keys",
            "a CHECK on dates only",
            "A",
            "A self-relationship becomes a self-FK (plus uniqueness for 1:1).",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            "Files and indexing",
            "Unspanned records of 300 bytes in 2048-byte blocks. Blocking factor is",
            6,
            "floor(2048/300)=6.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            "Files and indexing",
            "8000 such records (300 B, 2048 B blocks, unspanned, bf=6). Number of blocks needed is",
            math.ceil(8000 / 6),
            "ceil(8000/6)=1334.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "Warehousing and OLAP",
            "A junk dimension packs several low-cardinality flags (pay_type, gift_wrap, ... ) into",
            "one dimension table whose key is stored in the fact",
            "the date dimension",
            "a MOLAP cell comment",
            "an ER weak entity of the OLTP system only",
            "A",
            "Junk dimensions collect miscellaneous flags.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "Relational model and FDs",
            "Trivial FD X->Y means",
            "Y is a subset of X",
            "X is a candidate key",
            "Y is empty only",
            "X and Y are disjoint",
            "A",
            "Reflexivity: if Y ⊆ X then X->Y always holds.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            "Relational algebra and tuple calculus",
            "R has 10 tuples, sigma_P(R) keeps 3. pi_A(sigma_P(R)) has 2 distinct A values. Number of rows in the projection is",
            2,
            "Projection is a set of size 2.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            "Integrity constraints",
            "Entity integrity says",
            "no primary-key attribute may be NULL",
            "every FK is NULL",
            "every table has two keys",
            "CHECK constraints are forbidden",
            "A",
            "Entity integrity is the no-NULL-in-PK rule.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            "Data types and transformation",
            "Decimal(5,2) can store which of the following?",
            "123.45",
            "1234.5 (needs 5 digits to the left? 1234.5 is 6 significant with scale 2: 1234.50 needs precision 6)",
            "0.0001 stored exactly as four decimals of scale 2",
            "an arbitrary-length string",
            "A",
            "Precision 5 scale 2: up to 999.99 (3+2). 123.45 fits. 1234.5 does not. 0.0001 would round at 2 decimals.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        msq(
            "Warehousing and OLAP",
            "Kimball-style dimensional modelling. Which are true?",
            "facts are additive (or semi/non) numeric measurements at a declared grain",
            "dimensions provide the labels and hierarchies for slicing",
            "a star join is fact-to-dimension on surrogate keys",
            "every dimension must be a weak entity of the fact in the ER sense of double rectangles",
            "A;B;C",
            "Dimensions are not weak entities of the fact; they are conformed master data.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        nat(
            "SQL",
            "Table Q(a) has rows 1,1,2,NULL. SELECT COUNT(DISTINCT a) FROM Q returns",
            2,
            "DISTINCT a ignores NULL and collapses the two 1s: {1,2}.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            "SQL",
            "Same Q(a)={1,1,2,NULL}. SELECT COUNT(a) FROM Q returns",
            3,
            "COUNT(a) skips NULL but not duplicate 1s: three non-null rows.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "Files and indexing",
            "A covering index for query SELECT A,B FROM R WHERE A=5 is a B+ tree on",
            "(A,B) so the query can be answered from the index alone",
            "C only",
            "the heap RID list of an unrelated key",
            "a hash on B only, with A unindexed",
            "A",
            "Covering / index-only scan: all needed columns sit in the index.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "ER model",
            "Total participation of both sides of a 1:1 relationship Married(Person,Person) with two entity sets Man and Woman can be mapped as",
            "either key as a NOT NULL UNIQUE FK in the other table, or a single merged table",
            "an M:N table without uniqueness",
            "two independent tables with no FK",
            "a weak entity with no owner",
            "A",
            "Total 1:1 can even merge the entities; otherwise a mandatory unique FK.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        nat(
            "Relational model and FDs",
            "R(A,B,C) with FDs A->B, B->C. Number of candidate keys is",
            1,
            "Only A is a key.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            "Relational model and FDs",
            "That same R(A,B,C) with A->B, B->C is in",
            "2NF (single-attribute key, so no partial) but not 3NF (transitive C on A via B)",
            "BCNF",
            "3NF but not 2NF",
            "not 1NF",
            "A",
            "Classic 2NF-not-3NF chain with a simple key.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            "SQL",
            "SELECT * FROM R NATURAL JOIN S. If R(A,B) and S(B,C) then the result schema has attributes",
            "A,B,C",
            "A,B,B,C",
            "A,C only",
            "B only",
            "A",
            "Natural join equalises and keeps one copy of B.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            "Warehousing and OLAP",
            "A concept hierarchy of 4 levels Store<City<State<Country. Number of roll-up steps from Store to Country is",
            3,
            "Three climbs: Store to City to State to Country.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            "Data types and transformation",
            "Huffman coding a 4-symbol alphabet with probabilities 1/2, 1/4, 1/8, 1/8 has average code length (bits)",
            "1.75",
            "2",
            "4",
            "1",
            "A",
            "Optimal lengths 1,2,3,3: 0.5*1+0.25*2+0.125*3+0.125*3=1.75.",
            marks=2,
            diff="H",
        )
    )
    o.append(
        msq(
            "SQL",
            "GROUP BY vs DISTINCT. On Marks(sid,course) with duplicate (sid,course) forbidden by PK, which are true?",
            "SELECT sid FROM Marks GROUP BY sid returns each sid once",
            "SELECT DISTINCT sid FROM Marks returns each sid once",
            "SELECT sid, COUNT(*) FROM Marks GROUP BY sid is legal",
            "SELECT sid, COUNT(*) FROM Marks DISTINCT is the usual legal form",
            "A;B;C",
            "DISTINCT applies to the select list, not as SELECT ... DISTINCT COUNT with a leftover sid without GROUP BY.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            "Files and indexing",
            "Primary index versus secondary: a primary index is built on",
            "the ordering key of a sequentially ordered file",
            "any non-ordering attribute, densely",
            "a bitmap of gender only",
            "the log file",
            "A",
            "Primary/clustered indexes follow the file's sort order.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            "Integrity constraints",
            "Table R(a INT PRIMARY KEY). Inserts: 1, 2, 1, 3. How many rows does R contain after the four statements (the duplicate is rejected)?",
            3,
            "The second 1 fails; 1,2,3 remain.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            "Relational algebra and tuple calculus",
            "The five primitive RA operators of Codd's algebra are usually listed as",
            "select, project, union, difference, Cartesian product (rename sometimes added)",
            "join, division, outer join only",
            "GROUP BY and HAVING",
            "star and snowflake",
            "A",
            "Join and division are derived. Outer join is a later extension.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "ER model",
            "An attribute of a relationship (e.g. Enrolls.grade) is placed, after mapping an M:N relationship, in",
            "the relationship table",
            "both entity tables",
            "a CHECK constraint only",
            "the log",
            "A",
            "Relationship attributes become columns of the relationship relation.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            "Data types and transformation",
            "Equal-width bins on [0,100] of width 20. The number of bins is",
            5,
            "100/20=5.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            "Warehousing and OLAP",
            "A snapshot fact InventoryFact(date_id, sku_id, on_hand) at grain 'sku at end of day'. Summing on_hand over a month of dates for one sku is",
            "usually meaningless as a total (semi-additive); use last-day or average",
            "the true number of items manufactured that month",
            "a drill-down",
            "a lossless join",
            "A",
            "on_hand is a level, not a flow; summing over time double-counts stock.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        msq(
            "Files and indexing",
            "Height of a B+ tree (root at level 0) of n keys and minimum leaf fill of d keys, internal min fanout d, is",
            "O(log_d n)",
            "O(n) in the worst balanced case still, because B+ trees are balanced",
            "Theta(log_d n) because the tree is kept balanced",
            "Theta(n) because leaves are linked",
            "A;C",
            "Balance makes height logarithmic. Leaf links do not make height linear. B is self-contradictory.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            "SQL",
            "HAVING versus WHERE: HAVING",
            "filters groups after GROUP BY (and may use aggregates)",
            "always filters rows before grouping and cannot use COUNT(*)",
            "is a synonym of WHERE",
            "is only for ORDER BY",
            "A",
            "WHERE is pre-aggregation; HAVING is post-aggregation.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        nat(
            "Relational model and FDs",
            "A cover F has 4 FDs. A canonical cover of a chain A->B, B->C, C->D, A->D may drop A->D as redundant. The size of a minimal cover (number of FDs) is",
            3,
            "A->D follows by transitivity from the chain.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "Integrity constraints",
            "A composite foreign key (sid,cid) REFERENCES Enroll(sid,cid) requires that",
            "the pair matches some Enroll pair; matching sid and cid from different Enroll rows is not enough",
            "each component separately exists, even if the pair does not",
            "only sid exists",
            "the child table has no PK",
            "A",
            "FK matching is tuple-wise on the whole key.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        mcq(
            "ER model",
            "A disjoint total specialisation of Account into Savings and Checking, using subclass tables only (no Account table), is awkward because",
            "a query over all accounts must UNION the subclasses, and shared attributes are duplicated",
            "FKs cannot reference accounts",
            "1NF fails",
            "OLAP drill-down fails",
            "A",
            "The 'subclasses only' mapping duplicates the superclass attributes and complicates unified queries.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        nat(
            "SQL",
            "SELECT SUM(x) FROM (VALUES (1),(NULL),(3)) t(x) returns",
            4,
            "SUM skips NULL: 1+3=4.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            "Data types and transformation",
            "A DATE versus TIMESTAMP column: TIMESTAMP additionally stores",
            "a time-of-day (and possibly a time zone, depending on the type)",
            "only a year",
            "a B+ tree",
            "a cube measure",
            "A",
            "DATE is calendar day; TIMESTAMP is date+time.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        msq(
            "Relational algebra and tuple calculus",
            "Pushing selections. Which are valid for improving an RA plan?",
            "sigma_P(R ⋈ S) = sigma_P(R) ⋈ S if P mentions only R-attributes",
            "sigma_{P and Q}(R) = sigma_P(sigma_Q(R))",
            "sigma_P(R ∪ S) = sigma_P(R) ∪ sigma_P(S)",
            "sigma_P(R × S) cannot ever be pushed",
            "A;B;C",
            "Selections do push into products: sigma on R-only attributes of a product goes to R.",
            marks=2,
            diff="M",
        )
    )
    o.append(
        mcq(
            "Warehousing and OLAP",
            "An aggregate navigation / summary table (Product, Month, SUM(qty)) is a",
            "materialised roll-up of the base fact",
            "snowflake of StoreDim",
            "B+ internal node",
            "CHECK constraint",
            "A",
            "Warehouse performance uses pre-aggregated fact tables.",
            marks=1,
            diff="M",
        )
    )
    o.append(
        nat(
            "Files and indexing",
            "A dense index on a file of 5000 records has 5000 entries, 50 entries per index block. Number of first-level index blocks is",
            100,
            "5000/50=100.",
            marks=1,
            diff="E",
        )
    )
    o.append(
        mcq(
            "SQL",
            "Correlated subquery: SELECT * FROM R WHERE R.a > (SELECT AVG(S.b) FROM S WHERE S.k=R.k). The inner query is executed",
            "once per candidate R-row (conceptually)",
            "exactly once, always",
            "never",
            "only at COMMIT",
            "A",
            "Correlation binds S.k to the outer R.k.",
            marks=1,
            diff="M",
        )
    )
    return o


def items():
    o = []
    o.extend(_er())
    o.extend(_rel_fd())
    o.extend(_ra_trc())
    o.extend(_sql_items())
    o.extend(_integrity())
    o.extend(_files_index())
    o.extend(_transform())
    o.extend(_warehouse())
    o.extend(_more_db())
    return uniq(o)
