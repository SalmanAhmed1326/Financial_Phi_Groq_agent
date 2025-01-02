# Finance Agent: Built with Phidata and Groq Model

This repository provides a Python-based **Finance Agent** leveraging the **Phidata framework** and **Groq AI model**. The agent is designed for financial analysis, allowing users to retrieve and summarize stock-related information, analyst recommendations, company news, and more, presented in an easy-to-read table format.

---

## **Features**
- **Stock Price Retrieval**: Fetch real-time stock prices for companies.
- **Analyst Recommendations**: Summarize market analysts' views on selected stocks.
- **Company Information**: Access detailed company profiles and key details.
- **Company News**: Get the latest news related to specific companies.
- **Interactive Tables**: Financial data is displayed in tables for clarity and usability.

---

## **Tech Stack**
1. **Phidata Framework**: Simplifies agent creation and model integration.  
2. **Groq Model**: Utilizes the `llama-3.2-11b-vision-preview` model for AI-driven financial analysis.  
3. **YFinanceTools**: Provides data retrieval capabilities for stock prices, company information, and more.  
4. **Environment Management**: Configured via `.env` file for secure API key handling.

---

## **Command to Run Agent**

```bash
python Finance_agent_single_Phi_groq.py
```

---

## **How It Works**
1. **Environment Initialization**: Loads environment variables, including the Groq API key.
2. **Agent Creation**: Initializes a finance agent using the Groq model and YFinance tools.
3. **Query Execution**: Processes user queries (e.g., stock analysis) and outputs results in markdown-enhanced tables.

---


The agent fetches the latest data and presents it in a table format.

---

## **Dependencies**
- **Phidata**
- **Groq**
- **YFinanceTools**
- **Python Dotenv**

---

## **Contributing**
Contributions to improve the Finance Agent or extend its functionality are welcome. Submit issues or pull requests via GitHub.
