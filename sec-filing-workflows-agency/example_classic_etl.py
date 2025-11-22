#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "edgartools>=4.26.0,<5.0.0",  # SEC filing data access
#     "pandas>=2.0.0",               # Data manipulation
#     "sqlalchemy>=2.0.0",           # Database ORM
#     "psycopg2-binary>=2.9.0",      # PostgreSQL adapter
# ]
# ///
"""
Example 1: Classic ETL Workflow (Non-AI)

This workflow demonstrates a traditional ETL approach for extracting financial
statements from SEC 10-K filings and loading them into a data warehouse.

Use Case: Regular quarterly/annual financial data extraction for portfolio
companies for benchmarking and trend analysis.

Business Value:
- Automated data collection (saves 10-20 hours/week of manual work)
- Consistent data quality
- Historical trend analysis
- Multi-company comparisons

Technical Approach:
- No AI/LLM required
- Deterministic XBRL parsing
- Structured database storage
- Scheduled execution (e.g., daily)
"""

import sys
from datetime import datetime
from typing import List, Dict, Any
import pandas as pd
from edgartools import Company, Filing

# Database connection would be configured here
# from sqlalchemy import create_engine

class FinancialStatementETL:
    """Extract, transform, and load financial statements from SEC filings."""

    def __init__(self, companies: List[str], years: List[int]):
        """
        Initialize ETL workflow.

        Args:
            companies: List of ticker symbols
            years: List of years to process
        """
        self.companies = companies
        self.years = years
        self.results = []
        self.errors = []

    def extract(self, ticker: str, year: int) -> List[Filing]:
        """
        Extract 10-K filings for a company and year.

        Args:
            ticker: Company ticker symbol
            year: Year to retrieve filings for

        Returns:
            List of Filing objects
        """
        try:
            print(f"Extracting {ticker} {year} 10-K filings...")
            company = Company(ticker)
            filings = company.get_filings(form='10-K', year=year)
            return list(filings)
        except Exception as e:
            self.errors.append({
                'ticker': ticker,
                'year': year,
                'error': str(e),
                'stage': 'extract'
            })
            return []

    def transform(self, filing: Filing) -> Dict[str, Any]:
        """
        Transform filing into structured financial data.

        Args:
            filing: SEC Filing object

        Returns:
            Dictionary of financial metrics
        """
        try:
            print(f"Transforming {filing.company} {filing.filing_date}...")

            # Extract financial statements using XBRL
            financials = filing.financials()

            # Get key metrics (example - would be more comprehensive in production)
            income_statement = financials.get_income_statement()
            balance_sheet = financials.get_balance_sheet()
            cash_flow = financials.get_cash_flow_statement()

            # Extract specific metrics
            record = {
                'ticker': filing.company,
                'filing_date': filing.filing_date,
                'period_end': filing.period_end,
                'accession_number': filing.accession_number,

                # Income Statement
                'revenue': self._get_metric(income_statement, 'Revenues'),
                'operating_income': self._get_metric(income_statement, 'OperatingIncome'),
                'net_income': self._get_metric(income_statement, 'NetIncome'),

                # Balance Sheet
                'total_assets': self._get_metric(balance_sheet, 'Assets'),
                'total_liabilities': self._get_metric(balance_sheet, 'Liabilities'),
                'stockholders_equity': self._get_metric(balance_sheet, 'StockholdersEquity'),

                # Cash Flow
                'operating_cash_flow': self._get_metric(cash_flow, 'OperatingCashFlow'),
                'investing_cash_flow': self._get_metric(cash_flow, 'InvestingCashFlow'),
                'financing_cash_flow': self._get_metric(cash_flow, 'FinancingCashFlow'),

                # Metadata
                'extracted_at': datetime.utcnow().isoformat(),
                'edgartools_version': '4.26.0',  # Would get from package in production
            }

            # Calculate derived metrics
            record['profit_margin'] = (
                record['net_income'] / record['revenue']
                if record['revenue'] and record['revenue'] > 0
                else None
            )

            record['debt_to_equity'] = (
                record['total_liabilities'] / record['stockholders_equity']
                if record['stockholders_equity'] and record['stockholders_equity'] > 0
                else None
            )

            return record

        except Exception as e:
            self.errors.append({
                'ticker': filing.company,
                'accession_number': filing.accession_number,
                'error': str(e),
                'stage': 'transform'
            })
            return None

    def _get_metric(self, statement: Any, metric_name: str) -> float:
        """
        Safely extract a metric from a financial statement.

        Args:
            statement: Financial statement object
            metric_name: Name of the metric to extract

        Returns:
            Metric value or None if not found
        """
        try:
            if statement is None:
                return None
            # This is simplified - actual implementation would use
            # edgartools' XBRL APIs to find the right concept
            return statement.get(metric_name)
        except:
            return None

    def load(self, records: List[Dict[str, Any]]) -> None:
        """
        Load transformed records into data warehouse.

        Args:
            records: List of financial records to load
        """
        if not records:
            print("No records to load")
            return

        # Convert to DataFrame
        df = pd.DataFrame(records)

        print(f"Loading {len(df)} records to data warehouse...")

        # In production, this would write to database
        # engine = create_engine('postgresql://user:pass@host/db')
        # df.to_sql('financial_statements', engine, if_exists='append', index=False)

        # For this example, save to CSV
        output_file = f'financial_statements_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        df.to_csv(output_file, index=False)
        print(f"Saved to {output_file}")

        # Also display summary
        print("\nData Summary:")
        print(df[['ticker', 'filing_date', 'revenue', 'net_income', 'profit_margin']].to_string())

    def run(self) -> None:
        """Execute the complete ETL workflow."""
        print("=" * 80)
        print("Financial Statement ETL Workflow")
        print("=" * 80)

        for ticker in self.companies:
            for year in self.years:
                # Extract
                filings = self.extract(ticker, year)

                # Transform
                for filing in filings:
                    record = self.transform(filing)
                    if record:
                        self.results.append(record)

        # Load
        self.load(self.results)

        # Report errors
        if self.errors:
            print(f"\n{len(self.errors)} errors occurred:")
            for error in self.errors:
                print(f"  - {error}")

        print(f"\nWorkflow complete: {len(self.results)} records processed")


def main():
    """Main entry point."""
    # Example configuration
    companies = ['AAPL', 'MSFT', 'GOOGL']
    years = [2023, 2024]

    # Run ETL
    etl = FinancialStatementETL(companies=companies, years=years)
    etl.run()


if __name__ == '__main__':
    main()
