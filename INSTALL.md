# 安裝 HC Reasoning

[回到 README](README.md#install)

選擇你實際使用的介面。Skills CLI、Claude 自訂 skill、OpenAI plugin 是不同的安裝入口，不會互相同步。

<a id="claude"></a>
## Claude 網頁版與 Desktop

1. [下載 hc-reasoning-claude-skill.zip](https://github.com/kcchien/hc-reasoning/releases/latest/download/hc-reasoning-claude-skill.zip)。不用解壓縮，也不要改用 GitHub 的 Source code ZIP。
2. 開啟 Claude，進入 **Customize → Skills → + → Create skill → Upload a skill**，選取下載的 ZIP。此路徑依官方網頁說明；若 Desktop 選單不同，先在網頁版完成上傳，再確認 Desktop 的 Skills 清單。
3. 確認清單中的 **hc-reasoning** 已啟用，開新對話，貼上 [README 的第一個問題](README.md#first-use)。

看不到 Skills 時，先確認已啟用 code execution；工作區帳號也可能受到管理員權限限制。這是自訂 skill 的上傳入口，不是聊天附件或組織 plugin 上傳入口。[Claude 官方說明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

ZIP 內有一層 `hc-reasoning/`，包含 `SKILL.md`、參考資料與授權。安裝包不含封面和展示圖片；不影響操作指引與參考內容。[官方打包格式](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

<a id="openai-desktop"></a>
## Codex／ChatGPT desktop：從 GitHub 市集安裝

不需要下載 ZIP。在可存取本機檔案、已安裝 Codex CLI 的桌面對話，貼上 [README 的完整安裝提示](README.md#install)，或在終端機依序執行：

```sh
codex plugin marketplace add https://github.com/kcchien/hc-reasoning
codex plugin add hc-reasoning@kcchien-hc-reasoning
```

完成後重新啟動桌面 app，在 Plugins Directory 選取 `kcchien-hc-reasoning`，確認 plugin 已安裝並啟用，再開新對話。若找不到 `codex` 指令，先使用 README 的 Skills CLI 安裝方式，或完成 Codex CLI 設定。[OpenAI plugin 說明](https://developers.openai.com/plugins/build/plugins)

<a id="openai-web"></a>
## ChatGPT 網頁版

### 有工作區管理員權限：直接匯入 GitHub 市集

1. 開啟 **Admin → Plugins → Add → Import marketplace**。
2. **Source** 貼上 `https://github.com/kcchien/hc-reasoning`。
3. **Path 留空**；Branch 留空可跟隨 main 更新，若要固定本次內容則填入發布的 commit。
4. 按 **Import marketplace**，依畫面授權 GitHub 讀取此公開 repo。
5. 等待 Import results 顯示成功，將 plugin 的 Installation policy 設為適用角色的 **Available**。
6. 成員在 **Plugins** 找到 `hc-reasoning` 並安裝，開新對話後使用。

本 repo 已包含 `.agents/plugins/marketplace.json` 與獨立 plugin，不需另外建立市集或上傳 ZIP。需要帳號具備此管理入口；匯入與角色權限由管理員控制。[官方匯入步驟](https://learn.chatgpt.com/docs/enterprise/plugin-management)

### 一般個人帳號：目前尚未提供直接安裝

本專案尚未上架公開 Plugins Directory。公開上架後，使用者才能在 **Plugins** 搜尋並安裝；GitHub Release 不等於 OpenAI 目錄上架。不要為了網頁版下載 OpenAI plugin ZIP，也不要把聊天附件上傳當作安裝。[官方發布流程](https://developers.openai.com/plugins/deploy/submission)

部分工作區另有 **Plugins → Skills → Create → Upload from your computer** 入口；這與 plugin 市集不同。目前未完成該入口的格式與上傳實測，因此不提供未驗證的 ZIP 安裝承諾。[工作區 Skills 說明](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

## 檔案大小與格式

兩種安裝 ZIP 都低於 **1 MB**，解壓後也低於 **1 MB**。這是本專案的大小預算，不是所有平台的官方上限。

- Claude 自訂 skill 的官方頁面提到 ZIP 大小限制，但未公布數字；組織 plugin 的限制不能直接套用。
- OpenAI plugin 提交的官方上限是 ZIP 壓縮後 100 MB、解壓後 512 MiB、單一檔案 100 MiB，最多 5,000 個項目；另有個別 skill bundle 檢查，以提交入口回報為準。[官方限制](https://developers.openai.com/plugins/deploy/submission-errors#zip-structure-and-limit-errors)

如果找不到下載檔，請確認 [Releases](https://github.com/kcchien/hc-reasoning/releases) 是否已有包含上述檔名的版本。不要自行把整個 repo 壓縮後當安裝包。

<a id="english"></a>
## English

- **Claude web/Desktop:** [Download the skill ZIP](https://github.com/kcchien/hc-reasoning/releases/latest/download/hc-reasoning-claude-skill.zip), leave it zipped, then use **Customize → Skills → + → Create skill → Upload a skill**. Enable it and start a new conversation. Code execution and workspace permissions must allow skills.
- **Codex / ChatGPT desktop:** Run `codex plugin marketplace add https://github.com/kcchien/hc-reasoning`, then `codex plugin add hc-reasoning@kcchien-hc-reasoning`. Restart the desktop app and start a new conversation. No ZIP download is needed.
- **ChatGPT web workspace admins:** Open **Admin → Plugins → Add → Import marketplace**, set Source to `https://github.com/kcchien/hc-reasoning`, leave Path empty, import, and make the plugin available to the intended roles. Members can then install it from Plugins. This requires the workspace admin feature; personal accounts cannot use this route. The plugin is not yet listed in the public directory.

Both install archives are below 1 MB compressed and extracted. This is our packaging budget, not a claimed Claude limit. For terminal-based agents, use [Skills CLI](README.md#install).
