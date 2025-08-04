### 🎯 **Loyiha nomi:** `Contact Book` — OOP + JSON bilan ishlovchi kontaktlar kitobi

### 🧠 **Maqsad:**

OOP (Object-Oriented Programming) tushunchalarini mustahkamlash, va fayllar bilan ishlashni (JSON) o‘rganish.

---

### 📋 **Vazifa tavsifi:**

Sizga oddiy kontaktlar kitobini yaratish topshiriladi. Foydalanuvchi yangi kontakt qo‘sha olishi, o‘chira olishi, yangilay olishi, va barchasini ko‘ra olishi kerak. Barcha kontaktlar `contacts.json` faylida saqlanadi.

---

### 🧱 **Loyihada nimalar bo'lishi kerak:**

#### 1. **`Contact` class**

* Har bir kontakt quyidagi ma’lumotlarni o‘z ichiga oladi:

  * `name` (ism)
  * `phone` (telefon raqami)
  * `email` (ixtiyoriy)
  * `address` (ixtiyoriy)

#### 2. **`ContactBook` class**

* Barcha kontaktlar shu klass ichida ro‘yxat holida saqlanadi.
* Quyidagi metodlar bo'lishi kerak:

  * `add_contact(contact)` – yangi kontakt qo‘shish
  * `remove_contact(name)` – ism bo‘yicha kontaktni o‘chirish
  * `update_contact(name, new_contact)` – kontakt ma’lumotlarini yangilash
  * `list_contacts()` – barcha kontaktlarni chiqarish
  * `search_contact(name)` – ism bo‘yicha qidirish
  * `save_to_file()` – kontaktlarni JSON faylga yozish
  * `load_from_file()` – fayldan kontaktla2rni o‘qib olish

---

### ⚙️ **Texnik talablar:**

* Kod toza, modulga bo‘lingan bo‘lishi kerak (separate classes).
* JSON fayl bilan fayl ochish, yozish, o‘qish amaliyotlarini qo‘llang.
* Barcha metodlar ishlashini terminalda test qilib ko‘rsatish kerak.
* Loyihaga minimal CLI (command-line interface) qo‘shish mumkin.

---

### 🧪 **Bonus topshiriqlar (mustaqil o‘quvchilar uchun):**

* `ContactBook` sinfini telefon raqami bo‘yicha ham izlay oladigan qiling.
* Dublikat ismlarga yo‘l qo‘ymaslikni tekshiring.
* Kontaktlar JSON faylga avtomatik saqlansin har safar o‘zgartirishdan keyin.
* Kontaktlar oxirgi qo‘shilgan vaqtni ham saqlasin (`datetime` bilan).

---

### 📁 **Fayl tuzilmasi misoli:**

```
contact_book/
│
├── contact.py            # Contact class
├── contact_book.py       # ContactBook class
├── contacts.json         # Ma’lumotlar saqlanadigan fayl
└── main.py               # Loyihani ishga tushiruvchi fayl
```
