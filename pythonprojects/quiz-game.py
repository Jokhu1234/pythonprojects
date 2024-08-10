questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language if primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portugese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    
    {
        "prompt": "Who wrote 'To Kill a Mockingbird?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemmingway"],
        "answer": "A"
    },
    
    {   
        "prompt": "What Country has won the most World Cups?",
        "options": ["A. Argentina", "B. Portugal", "C. Brazil", "D. England"],
        "answer": "C"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct, hooray!" "\n")
            score += 1
        else:
            print("Sorry that was incorrect. The correct answer was", question["answer"], "\n")
            
        print(f"Your score is {score} out of {len(questions)} questions correct. Great Job!!" "\n")
        
            
            
run_quiz(questions)