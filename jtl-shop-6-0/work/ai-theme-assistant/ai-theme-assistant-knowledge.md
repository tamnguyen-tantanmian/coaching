# AI Theme Assistant — Knowledge Notes / Ghi chú kiến thức

JTL-Shop 6.0 · Theme Editor · Last updated / Cập nhật: 16 Oct 2026

Each section is written in English first (🇬🇧), then Vietnamese (🇻🇳). / Mỗi phần viết tiếng Anh trước (🇬🇧), sau đó tiếng Việt (🇻🇳).

## 0. Sources / Nguồn

🇬🇧

- *444 AI Theme Builder Technical Concept* (Confluence) — "the concept"
- *AI Theme Chat Cases* — the current dev build
- `6 Finalization/theme-settings-flow-logic.md` and `theme-editor-confluence.md` — save / apply rules
- Team discussions (15 Oct 2026)

🇻🇳

- *444 AI Theme Builder Technical Concept* (Confluence) — gọi là "concept"
- *AI Theme Chat Cases* — bản build hiện tại của dev
- `6 Finalization/theme-settings-flow-logic.md` và `theme-editor-confluence.md` — quy tắc lưu / apply
- Thảo luận của team (15/10/2026)

---

## 1. What the feature is / Tính năng là gì

### 🇬🇧 English

- Merchants change the shop's look by describing it in text, or text plus images (PNG/JPEG).
- The AI proposes changes; **nothing changes until the merchant confirms**.
- It can change theme styles (colors, typography, spacing, radius), layout options (e.g. column count), and block text when asked.
- Manual editing keeps working, including when the AI fails.
- **Target user:** merchant admin or staff with permission to configure the storefront layout.

### 🇻🇳 Tiếng Việt

- Merchant thay đổi giao diện shop bằng cách mô tả bằng chữ, hoặc chữ kèm hình (PNG/JPEG).
- AI đề xuất thay đổi; **không có gì thay đổi cho đến khi merchant xác nhận**.
- AI đổi được style của theme (màu, typography, khoảng cách, bo góc), tùy chọn layout (vd. số cột), và text trong block khi được yêu cầu.
- Chỉnh sửa thủ công vẫn hoạt động, kể cả khi AI lỗi.
- **Người dùng mục tiêu:** admin hoặc nhân viên của merchant có quyền cấu hình layout storefront.

---

## 2. How a request works (concept) / Một yêu cầu được xử lý thế nào (concept)

### 🇬🇧 English

1. Merchant sends a prompt (+ image) with `pageId` and `version` — never the full page.
2. Backend checks permission and starts the AI session.
3. AI maps the request to fields (`target`, `property`, `adjustment`).
4. MCP tool checks the field exists → `valid` / `needs_clarification` / `not_supported`.
5. MCP reads only the needed current values and limits.
6. AI proposes one complete change set; MCP validates it.
7. Merchant reviews and confirms.
8. Backend re-checks, applies, saves the draft.

**Rules:** one request = one complete change set (any invalid change rejects all) · version changed before confirmation → Apply refused, new proposal needed · requests limited per shop · failures leave the page untouched.

**Current build:** every reply is exactly one of *proposal / question / error*. Apply puts changes into the editor draft; saving the theme is a separate step. Images: max 6, PNG/JPEG, 5 MB each, 8 MB total, text always required. Images reach the AI only in the turn they were sent.

### 🇻🇳 Tiếng Việt

1. Merchant gửi prompt (+ hình) kèm `pageId` và `version` — không gửi cả trang.
2. Backend kiểm tra quyền và khởi động phiên AI.
3. AI ánh xạ yêu cầu sang field (`target`, `property`, `adjustment`).
4. Công cụ MCP kiểm tra field có tồn tại → `valid` / `needs_clarification` / `not_supported`.
5. MCP chỉ đọc giá trị hiện tại và giới hạn cần thiết.
6. AI đề xuất một nhóm thay đổi hoàn chỉnh; MCP kiểm tra.
7. Merchant xem lại và xác nhận.
8. Backend kiểm tra lại, áp dụng, lưu bản nháp.

**Quy tắc:** một yêu cầu = một nhóm thay đổi hoàn chỉnh (một thay đổi lỗi thì từ chối cả nhóm) · version thay đổi trước khi xác nhận → từ chối Apply, cần đề xuất mới · giới hạn số yêu cầu mỗi shop · khi lỗi, trang giữ nguyên.

**Bản build hiện tại:** mỗi câu trả lời là đúng một trong *đề xuất / câu hỏi / lỗi*. Apply đưa thay đổi vào bản nháp của editor; lưu theme là bước riêng. Hình: tối đa 6, PNG/JPEG, mỗi hình 5 MB, tổng 8 MB, luôn bắt buộc có text. AI chỉ thấy hình trong lượt chat được gửi kèm.

---

## 3. Save & publish model (recalled) / Mô hình lưu & publish (nhắc lại)

### 🇬🇧 English

#### Theme Editor has two scopes

| Scope | Name | Edits | Reach |
| --- | --- | --- | --- |
| Global | **Theme Settings** | Colour roles, text styles, theme identity, versions | Every page at once |
| Composition | **Theme Builder** | Sections, blocks, items on a page | Only the edited object |

Theme Settings defines the tokens; Theme Builder composes with them. Colour in the Builder can take a raw hex; type cannot.

#### Theme Settings — Draft / Version / Apply

- **One draft** per theme. *Save as Draft* overwrites it without a confirm. The draft is never live.
- **Up to 5 versions.** *Save as Version* adds one; at 5/5 a modal asks to drop the oldest unbadged version. Numbers only ever increase.
- **Apply this theme** = publish the **latest version** to the storefront. Older versions must be reset → saved as new → applied.
- **Apply publishes, Save records.** Applying never creates a version.
- Badges: **Live** (on the storefront, exactly one) and **Active** (loaded in the Theme Builder session, at most one). Neither can be deleted.
- The preview is read-only and shows the **latest saved version of the selected page**.

#### Theme Builder — Publish

- The shop header has **Publish** with a "Last publish" timestamp.
- The spec (Pflichtenheft) separates **draft** content (preview) from **published** content (live), plus versioned releases for themes and templates.
- ⚠️ The Theme Builder save/publish rules are documented separately and are **not in this folder** — confirm before relying on them.

### 🇻🇳 Tiếng Việt

#### Theme Editor có hai phạm vi

| Phạm vi | Tên | Chỉnh gì | Ảnh hưởng |
| --- | --- | --- | --- |
| Toàn cục | **Theme Settings** | Vai trò màu, text style, thông tin theme, version | Mọi trang cùng lúc |
| Bố cục | **Theme Builder** | Section, block, item trên một trang | Chỉ đối tượng đang sửa |

Theme Settings định nghĩa token; Theme Builder dùng token để dựng trang. Màu trong Builder được nhập hex trực tiếp; font thì không.

#### Theme Settings — Draft / Version / Apply

- **Một bản nháp** cho mỗi theme. *Save as Draft* ghi đè mà không hỏi lại. Bản nháp không bao giờ live.
- **Tối đa 5 version.** *Save as Version* thêm một bản; khi đủ 5/5, modal hỏi có bỏ version cũ nhất không có badge. Số version chỉ tăng.
- **Apply this theme** = publish **version mới nhất** lên storefront. Version cũ phải reset → lưu thành version mới → rồi apply.
- **Apply là publish, Save là ghi lại.** Apply không tạo version.
- Badge: **Live** (đang trên storefront, đúng một) và **Active** (đang mở trong phiên Theme Builder, tối đa một). Không xóa được cả hai.
- Preview chỉ xem, hiển thị **version đã lưu mới nhất của trang đang chọn**.

#### Theme Builder — Publish

- Header của shop có nút **Publish** kèm thời điểm "Last publish".
- Spec (Pflichtenheft) tách nội dung **draft** (để preview) và **published** (live), cùng các bản phát hành có version cho theme và template.
- ⚠️ Quy tắc lưu/publish của Theme Builder được tài liệu hóa riêng và **không có trong folder này** — cần xác nhận trước khi dựa vào.

---

## 4. Current AI behaviour vs the save model (discussion 15 Oct) / Hành vi AI hiện tại so với mô hình lưu (thảo luận 15/10)

### 🇬🇧 English

- **Today:** prompt → AI suggests → accept → system keeps a **temporary copy** (lost on reload) → merchant has to realise they must *Save as Draft / Version* themselves.
- **Page A → page B:** the copy is temporary, so the FE can't render page B → the prompt can't run, the AI can't update.
- **One prompt touching Theme Settings + Theme Builder:** the AI returns everything in one chat → merchant must check and confirm all of it → the AI updates several pages plus settings at once → **no way yet to review those changes**.
- **AI is split per scope today.** It can tell settings from builder only when each is separate. A global AI (one assistant for both, no tab switch) is not possible yet and would expand scope.

### 🇻🇳 Tiếng Việt

- **Hiện tại:** prompt → AI đề xuất → accept → hệ thống giữ **bản tạm** (reload là mất) → merchant phải tự hiểu để *Save as Draft / Version*.
- **Ở trang A muốn sửa trang B:** do là bản tạm, FE chưa render được trang B → prompt không chạy được, AI không cập nhật được.
- **Một prompt sửa cả Theme Settings + Theme Builder:** AI trả toàn bộ kết quả trong một khung chat → merchant phải kiểm tra và xác nhận tất cả → AI cập nhật nhiều trang cùng lúc kèm settings → **chưa có cách xem lại các thay đổi**.
- **Hiện tại AI tách riêng theo từng phạm vi.** AI chỉ phân biệt được settings hay builder khi tách riêng. AI toàn cục (dùng chung cho cả hai, không đổi tab) chưa làm được, phải mở rộng scope.

---

## 5. Brainstormed options / Các phương án đã brainstorm

### 🇬🇧 English

| Option | How it works | Trade-off |
| --- | --- | --- |
| **A. Temporary copy** (today) | Changes live in memory until the merchant saves | Lost on reload or when moving to another page; can't edit page B from page A |
| **B. Auto-save into Draft** | Prompt → reconfirm → merchant accepts → FE renders the update and **saves straight into the Draft** | Technically OK. The single draft is **overwritten**; the previous draft can't be reviewed |
| **C. Force a page** | Merchant must pick a specific page before the AI can edit it | Simple, but blocks cross-page and global requests |
| **D. "Edit page B" hand-off** | AI says the change belongs to page B → link → navigate → request runs there | Still lost on reload / page change if the copy is temporary |

**Fits with the save model:** Option B matches the existing rule that the draft is a single scratch slot overwritten without confirm — but it means the merchant's own unsaved draft work can be silently replaced by the AI.

### 🇻🇳 Tiếng Việt

| Phương án | Cách hoạt động | Đánh đổi |
| --- | --- | --- |
| **A. Bản tạm** (hiện tại) | Thay đổi nằm trong bộ nhớ đến khi merchant lưu | Mất khi reload hoặc chuyển trang; không sửa được trang B từ trang A |
| **B. Tự lưu vào Draft** | Prompt → xác nhận lại → merchant accept → FE render bản mới và **lưu thẳng vào Draft** | Về kỹ thuật ổn. Bản nháp duy nhất **bị ghi đè**; không xem lại được bản trước |
| **C. Bắt chọn trang** | Merchant phải chọn một trang cụ thể thì AI mới sửa được | Đơn giản, nhưng chặn yêu cầu sửa nhiều trang hoặc toàn cục |
| **D. Chuyển sang trang B** | AI báo thay đổi thuộc trang B → link → chuyển trang → yêu cầu mới chạy | Vẫn mất khi reload / chuyển trang nếu là bản tạm |

**Khớp với mô hình lưu:** phương án B đúng với quy tắc hiện có là bản nháp chỉ có một và bị ghi đè không hỏi lại — nhưng nghĩa là phần nháp merchant tự làm mà chưa lưu có thể bị AI thay thế mà không báo.

---

## 6. UI decisions so far / Các quyết định UI đến hiện tại

### 🇬🇧 English

- **Layout:** the chat **replaces the config panel** (Shopify Sidekick style), not a floating box. Canvas stays fully visible. × returns to the config panel without losing the chat.
- **Scope labels (proposed):** each change shows **Theme settings** (all pages) or **Theme builder · page** (this page only).
- **Ask-back (proposed):**
  - "Make it red" with no target → first ask *which element* (button, background, banner…), then *which colour*.
  - Colour question: swatch options **plus a manual hex input** with validation.
  - 5+ questions: one card with "Question 3 of 5", progress bar, answered items collapsed with Edit, then a summary.
- **External AI agents:** no UI impact on the chat panel.

#### Flows design must cover

| # | Flow | Design work |
| --- | --- | --- |
| 1 | Opening the chat | Built — review only |
| 2 | Writing + images | Gap: images without text → no hint |
| 3 | Waiting for reply | Gap: raw tool names; no Stop |
| 4 | Proposal → Apply → Save ⭐ | Gap: no save reminder. Partial apply / Undo need confirmation |
| 5 | AI asks back / can't do it | Gap: "can't be changed" looks like a question |
| 6 | Errors & recovery | Gap: no retry, technical copy. Not built: version changed, apply/save failed, rate limit |
| 7 | Ending the chat | Built |

Priority: 4 → 6 → 5 & 3 → 2 → 1 & 7.

### 🇻🇳 Tiếng Việt

- **Layout:** khung chat **thay chỗ config panel** (kiểu Shopify Sidekick), không phải khung nổi. Canvas luôn hiện đầy đủ. Nút × quay về config panel mà không mất chat.
- **Nhãn phạm vi (đề xuất):** mỗi thay đổi ghi **Theme settings** (tất cả trang) hoặc **Theme builder · trang** (chỉ trang này).
- **AI hỏi lại (đề xuất):**
  - "Make it red" không có đối tượng → hỏi trước *phần tử nào* (nút, nền, banner…), rồi hỏi *màu nào*.
  - Câu hỏi màu: các lựa chọn màu **cộng ô nhập hex thủ công** có kiểm tra.
  - Từ 5 câu hỏi trở lên: một thẻ có "Question 3 of 5", thanh tiến độ, câu đã trả lời thu gọn kèm Edit, cuối cùng là bản tóm tắt.
- **External AI agent:** không ảnh hưởng UI của chat panel.

#### Các luồng design cần làm

| # | Luồng | Việc của design |
| --- | --- | --- |
| 1 | Mở chat | Đã có — chỉ rà lại |
| 2 | Soạn tin + hình | Thiếu: có hình không có text → không có gợi ý |
| 3 | Chờ trả lời | Thiếu: tên công cụ thô; không có Stop |
| 4 | Đề xuất → Apply → Save ⭐ | Thiếu: không nhắc lưu. Apply một phần / Undo cần xác nhận |
| 5 | AI hỏi lại / không làm được | Thiếu: "không đổi được" trông như câu hỏi |
| 6 | Lỗi & phục hồi | Thiếu: không có thử lại, câu chữ kỹ thuật. Chưa có: version thay đổi, apply/lưu thất bại, hết lượt |
| 7 | Kết thúc chat | Đã có |

Ưu tiên: 4 → 6 → 5 & 3 → 2 → 1 & 7.

---

## 7. Open questions / Câu hỏi còn mở

### 🇬🇧 English

1. **Where do AI changes land?** Temporary copy (A) or auto-save into Draft (B)?
2. **Editing page B from page A**, or from Theme Settings: **which version** is edited — the Theme Settings draft, the latest version, the Active version, or the page's own draft?
3. **Mixed prompts** (settings + builder, several pages): how does the merchant review all changes before and after Apply?
4. **Global AI vs per-scope AI:** stay split, or expand scope?
5. **Naming clash:** the chat's "Apply changes" (write to draft) vs Theme Settings' "Apply this theme" (publish). Same word, different meaning — rename one.
6. Can the AI say up front how many questions it will ask (for "Question 3 of 5")?
7. How do version-changed, apply/save-failed and rate-limit surface in the chat?
8. Partial apply and Undo — wanted? Not in the concept.

### 🇻🇳 Tiếng Việt

1. **Thay đổi của AI lưu vào đâu?** Bản tạm (A) hay tự lưu vào Draft (B)?
2. **Sửa trang B từ trang A**, hoặc từ Theme Settings: sửa vào **version nào** — draft của Theme Settings, version mới nhất, version Active, hay draft riêng của trang?
3. **Prompt hỗn hợp** (settings + builder, nhiều trang): merchant xem lại toàn bộ thay đổi trước và sau Apply bằng cách nào?
4. **AI toàn cục hay AI theo từng phạm vi:** giữ tách riêng, hay mở rộng scope?
5. **Trùng tên:** "Apply changes" trong chat (ghi vào draft) và "Apply this theme" trong Theme Settings (publish). Cùng chữ, khác nghĩa — cần đổi tên một bên.
6. AI có cho biết trước sẽ hỏi bao nhiêu câu không (để hiện "Question 3 of 5")?
7. Version thay đổi, apply/lưu thất bại và hết lượt hiển thị thế nào trong chat?
8. Apply một phần và Undo — có cần không? Không có trong concept.

---

## 8. Files / File liên quan

### 🇬🇧 English

| File | What it is |
| --- | --- |
| `ai-chat-panel-flows.html` | Prototype: chat panel per flow and case |
| `ai-technical-concept-knowledge-base.html` | Bilingual knowledge base of the concept + build cases |
| `ai-theme-assistant-states.html` | Earlier floating-panel exploration (superseded by the replace-panel layout) |

**Ticket:** "Theme Builder AI chat: move the panel into the config panel and design all chat flows" — 13 SP as one ticket, or 5 + 5 + 5 + 3 if split.

### 🇻🇳 Tiếng Việt

| File | Nội dung |
| --- | --- |
| `ai-chat-panel-flows.html` | Prototype: khung chat theo từng luồng và case |
| `ai-technical-concept-knowledge-base.html` | Cơ sở kiến thức song ngữ về concept + case của bản build |
| `ai-theme-assistant-states.html` | Bản thử khung nổi trước đó (đã thay bằng layout thay config panel) |

**Ticket:** "Theme Builder AI chat: move the panel into the config panel and design all chat flows" — 13 SP nếu một ticket, hoặc 5 + 5 + 5 + 3 nếu tách.
