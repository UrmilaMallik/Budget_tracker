import matplotlib.pyplot as plt
import datetime
import time

class BudgetTracker:
    def __init__(self):
        self.expenses = []
        self.budget_limit = 0

    def set_budget_limit(self, limit):
        self.budget_limit = limit
        print(f"Budget limit set to {self.budget_limit}")

    def add_expense(self, amount, category):
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.expenses.append({'amount': amount, 'category': category, 'date': date})
        print(f"Added expense: ${amount} for {category} on {date}")
        self.check_budget()

    def check_budget(self):
        total_expense = sum(expense['amount'] for expense in self.expenses)
        if total_expense > self.budget_limit:
            print("\n\u26A0 Warning: You have exceeded your budget limit!\n")
            self.trigger_alarm()

    def trigger_alarm(self):
        print("\a")  # This triggers a system beep sound
        print("\u26A0 Alarm: Budget Limit Exceeded!")

    def show_expense_summary(self):
        print("\nExpense Summary:")
        for expense in self.expenses:
            print(f"{expense['date']} - ${expense['amount']} - {expense['category']}")

    def plot_expenses(self):
        categories = [expense['category'] for expense in self.expenses]
        amounts = [expense['amount'] for expense in self.expenses]

        if not amounts:
            print("No expenses to plot.")
            return

        plt.figure(figsize=(8, 5))
        plt.bar(categories, amounts, color='skyblue')
        plt.title('Expense Analysis by Category')
        plt.xlabel('Category')
        plt.ylabel('Amount Spent ($)')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()


# Instantiate the budget tracker
tracker = BudgetTracker()

# Set budget limit
tracker.set_budget_limit(500)

# Add expenses
tracker.add_expense(100, 'Groceries')
tracker.add_expense(50, 'Transport')
tracker.add_expense(400, 'Shopping')  # This should trigger an alarm

# Show summary and plot
tracker.show_expense_summary()
tracker.plot_expenses()