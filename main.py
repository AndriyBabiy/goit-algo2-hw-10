"""
HW10: Class Scheduling Using Greedy Algorithm (100 points)

Problem: Implement a program for scheduling classes at a university using
a greedy algorithm for the Set Cover Problem. Assign teachers to subjects
to minimize the number of teachers while covering all subjects.

Set Cover Problem:
- Universe U = set of subjects to cover
- Collection S = subsets (subjects each teacher can teach)
- Goal: Find minimum number of subsets that cover all elements

The greedy algorithm provides O(log n) approximation:
1. While uncovered subjects exist:
   a. Choose teacher covering most uncovered subjects
   b. If tie, choose youngest teacher
   c. Assign covered subjects to that teacher
   d. Remove covered subjects from uncovered set

Given Data:
- Subjects: {Mathematics, Physics, Chemistry, Computer Science, Biology}
- Teachers: 6 teachers with varying subject capabilities (see below)

Acceptance Criteria:
- Program covers all subjects from the subject set (40 pts)
- If impossible to cover all subjects, displays appropriate message (30 pts)
- All subjects covered by teachers, all teachers assigned correctly (30 pts)
"""

from typing import List, Set, Optional


class Teacher:
    """
    Represents a teacher with personal info and teaching capabilities.

    Attributes:
        first_name: Teacher's first name
        last_name: Teacher's last name
        age: Teacher's age in years
        email: Teacher's email address
        can_teach_subjects: Set of subjects the teacher can teach
        assigned_subjects: Set of subjects assigned during scheduling
    """

    def __init__(self, first_name: str, last_name: str, age: int,
                 email: str, can_teach_subjects: Set[str]):
        """
        Initialize a Teacher instance.

        Args:
            first_name: Teacher's first name
            last_name: Teacher's last name
            age: Teacher's age in years
            email: Teacher's email address
            can_teach_subjects: Set of subjects the teacher can teach

        Example:
            teacher = Teacher(
                "Oleksandr", "Ivanenko", 45,
                "o.ivanenko@example.com",
                {"Mathematics", "Physics"}
            )
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        # Will be populated during scheduling
        self.assigned_subjects = set()

    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"Teacher({self.first_name} {self.last_name}, age={self.age})"

    @property
    def full_name(self) -> str:
        """Return full name of teacher."""
        return f"{self.first_name} {self.last_name}"


def create_schedule(subjects: Set[str], teachers: List[Teacher]) -> Optional[List[Teacher]]:
    """
    Create a class schedule using greedy set cover algorithm.

    Selects teachers to cover all subjects while minimizing the number
    of teachers used. At each step, chooses the teacher who can cover
    the most uncovered subjects. Ties are broken by selecting the
    youngest teacher.

    Args:
        subjects: Set of subjects that need to be covered
        teachers: List of available Teacher objects

    Returns:
        List of selected teachers with assigned_subjects populated,
        or None if impossible to cover all subjects

    Algorithm (Greedy Set Cover):
        1. uncovered = copy of subjects
        2. selected = empty list
        3. While uncovered is not empty:
           a. For each available teacher:
              - Calculate coverage = can_teach & uncovered
           b. Select teacher with:
              - Maximum |coverage|
              - If tie: youngest age
           c. If no teacher can cover anything: return None
           d. Assign coverage to selected teacher
           e. Add teacher to selected list
           f. Remove coverage from uncovered
           g. Remove teacher from available teachers
        4. Return selected teachers

    Complexity:
        Time: O(n * m) where n = |subjects|, m = |teachers|
        Space: O(n + m)
    """
    uncovered = subjects.copy()
    selected_teachers = []
    available_teachers = list(teachers)

    while uncovered:
        best_teacher = None
        best_coverage = set()

        for teacher in available_teachers:
            # Calculate how many uncovered subjects this teacher covers
            coverage = teacher.can_teach_subjects & uncovered

            # Compare with best so far
            if len(coverage) > len(best_coverage):
                best_teacher = teacher
                best_coverage = coverage
            elif len(coverage) == len(best_coverage) and len(coverage) > 0:
                # Tie-breaker: choose younger teacher
                if best_teacher is None or teacher.age < best_teacher.age:
                    best_teacher = teacher
                    best_coverage = coverage

        # Check if any teacher can cover remaining subjects
        if best_teacher is None or len(best_coverage) == 0:
            return None  # Impossible to cover all subjects

        # Assign subjects to teacher
        best_teacher.assigned_subjects = best_coverage

        # Add to selected list
        selected_teachers.append(best_teacher)

        # Remove covered subjects from uncovered
        uncovered -= best_coverage

        # Remove selected teacher from available
        available_teachers.remove(best_teacher)

    return selected_teachers


def create_teachers() -> List[Teacher]:
    """
    Create the list of teachers with their subjects from assignment.

    Returns:
        List of 6 Teacher objects as specified in assignment

    Teacher data from assignment:
    | # | Name                | Age | Email                      | Can Teach                  |
    |---|---------------------|-----|----------------------------|----------------------------|
    | 1 | Oleksandr Ivanenko  | 45  | o.ivanenko@example.com     | Mathematics, Physics       |
    | 2 | Maria Petrenko      | 38  | m.petrenko@example.com     | Chemistry                  |
    | 3 | Serhiy Kovalenko    | 50  | s.kovalenko@example.com    | Computer Science, Math     |
    | 4 | Natalia Shevchenko  | 29  | n.shevchenko@example.com   | Biology, Chemistry         |
    | 5 | Dmytro Bondarenko   | 35  | d.bondarenko@example.com   | Physics, Computer Science  |
    | 6 | Olena Hrytsenko     | 42  | o.hrytsenko@example.com    | Biology, Computer Science  |
    """
    teachers = [
        # TODO: Create Teacher 1 - Oleksandr Ivanenko
        Teacher(
            "Oleksandr", "Ivanenko", 45,
            "o.ivanenko@example.com",
            {"Mathematics", "Physics"}
        ),

        # TODO: Create Teacher 2 - Maria Petrenko
        Teacher(
            "Maria", "Petrenko", 38,
            "m.petrenko@example.com",
            {"Chemistry"}
        ),

        # TODO: Create Teacher 3 - Serhiy Kovalenko
        Teacher(
            "Serhiy", "Kovalenko", 50,
            "s.kovalenko@example.com",
            {"Computer Science", "Mathematics"}
        ),

        # TODO: Create Teacher 4 - Natalia Shevchenko
        Teacher(
            "Natalia", "Shevchenko", 29,
            "n.shevchenko@example.com",
            {"Biology", "Chemistry"}
        ),

        # TODO: Create Teacher 5 - Dmytro Bondarenko
        Teacher(
            "Dmytro", "Bondarenko", 35,
            "d.bondarenko@example.com",
            {"Physics", "Computer Science"}
        ),

        # TODO: Create Teacher 6 - Olena Hrytsenko
        Teacher(
            "Olena", "Hrytsenko", 42,
            "o.hrytsenko@example.com",
            {"Biology", "Computer Science"}
        ),
    ]
    return teachers


def print_schedule(schedule: Optional[List[Teacher]]) -> None:
    """
    Print the schedule in formatted output.

    Args:
        schedule: List of teachers with assignments, or None if impossible
    """
    if schedule is None:
        print("It is not possible to cover all subjects with available teachers.")
        return

    print("Class schedule:")
    for teacher in schedule:
        print(f"{teacher.first_name} {teacher.last_name}, "
              f"{teacher.age} years, email: {teacher.email}")
        subjects_str = ", ".join(sorted(teacher.assigned_subjects))
        print(f"  Teaches subjects: {subjects_str}\n")


def verify_coverage(subjects: Set[str], schedule: List[Teacher]) -> bool:
    """
    Verify that all subjects are covered by the schedule.

    Args:
        subjects: Set of subjects that should be covered
        schedule: List of teachers with assignments

    Returns:
        True if all subjects are covered, False otherwise
    """
    covered = set()
    for teacher in schedule:
        covered |= teacher.assigned_subjects

    missing = subjects - covered
    if missing:
        print(f"Warning: Missing subjects: {missing}")
        return False

    return True


# ============== MAIN ==============

if __name__ == "__main__":
    print("=" * 60)
    print("HW10: Class Scheduling Using Greedy Algorithm")
    print("=" * 60)

    # Define subjects to cover
    subjects = {"Mathematics", "Physics", "Chemistry", "Computer Science", "Biology"}
    print(f"\nSubjects to cover: {subjects}")

    # Create list of teachers
    teachers = create_teachers()
    print(f"Available teachers: {len(teachers)}")

    if teachers:
        for t in teachers:
            print(f"  - {t.full_name} ({t.age}): {t.can_teach_subjects}")

    # Create schedule using greedy algorithm
    print("\n" + "-" * 60)
    print("Running greedy set cover algorithm...")
    print("-" * 60)

    schedule = create_schedule(subjects, teachers)

    # Output results
    print()
    print_schedule(schedule)

    # Verify coverage
    if schedule:
        print("-" * 60)
        if verify_coverage(subjects, schedule):
            print(f"✓ All {len(subjects)} subjects covered by {len(schedule)} teachers")
        else:
            print("✗ Coverage verification failed")

    # Show expected output
    print("\n" + "=" * 60)
    print("Expected Output:")
    print("=" * 60)
    print("""
Class schedule:
Natalia Shevchenko, 29 years, email: n.shevchenko@example.com
  Teaches subjects: Biology, Chemistry

Dmytro Bondarenko, 35 years, email: d.bondarenko@example.com
  Teaches subjects: Computer Science, Physics

Oleksandr Ivanenko, 45 years, email: o.ivanenko@example.com
  Teaches subjects: Mathematics

Note: Exact output may vary based on tie-breaking (youngest teacher)
and the order teachers are selected.
    """)

    # Algorithm walkthrough
    print("=" * 60)
    print("Algorithm Walkthrough:")
    print("=" * 60)
    print("""
Initial: Uncovered = {Mathematics, Physics, Chemistry, Computer Science, Biology}

Step 1: Find teacher covering most subjects
  - Multiple teachers cover 2 subjects
  - Tie-breaker: Shevchenko (29) is youngest
  - Select: Shevchenko → {Biology, Chemistry}
  - Uncovered: {Mathematics, Physics, Computer Science}

Step 2: Find teacher covering most remaining subjects
  - Multiple teachers cover 2 subjects
  - Tie-breaker: Bondarenko (35) is youngest
  - Select: Bondarenko → {Physics, Computer Science}
  - Uncovered: {Mathematics}

Step 3: Only Mathematics remains
  - Ivanenko or Kovalenko can cover it
  - Tie-breaker: Ivanenko (45) < Kovalenko (50)
  - Select: Ivanenko → {Mathematics}
  - Uncovered: {} (done!)

Result: 3 teachers cover all 5 subjects
    """)
