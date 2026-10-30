def calculate_grade(marks):
    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    elif marks >= 40:
        return "Pass"
    else:
        return "Fail"

if __name__ == "__main__":
    score = 80
    print(f"Marks: {score}, Grade: {calculate_grade(score)}")