# explanation_engine.py

def generate_explanation(vulnerability):

    explanations = {

        "SQL Injection": {
            "type": "SQL Injection",
            "attack": "Attacker injects malicious SQL into query.",
            "impact": "Database manipulation, data theft, authentication bypass.",
            "fix": "Use parameterized queries (prepared statements).",
            "secure_pattern": "cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))"
        },

        "Cross-Site Scripting (XSS)": {
            "type": "XSS",
            "attack": "Attacker injects JavaScript into web page.",
            "impact": "Session hijacking, data theft.",
            "fix": "Escape or encode output before rendering.",
            "secure_pattern": "Use template auto-escaping."
        },

        "Command Injection": {
            "type": "Command Injection",
            "attack": "Attacker executes OS commands.",
            "impact": "Full server compromise.",
            "fix": "Avoid passing user input to system commands.",
            "secure_pattern": "Use safe libraries instead of shell."
        },

        "Hardcoded Secret": {
            "type": "Hardcoded Secret",
            "attack": "Attacker extracts credentials from code.",
            "impact": "Account takeover.",
            "fix": "Store secrets in environment variables.",
            "secure_pattern": "os.getenv('API_KEY')"
        }
    }

    return explanations.get(vulnerability)
