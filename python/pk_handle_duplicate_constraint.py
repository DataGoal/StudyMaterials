import re

def fix_duplicate_constraint_names(sql):
    constraint_counts = {}
    lines = sql.split('\n')
    for i, line in enumerate(lines):
        match = re.search(r'ADD CONSTRAINT (\w+)', line)
        if match:
            constraint_name = match.group(1)
            if constraint_name in constraint_counts:
                constraint_counts[constraint_name] += 1
                lines[i] = re.sub(r'(\bADD CONSTRAINT \w+)', fr'\1_{constraint_counts[constraint_name]}', line)
            else:
                constraint_counts[constraint_name] = 1
    return '\n'.join(lines)

# Example usage:
sql = """ALTER TABLE employee ADD CONSTRAINT emp_pk PRIMARY KEY(emp_name);
ALTER TABLE cust ADD CONSTRAINT cus_pk PRIMARY KEY(cus_no);
ALTER TABLE employee ADD CONSTRAINT emp_pk PRIMARY KEY(emp_name);
ALTER TABLE employee ADD CONSTRAINT emp_pk PRIMARY KEY(emp_id);"""

fixed_sql = fix_duplicate_constraint_names(sql)
print(fixed_sql)
