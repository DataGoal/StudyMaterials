-- Employees Earning More Than Their Managers
-- Write an SQL query to find the employees who earn more than their managers.
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
SELECT e1.first_name, e1.salary as employee from employee e1 where e1.salary > (SELECT e2.salary from employee e2 where e1.manager_id = e2.id)
--OR
SELECT abc.first_name, abc.reportee_salary FROM (SELECT e1.salary AS manager_salary, e2.first_name, e2.salary AS reportee_salary FROM employee e1 JOIN employee e2 ON e1.id = e2.manager_id) AS abc WHERE abc.reportee_salary > abc.manager_salary

-- Manager of the Largest Department
-- Given a list of a company's employees, find the name of the manager from the largest department. Manager is each employee that contains word "manager" under their position.  Output their first and last name.
-- https://platform.stratascratch.com/coding/2060-manager-of-the-largest-department?code_type=3
WITH cte AS (SELECT first_name,last_name,department_id, position, DENSE_RANK() OVER(ORDER BY COUNT(department_id) DESC) AS rnk FROM az_employees GROUP BY department_id)
SELECT a.first_name, a.last_name FROM az_employees a JOIN cte c ON a.department_id = c.department_id WHERE c.rnk = 1 AND LOWER(a.position) LIKE ('%manager%')

-- Employees Whose Manager Left the Company
-- Write an SQL query to report the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.
-- https://leetcode.com/problems/employees-whose-manager-left-the-company/
SELECT abc.employee_id FROM (SELECT employee_id, salary FROM employees WHERE manager_id NOT IN (SELECT employee_id FROM employees)) AS abc WHERE abc.salary < 30000 ORDER BY 1

-- All People Report to the Given Manager
-- Write an SQL query to find employee_id of all employees that directly or indirectly report their work to the head of the company. The indirect relation between managers will not exceed three managers as the company is small.
-- https://leetcode.com/problems/all-people-report-to-the-given-manager/
SELECT e1.employee_id
FROM Employees e1
JOIN Employees e2
ON e1.manager_id = e2.employee_id
JOIN Employees e3
ON e2.manager_id = e3.employee_id
WHERE e3.manager_id = 1 AND e1.employee_id != 1
-- OR
SELECT main.employee_id FROM Employees AS main
LEFT JOIN Employees AS t1 ON main.manager_id = t1.employee_id
LEFT JOIN Employees AS t2 ON t1.manager_id = t2.employee_id
WHERE main.employee_id != 1 AND t2.manager_id = 1

-- Managers with at Least 5 Direct Reports
-- Write an SQL query to report the managers with at least five direct reports.
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
SELECT name FROM employee WHERE ID IN (SELECT managerid FROM employee GROUP BY managerid having COUNT(managerid) >= 5)

-- Warehouse Manager
-- Write an SQL query to report the number of cubic feet of volume the inventory occupies in each warehouse.
-- https://leetcode.com/problems/warehouse-manager/
SELECT w.name AS warehouse_name, SUM(p.width*p.length*p.height*w.units) AS volume FROM Warehouse w JOIN products p ON w.product_id = p.product_id GROUP BY 1

-- Highest Target Under Manager
-- Find the highest target achieved by the employee or employees who works under the manager id 13. Output the first name of the employee and target achieved. The solution should show the highest target achieved under manager_id=13 and which employee(s) achieved it.
-- https://platform.stratascratch.com/coding/9905-highest-target-under-manager?code_type=3
SELECT abc.first_name, abc.target FROM (SELECT manager_id, first_name, target, DENSE_RANK() OVER(ORDER BY target DESC) AS rnk FROM salesforce_employees WHERE manager_id = 13) AS abc WHERE abc.rnk = 1

-- Super Managers
-- Find managers with at least 7 direct reporting employees. Output first names of managers.
-- https://platform.stratascratch.com/coding/9901-super-managers?code_type=3
WITH cte AS (SELECT manager_id, COUNT(id) FROM employee GROUP BY manager_id HAVING COUNT(id) >= 7 ORDER BY 1)
SELECT e.first_name FROM employee e JOIN cte c ON e.id = c.manager_id;

-- Find all workers who are also managers
-- Find all workers who are also managers.  Worker is manager if it's title equals to "Manager" Output the first name along with the corresponding title.
-- https://platform.stratascratch.com/coding/9848-find-all-workers-who-are-also-managers?code_type=3
SELECT  w.first_name, t.worker_title FROM worker w JOIN title t ON w.worker_id = t.worker_ref_id WHERE t.worker_title = 'Manager'