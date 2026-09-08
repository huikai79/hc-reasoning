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
## Codex／ChatGPT desktop：本機安裝

如果只使用 Codex CLI，直接用 [README 的 Skills CLI 指令](README.md#install)即可。要透過桌面介面的 Plugins Directory 管理，可[下載 OpenAI plugin ZIP](https://github.com/kcchien/hc-reasoning/releases/latest/download/hc-reasoning-openai-plugin.zip)，或在能存取本機檔案的 Codex／ChatGPT Work 對話貼上完整提示：

```text
請下載 https://github.com/kcchien/hc-reasoning/releases/latest/download/hc-reasoning-openai-plugin.zip，檢查內容並解壓縮。請用 plugin-creator 將其中的 hc-reasoning 加入我的本機 plugin 市集，保留其他已安裝項目，完成安裝並確認結果；不要發布或分享。
```

依 agent 提示完成本機安裝後，重新啟動桌面 app，在 Plugins Directory 選取本機市集，確認 **HC Reasoning** 已安裝並啟用，再開新對話使用。只有下載或解壓縮並不等於已安裝。[OpenAI 本機 plugin 說明](https://developers.openai.com/plugins/build/plugins)

這個 ZIP 包含 `.codex-plugin/plugin.json` 與 `skills/hc-reasoning/SKILL.md`，不能拿到 Claude 的自訂 skill 入口上傳。本機市集不會自動變成網頁版可用的公開項目。

<a id="openai-web"></a>
## ChatGPT 網頁版：先確認帳號入口

OpenAI 有兩種不同的發布方式：

- **工作區 Skills：**符合資格的 Business、Enterprise、Healthcare、Edu 帳號，可在 **Plugins → Skills → Create → Upload from your computer** 上傳 skill，實際可用性依工作區設定。官方說明尚未列出該入口的完整 ZIP 結構與數字大小上限，因此本專案不把 Claude ZIP 或 plugin ZIP 標為已驗證的工作區上傳包。[官方說明](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- **Plugins Directory：**OpenAI plugin 經送審與正式發布後，才能從共用公開目錄安裝到支援的 web／desktop 介面。本專案提供 plugin 發布包，但尚未在公開目錄上架；下載 ZIP 不會讓網頁版自動安裝它。[發布方式](https://developers.openai.com/plugins/deploy/submission)

工作區管理員另可透過 GitHub 市集分發 plugins，不必走公開目錄；這需要管理員設定與對應的 marketplace，不是直接上傳這份 ZIP。[組織分發說明](https://learn.chatgpt.com/docs/enterprise/plugin-management)

若現在需要使用，可先選上面的 Claude 自訂 skill 安裝，或 Codex 本機安裝。不要把一般聊天附件上傳成功當作 skill 安裝成功。

## 檔案大小與格式

兩種安裝 ZIP 都低於 **1 MB**，解壓後也低於 **1 MB**。這是本專案的大小預算，不是所有平台的官方上限。

- Claude 自訂 skill 的官方頁面提到 ZIP 大小限制，但未公布數字；組織 plugin 的限制不能直接套用。
- OpenAI plugin 提交的官方上限是 ZIP 壓縮後 100 MB、解壓後 512 MiB、單一檔案 100 MiB，最多 5,000 個項目；另有個別 skill bundle 檢查，以提交入口回報為準。[官方限制](https://developers.openai.com/plugins/deploy/submission-errors#zip-structure-and-limit-errors)

如果找不到下載檔，請確認 [Releases](https://github.com/kcchien/hc-reasoning/releases) 是否已有包含上述檔名的版本。不要自行把整個 repo 壓縮後當安裝包。

<a id="english"></a>
## English

- **Claude web/Desktop:** [Download the skill ZIP](https://github.com/kcchien/hc-reasoning/releases/latest/download/hc-reasoning-claude-skill.zip), leave it zipped, then use **Customize → Skills → + → Create skill → Upload a skill**. Enable it and start a new conversation. Code execution and workspace permissions must allow skills.
- **Codex / ChatGPT desktop with local filesystem access:** [Download the OpenAI plugin ZIP](https://github.com/kcchien/hc-reasoning/releases/latest/download/hc-reasoning-openai-plugin.zip). Ask plugin-creator to inspect it, extract it, add it to your local marketplace without replacing other entries, and verify installation. Restart the desktop app, select your marketplace in Plugins Directory, confirm the plugin is installed and enabled, then start a new conversation.
- **ChatGPT web:** Eligible business workspaces have a separate Skills upload flow. Its archive contract and size limit are not fully documented; these downloads are not certified for that flow. The OpenAI plugin package is prepared for distribution, but is not yet listed in the public Plugins Directory. A chat attachment is not an installation.

Both install archives are below 1 MB compressed and extracted. This is our packaging budget, not a claimed Claude limit. For terminal-based agents, use [Skills CLI](README.md#install).
