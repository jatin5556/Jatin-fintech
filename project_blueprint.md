# Jatin FinTech – Project Blueprint

## Inputs
| Input | Type | Example |
|-------|------|---------|
| Income | Number (₹/month) | 60000 |
| Expenses | Number (₹/month) | 20000 |
| Loans | Yes/No | No |
| Loan Amount | Number (₹) | 0 |
| Age | Number | 28 |
| Employment Status | Dropdown | Employed/Self-employed/Other |

## Scoring Logic
- Income > ₹50k → +30 points  
- Expenses < ₹20k → +20 points  
- No bad loans → +30 points  
- Age 25–40 → +20 points  

*Total Score Example:*  
Income = 60000 → +30  
Expenses = 20000 → 0  
No bad loans → +30  
Age 28 → +20  

*Total = 80*  

## Output (Credit Score Category)
| Score | Result |
|-------|--------|
| 80–100 | High – Credit Worthy ✅ |
| 50–79 | Medium – Caution ⚠ |
| 0–49 | Low – Not Eligible ❌ |

## Flow Diagram
