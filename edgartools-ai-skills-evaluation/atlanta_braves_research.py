#!/usr/bin/env python3
"""
Research script for Atlanta Braves (BATRB) using edgartools.

This script demonstrates using edgartools to:
1. Get company information
2. Retrieve recent filings
3. Extract financial statements
4. Analyze the data
"""

from edgar import Company, set_identity
from rich import print as rprint
import sys

# Set user identity as required by SEC
set_identity("Research Agent research@example.com")

def research_atlanta_braves():
    """Research Atlanta Braves using edgartools."""

    print("=" * 80)
    print("ATLANTA BRAVES (BATRB) RESEARCH")
    print("=" * 80)
    print()

    try:
        # Step 1: Get Company Information
        print("Step 1: Getting Company Information...")
        print("-" * 80)
        company = Company("BATRB")
        print(f"\nCompany Name: {company.name}")
        print(f"Ticker: {company.tickers}")
        print(f"CIK: {company.cik}")
        print(f"SIC: {company.sic}")
        print(f"Industry: {company.industry}")
        print(f"Fiscal Year End: {company.fiscal_year_end}")
        print()

        # Step 2: Get Recent Filings
        print("\nStep 2: Getting Recent Filings...")
        print("-" * 80)
        filings = company.get_filings(form=["10-K", "10-Q", "8-K"])
        recent_filings = filings.head(10)
        print(f"\nFound {len(filings)} total filings")
        print(f"\nMost Recent 10 Filings:")
        print(recent_filings)
        print()

        # Step 3: Get Latest 10-K
        print("\nStep 3: Analyzing Latest 10-K Filing...")
        print("-" * 80)
        ten_k_filings = company.get_filings(form="10-K")
        if len(ten_k_filings) > 0:
            latest_10k = ten_k_filings.latest(1)
            print(f"\nLatest 10-K:")
            print(f"  Filing Date: {latest_10k.filing_date}")
            print(f"  Period: {latest_10k.period_of_report}")
            print(f"  Accession Number: {latest_10k.accession_number}")
            print()

            # Try to get XBRL data
            print("\nStep 4: Extracting Financial Statements...")
            print("-" * 80)
            try:
                xbrl = latest_10k.xbrl()
                if xbrl:
                    print("\n✓ XBRL data available")

                    # Income Statement
                    try:
                        income_stmt = xbrl.statements.income_statement()
                        if income_stmt:
                            print("\n✓ Income Statement extracted")
                            print(income_stmt)
                    except Exception as e:
                        print(f"\n✗ Income Statement error: {e}")

                    # Balance Sheet
                    try:
                        balance_sheet = xbrl.statements.balance_sheet()
                        if balance_sheet:
                            print("\n✓ Balance Sheet extracted")
                            print(balance_sheet)
                    except Exception as e:
                        print(f"\n✗ Balance Sheet error: {e}")

                    # Cash Flow
                    try:
                        cash_flow = xbrl.statements.cash_flow_statement()
                        if cash_flow:
                            print("\n✓ Cash Flow Statement extracted")
                            print(cash_flow)
                    except Exception as e:
                        print(f"\n✗ Cash Flow error: {e}")
                else:
                    print("\n✗ No XBRL data available for this filing")
            except Exception as e:
                print(f"\n✗ Error extracting XBRL: {e}")
        else:
            print("\n✗ No 10-K filings found")

        # Step 5: Try Multi-Period Financial Analysis using Entity Facts API
        print("\n\nStep 5: Multi-Period Financial Analysis...")
        print("-" * 80)
        try:
            # Try to get income statement for multiple periods
            income_multi = company.income_statement(periods=3)
            if income_multi:
                print("\n✓ Multi-period Income Statement (3 fiscal years):")
                print(income_multi)
        except Exception as e:
            print(f"\n✗ Multi-period analysis error: {e}")

        print("\n" + "=" * 80)
        print("RESEARCH COMPLETE")
        print("=" * 80)

        return {
            "success": True,
            "company": company,
            "filings_count": len(filings),
            "latest_10k": latest_10k if len(ten_k_filings) > 0 else None
        }

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return {
            "success": False,
            "error": str(e)
        }

if __name__ == "__main__":
    result = research_atlanta_braves()
    sys.exit(0 if result["success"] else 1)
