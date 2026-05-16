# 🤖 QA Automation — Urban Routes Web Application

Automated UI test suite for a ride-sharing web application, built with **Selenium WebDriver** and **Python**. Covers the complete end-to-end booking flow using the Page Object Model pattern.

---

## 🎯 What was tested

The Urban Routes application allows users to book rides by selecting a route, fare, and trip preferences. This suite automates and validates the full user journey from address input to driver assignment.

**Covered flows:**
- Route address input and field validation
- Fare type selection (Comfort)
- Phone number setup with automated SMS code retrieval via Chrome DevTools Protocol
- Credit card addition through payment modal
- Driver message input
- Optional extras: blanket, tissues, ice creams
- Taxi order placement and modal verification
- Driver assignment confirmation

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Test scripting language |
| Selenium WebDriver | Browser automation |
| pytest | Test runner |
| Chrome DevTools Protocol (CDP) | Automated SMS code capture for phone verification |
| PyCharm | IDE |
| Page Object Model | Test architecture pattern |

---

## 📁 Project Structure

```
qa-automation-urban-routes/
│
├── main.py               # Test class with all 9 test methods (pytest)
├── pages.py              # Page Object Model — UrbanRoutesPage class
├── data.py               # Test data: URL, addresses, phone, card, message
├── helpers.py            # Helper: SMS code retrieval via CDP network logs
├── requirements.txt      # Python dependencies
└── README.md
```

---

## ▶️ How to run

**1. Clone the repository**
```bash
git clone https://github.com/sZagal04/qa-automation-urban-routes.git
cd qa-automation-urban-routes
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run all tests**
```bash
pytest main.py -v
```

---

## ✅ Test Cases

| Test | Description | Result |
|------|-------------|--------|
| `test_set_route` | Sets origin and destination, validates field values | ✅ Pass |
| `test_verify_tarifa_comfort` | Selects Comfort fare, verifies active CSS class | ✅ Pass |
| `test_fill_phone_number` | Enters phone, retrieves SMS code via CDP automatically | ✅ Pass |
| `test_add_credit_card` | Adds card number + CVV through payment modal | ✅ Pass |
| `test_set_message` | Types a message for the driver, validates stored value | ✅ Pass |
| `test_request_blanket_and_tissues` | Toggles both extras, verifies checked state | ✅ Pass |
| `test_add_icecreams` | Clicks counter twice, validates displayed quantity | ✅ Pass |
| `test_order_taxies` | Submits order, confirms search modal appears | ✅ Pass |
| `test_wait_for_search_modal` | Waits for driver assignment info to load | ✅ Pass |

**9/9 tests passing — 100% pass rate**

---

## 🏗️ Architecture Highlights

- **Page Object Model**: All locators and interactions live in `pages.py` — tests stay clean and maintainable
- **Explicit waits**: `WebDriverWait` + `expected_conditions` used throughout to handle dynamic UI reliably
- **CDP integration**: `helpers.py` intercepts network performance logs to extract the SMS code automatically — no manual step needed
- **JavaScript fallbacks**: `execute_script` used where standard Selenium clicks are blocked by overlapping elements

---

## 🔗 Related projects

- [API Testing](https://github.com/sZagal04/qa-api-testing)
- [Manual Testing](https://github.com/sZagal04/qa-manual-testing)
- [Database Testing](https://github.com/sZagal04/qa-database-testing)
