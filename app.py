import streamlit as st
import matplotlib.pyplot as plt
import datetime

# BudgetTracker class remains the same
class BudgetTracker:
    def __init__(self):
        self.expenses = []
        self.budget_limit = 0

    def set_budget_limit(self, limit):
        self.budget_limit = limit
        st.write(f"Budget limit set to ${self.budget_limit}")

    def add_expense(self, amount, category):
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.expenses.append({'amount': amount, 'category': category, 'date': date})
        st.write(f"Added expense: ${amount} for {category} on {date}")
        self.check_budget()

    def check_budget(self):
        total_expense = sum(expense['amount'] for expense in self.expenses)
        if total_expense > self.budget_limit:
            st.warning("⚠️ You have exceeded your budget limit!")
            self.trigger_alarm()

    def trigger_alarm(self):
        st.error("⚠️ Alarm: Budget Limit Exceeded!")

    def show_expense_summary(self):
        st.subheader("Expense Summary:")
        for expense in self.expenses:
            st.write(f"{expense['date']} - ${expense['amount']} - {expense['category']}")

    def plot_expenses(self):
        categories = [expense['category'] for expense in self.expenses]
        amounts = [expense['amount'] for expense in self.expenses]

        if not amounts:
            st.write("No expenses to plot.")
            return

        plt.figure(figsize=(8, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.title('Expense Analysis by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount Spent ($)')
        plt.xticks(rotation=45, ha='right')
        st.pyplot(plt)


# Streamlit UI to interact with the BudgetTracker
def main():
    st.title("Budget Tracker")

    tracker = BudgetTracker()

    # Set budget limit
    budget_limit = st.number_input("Set your budget limit", min_value=0, value=500)
    tracker.set_budget_limit(budget_limit)

    # Input for adding expenses
    st.subheader("Add an Expense")
    amount = st.number_input("Expense Amount", min_value=0)
    category = st.text_input("Category")
    if st.button("Add Expense"):
        if amount > 0 and category:
            tracker.add_expense(amount, category)
        else:
            st.warning("Please enter a valid amount and category.")

    # Show expense summary
    if st.button("Show Expense Summary"):
        tracker.show_expense_summary()

    # Plot expenses
    if st.button("Plot Expenses"):
        tracker.plot_expenses()


if __name__ == "__main__":
    main()
