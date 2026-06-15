def main():
    scores = [55, 75, 87, 82, 91]
    students = ["alice", "bob", "jerry", "jane", "bill"]
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")
    # create a dictionary of names and scores
    student_scores = {
    "alice": 55,
    "bob": 75,
    "jerry": 82,
    "jane": 82,
    "bill": 91
    }
    print(f"\nPrint bob and janes scores\n------------")
    print(student_scores["bob"])
    print(student_scores["jane"])
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")


main()