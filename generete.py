from main import chatgpt4_query
import os

def generae_text_parse(subject):
    text = f"""
        Create for me on "{subject}" topics for the sections of my book, of the kind, observing categories, chapters can be up to 5 and sections in each chapter can be maximum 5 as I will provide below:

        BOOK TITLE: Amplify Your Fortune: Unlocking Wealth Beyond Dreams

        Introduction: Understanding Wealth Amplification
        The Power of Wealth Amplification
        Overcoming the Mental Barriers to Wealth

        Chapter 1: Foundations of Fortune
        Assessing Your Financial Health
        Understanding Your Current Financial Position
        Setting Clear Financial Goals
        Developing a Wealth Mindset
        Cultivating a Positive Attitude towards Money
        Overcoming Limiting Beliefs

        Chapter 2: Strategies for Financial Growth
        Investment Essentials
        Understanding Different Investment Vehicles
        Building a Diverse Investment Portfolio
        The Business of Wealth
        Evaluating Business Opportunities
        Starting and Scaling Your Business

        Chapter 3: Maximizing Your Money
        Smart Saving Techniques
        Cutting Costs without Sacrificing Quality of Life
        Tools and Techniques for Efficient Saving
        Income Multiplication
        Identifying and Creating Multiple Income Streams
        Negotiating Salaries and Raises

        Chapter 4: Advanced Wealth Building
        Real Estate Investment
        Getting Started in Property Investment
        Strategies for Long-Term Property Wealth
        Stock Market Mastery
        Analyzing Stocks for Maximum Gain
        Timing the Market: Myths and Realities

        Chapter 5: Protecting Your Wealth
        Risk Management and Insurance
        Understanding and Mitigating Financial Risks
        Choosing the Right Insurance for Your Wealth
        Tax Planning and Efficiency
        Legal Strategies to Minimize Taxes
        Utilizing Tax-Advantaged Accounts

        Chapter 6: The Entrepreneurial Path to Riches
        Finding Your Niche
        Discovering Lucrative Markets
        Crafting Your Unique Value Proposition
        The Business Plan
        Writing a Winning Business Plan
        Funding and Financing Your Venture

        Chapter 7: The Investor’s Mindset
        Psychological Aspects of Investing
        Dealing with Losses
        The Psychology of Risk and Reward
        Advanced Investment Strategies
        Leveraging Debts and Loans
        Alternative Investments and Opportunities

        Chapter 8: Long-Term Wealth Sustenance
        Estate Planning and Wealth Transfer
        Preserving Wealth for Future Generations
        Legal Aspects of Wealth Transfer
        Staying Updated and Adapting to Change
        Keeping Abreast of Economic Changes
        Pivoting Strategies According to Market Conditions
    """

    text = chatgpt4_query(text)

    return text

if __name__ == "__main__":
    inp = input("[BOT] Write book subject... Example: First Steps in Python. Where to start learning Python:\n")
    result = generae_text_parse(inp)
    with open(os.path.join(os.getcwd(), 'text.txt'), 'w') as f:
        f.write(result)
    print(result)