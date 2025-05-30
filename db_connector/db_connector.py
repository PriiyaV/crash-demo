import time

def connect_to_cloud_sql():
    print("Connecting to Cloud SQL...")
    time.sleep(2)
    raise TimeoutError("Connection to Cloud SQL instance timed out after 30 seconds")

def main():
    try:
        connect_to_cloud_sql()
    except TimeoutError as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()
