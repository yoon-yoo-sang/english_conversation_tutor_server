functions = [
    {
        "type": "function",
        "function": {
            "name": "subscription_recommendation",
            "description": "Recommend a subscription plan based on the user's usage."
                           "Call this function when the user wants to subscribe to a subscription plan.",
            "parameters": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "The message that the user sent to the chatbot."
                                       "```Plan List: \n"
                                        "1. Basic Plan\n"
                                        "2. Premium Plan\n"
                                        "3. Pro Plan```",
                    },
                },
                "required": ["message"],
            },
        },
    }
]
