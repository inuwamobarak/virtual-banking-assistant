balance_inquiry = {
    "type": "function",
    "function": {
        "name": "check_balance",
        "description": "Check the balance of a user's account",
        "parameters": {
            "type": "object",
            "properties": {
                "account_number": {
                    "type": "string",
                    "description": "The user's bank account number",
                }
            },
            "required": ["account_number"],
        },
    },
}

fund_transfer = {
    "type": "function",
    "function": {
        "name": "transfer_funds",
        "description": "Transfer funds from one account to another",
        "parameters": {
            "type": "object",
            "properties": {
                "from_account": {
                    "type": "string",
                    "description": "The sender's account number",
                },
                "to_account": {
                    "type": "string",
                    "description": "The recipient's account number",
                },
                "amount": {
                    "type": "number",
                    "description": "The amount to transfer",
                }
            },
            "required": ["from_account", "to_account", "amount"],
        },
    },
}

bill_payment = {
    "type": "function",
    "function": {
        "name": "pay_bill",
        "description": "Pay a utility bill from the user's account",
        "parameters": {
            "type": "object",
            "properties": {
                "account_number": {
                    "type": "string",
                    "description": "The user's bank account number",
                },
                "bill_type": {
                    "type": "string",
                    "description": "The type of bill to pay (e.g., electricity, water, internet)",
                },
                "amount": {
                    "type": "number",
                    "description": "The bill amount to pay",
                }
            },
            "required": ["account_number", "bill_type", "amount"],
        },
    },
}

account_history = {
    "type": "function",
    "function": {
        "name": "get_account_history",
        "description": "Retrieve the transaction history of a user's account",
        "parameters": {
            "type": "object",
            "properties": {
                "account_number": {
                    "type": "string",
                    "description": "The user's bank account number",
                },
                "num_transactions": {
                    "type": "integer",
                    "description": "The number of recent transactions to retrieve",
                }
            },
            "required": ["account_number", "num_transactions"],
        },
    },
}