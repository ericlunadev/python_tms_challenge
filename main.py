
# Mock Data
loads = [
    {'load_id': 1, 'carrier_id': None, 'status': 'pending', 'pickup_date': '2024-10-01', 'delivery_date': '2024-10-02'},
    {'load_id': 2, 'carrier_id': None, 'status': 'pending', 'pickup_date': '2024-10-03', 'delivery_date': '2024-10-04'},
    {'load_id': 3, 'carrier_id': None, 'status': 'pending', 'pickup_date': '2024-09-25', 'delivery_date': '2024-09-26'},
    {'load_id': 4, 'carrier_id': 1, 'status': 'assigned', 'pickup_date': '2024-09-28', 'delivery_date': '2024-09-30'},
    {'load_id': 5, 'carrier_id': 2, 'status': 'confirmed', 'pickup_date': '2024-10-10', 'delivery_date': '2024-10-12'},
    {'load_id': 6, 'carrier_id': None, 'status': 'pending', 'pickup_date': '2024-10-08', 'delivery_date': '2024-10-09'},
    {'load_id': 7, 'carrier_id': 3, 'status': 'assigned', 'pickup_date': '2024-09-29', 'delivery_date': '2024-10-01'},
    {'load_id': 8, 'carrier_id': None, 'status': 'pending', 'pickup_date': '2024-09-27', 'delivery_date': '2024-09-28'},
]

carriers = [
    {'carrier_id': 1, 'email': 'carrier1@example.com'},
    {'carrier_id': 2, 'email': 'carrier2@example.com'},
    {'carrier_id': 3, 'email': 'carrier3@example.com'},
    {'carrier_id': 4, 'email': 'carrier4@example.com'},
    {'carrier_id': 5, 'email': 'carrier5@example.com'},
]

def send_email(carrier_email, load_details):
    pass

# Function to Assign Loads to Carriers
def assign_loads(loads, carriers):
    for load in loads:
        if load['status'] == 'pending':
            # Assign load to the first available carrier (simple rule)
            carrier = carriers[0]

            load['carrier_id'] = carrier['carrier_id']
            load['status'] = 'assigned'

            print(f"Assigned load {load['load_id']} to carrier {carrier['carrier_id']}")

            # Send confirmation email
            email_success = send_email(carrier['email'], load)

            if email_success:
                load['status'] = 'confirmed'
            else:
                print(f"Failed to confirm load {load['load_id']}, keeping it as 'assigned'.")

# Main Execution
if __name__ == "__main__":
    print("Starting Load Assignment Process...\n")
    assign_loads(loads, carriers)
    print("\nLoad Assignment Process Complete.")
    print("Final Loads Status:", loads)
