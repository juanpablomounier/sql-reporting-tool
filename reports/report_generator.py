"""
REPORT_GENERATOR.PY
"""
from database.database_manager import DatabaseManager

class ReportGenerator:
    def __init__(self, option):
        self.option = option
    
    def generate_report(self):
        if self.option == 1:
            res = self.generate_report_sales_per_client()

        elif self.option == 2:
            res = self.generate_report_top_sold_products()

        else:
            res = self.generate_report_total_sales()
    
        return res
    

    
    def generate_report_sales_per_client(self):
        query = """SELECT
                customers.id,
                customers.name,
                SUM(sales.quantity * products.price) AS total_sales
            FROM customers
            JOIN sales
                ON customers.id = sales.customer_id
            JOIN products
                ON sales.product_id = products.id
            GROUP BY customers.id, customers.name;"""
        manager = DatabaseManager()
        res = manager.execute_query(query)
        return res

    def generate_report_top_sold_products(self):
        pass

    def generate_report_total_sales(self):
        pass