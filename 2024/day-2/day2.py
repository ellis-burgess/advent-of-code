reports = []

with open('input.txt') as f:
  for line in f:
    report = [int(i) for i in line.strip().split()]
    reports.append(report)

def is_report_safe(report):
  if report != sorted(report, reverse=False) and report != sorted(report, reverse=True):
    return False
  if len(set(report)) != len(report):
    return False
  else:
    report_delta = [abs(report[i] - report[max(i - 1, 0)]) for i in range(len(report))]
    if all([i > 0 and i < 4 for i in report_delta[1:]]):
      return True

count = 0
tolerated_count = 0

for report in reports:
  if is_report_safe(report):
    count += 1
    tolerated_count += 1
  else:
    masked_reports = [report[0:i] + report[i+1:] for i in range(len(report))]
    if any([is_report_safe(masked_report) for masked_report in masked_reports]):
      tolerated_count += 1

print(count)
print(tolerated_count)