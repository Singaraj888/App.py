"""Menu-driven cyber-safety learning utility.

This is a standalone educational CLI app. It is not the unavailable original
internship App.py file; its purpose is documented in the repository README.
"""
import re
from urllib.parse import urlparse


def password_feedback(password: str) -> str:
    checks = {
        "at least 8 characters": len(password) >= 8,
        "uppercase letter": bool(re.search(r"[A-Z]", password)),
        "lowercase letter": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"\d", password)),
        "special character": bool(re.search(r"[^A-Za-z0-9]", password)),
    }
    score = sum(checks.values())
    labels = ["Very weak", "Weak", "Fair", "Good", "Strong", "Very strong"]
    lines = [f"Estimated strength: {labels[score]} ({score}/5 checks passed)"]
    lines.extend(f"[{'OK' if passed else '  '}] {name}" for name, passed in checks.items())
    if score < 5:
        lines.append("Tip: " + "; ".join(name for name, passed in checks.items() if not passed))
    lines.append("This estimate does not guarantee password security.")
    return "\n".join(lines)


def inspect_url(url: str) -> str:
    candidate = url if "://" in url else "https://" + url
    parsed = urlparse(candidate)
    if not parsed.hostname:
        return "The text does not appear to contain a valid hostname."
    warnings = []
    if parsed.scheme != "https":
        warnings.append("The link does not use HTTPS.")
    if parsed.username or parsed.password:
        warnings.append("The URL contains user-info before the hostname; inspect it carefully.")
    if parsed.hostname.replace(".", "").isdigit():
        warnings.append("The host looks like an IP address rather than a familiar domain.")
    if not warnings:
        warnings.append("No simple warning was detected. This does not prove the link is safe.")
    return f"Host: {parsed.hostname}\n" + "\n".join(f"- {item}" for item in warnings)


def main() -> None:
    while True:
        print("\n=== Cyber Safety Learning Utility ===")
        print("1. Check password characteristics")
        print("2. Inspect a URL (basic checks)")
        print("3. Cyber-safety tips")
        print("0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            print(password_feedback(input("Enter a SAMPLE password (not a real one): ")))
        elif choice == "2":
            print(inspect_url(input("Enter a URL to inspect: ").strip()))
        elif choice == "3":
            print("- Use unique passwords and a password manager.")
            print("- Enable multi-factor authentication.")
            print("- Verify unexpected links using the official website.")
            print("- Never share OTPs, passwords, or recovery codes.")
            print("- Keep software and devices updated.")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Please choose a listed option.")


if __name__ == "__main__":
    main()
