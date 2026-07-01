"""
MAIN.PY

"""

from ui.menu import get_option
from reports.report_generator import ReportGenerator


print("\n\n")
print("="*29)
print("WELCOME TO SQL REPORTING TOOL")
print("="*29)
print("\n")

option = get_option()
if (option >= 1 and option <= 3):
    reporter = ReportGenerator(option)
    report = reporter.generate_report()
    print(report)

