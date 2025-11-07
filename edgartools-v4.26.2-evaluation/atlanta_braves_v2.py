#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "edgartools>=4.26.2",
# ]
# ///
"""
Atlanta Braves Research - v4.26.2 Edition

Testing the updated edgartools with improved documentation.
This version uses to_context() from the start as documented in SKILL.md.

Usage:
    uv run atlanta_braves_v2.py
"""

from edgar import set_identity, Company
import sys

# Set identity FIRST (learned from Prerequisites section)
set_identity("Research Agent research@example.com")

def research_atlanta_braves_v2():
    """Research Atlanta Braves using improved v4.26.2 APIs."""

    print("=" * 80)
    print("ATLANTA BRAVES (BATRB) RESEARCH - v4.26.2 Edition")
    print("=" * 80)
    print()

    try:
        # Step 1: Get Company Information (using to_context()!)
        print("Step 1: Getting Company Information")
        print("-" * 80)
        company = Company("BATRB")

        # Use to_context() first as recommended
        print("\n📊 Company Profile (using to_context()):")
        print(company.to_context())
        print()

        # Step 2: Get Recent Filings
        print("\nStep 2: Getting Recent Filings")
        print("-" * 80)
        filings = company.get_filings(form=["10-K", "10-Q", "8-K"])

        # Use to_context() for filings collection
        print("\n📊 Filings Summary (using to_context()):")
        print(filings.to_context())
        print()

        # Step 3: Get Latest 10-K
        print("\nStep 3: Analyzing Latest 10-K Filing")
        print("-" * 80)
        ten_k_filings = company.get_filings(form="10-K")

        if len(ten_k_filings) > 0:
            latest_10k = ten_k_filings.latest()

            # Use to_context() for filing
            print("\n📊 Latest 10-K (using to_context()):")
            print(latest_10k.to_context())
            print()

            # Step 4: Extract Financial Statements
            print("\nStep 4: Extracting Financial Statements")
            print("-" * 80)

            try:
                xbrl = latest_10k.xbrl()

                if xbrl:
                    # Use to_context() first to see what's available!
                    print("\n📊 XBRL Summary (using to_context()):")
                    print(xbrl.to_context())
                    print()

                    # Now get specific statements (we know they exist from to_context())
                    print("\n💰 Income Statement:")
                    try:
                        income_stmt = xbrl.statements.income_statement()
                        print(income_stmt)
                    except Exception as e:
                        print(f"✗ Income Statement error: {e}")

                    print("\n📈 Balance Sheet:")
                    try:
                        balance_sheet = xbrl.statements.balance_sheet()
                        print(balance_sheet)
                    except Exception as e:
                        print(f"✗ Balance Sheet error: {e}")

                else:
                    print("\n✗ No XBRL data available for this filing")
            except Exception as e:
                print(f"\n✗ Error extracting XBRL: {e}")
        else:
            print("\n✗ No 10-K filings found")

        # Step 5: Multi-Period Financial Analysis using Entity Facts API
        print("\n\nStep 5: Multi-Period Financial Analysis")
        print("-" * 80)
        try:
            # Entity Facts API - most token-efficient for multi-period
            income_multi = company.income_statement(periods=3)
            if income_multi:
                print("\n📊 Multi-period Income Statement (3 fiscal years):")
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
    result = research_atlanta_braves_v2()
    sys.exit(0 if result["success"] else 1)
