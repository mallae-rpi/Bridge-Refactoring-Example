class SalesCSVReport:
    def generate(self) -> None:
        print("Sales Report")
        print("  Period : Q1 2026")
        print("  Revenue: $500,000")
        print("  Format : CSV")

class SalesJSONReport:
    def generate(self) -> None:
        print("Sales Report")
        print("  Period : Q1 2026")
        print("  Revenue: $500,000")
        print("  Format : JSON")

class SalesMarkdownReport:
    def generate(self) -> None:
        print("Sales Report")
        print("  Period : Q1 2026")
        print("  Revenue: $500,000")
        print("  Format : Markdown")

class SalesPDFReport:
    def generate(self) -> None:
        print("Sales Report")
        print("  Period : Q1 2026")
        print("  Revenue: $500,000")
        print("  Format : PDF")


class InventoryCSVReport:
    def generate(self) -> None:
        print("Inventory Report")
        print("  SKUs in stock: 1,042")
        print("  Low stock    : 17 items")
        print("  Format : CSV")

class InventoryJSONReport:
    def generate(self) -> None:
        print("Inventory Report")
        print("  SKUs in stock: 1,042")
        print("  Low stock    : 17 items")
        print("  Format : JSON")

class InventoryMarkdownReport:
    def generate(self) -> None:
        print("Inventory Report")
        print("  SKUs in stock: 1,042")
        print("  Low stock    : 17 items")
        print("  Format : Markdown")

class InventoryPDFReport:
    def generate(self) -> None:
        print("Inventory Report")
        print("  SKUs in stock: 1,042")
        print("  Low stock    : 17 items")
        print("  Format : PDF")


class UserActivityCSVReport:
    def generate(self) -> None:
        print("User Activity Report")
        print("  Active users: 8,301")
        print("  Avg session : 4m 22s")
        print("  Format : CSV")

class UserActivityJSONReport:
    def generate(self) -> None:
        print("User Activity Report")
        print("  Active users: 8,301")
        print("  Avg session : 4m 22s")
        print("  Format : JSON")

class UserActivityMarkdownReport:
    def generate(self) -> None:
        print("User Activity Report")
        print("  Active users: 8,301")
        print("  Avg session : 4m 22s")
        print("  Format : Markdown")

class UserActivityPDFReport:
    def generate(self) -> None:
        print("User Activity Report")
        print("  Active users: 8,301")
        print("  Avg session : 4m 22s")
        print("  Format : PDF")


if __name__ == "__main__":
    reports = [
        SalesCSVReport(), SalesJSONReport(),
        SalesMarkdownReport(), SalesPDFReport(),
        InventoryCSVReport(), InventoryJSONReport(),
        InventoryMarkdownReport(), InventoryPDFReport(),
        UserActivityCSVReport(), UserActivityJSONReport(),
        UserActivityMarkdownReport(), UserActivityPDFReport(),
    ]
    for r in reports:
        r.generate()
        print()
