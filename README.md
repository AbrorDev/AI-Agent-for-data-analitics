# 📊 AI Agent for Data Analytics

Ushbu loyiha foydalanuvchi tomonidan berilgan natural savolni qabul qiladi, savolni **SQL query** ga aylantiradi va natijani **Excel** fayl shaklida qaytaradi. Excel faylda jadval bilan birga **bar chart** va **line chart** ham avtomatik yaratiladi. Foydalanuvchi ushbu faylni yuklab olib, tahlil qilishi mumkin.  

---

## 🗄️ Ma’lumotlar bazasi tuzilishi

Loyiha quyidagi **SQLite** ma’lumotlar bazasi tuzilmasidan foydalanadi:

### Clients
| Ustun nomi  | Tavsif                |
|-------------|-----------------------|
| `id`        | Mijozning noyob ID raqami |
| `name`      | Mijozning ismi        |
| `birth_date`| Tug‘ilgan sana        |
| `region`    | Mintaqa               |

### Accounts
| Ustun nomi  | Tavsif                         |
|-------------|--------------------------------|
| `id`        | Hisob raqami ID                |
| `client_id` | `Clients.id` ga tashqi kalit   |
| `balance`   | Hisobdagi qoldiq summa         |
| `open_date` | Hisob ochilgan sana            |

### Transactions
| Ustun nomi  | Tavsif                         |
|-------------|--------------------------------|
| `id`        | Tranzaksiya ID                 |
| `account_id`| `Accounts.id` ga tashqi kalit  |
| `amount`    | Tranzaksiya summasi            |
| `date`      | Tranzaksiya sanasi             |
| `type`      | Tranzaksiya turi (masalan, kirim/chiqim) |

---

## 🚀 Ishlash jarayoni

1. Foydalanuvchi savol beradi:  
   _“Toshkent shahrida 2022 va 2023 yillardagi alohida tranzaksiyalar summasi kerak”_  

2. AI Agent savolni **SQL query** ga aylantiradi:  
   ```sql
   SELECT strftime('%Y', t.date) AS year, SUM(t.amount) AS total_transactions
   FROM Transactions t
   JOIN Accounts a ON t.account_id = a.id
   JOIN Clients c ON a.client_id = c.id
   WHERE c.region = 'Tashkent' AND (strftime('%Y', t.date) = '2022' OR strftime('%Y', t.date) = '2023')
   GROUP BY year
   ORDER BY year;

3. Natijalar Excel faylga yoziladi (jadval + grafik).

4. Foydalanuvchi Streamlit interfeysi orqali faylni yuklab oladi.