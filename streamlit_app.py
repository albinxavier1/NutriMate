import streamlit as st
from groq import Groq

def get_response(prompt):
    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content

def main():
    st.title("Nutrition Bot")

    prompt = st.text_input("You:", "")


    context_prompt = f"Act as an nutirionist and prepare strategies , diet plans and basic home excercise as per user input . The diet plan should have accurate nutrient values. the user input is as follows {prompt}"

    if st.button("Send"):
        response = get_response(context_prompt)
        st.write(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
