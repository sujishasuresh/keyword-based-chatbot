import time

data = {
    # Greetings
    "hey": "Hey there!",
    "hi": "Hello! How can I help you?",
    "hello": "Hello! I'm your HCM Assistant.",
    "good morning": "Good morning! How can I assist you?",
    "good afternoon": "Good afternoon! How can I assist you?",
    "good evening": "Good evening! How can I assist you?",

    # About the chatbot
    "who are you": "I'm HCM Assistant, a rule-based chatbot designed to help with HR-related queries.",
    "what can you do": "I can help you with common HR queries such as leave, attendance, payroll, policies, and employee information.",
    "help": "You can ask me about leave, attendance, payroll, holidays, working hours, HR policies, or employee benefits.",

    # Leave
    "leave": "I can help you with leave-related information. You can ask about leave balance, leave policy, or how to apply for leave.",
    "leave balance": "Please check your employee portal to view your current leave balance.",
    "how to apply for leave": "You can apply for leave through the employee portal by selecting the appropriate leave type and submitting your request.",
    "leave policy": "Please refer to the company's official leave policy for details about eligibility, leave types, and approval procedures.",
    "sick leave": "Sick leave is available to eligible employees according to the company's leave policy.",
    "casual leave": "Casual leave can be taken according to the company's leave policy and approval process.",

    # Attendance
    "attendance": "You can check your attendance records through the employee portal.",
    "attendance policy": "Please refer to the company's attendance policy for details about working hours, late attendance, and regularization.",
    "working hours": "Working hours are based on the company's official work schedule.",
    "late attendance": "If you arrive late, please follow the company's attendance regularization procedure.",

    # Payroll
    "salary": "You can view your salary details through the employee portal or contact the HR department.",
    "payroll": "Payroll information is available through the employee portal.",
    "salary slip": "You can download your salary slip from the employee portal.",
    "payslip": "You can download your payslip from the employee portal.",
    "salary date": "Salary is processed according to the company's payroll schedule.",

    # Holidays
    "holiday": "You can check the company's holiday calendar for upcoming holidays.",
    "holidays": "The complete holiday list is available in the employee portal.",
    "next holiday": "Please check the latest company holiday calendar for the next scheduled holiday.",

    # Benefits
    "benefits": "Employee benefits may include insurance, leave benefits, and other company-provided benefits. Please contact HR for details.",
    "health insurance": "Please contact HR or check the employee benefits portal for health insurance information.",
    "insurance": "Insurance-related information is available through HR or the employee benefits portal.",

    # HR
    "hr": "You can contact the HR department for assistance with employee-related matters.",
    "hr contact": "Please refer to the company directory or employee portal for HR contact information.",
    "hr department": "The HR department handles employee-related matters including leave, attendance, payroll, and policies.",

    # Policies
    "company policy": "Company policies are available through the employee portal or HR department.",
    "hr policy": "Please refer to the company's HR policy documents for detailed information.",
    "work from home": "Work-from-home eligibility depends on company policy and the employee's role.",

    # Goodbye
    "bye": "See you next time!",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "thank you": "You're welcome! I'm happy to help."
}


print("-- HCM Assistant --")
while True:
    user_input=input("Enter the query: ").strip().lower()
    if user_input in data:
        if user_input in ['bye','goodbye','thanks','thank you']:
            print(data[user_input])
            break
        else:
            if user_input not in ['hi','hey','hello','good morning','good afternoon','good evening']:
                print("Thinking...")
                time.sleep(3)
                print(data[user_input])
            else:
                print(data[user_input])
    else:
        print("Sorry, I didn't get that")
