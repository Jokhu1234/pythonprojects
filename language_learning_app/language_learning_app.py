import random

words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "from"},
    {"spanish": "que", "english": "that"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to"},
    {"spanish": "en", "english": "in"},
    {"spanish": "un", "english": "a"},
    {"spanish": "ser", "english": "be"},
    {"spanish": "se", "english": "he"},
    {"spanish": "no", "english": "no"},
    {"spanish": "haber", "english": "have"},
    {"spanish": "por", "english": "by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his"},
    {"spanish": "para", "english": "for"},
    {"spanish": "como", "english": "as"},
    {"spanish": "estar", "english": "be"},
    {"spanish": "tener", "english": "have"},
    {"spanish": "le", "english": "you"},
    {"spanish": "lo", "english": "it"},
]

def quiz_user(words):
    random.shuffle(words)
    score = 0
    
    for word in words:
        print(f"What is the English translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()
        
        if user_answer == correct_answer:
            print("Correct!!\n!")
            score += 1
            
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")
    
    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press enter to start the quiz...")
    quiz_user(words)
    
if __name__ == "__main__":
    main()