import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# 1. Load the .env file
load_dotenv()

def test_connection():
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not found in environment!")
        return

    print(f"Checking connection with API Key: {api_key[:8]}...****")

    try:
        # 2. Initialize the LLM
        llm = ChatOpenAI(model="gpt-4o-mini", timeout=10) # Using mini for a fast/cheap test
        
        print("📡 Sending request to OpenAI...")
        
        # 3. Simple text-only request
        response = llm.invoke([HumanMessage(content="Say 'OpenAI is working!'")])
        
        print(f"✅ SUCCESS: {response.content}")

    except Exception as e:
        import traceback
        print(f"❌ FAILED to connect to OpenAI.")
        print("-" * 60)
        traceback.print_exc() # This will show the exact line and file causing the error
        print("-" * 60)
        print(f"Error Details: {str(e)}")

if __name__ == "__main__":
    test_connection()