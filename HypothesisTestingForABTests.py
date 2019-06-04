# Load modules
from scipy.stats import chi2_contingency

# Record Data from Google Analytics
control_group = 7700
variant_group = 7700
control_success = 231
variant_success = 308
control_fail = control_group - control_success
variant_fail = variant_group - variant_success

# Perform Chi2 Test
results = chi2_contingency([
  [control_fail, control_success],
  [variant_fail, variant_success]
])

p = results[1]

# Paste Code Here:
if p < 0.05:
    print("Significant!")
if p > 0.05:
    print("Not significant!")
