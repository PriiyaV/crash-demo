import os

def load_configuration():
    required_env_var = "GOOGLE_APPLICATION_CREDENTIALS"
    credentials_path = os.getenv(required_env_var)
    
    if not credentials_path:
        raise EnvironmentError(f"Missing required environment variable {required_env_var}")
    
    if not credentials_path.endswith(".json"):
        raise ValueError("Invalid API key format in configuration")

    print("Configuration loaded successfully.")

def main():
    try:
        load_configuration()
    except (EnvironmentError, ValueError) as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()
