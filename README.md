## Context:

In the Transportation Management System (TMS) industry, assigning loads to carriers and confirming their acceptance is a common task. This challenge simulates the process of automating load assignments and sending email confirmations to carriers.

## Objective:

Create a Python program that automates the assignment of pending loads to available carriers and sends confirmation emails. Your program will update the status of the loads based on the success or failure of the email confirmation.

## Instructions:
 
1.	Load Data:
 
- You are given two arrays, loads and carriers, which represent the current loads and available carriers, respectively.
- Loads: Each load has an ID, a status (pending, assigned, or confirmed), a pickup date, and a delivery date.
- Carriers: Each carrier has an ID and an email address.
3.	Task Requirements:
- Implement a function to assign pending loads to carriers. Start by assigning loads with the earliest pickup_date.
- Once a load is assigned to a carrier, update the load’s carrier_id and set its status to assigned.
-	Email Confirmation:
-	Implement a function to send a confirmation email to the carrier with the details of the assigned load (load ID, pickup date, and delivery date).
-	If the email is successfully sent, update the load’s status to confirmed. If the email fails to send, keep the status as assigned.

## Expected Outcome:
By the end of the challenge, you should have a working Python program that correctly assigns loads to carriers, sends confirmation emails, and updates the load statuses. Your code should be clean, modular, and easy to understand.
