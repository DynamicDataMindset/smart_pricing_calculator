# Smart Pricing Calculator 💰

A Streamlit web app that automates product pricing for businesses dealing with fluctuating exchange rates.  
The app fetches **live USD/ZAR exchange rates**, applies business-specific logic (exchange adjustment, markup, VAT), and returns instant client-ready prices.  

---

## 📝 The Problem
At Msquared Medical, we faced a major challenge in providing quick and accurate pricing to clients:
- We **don’t keep stock** in the office, so prices depend on manufacturers.  
- Every time a client asked for a price, we had to request updated quotes from suppliers, which could take **2+ days**.  
- Prices fluctuate constantly due to the **USD/ZAR exchange rate**.  
- We also needed to factor in **markup (profit margin)** and **VAT**, but doing this manually was slow and error-prone.  

This created inefficiency for the sales team and frustration for clients who wanted instant quotes.  

---

## 💡 The Solution
I built a **web-based pricing calculator** using **Python + Streamlit** that automates this entire workflow:
1. Fetches the **live USD/ZAR exchange rate** from Yahoo Finance.  
2. Applies a **fixed exchange adjustment (+$1.50)** to cover costs.  
3. Multiplies the adjusted rate with the **product’s USD price**.  
4. Applies a **markup factor (1.35 = 35% margin)**.  
5. Calculates both **Excl. VAT** and **Incl. VAT** prices at **15% VAT**.  
6. Displays the result in a clean calculator-style interface.

<img width="1900" height="1164" alt="image" src="https://github.com/user-attachments/assets/5c3a8b16-cb8f-4b54-a35f-164403c2f5cf" />

🔴 Problem box → highlighted in light red
🟡 Solution Plan → highlighted in light yellow
🟢 Tools → highlighted in light green
🔵 Outcome → highlighted in light blue

---

## ⚙️ Tools & Methods Used
- **Python** → core logic  
- **Streamlit** → lightweight web app framework for UI  
- **yFinance API** → real-time USD/ZAR exchange rate  
- **GitHub + Streamlit Cloud** → hosting and deployment  

---

## 🚀 Features
- ✅ Fetches **live exchange rates** in real time  
- ✅ Shows both **current exchange rate** and **adjusted rate (+$1.50)**  
- ✅ Instant calculation of **Excl. VAT** and **Incl. VAT**  
- ✅ Easy-to-use calculator-style interface for sales teams  
- ✅ Deployable as a **public web app** accessible from any browser  

---

## 🖥️ Demo
👉 Live App: [https://smart-pricing-calculator.streamlit.app](https://smart-pricing-calculator.streamlit.app)  

---

## 🛠️ How to Run Locally
1. Clone this repo:  
   ```bash
   git clone https://github.com/<your-username>/smart-pricing-calculator.git
   cd smart-pricing-calculator
   
✅ The Outcome

With this app, the sales team can now:
Generate instant and accurate quotes without waiting for supplier updates.
Provide clients with both Excl. VAT and Incl. VAT prices transparently.
Reduce response times from 2+ days → a few seconds.
This not only improved efficiency but also enhanced customer trust and professionalism in pricing communication.

📌 Tech Stack

Python
Streamlit
yFinance API
GitHub / Streamlit Cloud

📬 Author

👤 Boniface Ramushu
GitHub: @dynamicdatamindset
