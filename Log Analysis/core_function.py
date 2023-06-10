# Import module regex
import re

# Hàm tìm thông tin từ file log theo dòng, trả về một biến dạng dictionary
def find_pattern_in_line(file_path, pattern):
    result_dict = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall(pattern, line)
            for msg in matches:
                result_dict[msg] = result_dict.get(msg, 0) + 1
                
    return result_dict

import matplotlib.pyplot as plt
import operator

# Hàm generate report và chart 
def generate_attack_report(attack_dict, threshold,title,chart_png):
    # Sort attacks by the number of times attacked descendingly
    sorted_attacks = sorted(attack_dict.items(), key=operator.itemgetter(1), reverse=True)

    total_attacks = sum(attack_dict.values())

    # Initialize lists to store data for the report
    attacks = []
    num_attacks = []
    percentages = []

    # Iterate over the sorted attacks
    for attack, count in sorted_attacks:
        # Calculate the percentage of attacks
        percentage = (count / total_attacks) * 100

        # Add attack details to the report lists
        attacks.append(attack)
        num_attacks.append(count)
        percentages.append(percentage)

    # Write the report to a file
    with open(title, "w") as report_file:
        report_file.write("Attack Report:\n")
        report_file.write("{:<90} {:<20} {:<10}\n".format("Attack", "Number of Attacks", "Percentage"))
        report_file.write("-" * 120 + "\n")
        report_file.write("{:<90} {:<20} {:<10}%\n".format("Total", total_attacks, "100"))
        for attack, count, percentage in zip(attacks, num_attacks, percentages):
            report_file.write("{:<90} {:<20} {:<10.2f}%\n".format(attack, count, percentage))

    # Combine attacks with small percentages into the "Other" category
    other_attacks = [attack for attack, percentage in zip(attacks, percentages) if percentage < threshold]
    other_percentage = sum(percentage for percentage in percentages if percentage < threshold)
    attacks = [attack for attack in attacks if attack not in other_attacks]
    num_attacks = [count for count, attack in zip(num_attacks, attacks) if attack not in other_attacks]
    percentages = [percentage for percentage in percentages if percentage >= threshold]
    attacks.append("Other")
    num_attacks.append(sum(num_attacks))
    percentages.append(other_percentage)

    # Plot the pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(percentages, labels=attacks, autopct='%1.1f%%')
    plt.title(title)
    plt.axis('equal')
    plt.savefig(chart_png)  # Save the pie chart as an image file