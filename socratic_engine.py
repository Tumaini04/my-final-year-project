# socratic_engine.py

"""
Interactive Socratic Engine
This module asks structured questions,
checks answers, and provides feedback.
"""

def run_socratic_session(vulnerability):

    # Question bank with expected keywords and explanations
    question_bank = {

        "SQL Injection": [
            {
                "question": "How is this SQL query constructed?",
                "keywords": ["concatenate", "+", "string", "dynamic"],
                "explanation": "The query is dynamically constructed using string concatenation. This allows user input to modify SQL structure."
            },
            {
                "question": "Is user input treated as code or data?",
                "keywords": ["code", "interpreted", "sql"],
                "explanation": "User input is treated as SQL code instead of data, which allows injection."
            },
            {
                "question": "What would OR '1'='1' do here?",
                "keywords": ["true", "bypass", "always"],
                "explanation": "OR '1'='1' makes the condition always true, allowing authentication bypass."
            }
        ],

        "Cross-Site Scripting (XSS)": [
            {
                "question": "Where is user input rendered?",
                "keywords": ["browser", "html", "output"],
                "explanation": "User input is rendered in the browser without sanitization."
            },
            {
                "question": "What happens if <script> is injected?",
                "keywords": ["javascript", "execute", "run"],
                "explanation": "The browser executes injected JavaScript, leading to session hijacking or data theft."
            }
        ],

        "Command Injection": [
            {
                "question": "Is user input passed to the OS?",
                "keywords": ["os", "system", "shell"],
                "explanation": "User input is passed directly into system commands, allowing command execution."
            }
        ],

        "Hardcoded Secret": [
            {
                "question": "Why is storing secrets in source code dangerous?",
                "keywords": ["exposed", "repository", "leak"],
                "explanation": "Secrets in source code can be exposed in repositories or version control history."
            }
        ]
    }

    questions = question_bank.get(vulnerability, [])

    for item in questions:

        while True:
            answer = input(f"\n{item['question']}\nYour answer: ").lower()

            # Check if any expected keyword appears in answer
            if any(keyword in answer for keyword in item["keywords"]):
                print("✅ Correct. Moving to next question.")
                break
            else:
                print("❌ Not quite.")
                print("Explanation:", item["explanation"])
                retry = input("Try again? (yes/no): ")
                if retry.lower() != "yes":
                    break
