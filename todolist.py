tasks = []
while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    ch = input("Choice: ")
    if ch=='1':
        tasks.append(input("Enter task: "))
        print("Added")
    elif ch=='2':
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif ch=='3':
        try:
            n = int(input("Number to delete: "))
            tasks.pop(n-1)
        except:
            print("Invalid")
    elif ch=='4':
        break
