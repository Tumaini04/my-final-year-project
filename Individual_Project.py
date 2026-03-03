from detector import detect_vulnerability
from socratic_engine import generate_socratic_questions
from explanation_engine import generate_explanation
from validator import validate_fix
from session_manager import SessionManager


def run_chatbot():

    session = SessionManager()

    print("\n🔐 AI Socratic Vulnerability Tutor (Final Year Version)\n")

    student_code = input("Submit your code:\n")

    vuln = detect_vulnerability(student_code)

    if not vuln:
        print("No obvious vulnerability detected.")
        return

    session.set_vulnerability(vuln)

    print(f"\n⚠ Detected: {vuln}")
    print("\nEntering Socratic Mode...\n")

    questions = generate_socratic_questions(vuln)

    for q in questions:
        input(f"{q}\n(Press Enter to continue)\n")

    while True:

        proposed_fix = input("\nPropose your fixed code:\n")
        session.increment_attempt()

        if validate_fix(vuln, proposed_fix):
            print("\n✅ Correct Fix!")
            session.mark_correct()
            break

        else:
            print("\n❌ Incorrect. Explanation Mode:\n")
            explanation = generate_explanation(vuln)

            if explanation:
                print("Type:", explanation["type"])
                print("Attack:", explanation["attack"])
                print("Impact:", explanation["impact"])
                print("Fix:", explanation["fix"])
                print("Secure Pattern:", explanation["secure_pattern"])

            retry = input("\nTry again? (yes/no): ")
            if retry.lower() != "yes":
                break

    session.end_session()
    print("\nSession logged successfully.\n")


if __name__ == "__main__":
    run_chatbot()





