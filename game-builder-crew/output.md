```python
import streamlit as st
from openai.embeddingsapi import EmbeddingsAPI

# Initialize caching mechanism
@st.cache(ttl=60)
def get_api_response(query):
    try:
        api = EmbeddingsAPI("YOUR_API_KEY_HERE")
        response = api.create_embeddings(input=query)
        return response['choices'][0]['message']
    except Exception as e:
        raise Exception(f"Error: {str(e)}")

def handle_input():
    user_query = st.text_input("Enter your query")
    if user_query:
        try:
            response = get_api_response(user_query)
            st.write(response)
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

def main():
    handle_input()
```

In this code, I've incorporated the OpenAI API key, added a caching mechanism using Streamlit's built-in caching functionality, and handled potential errors during API connections.