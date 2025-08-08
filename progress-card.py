# progress tracker for degree students
# by MUFAZ-VK
import csv
import matplotlib.pyplot as plt

class Mark:
    def __init__(self, subject, score, year):
        self.subject = subject
        self.score = score
        self.year = year

class ProgressCard:
    def __init__(self, student_name):
        self.student_name = student_name
        self.marks = []
        self.filename = f"student_marks_{self.student_name.replace(' ', '_')}.csv"
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)
                for row in reader:
                    subject, score, year = row
                    self.marks.append(Mark(subject, int(score), int(year)))
        except (FileNotFoundError, StopIteration, ValueError):
            self.marks = []

    def save_data(self):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['subject', 'score', 'year'])
            for mark in self.marks:
                writer.writerow([mark.subject, mark.score, mark.year])

    def add_mark(self):
        print("\n-- ADD A NEW MARK --")
        try:
            year = int(input("Enter the academic year (1, 2, 3): "))
            if year not in [1, 2, 3]:
                print("\n Invalid year. Please enter 1, 2, 3")
                return
            subject = input("Enter the subject name: ").strip().capitalize()
            score = int(input(f"Enter the score for {subject} (0-100): "))
            if not 0 <= score <= 100:
                print("\n Invalid score. Please enter a value between 0 and 100.")
                return
            new_mark = Mark(subject, score, year)
            self.marks.append(new_mark)
            self.save_data()
            print(f"\n Added '{subject}: {score}%' for Year {year}!")
        except ValueError:
            print("\n Invalid input. Please enter a valid number for score and year.")

    def show_all_marks(self):
        if not self.marks:
            print("\nNo marks found. Try adding some first!")
            return
            
        print(f"\n-- ALL MARKS FOR {self.student_name} --")
        sorted_marks = sorted(self.marks, key=lambda x: (x.year, x.subject))
        for i, mark in enumerate(sorted_marks, 1):
            print(f"{i}. Year {mark.year} - {mark.subject}: {mark.score}%")

    def yearly_graph(self):
        if not self.marks:
            print("\nNo data to plot. Please add marks first.")
            return
        yearly_data = {1: [], 2: [], 3: []}
        for mark in self.marks:
            if mark.year in yearly_data:
                yearly_data[mark.year].append(mark.score)

        labels = []
        averages = []
        for year, scores in yearly_data.items():
            if scores:
                labels.append(f"Year {year}")
                averages.append(sum(scores) / len(scores))
        
        if not labels:
            print("\nNot enough data to create a yearly summary.")
            return
        plt.figure(figsize=(8, 6))
        plt.bar(labels, averages, color='purple')
        plt.ylabel("Average Score (%)")
        plt.title(f"Average Performance Per Year for {self.student_name}")
        plt.ylim(0, 100)
        print("\n processing your yearly performance graph...")
        plt.show()

    def subject_chart(self):
        if not self.marks:
            print("\nNo data to plot. Please add marks first.")
            return
        subject_data = {}
        for mark in self.marks:
            if mark.subject not in subject_data:
                subject_data[mark.subject] = []
            subject_data[mark.subject].append(mark.score)

        labels = []
        averages = []
        for subject, scores in subject_data.items():
            labels.append(subject)
            averages.append(sum(scores) / len(scores))

        fig, ax = plt.subplots()
        ax.pie(averages, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title(f"Average Score by Subject for {self.student_name}")
        ax.axis('equal')
        print("\n processing your subject performance chart...")
        plt.show()

def main():
    student_name = input(" enter your name : ").strip().title()
    print(f"\nWelcome to the Progress Card")
    card = ProgressCard(student_name)
    
    while True:
        print("\n--- MENU ---")
        print("1. Add a new mark")
        print("2. View all marks")
        print("3. Show yearly performance graph)")
        print("4. Show subject performance chart)")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            card.add_mark()
        elif choice == '2':
            card.show_all_marks()
        elif choice == '3':
            card.yearly_graph()
        elif choice == '4':
            card.subject_chart()
        elif choice == '5':
            print("\nthank you.. Your data has been saved.")
            break
        else:
            print("\nInvalid choice. Please try again")
        
        if choice in ['1', '2', '3', '4']:
             input("\nPress Enter to return to the menu...")

if __name__ == "__main__":
    main()
