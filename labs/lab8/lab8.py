"""
Name: <Kate Culpepper>
<Lab8>.py

Problem: <This function takes data from a file and then calculates th weighted average of each student >

Certification of Authenticity:

I certify that this assignment is entirely my own work.

"""


def weighted_average(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    clas_avg = 0
    student_count = 0

    for line in infile:

        line = line.strip()
        split_line = line.split(": ")
        out_name = str(split_line[0]) + "'s average:"
        split_nums = split_line[1].split(" ")
        avg_nums = []
        for j in range(0, len(split_nums)):
            avg_nums.append(int(split_nums[j]))

        weight_sum = 0
        for i in range(0, len(avg_nums), 2):
            weight_sum = weight_sum + avg_nums[i]

        if weight_sum < 100:
            print(out_name, "Error: The weights are less than 100.", file=outfile)
        elif weight_sum > 100:
            print(out_name, "Error: The weights are more than 100.", file=outfile)
        else:
            average = 0
            student_count = student_count + 1
            for k in range(0, len(avg_nums), 2):
                average = average + (avg_nums[k] * avg_nums[k + 1])
            average = average / 100
            clas_avg = clas_avg + average
            print(out_name, average, file=outfile)

    clas_avg = clas_avg / student_count
    print("Class average:", clas_avg, file=outfile)
    infile.close()
    outfile.close()


if __name__ == '__main__':
    weighted_average("grades.txt", "avg.txt")
