
# валідуємо інпут користувача та відразу прописуємо підказку,
# щоб розуміти зміст текту, що був до того

def get_user_input(prompt):
    user_input = input(prompt).strip()
    if len(user_input.split()) >= 2:
        return user_input
    else:
        print("Please enter at least three words.")
        return get_user_input(prompt)


# відкриваємо та читаємо обидва файли; елемент списку - кожен рядок(лінія) з чаптеру.

with open('character1(student)', 'r') as file1, open('character2(lector)', 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

#в цей лист будемо закидати по черзі фіналізовані репліки

combined_script = []

#спочатку проходимось по всіх рядках ->
#формується повідомлення prompt_1 для користувача, що включає попередній рядок з файлу ->
#викликається функція get_user_input

max_lines = max(len(lines1), len(lines2))
for i in range(max_lines):
    if i < len(lines1): #поки і менше за довижину першого файлу - буде викононуватися код
        if lines1[i].strip() == '$$$':
            prompt_1 = f"Character1 previous line: {lines1[i - 1].strip()}\nEnter new line for character 1: "
            user_input = get_user_input(prompt_1)
            combined_script.append(user_input + '\n')
        else:
            combined_script.append(lines1[i])

    if i < len(lines2):
        if lines2[i].strip() == '$$$':
            prompt_2 = f"Character2's phrase: {lines2[i - 1].strip()}\nEnter a reaction for character 2: "
            user_input = get_user_input(prompt_2)
            combined_script.append(user_input + '\n')
        else:
            combined_script.append(lines2[i])

with open('script.txt', 'w') as script_file:
    script_file.writelines(combined_script)
    #записуєм весь текст з ліста

print("The script is ready and saved as script.txt.")
