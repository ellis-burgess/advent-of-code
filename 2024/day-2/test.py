reports = [[7, 6, 4, 2, 1],
[1, 2, 7, 8, 9],
[9, 7, 6, 2, 1],
[1, 3, 2, 4, 5],
[8, 6, 4, 4, 1],
[1, 3, 6, 7, 9]]

# A report only counts as safe if both of the following are true:
# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.

count = 0

for report in reports:
  if report != sorted(report, reverse=False) and report != sorted(report, reverse=True):
    continue
  elif len(set(report)) != len(report):
    continue
  else:
    report_delta = [abs(report[i] - report[max(i - 1, 0)]) for i in range(len(report))]
    if all([i > 0 and i < 4 for i in report_delta[1:]]):
      count += 1

print(count)