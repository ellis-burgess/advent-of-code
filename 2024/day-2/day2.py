reports = []

with open('input.txt') as f:
  for line in f:
    report = [int(i) for i in line.strip().split()]
    reports.append(report)

print(reports[0])

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