import os 

os.system("gcc -Wall -pedantic-errors -ansi the1.c -o the1")

total_cases = 500
passed_cases = 0

for i in range(0, total_cases):

	with open(f"test/outputs/output{i}.txt","r") as correct:
		correct_output = correct.read()

	os.system(f"./the1 < test/cases/case{i}.txt > output.txt")

	with open("output.txt","r") as output:
		given_output = output.read()

	if given_output == correct_output:
		passed_cases += 1
		print(passed_cases)
	else:
		print(f"case {i} is wrong.")
		print("correct output:\n", correct_output)
		print("your output:\n", given_output)

os.system("rm -rf output.txt")

print(passed_cases, "cases are correct out of", total_cases, "cases.")
