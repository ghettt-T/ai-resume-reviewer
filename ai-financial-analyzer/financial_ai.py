from openai import OpenAI
client = OpenAI()
print("\n💰AI Financial Analyzer")
print("------------------------")
income=input("Enter your monthly income: ")
expenses=input("Enter your monthly expenses: ") 
debt=input("Enter your total debt: ")
response=client.responses.create(
    model="gpt-4.1-mini",
    input=f"""
You are a financial advisor
Analyze this person's finances:
income: {income}
expenses: {expenses}
debt: {debt}
Return:
1. Financial Health Score (1-10)
2. 3 specific improvements
3. One aggressive wealth-building tip
"""
)
advice=response.output_text
print("\n📊 Financial Analysis REPORT:\n")
print(advice)
with open("financial_report.txt","w") as file:
    file.write(advice)
    print("\✅ Report saved to financial_report.txt")
