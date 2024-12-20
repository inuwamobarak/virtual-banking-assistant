import json
from foundation import ask_llm
import functions as bf

if __name__ == "__main__":
    print("Welcome to Virtual Banking Assistant!\n")
    print("Select an action:")
    print("1. Check Balance")
    print("2. Transfer Funds")
    print("3. Pay a Bill")
    print("4. View Account History")
    print("5. Chat with AI Agent")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        account_number = input("Enter your account number: ")
        response = ask_llm(
            question="Check my account balance.",
            functions=[bf.balance_inquiry],
            tool_choice="check_balance"
        )
        print("AI Response:", json.dumps(response['choices'][0]['message']['tool_calls'], indent=2))

    elif choice == "2":
        from_account = input("Enter sender account number: ")
        to_account = input("Enter recipient account number: ")
        amount = str(input("Enter amount to transfer: "))
        response = ask_llm(
            question=f"Transfer {amount} from {from_account} to {to_account}.",
            functions=[bf.fund_transfer],
            tool_choice="transfer_funds"
        )
        print("AI Response:", json.dumps(response['choices'][0]['message']['tool_calls'], indent=2))

    elif choice == "3":
        account_number = input("Enter your account number: ")
        bill_type = input("Enter bill type (e.g., electricity, water, internet): ")
        amount = input("Enter bill amount: ")
        response = ask_llm(
            question=f"Pay {bill_type} bill of {amount} for account {account_number}.",
            functions=[bf.bill_payment],
            tool_choice="pay_bill"
        )
        print("AI Response:", json.dumps(response['choices'][0]['message']['tool_calls'], indent=2))

    elif choice == "4":
        account_number = input("Enter your account number: ")
        num_transactions = input("Enter number of recent transactions to view: ")
        response = ask_llm(
            question=f"Show my last {num_transactions} transactions for account {account_number}.",
            functions=[bf.account_history],
            tool_choice="get_account_history"
        )
        print("AI Response:", json.dumps(response['choices'][0]['message']['tool_calls'], indent=2))

    elif choice == "5":
        topic = input("I am happy that you want to talk to me. What topic or questions do you have?: ")
        response = ask_llm(
            question=f"The user has selected the option to talk to you. As an AI agent working in a bank, "
                     f"please respond to their query and try to discus around banking and remain professional."
                     f"User query: {topic}",
            functions=None,
            tool_choice=None
        )
        print("AI Response:", json.dumps(response['choices'][0]['message']['content'], indent=2))

    else:
        response = ask_llm(
            question=f"The user has entered an invalid response. Invalid choice.",
            functions=None,
            tool_choice=None
        )
        print("AI Response:", json.dumps(response['choices'][0]['message']['content'], indent=2))
