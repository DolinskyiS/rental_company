from src.model.residency import transaction_history

def identify_late_payments():
    all_late_payments = []
    for payment in transaction_history.transactions:
        if payment.is_late():
            all_late_payments.append(payment.payment_id)

    print(f"All Late Payments: {all_late_payments}")


def calculate_total_revenue():
    total_revenue = 0
    for payment in transaction_history.transactions:
        total_revenue += payment.amount

    print(f"Total Revenue: {total_revenue}")



if __name__ == "__main__":
    identify_late_payments()
    calculate_total_revenue()