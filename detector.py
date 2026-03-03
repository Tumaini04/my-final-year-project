# detector.py

"""
This file is responsible for detecting vulnerabilities
in student-submitted code.

It uses simple rule-based pattern matching (regex and keyword checks).
Later, this can be upgraded to hybrid detection using an LLM.
"""

import re  # Regular expressions module for pattern matching


def detect_vulnerability(code):
    """
    This function takes a string of source code as input
    and returns the detected vulnerability type.
    
    If no vulnerability is found, it returns None.
    """

    # -----------------------------
    # 1️⃣ SQL Injection Detection
    # -----------------------------
    # Detects dynamic SQL query concatenation
    # Example vulnerable pattern:
    # query = "SELECT * FROM users WHERE id=" + user_input

    sql_pattern = r"SELECT\s+.*\+.*"

    if re.search(sql_pattern, code, re.IGNORECASE):
        return "SQL Injection"

    # -----------------------------
    # 2️⃣ Cross-Site Scripting (XSS)
    # -----------------------------
    # Detects raw <script> tag usage
    # Example:
    # return "<script>alert('Hacked')</script>"

    if "<script>" in code.lower():
        return "Cross-Site Scripting (XSS)"

    # -----------------------------
    # 3️⃣ Command Injection
    # -----------------------------
    # Detects dangerous OS command execution
    # Example:
    # os.system(user_input)

    if "os.system" in code or "subprocess" in code:
        return "Command Injection"

    # -----------------------------
    # 4️⃣ Hardcoded Secret
    # -----------------------------
    # Detects hardcoded passwords or API keys
    # Example:
    # password = "admin123"

    secret_pattern = r"(password|api_key)\s*=\s*['\"]"

    if re.search(secret_pattern, code, re.IGNORECASE):
        return "Hardcoded Secret"

    # -----------------------------
    # If nothing matched
    # -----------------------------
    return None
