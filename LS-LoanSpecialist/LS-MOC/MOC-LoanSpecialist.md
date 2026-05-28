# MOC — Loan Specialist

> Navigation layer cho kiến thức nghiệp vụ ngân hàng và xử lý hồ sơ vay.
> **Agent:** tầng 1 — đọc để route xuống đúng layer sub-MOC.

← [[MOC-MASTER]]

---

## Routing Theo Nhu Cầu

| Cần gì | Đọc sub-MOC | Trạng thái |
|---|---|---|
| Khung tiếp nhận KH, quy trình 7 bước | [[LS-L1-MOC]] | ✅ 1 note |
| Sản phẩm vay thị trường, thẩm định, nguồn KH | [[LS-L2-MOC]] | ✅ 4 notes |
| VPBank ops: sản phẩm / lãi suất / checklist / luồng / ngoại lệ | [[LS-L3-MOC]] | ✅ 6 notes |
| Template 4F + 36 cases đã phân tích | [[LS-L4-MOC]] | ✅ 36 cases |

---

## L1 — Framework Tư Duy → [[LS-L1-MOC]]

> Agent: đọc trước Phase 1 Case Study — nắm logic tiếp nhận hồ sơ.
> **Status:** ✅ 1 note — quy trình tín dụng 7 bước + nguồn trả nợ KHCN.

📁 `LS-LoanSpecialist/LS-01-Atomic/L1-Framework/`
→ Template: [[_template-framework-ls]]

---

## L2 — Kiến Thức Nghề → [[LS-L2-MOC]]

> Agent: so sánh sản phẩm thị trường, không phải quy trình VPBank.

📁 `LS-LoanSpecialist/LS-01-Atomic/L2-KienThucNghe/`
→ Template: [[_template-concept-banking]]

---

## L3 — Kiến Thức Đặc Thù → [[LS-L3-MOC]]

> Agent: tra cứu quy trình / điều kiện VPBank cụ thể.

📁 `LS-LoanSpecialist/LS-01-Atomic/L3-KienThucDacThu/`
→ Template: [[_template-domain-banking-ops]]

---

## L4 — PDCA / Case Library → [[LS-L4-MOC]]

> Agent: **bắt đầu Case Study workflow tại đây** — lấy template 4F.
> **Status:** ✅ 36 cases (14 giải ngân + 22 không thành công)

📁 `LS-LoanSpecialist/LS-01-Atomic/L4-PDCA/`

---

## Inbox

→ Raw hồ sơ, tài liệu nghiệp vụ: `LS-LoanSpecialist/LS-00-Inbox/`

---

← [[MOC-MASTER]]
