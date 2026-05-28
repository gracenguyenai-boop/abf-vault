# Example: PDF Hồ Sơ → LS / 4fcase (hoặc Inbox nếu thiếu F)

> Minh hoạ xử lý PDF hồ sơ vay, bao gồm trường hợp đủ 4F và thiếu F.

---

## Input

**Loại:** PDF
**Nội dung:** Hồ sơ vay mua nhà của KH A, 2.5 tỷ, có sổ đỏ, thu nhập được xác minh, CIC sạch. File chứa tờ khai, CMND, xác nhận thu nhập. Không có ghi chú cảm xúc/áp lực của KH (thiếu F2).

---

## Phase 0: EXTRACT

```
SOURCE_TYPE : pdf
SUMMARY     : Hồ sơ vay mua nhà 2.5 tỷ, KH A. Tài sản thế chấp: sổ đỏ nhà
              120m2 Q.Bình Thạnh định giá 3.2 tỷ. Thu nhập 35tr/tháng. CIC
              không có nợ xấu. Không có thông tin về tâm lý / bối cảnh KH.
INTENT      : Ghi lại thông tin một case vay thực tế đủ điều kiện xét duyệt.
              Hữu ích cho LS vì là dữ liệu case để phân tích và rút kinh nghiệm.
MULTI_NOTE  : NO
```

---

## Phase 1-2: BRANCH + TYPE

- Branch: LS (Ownership Test "Giúp xử lý hồ sơ vay cụ thể?" → YES)
- Type: L4/4fcase (Ownership Test "Có đủ 4F?" → cần kiểm tra)

---

## Phase 5: CONFLICT CHECK → NEW

---

## Phase 6: GAP DETECT — 4fcase thiếu F2

**Kiểm tra 4F:**
- F1 Facts: ✅ Có đầy đủ số liệu tài chính
- F2 Feelings: ❌ THIẾU — không có thông tin tâm lý / bối cảnh KH
- F3 Findings: ✅ Có thể suy ra từ F1
- F4 Future: ✅ Có thể đề xuất gói vay

**→ 4fcase điều kiện bắt buộc: đủ 4F → KHÔNG tạo 4fcase**

---

## Phase 7: PROPOSE

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 ĐỀ XUẤT ATOMIZE — ho-so-kh-a-mua-nha-2026-05.pdf
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INTENT     : Hồ sơ vay mua nhà 2.5 tỷ của KH A. Hữu ích cho LS để phân tích
             case thực tế và rút kinh nghiệm xử lý.
Source type: pdf

PHÂN LOẠI:
  Nhánh    : LS
  Lý do    : "Giúp xử lý hồ sơ vay cụ thể" → YES
  Type     : L4/4fcase
  Lý do    : Là case data cụ thể, không phải lesson learned

⚠️ GAP DETECTED — 4fcase thiếu F2
  F2 Feelings: THIẾU — file không có thông tin tâm lý / bối cảnh KH
  Điều kiện 4fcase yêu cầu đủ 4F → KHÔNG thể tạo 4fcase

ĐỀ XUẤT:
  Lưu vào LS-00-Inbox/incomplete/ với tag needs-f2
  Sau khi bổ sung F2 từ cuộc gặp KH → atomize lại thành 4fcase đầy đủ

ĐẦU RA (tạm):
  Path    : LS-LoanSpecialist/LS-00-Inbox/incomplete/
  Tên file: 2026-05-22-ho-so-kh-a-mua-nha-incomplete.md
  Note    : YAML status: incomplete | needs: F2-feelings

MOC CẦN CẬP NHẬT: Không (chưa tạo atomic note hoàn chỉnh)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Xác nhận? (yes / chỉnh sửa [field] / skip)
```

---

## Khi đủ 4F: Flow bình thường

Nếu file có đủ F1+F2+F3+F4:
- Phase 7 propose: `LS-LoanSpecialist/LS-01-Atomic/L4-PDCA/4fcases/YYYY-MM-DD-[ma-ho-so].md`
- Template: `_template-4fcase.md`
- YAML: `type: story | subtype: case-study`
- MOC update: `MOC-LoanSpecialist.md` section L4/4fcases + MOC-MASTER
