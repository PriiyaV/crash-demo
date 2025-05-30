import time
import random

def call_api():
    # Simulate rate limit being exceeded
    raise Exception("OpenAI API rate limit reached (100 requests/min)")

def main():
    try:
        call_api()
    except Exception as e:
        print(f"ERROR: {e}")
        print("Retrying in 120 seconds...")
        time.sleep(2)  # Use 120 in real case

if __name__ == "__main__":
    main()
