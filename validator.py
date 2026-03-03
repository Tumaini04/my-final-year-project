# validator.py

def validate_fix(vulnerability, code):

    if vulnerability == "SQL Injection":
        return "execute(" in code and "?" in code

    if vulnerability == "Cross-Site Scripting (XSS)":
        return "escape" in code or "encode" in code

    if vulnerability == "Command Injection":
        return "os.system" not in code

    if vulnerability == "Hardcoded Secret":
        return "os.getenv" in code

    return False