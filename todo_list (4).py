# ============================================================
#   DecodeLabs | Python Programming - Project 1
#   The To-Do List | Industrial Training Kit | Batch 2026
# ============================================================

my_tasks = []


def add_task(task):
    """Add a new task to the list (INSERT operation)."""
    my_tasks.append(task)
    print(f"\n  ✅ Task added: '{task}'")


def view_tasks():
    """Display all tasks using the Iterator Protocol (READ operation)."""
    print("\n" + "=" * 40)
    print("       📋 YOUR TO-DO LIST")
    print("=" * 40)

    if not my_tasks:
        print("  No tasks yet. Add some tasks!")
    else:
        for index, task in enumerate(my_tasks, start=1):
            print(f"  {index}. {task}")

    print("=" * 40)


def main():
    print("\n" + "=" * 40)
    print("  🚀 DecodeLabs To-Do List App")
    print("     Python Project 1 | Batch 2026")
    print("=" * 40)

    while True:
        print("\n  MENU:")
        print("  [1] Add Task")
        print("  [2] View Tasks")
        print("  [3] Exit")

        choice = input("\n  Enter your choice (1/2/3): ").strip()

        if choice == "1":
            task = input("  Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("  ⚠️  Task cannot be empty.")

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            print("\n  👋 Exiting. Keep building!\n")
            break

        else:
            print("  ⚠️  Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
